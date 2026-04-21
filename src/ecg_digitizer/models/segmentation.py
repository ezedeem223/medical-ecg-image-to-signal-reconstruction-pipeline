from __future__ import annotations

from dataclasses import dataclass

import cv2
import numpy as np

from ecg_digitizer.models.registry import ModelArtifact


@dataclass
class SMPUnetBinarySegmenter:
    artifact: ModelArtifact
    device: str

    def __post_init__(self) -> None:
        import torch
        import segmentation_models_pytorch as smp

        encoder_name = self.artifact.encoder_name or "resnet50"
        model = smp.Unet(
            encoder_name=encoder_name,
            encoder_weights=None,
            in_channels=3,
            classes=1,
            decoder_attention_type=self.artifact.decoder_attention_type or "scse",
        )
        state_dict = torch.load(self.artifact.path, map_location="cpu")
        if isinstance(state_dict, dict) and "state_dict" in state_dict and isinstance(state_dict["state_dict"], dict):
            state_dict = state_dict["state_dict"]
        if isinstance(state_dict, dict):
            state_dict = {key.replace("module.", "", 1): value for key, value in state_dict.items()}
        model.load_state_dict(state_dict, strict=True)
        self._torch = torch
        self._model = model.to(self.device).eval()

    def predict_probmap(
        self,
        crop_rgb: np.ndarray,
        *,
        target_height: int,
        max_width: int,
        hflip: bool = True,
    ) -> tuple[np.ndarray, float]:
        torch = self._torch
        crop_height, crop_width = crop_rgb.shape[:2]
        scale = target_height / float(crop_height)
        new_width = int(max(1, crop_width * scale))
        if new_width > max_width:
            new_width = max_width
            scale = new_width / float(crop_width)

        resized = cv2.resize(crop_rgb, (new_width, target_height), interpolation=cv2.INTER_AREA)
        tensor = torch.from_numpy(resized).permute(2, 0, 1).float() / 255.0
        padded_width = min(int(np.ceil(new_width / 32.0) * 32), max_width)
        batch = torch.zeros((1, 3, target_height, padded_width), dtype=torch.float32, device=self.device)
        batch[0, :, :, :new_width] = tensor[:, :, :new_width].to(self.device)

        with torch.no_grad():
            if self.device == "cuda":
                with torch.amp.autocast(device_type="cuda", enabled=True):
                    prediction = torch.sigmoid(self._model(batch))
                    if hflip:
                        flipped = torch.sigmoid(self._model(torch.flip(batch, [3])))
                        prediction = (prediction + torch.flip(flipped, [3])) / 2.0
            else:
                prediction = torch.sigmoid(self._model(batch))
                if hflip:
                    flipped = torch.sigmoid(self._model(torch.flip(batch, [3])))
                    prediction = (prediction + torch.flip(flipped, [3])) / 2.0

        probmap = prediction.detach().float().cpu().numpy()[0, 0, :, :new_width].astype(np.float32)
        return probmap, scale

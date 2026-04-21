from __future__ import annotations

import ast
import base64
import csv
import hashlib
import json
import math
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import textwrap
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "docs" / "file-audit"
NOTEBOOK_OUTPUT = OUTPUT_ROOT / "notebooks"
MODEL_OUTPUT = OUTPUT_ROOT / "models"
IMAGE_OUTPUT = OUTPUT_ROOT / "image-outputs"
CHECKPOINT_COMPANION_OUTPUT = OUTPUT_ROOT / "checkpoint-companion-summary.md"
SYNTHESIS_OUTLINE_OUTPUT = ROOT / "docs" / "final_synthesis_outline.md"

NOTEBOOK_PATTERN = "ecg-sim2real-datagenerator-mohamad-sabbagh"
MODEL_SUFFIXES = {".pt", ".pth"}
TEXT_FILE_EXTENSIONS = {
    ".csv",
    ".parquet",
    ".json",
    ".txt",
    ".yaml",
    ".yml",
    ".xml",
    ".whl",
    ".py",
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".gif",
    ".svg",
    ".wfdb",
    ".hea",
    ".mat",
    ".dat",
}
PARAMETER_TERMS = {"weight", "bias", "running_mean", "running_var", "num_batches_tracked"}
ENV_MARKERS = {
    "Kaggle input mount": "/kaggle/input",
    "Kaggle working directory": "/kaggle/working",
    "Colab runtime detection": "google.colab",
    "Colab content root": "/content/",
    "pip install usage": "pip install",
    "subprocess usage": "subprocess",
    "YOLO loader": "YOLO(",
    "segmentation_models_pytorch": "segmentation_models_pytorch",
    "torch.load": "torch.load",
}
CALL_READ_FUNCS = {
    "open",
    "pd.read_csv",
    "pd.read_parquet",
    "pd.read_pickle",
    "np.load",
    "cv2.imread",
    "Image.open",
    "wfdb.rdrecord",
    "wfdb.rdsamp",
    "glob.glob",
    "torch.load",
    "zipfile.ZipFile",
    "os.path.exists",
    "os.listdir",
    "os.walk",
    "glob.iglob",
}
CALL_WRITE_FUNCS = {
    "open",
    "df.to_csv",
    "df.to_parquet",
    "pd.DataFrame.to_csv",
    "pd.DataFrame.to_parquet",
    "np.save",
    "np.savez",
    "cv2.imwrite",
    "plt.savefig",
    "torch.save",
}
MODEL_LOAD_CALL_NAMES = {"torch.load", "YOLO", "YOLO.load"}
MODEL_SAVE_CALL_NAMES = {"torch.save"}
MODEL_PROBE_CALL_NAMES = {"os.path.exists"}
SUBPROCESS_CALL_PREFIXES = ("subprocess.",)
WARNING_MARKERS = ("warning", "warn", "⚠", "deprecated", "FutureWarning")

from file_audit_manual_notes import load_manual_notes


def main() -> None:
    notebooks = ordered_notebooks(ROOT)
    models = ordered_models(ROOT)
    if not notebooks and not models:
        raise SystemExit("No notebooks or checkpoints found in repository root.")

    manual_notes = load_manual_notes()
    shutil.rmtree(OUTPUT_ROOT, ignore_errors=True)
    NOTEBOOK_OUTPUT.mkdir(parents=True, exist_ok=True)
    MODEL_OUTPUT.mkdir(parents=True, exist_ok=True)
    IMAGE_OUTPUT.mkdir(parents=True, exist_ok=True)

    used_slugs: set[str] = set()

    notebook_analyses: list[dict[str, Any]] = []
    notebook_text_index: dict[str, str] = {}
    for notebook_path in notebooks:
        analysis = analyze_notebook(notebook_path, used_slugs, manual_notes.get("notebooks", {}).get(notebook_path.name, {}))
        notebook_analyses.append(analysis)
        notebook_text_index[notebook_path.name] = analysis["full_text"]

    enrich_notebook_differences(notebook_analyses)

    model_analyses: list[dict[str, Any]] = []
    for model_path in models:
        analysis = analyze_model(model_path, notebook_text_index, used_slugs, manual_notes.get("models", {}).get(model_path.name, {}))
        model_analyses.append(analysis)

    manifest_rows = []
    for analysis in notebook_analyses:
        report = render_notebook_report(analysis, notebook_analyses)
        report_path = NOTEBOOK_OUTPUT / analysis["report_name"]
        report_path.write_text(report, encoding="utf-8")
        manifest_rows.append(manifest_row(analysis, "notebook", f"notebooks/{analysis['report_name']}"))

    for analysis in model_analyses:
        report = render_model_report(analysis)
        report_path = MODEL_OUTPUT / analysis["report_name"]
        report_path.write_text(report, encoding="utf-8")
        manifest_rows.append(manifest_row(analysis, "model", f"models/{analysis['report_name']}"))

    write_manifest(manifest_rows)
    write_checkpoint_companion_summary(notebook_analyses, model_analyses)
    write_synthesis_outline(notebook_analyses, model_analyses)
    write_readme(notebook_analyses, model_analyses, manifest_rows)


def ordered_notebooks(root: Path) -> list[Path]:
    main_name = f"{NOTEBOOK_PATTERN}.ipynb"
    numbered: list[tuple[int, Path]] = []
    main_notebook: Path | None = None
    for path in root.glob("*.ipynb"):
        if path.name == main_name:
            main_notebook = path
            continue
        match = re.fullmatch(rf"{re.escape(NOTEBOOK_PATTERN)} \((\d+)\)\.ipynb", path.name)
        if match:
            numbered.append((int(match.group(1)), path))
    ordered = []
    if main_notebook is not None:
        ordered.append(main_notebook)
    ordered.extend(path for _, path in sorted(numbered, key=lambda item: item[0]))
    return ordered


def ordered_models(root: Path) -> list[Path]:
    return sorted([path for path in root.iterdir() if path.suffix.lower() in MODEL_SUFFIXES and path.is_file()], key=lambda p: p.name.lower())


def manifest_row(analysis: dict[str, Any], entry_type: str, report_path: str) -> dict[str, str]:
    return {
        "review_order": str(analysis["review_order"]),
        "source_name": analysis["source_name"],
        "entry_type": entry_type,
        "size_bytes": str(analysis["size_bytes"]),
        "modified_utc": analysis["modified_utc"],
        "sha256": analysis["sha256"],
        "report_path": report_path.replace("\\", "/"),
        "status": "completed",
        "editorial_status": analysis["editorial_status"],
        "editorial_cell_notes": str(analysis["editorial_cell_note_count"]),
        "editorial_output_notes": str(analysis["editorial_output_note_count"]),
        "summary_status": analysis["summary_status"],
        "open_questions_count": str(analysis["open_questions_count"]),
        "confidence": analysis["confidence"],
        "delta_notes_count": str(analysis["delta_notes_count"]),
        "editorial_complete": analysis["editorial_complete"],
    }


def write_manifest(rows: list[dict[str, str]]) -> None:
    manifest_path = OUTPUT_ROOT / "manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "review_order",
                "source_name",
                "entry_type",
                "size_bytes",
                "modified_utc",
                "sha256",
                "report_path",
                "status",
                "editorial_status",
                "editorial_cell_notes",
                "editorial_output_notes",
                "summary_status",
                "open_questions_count",
                "confidence",
                "delta_notes_count",
                "editorial_complete",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def analyze_notebook(path: Path, used_slugs: set[str], manual_notes: dict[str, Any]) -> dict[str, Any]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    cells = notebook.get("cells", [])
    ordered_index = notebook_review_order(path)
    slug = unique_slug(normalize_name(path.stem), used_slugs)
    cell_analyses = []

    aggregate_imports: Counter[str] = Counter()
    aggregate_pip_packages: Counter[str] = Counter()
    aggregate_paths: Counter[str] = Counter()
    aggregate_reads: Counter[str] = Counter()
    aggregate_writes: Counter[str] = Counter()
    aggregate_commands: Counter[str] = Counter()
    aggregate_subprocess: Counter[str] = Counter()
    aggregate_models: Counter[str] = Counter()
    aggregate_model_saves: Counter[str] = Counter()
    aggregate_model_probes: Counter[str] = Counter()
    aggregate_functions: Counter[str] = Counter()
    aggregate_classes: Counter[str] = Counter()
    aggregate_constants: Counter[str] = Counter()
    aggregate_output_types: Counter[str] = Counter()
    aggregate_mimes: Counter[str] = Counter()
    warning_messages: list[str] = []
    error_summaries: list[str] = []

    for idx, cell in enumerate(cells, start=1):
        analysis = analyze_cell(cell, idx, slug, manual_notes)
        cell_analyses.append(analysis)
        aggregate_imports.update(analysis["imports"])
        aggregate_pip_packages.update(analysis["pip_packages"])
        aggregate_paths.update(analysis["paths"])
        aggregate_reads.update(analysis["file_reads"])
        aggregate_writes.update(analysis["file_writes"])
        aggregate_commands.update(analysis["shell_commands"])
        aggregate_subprocess.update(analysis["subprocess_calls"])
        aggregate_models.update(analysis["model_loads"])
        aggregate_model_saves.update(analysis["model_saves"])
        aggregate_model_probes.update(analysis["model_probes"])
        aggregate_functions.update(analysis["functions"])
        aggregate_classes.update(analysis["classes"])
        aggregate_constants.update(analysis["constants"])
        aggregate_output_types.update(analysis["output_type_counter"])
        aggregate_mimes.update(analysis["mime_counter"])
        warning_messages.extend(analysis["warnings"])
        error_summaries.extend(analysis["exceptions"])

    full_text = "\n\n".join(cell["source_text"] for cell in cell_analyses)
    metadata = notebook.get("metadata", {})
    kernelspec = metadata.get("kernelspec", {})
    language_info = metadata.get("language_info", {})

    environment_flags = [label for label, marker in ENV_MARKERS.items() if marker in full_text]
    inferred_role = infer_notebook_role(full_text, cell_analyses, aggregate_imports, aggregate_commands)
    notes = infer_notebook_notes(full_text, cell_analyses, environment_flags, error_summaries, warning_messages)
    risk_overrides = manual_notes.get("risk_overrides", [])
    if risk_overrides:
        notes = dedupe_preserve_order(notes + risk_overrides)
    notebook_summary = list(manual_notes.get("notebook_summary", []))
    delta_notes = list(manual_notes.get("delta_notes", []))
    open_questions = list(manual_notes.get("open_questions", []))
    confidence = str(manual_notes.get("confidence", "")).strip().lower()
    editorial_cell_note_count = sum(1 for cell in cell_analyses if cell["editorial_note"])
    editorial_output_note_count = sum(len(cell["output_notes"]) for cell in cell_analyses)
    dependency_summary = build_notebook_dependency_summary(
        imports=sorted(aggregate_imports),
        model_references=sorted(set(aggregate_models) | set(aggregate_model_saves) | set(aggregate_model_probes)),
        paths=sorted(aggregate_paths),
        file_reads=sorted(aggregate_reads),
        file_writes=sorted(aggregate_writes),
        model_saves=sorted(aggregate_model_saves),
        shell_commands=sorted(aggregate_commands),
        environment_flags=environment_flags,
    )
    summary_status = "present" if notebook_summary else "missing"
    delta_notes_count = len(delta_notes)
    open_questions_count = len(open_questions)
    editorial_complete = (
        "yes"
        if (
            summary_status == "present"
            and editorial_cell_note_count == len(cells)
            and confidence in {"high", "medium", "low"}
            and delta_notes_count > 0
            and open_questions is not None
        )
        else "no"
    )

    return {
        "review_order": ordered_index,
        "source_name": path.name,
        "source_path": path,
        "report_name": f"{slug}.md",
        "size_bytes": path.stat().st_size,
        "modified_utc": utc_mtime(path),
        "sha256": sha256_file(path),
        "nbformat": notebook.get("nbformat"),
        "nbformat_minor": notebook.get("nbformat_minor"),
        "metadata": metadata,
        "kernelspec": kernelspec,
        "language_info": language_info,
        "cell_count": len(cells),
        "code_cells": sum(1 for cell in cells if cell.get("cell_type") == "code"),
        "markdown_cells": sum(1 for cell in cells if cell.get("cell_type") == "markdown"),
        "raw_cells": sum(1 for cell in cells if cell.get("cell_type") == "raw"),
        "cell_analyses": cell_analyses,
        "full_text": full_text,
        "imports": sorted(aggregate_imports),
        "pip_packages": sorted(aggregate_pip_packages),
        "paths": sorted(aggregate_paths),
        "file_reads": sorted(aggregate_reads),
        "file_writes": sorted(aggregate_writes),
        "shell_commands": sorted(aggregate_commands),
        "subprocess_calls": sorted(aggregate_subprocess),
        "model_loads": sorted(aggregate_models),
        "model_saves": sorted(aggregate_model_saves),
        "model_probes": sorted(aggregate_model_probes),
        "model_references": sorted(set(aggregate_models) | set(aggregate_model_saves) | set(aggregate_model_probes)),
        "functions": sorted(aggregate_functions),
        "classes": sorted(aggregate_classes),
        "constants": sorted(aggregate_constants),
        "output_type_counter": dict(aggregate_output_types),
        "mime_counter": dict(aggregate_mimes),
        "warning_messages": dedupe_preserve_order(warning_messages),
        "error_summaries": dedupe_preserve_order(error_summaries),
        "environment_flags": environment_flags,
        "inferred_role": inferred_role,
        "notes": notes,
        "notebook_summary": notebook_summary,
        "delta_notes": delta_notes,
        "open_questions": open_questions,
        "confidence": confidence or "missing",
        "editorial_status": "cell-reviewed" if editorial_cell_note_count == len(cells) else "partial-review",
        "editorial_cell_note_count": editorial_cell_note_count,
        "editorial_output_note_count": editorial_output_note_count,
        "summary_status": summary_status,
        "open_questions_count": open_questions_count,
        "delta_notes_count": delta_notes_count,
        "editorial_complete": editorial_complete,
        "dependency_summary": dependency_summary,
        "image_output_count": sum(len(cell["output_artifacts"]) for cell in cell_analyses),
        "manual_output_note_count": editorial_output_note_count,
        "cell_hashes": [cell["source_hash"] for cell in cell_analyses],
        "first_lines": [cell["first_line"] for cell in cell_analyses if cell["first_line"]],
        "previous_diff": None,
    }


def build_notebook_dependency_summary(
    *,
    imports: list[str],
    model_references: list[str],
    paths: list[str],
    file_reads: list[str],
    file_writes: list[str],
    model_saves: list[str],
    shell_commands: list[str],
    environment_flags: list[str],
) -> dict[str, list[str]]:
    referenced_checkpoints = extract_checkpoint_basenames(model_references + paths + file_reads + file_writes + model_saves)
    dataset_refs = summarize_dataset_dependencies(paths, file_reads)
    external_files = dedupe_preserve_order(
        compact_items(file_reads, limit=8) + compact_items(file_writes, limit=4)
    )
    runtime_assumptions = summarize_runtime_assumptions(imports, shell_commands, environment_flags, paths)
    outputs_created = dedupe_preserve_order(compact_items(model_saves, limit=4) + compact_items(file_writes, limit=6))
    return {
        "referenced_checkpoints": referenced_checkpoints,
        "referenced_datasets": dataset_refs,
        "external_files": external_files,
        "runtime_assumptions": runtime_assumptions,
        "outputs_created": outputs_created,
    }


def analyze_cell(cell: dict[str, Any], index: int, notebook_slug: str, manual_notes: dict[str, Any]) -> dict[str, Any]:
    source_text = cell_source_text(cell)
    first_line = first_non_empty_line(source_text)
    shell_commands = extract_shell_commands(source_text)
    python_source = prepare_python_source(source_text)
    tree = safe_parse_ast(python_source)
    cell_bindings = collect_string_bindings(tree)
    imports, functions, classes, constants = collect_symbols(tree)
    call_uses = collect_call_uses(tree, cell_bindings)
    paths = collect_paths(source_text, cell_bindings)
    pip_packages = extract_pip_packages(shell_commands)
    outputs = analyze_outputs(cell.get("outputs", []), notebook_slug, index, manual_notes)
    source_summary = summarize_cell_role(cell.get("cell_type"), first_line, imports, functions, classes, shell_commands, call_uses, outputs)
    editorial_note = manual_notes.get("cell_notes", {}).get(index, "")

    return {
        "index": index,
        "cell_type": cell.get("cell_type", "unknown"),
        "execution_count": cell.get("execution_count"),
        "first_line": first_line,
        "source_text": source_text,
        "source_hash": hashlib.sha256(source_text.encode("utf-8")).hexdigest(),
        "imports": imports,
        "functions": functions,
        "classes": classes,
        "constants": constants,
        "constant_bindings": cell_bindings,
        "paths": paths,
        "file_reads": dedupe_preserve_order(call_uses["reads"]),
        "file_writes": dedupe_preserve_order(call_uses["writes"]),
        "shell_commands": shell_commands,
        "pip_packages": pip_packages,
        "subprocess_calls": dedupe_preserve_order(call_uses["subprocess"]),
        "model_loads": dedupe_preserve_order(call_uses["model_loads"]),
        "model_saves": dedupe_preserve_order(call_uses["model_saves"]),
        "model_probes": dedupe_preserve_order(call_uses["model_probes"]),
        "output_items": outputs["items"],
        "output_artifacts": outputs["artifacts"],
        "output_notes": outputs["notes"],
        "output_type_counter": outputs["output_type_counter"],
        "mime_counter": outputs["mime_counter"],
        "exceptions": outputs["exceptions"],
        "warnings": dedupe_preserve_order(outputs["warnings"]),
        "source_summary": source_summary,
        "editorial_note": editorial_note,
    }


def cell_source_text(cell: dict[str, Any]) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(source)
    return str(source)


def first_non_empty_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped[:180]
    return ""


def extract_shell_commands(source_text: str) -> list[str]:
    commands = []
    for line in source_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("!") or stripped.startswith("%"):
            commands.append(stripped)
    return commands


def prepare_python_source(source_text: str) -> str:
    prepared = []
    for line in source_text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("!") or stripped.startswith("%"):
            prepared.append("# notebook magic stripped for AST analysis")
        else:
            prepared.append(line)
    return "\n".join(prepared)


def safe_parse_ast(source_text: str) -> ast.AST | None:
    if not source_text.strip():
        return None
    try:
        return ast.parse(source_text)
    except SyntaxError:
        return None


def collect_string_bindings(tree: ast.AST | None) -> dict[str, Any]:
    bindings: dict[str, Any] = {}
    if tree is None:
        return bindings

    class BindingCollector(ast.NodeVisitor):
        def visit_Assign(self, node: ast.Assign) -> None:
            resolved_value = resolve_assignment_value(node.value, bindings)
            if resolved_value is not None:
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        bindings[target.id] = resolved_value
            self.generic_visit(node)

        def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
            if isinstance(node.target, ast.Name) and node.value is not None:
                resolved_value = resolve_assignment_value(node.value, bindings)
                if resolved_value is not None:
                    bindings[node.target.id] = resolved_value
            self.generic_visit(node)

        def visit_Expr(self, node: ast.Expr) -> None:
            if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Attribute):
                attr = node.value.func
                if attr.attr == "append" and isinstance(attr.value, ast.Name) and attr.value.id in bindings:
                    current = bindings.get(attr.value.id)
                    if isinstance(current, list) and node.value.args:
                        appended = resolve_expr_strings(node.value.args[0], bindings)
                        if appended:
                            current.extend(appended)
            self.generic_visit(node)

    BindingCollector().visit(tree)
    return bindings


def collect_symbols(tree: ast.AST | None) -> tuple[list[str], list[str], list[str], list[str]]:
    imports: list[str] = []
    functions: list[str] = []
    classes: list[str] = []
    constants: list[str] = []
    if tree is None:
        return imports, functions, classes, constants

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and (target.id.isupper() or isinstance(node.value, ast.Constant)):
                    constants.append(target.id)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.target.id.isupper() or isinstance(node.value, ast.Constant):
                constants.append(node.target.id)

    return dedupe_preserve_order(imports), dedupe_preserve_order(functions), dedupe_preserve_order(classes), dedupe_preserve_order(constants)


def collect_call_uses(tree: ast.AST | None, bindings: dict[str, Any]) -> dict[str, list[str]]:
    results = {"reads": [], "writes": [], "subprocess": [], "model_loads": [], "model_saves": [], "model_probes": []}
    if tree is None:
        return results

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        call_name = dotted_name(node.func)
        arg_values = resolve_call_paths(node, bindings)

        if call_name in CALL_READ_FUNCS:
            for value in arg_values:
                results["reads"].append(f"{call_name}: {value}")
        if call_name in CALL_WRITE_FUNCS:
            for value in arg_values:
                results["writes"].append(f"{call_name}: {value}")
        if call_name == "open":
            mode = resolve_open_mode(node, bindings)
            for value in arg_values:
                if mode and any(flag in mode for flag in ("w", "a", "x")):
                    results["writes"].append(f"open[{mode}]: {value}")
                else:
                    results["reads"].append(f"open[{mode or 'r?'}]: {value}")
        if call_name in MODEL_LOAD_CALL_NAMES:
            for value in arg_values:
                if value.lower().endswith((".pt", ".pth")):
                    results["model_loads"].append(f"{call_name or 'call'}: {value}")
        if call_name in MODEL_SAVE_CALL_NAMES:
            for value in arg_values:
                if value.lower().endswith((".pt", ".pth")):
                    results["model_saves"].append(f"{call_name}: {value}")
        if call_name in MODEL_PROBE_CALL_NAMES:
            for value in arg_values:
                if value.lower().endswith((".pt", ".pth")):
                    results["model_probes"].append(f"{call_name}: {value}")
        if call_name.startswith(SUBPROCESS_CALL_PREFIXES):
            descriptor = render_subprocess_descriptor(node, call_name, bindings)
            results["subprocess"].append(descriptor)

    return {key: dedupe_preserve_order(values) for key, values in results.items()}


def dotted_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = dotted_name(node.value)
        return f"{base}.{node.attr}" if base else node.attr
    return ""


def resolve_call_paths(node: ast.Call, bindings: dict[str, Any]) -> list[str]:
    values = []
    for arg in list(node.args) + [keyword.value for keyword in node.keywords]:
        for resolved in resolve_expr_strings(arg, bindings):
            if resolved and looks_like_path_or_artifact(resolved):
                values.append(resolved)
    return dedupe_preserve_order(values)


def resolve_open_mode(node: ast.Call, bindings: dict[str, Any]) -> str | None:
    if len(node.args) >= 2:
        resolved = resolve_expr_strings(node.args[1], bindings)
        return resolved[0] if resolved else None
    for keyword in node.keywords:
        if keyword.arg == "mode":
            resolved = resolve_expr_strings(keyword.value, bindings)
            return resolved[0] if resolved else None
    return None


def resolve_assignment_value(node: ast.AST, bindings: dict[str, Any]) -> Any:
    if isinstance(node, (ast.List, ast.Tuple)):
        values = resolve_expr_strings(node, bindings)
        return values
    resolved_values = resolve_expr_strings(node, bindings)
    if len(resolved_values) == 1:
        return resolved_values[0]
    return None


def resolve_expr_strings(node: ast.AST, bindings: dict[str, Any]) -> list[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return [node.value]
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float, bool)):
        return [str(node.value)]
    if isinstance(node, ast.Name):
        if node.id in bindings:
            bound = bindings[node.id]
            if isinstance(bound, list):
                return [str(item) for item in bound]
            return [str(bound)]
        return [node.id]
    if isinstance(node, ast.Attribute):
        dotted = dotted_name(node)
        if dotted in bindings:
            bound = bindings[dotted]
            if isinstance(bound, list):
                return [str(item) for item in bound]
            return [str(bound)]
        return [dotted] if dotted else []
    if isinstance(node, ast.JoinedStr):
        parts: list[str] = []
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                parts.append(value.value)
            elif isinstance(value, ast.FormattedValue):
                if isinstance(value.value, ast.Name) and value.value.id not in bindings:
                    parts.append(f"{{{value.value.id}}}")
                else:
                    formatted = resolve_expr_strings(value.value, bindings)
                    if formatted:
                        parts.append(formatted[0])
                    else:
                        placeholder = dotted_name(value.value)
                        parts.append(f"{{{placeholder or 'expr'}}}")
        return ["".join(parts)]
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        if isinstance(node.left, ast.Call) or isinstance(node.right, ast.Call):
            return []
        left_values = resolve_expr_strings(node.left, bindings)
        right_values = resolve_expr_strings(node.right, bindings)
        if left_values and right_values:
            return [left_values[0] + right_values[0]]
    if isinstance(node, ast.Call):
        call_name = dotted_name(node.func)
        if call_name in {"os.path.join", "posixpath.join", "ntpath.join", "Path"}:
            parts = []
            for arg in node.args:
                resolved = resolve_expr_strings(arg, bindings)
                if resolved:
                    parts.append(resolved[0])
            if parts:
                return [join_path_parts(parts)]
        if call_name in {"glob.glob", "glob.iglob", "os.path.dirname", "os.path.basename", "str"} and node.args:
            return resolve_expr_strings(node.args[0], bindings)
    if isinstance(node, ast.Subscript):
        base = resolve_expr_strings(node.value, bindings) or [dotted_name(node.value) or "subscript"]
        index = render_index(node.slice, bindings)
        return [f"{base[0]}[{index}]"]
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        values = []
        for element in node.elts:
            element_values = resolve_expr_strings(element, bindings)
            if element_values:
                values.append(element_values[0])
        return values
    return []


def render_index(node: ast.AST, bindings: dict[str, Any]) -> str:
    values = resolve_expr_strings(node, bindings)
    if values:
        return values[0]
    dotted = dotted_name(node)
    return dotted or "idx"


def join_path_parts(parts: list[str]) -> str:
    if not parts:
        return ""
    normalized = []
    current_sep = "/"
    if any("\\" in part or re.match(r"^[A-Za-z]:\\", part) for part in parts):
        current_sep = "\\"
    for index, part in enumerate(parts):
        cleaned = part.strip().strip("\"'")
        if index == 0:
            normalized.append(cleaned.rstrip("/\\"))
        else:
            normalized.append(cleaned.strip("/\\"))
    joined = current_sep.join(part for part in normalized if part)
    if parts and parts[0].startswith("/"):
        joined = "/" + joined.lstrip("/\\")
    return joined


def render_subprocess_descriptor(node: ast.Call, call_name: str, bindings: dict[str, Any]) -> str:
    if node.args:
        first = node.args[0]
        tokens = resolve_command_tokens(first, bindings)
        if tokens:
            return f"{call_name}: {' '.join(tokens)}"
    for keyword in node.keywords:
        if keyword.arg in {"args", "cmd"}:
            tokens = resolve_command_tokens(keyword.value, bindings)
            if tokens:
                return f"{call_name}: {' '.join(tokens)}"
    return call_name


def resolve_command_tokens(node: ast.AST, bindings: dict[str, Any]) -> list[str]:
    if isinstance(node, (ast.List, ast.Tuple)):
        tokens = []
        for element in node.elts:
            if isinstance(element, ast.Starred):
                tokens.extend(resolve_command_tokens(element.value, bindings))
                continue
            resolved = resolve_expr_strings(element, bindings)
            if resolved:
                tokens.append(resolved[0])
            else:
                dotted = dotted_name(element)
                if dotted:
                    tokens.append(f"<{dotted}>")
        return tokens
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return [node.value]
    return resolve_expr_strings(node, bindings)


def collect_paths(source_text: str, bindings: dict[str, Any]) -> list[str]:
    paths = []
    for value in bindings.values():
        if isinstance(value, list):
            paths.extend(item for item in value if looks_like_path_or_artifact(item))
        elif isinstance(value, str) and looks_like_path_or_artifact(value):
            paths.append(value)
    regex_matches = re.findall(r"['\"]([^'\"]{2,}?)['\"]", source_text)
    for match in regex_matches:
        if looks_like_path_or_artifact(match):
            paths.append(match)
    return sorted(set(path.strip() for path in paths if path.strip()))


def looks_like_path_or_artifact(value: str) -> bool:
    if not value:
        return False
    if "\n" in value or "\r" in value:
        return False
    value = value.strip()
    if not value or len(value) > 260:
        return False
    lowered = value.lower()
    if value.count(" ") > 2 and not lowered.startswith(("http://", "https://")):
        return False
    if lowered.startswith("http://") or lowered.startswith("https://"):
        return True
    if any(lowered.endswith(ext) for ext in TEXT_FILE_EXTENSIONS | MODEL_SUFFIXES):
        return True
    if any(marker in value for marker in ("/kaggle/", "/content/", "/usr/", "/tmp/", "../", "./", ":/")):
        return True
    if "/" in value and re.search(r"(?:^|[A-Za-z0-9_.{}*-])/(?:[A-Za-z0-9_.{}*-])", value):
        return True
    if re.match(r"^[A-Za-z]:\\", value):
        return True
    if "\\" in value and not value.startswith(("\\n", "\\t", "\\r")) and re.search(r"[A-Za-z0-9_.{}*-]\\[A-Za-z0-9_.{}*-]", value):
        return True
    return False


def extract_pip_packages(shell_commands: list[str]) -> list[str]:
    packages = []
    for command in shell_commands:
        normalized = command.lstrip("!%")
        if "pip install" not in normalized:
            continue
        try:
            tokens = shlex.split(normalized)
        except ValueError:
            tokens = normalized.split()
        capture = False
        skip_next = False
        for token in tokens:
            if skip_next:
                skip_next = False
                continue
            if token == "install":
                capture = True
                continue
            if not capture:
                continue
            if token.startswith("-"):
                if token in {"-r", "--requirement", "--find-links", "-f", "--extra-index-url", "--index-url"}:
                    skip_next = True
                continue
            packages.append(token)
    return dedupe_preserve_order(packages)


def analyze_outputs(outputs: list[dict[str, Any]], notebook_slug: str, cell_index: int, manual_notes: dict[str, Any]) -> dict[str, Any]:
    items = []
    artifacts = []
    notes = []
    output_type_counter: Counter[str] = Counter()
    mime_counter: Counter[str] = Counter()
    exceptions = []
    warnings = []
    manual_output_notes = manual_notes.get("output_notes", {})

    for idx, output in enumerate(outputs, start=1):
        manual_note = manual_output_notes.get(f"{cell_index}:{idx}")
        output_type = output.get("output_type", "unknown")
        output_type_counter[output_type] += 1
        if output_type == "stream":
            text = normalize_output_text(output.get("text", ""))
            line_count = len(text.splitlines()) if text else 0
            summary = f"stream[{output.get('name', 'stdout')}] with {line_count} line(s)"
            excerpt = excerpt_text(text)
            if excerpt:
                summary += f"; excerpt: {excerpt}"
            items.append(summary)
            warnings.extend(find_warning_lines(text))
        elif output_type in {"display_data", "execute_result"}:
            data = output.get("data", {})
            mime_types = sorted(data.keys())
            mime_counter.update(mime_types)
            summary_parts = [f"{output_type} MIME={', '.join(mime_types) or 'none'}"]
            if any(mime.startswith("image/") for mime in mime_types):
                summary_parts.append("image payload present")
            if "image/png" in data:
                artifact_path = write_image_artifact(notebook_slug, cell_index, idx, data.get("image/png"))
                if artifact_path:
                    artifacts.append(artifact_path)
                    summary_parts.append(f"artifact={artifact_path}")
            text_payload = normalize_output_text(data.get("text/plain", ""))
            html_payload = normalize_output_text(data.get("text/html", ""))
            if text_payload:
                summary_parts.append(f"text excerpt: {excerpt_text(text_payload)}")
                warnings.extend(find_warning_lines(text_payload))
            if html_payload:
                summary_parts.append(f"html lines={len(html_payload.splitlines())}")
                warnings.extend(find_warning_lines(html_payload))
            items.append("; ".join(summary_parts))
        elif output_type == "error":
            ename = output.get("ename", "Error")
            evalue = output.get("evalue", "")
            traceback_text = "\n".join(output.get("traceback", []))
            summary = f"{ename}: {evalue}".strip()
            items.append(f"error {summary}")
            exceptions.append(summary)
            warnings.extend(find_warning_lines(traceback_text))
        else:
            items.append(f"{output_type} output")
        if manual_note:
            notes.append(f"Output {idx}: {manual_note}")

    return {
        "items": items,
        "artifacts": artifacts,
        "notes": notes,
        "output_type_counter": output_type_counter,
        "mime_counter": mime_counter,
        "exceptions": dedupe_preserve_order(exceptions),
        "warnings": dedupe_preserve_order(warnings),
    }


def write_image_artifact(notebook_slug: str, cell_index: int, output_index: int, payload: Any) -> str:
    if not payload:
        return ""
    encoded = "".join(payload) if isinstance(payload, list) else str(payload)
    target_dir = IMAGE_OUTPUT / notebook_slug
    target_dir.mkdir(parents=True, exist_ok=True)
    target_name = f"cell-{cell_index:02d}-output-{output_index:02d}.png"
    target_path = target_dir / target_name
    try:
        target_path.write_bytes(base64.b64decode(encoded))
    except Exception:
        return ""
    return f"image-outputs/{notebook_slug}/{target_name}"


def normalize_output_text(value: Any) -> str:
    if isinstance(value, list):
        return "".join(str(item) for item in value)
    if value is None:
        return ""
    return str(value)


def excerpt_text(text: str, limit: int = 180) -> str:
    compact = " ".join(line.strip() for line in text.splitlines() if line.strip())
    if not compact:
        return ""
    return compact[:limit] + ("..." if len(compact) > limit else "")


def find_warning_lines(text: str) -> list[str]:
    warnings = []
    for line in text.splitlines():
        lowered = line.lower()
        if any(marker.lower() in lowered for marker in WARNING_MARKERS):
            warnings.append(line.strip()[:220])
    return warnings


def summarize_cell_role(
    cell_type: str,
    first_line: str,
    imports: list[str],
    functions: list[str],
    classes: list[str],
    shell_commands: list[str],
    call_uses: dict[str, list[str]],
    outputs: dict[str, Any],
) -> str:
    lowered = first_line.lower()
    if cell_type == "markdown":
        return "Narrative / markdown cell."
    if shell_commands:
        if any("pip install" in command for command in shell_commands):
            return "Environment bootstrap cell with package installation commands."
        return "Notebook magic / shell orchestration cell."
    if "train" in lowered or "تدريب" in lowered:
        return "Training or fine-tuning orchestration cell."
    if "render" in lowered or "الرسم" in lowered:
        return "Rendering / synthetic ECG image generation cell."
    if "predict" in lowered or "infer" in lowered or "submission" in lowered:
        return "Inference / submission generation cell."
    if functions or classes:
        pieces = []
        if functions:
            pieces.append(f"defines {len(functions)} function(s)")
        if classes:
            pieces.append(f"{len(classes)} class(es)")
        return "Definition cell that " + " and ".join(pieces) + "."
    if call_uses["model_loads"]:
        return "Model loading or model wiring cell."
    if call_uses["reads"] or call_uses["writes"]:
        return "Data I/O and pipeline coordination cell."
    if outputs["items"]:
        return "Execution cell with stored outputs."
    if imports:
        return "Import / dependency declaration cell."
    return "General computation cell."


def infer_notebook_role(
    full_text: str,
    cell_analyses: list[dict[str, Any]],
    aggregate_imports: Counter[str],
    aggregate_commands: Counter[str],
) -> str:
    lowered = full_text.lower()
    if "phase 10" in lowered and "fine-tuning" in lowered:
        return "Phase 10 real-world fine-tuning notebook."
    if "phase 10" in lowered and "pseudo" in lowered:
        return "Phase 10 pseudo-label / real-world adaptation notebook."
    if "smart offline install" in lowered or "/kaggle/input/**/*.whl" in lowered:
        return "Offline Kaggle inference pipeline variant with packaged dependencies."
    if "ultimate renderer" in lowered and "sample_submission" in lowered and "yolo" in lowered:
        return "Kaggle ECG digitization inference notebook combining YOLO and segmentation."
    if "توليد البيانات" in lowered or "render_to_memory" in lowered:
        if "تدريب" in lowered or "train" in lowered:
            return "End-to-end synthetic data generation and training notebook."
        return "Synthetic ECG rendering / data generation notebook."
    if cell_analyses and any(cell["classes"] for cell in cell_analyses):
        return "Prototype notebook with custom dataset / model helper definitions."
    if "segmentation_models_pytorch" in " ".join(aggregate_imports.keys()):
        return "Segmentation-centric experiment notebook."
    if aggregate_commands:
        return "Notebook variant with explicit environment bootstrapping."
    return "Pipeline revision notebook."


def infer_notebook_notes(
    full_text: str,
    cell_analyses: list[dict[str, Any]],
    environment_flags: list[str],
    errors: list[str],
    warnings: list[str],
) -> list[str]:
    notes = []
    if "/kaggle/input" in full_text:
        notes.append("Hard-coded Kaggle input paths make the notebook environment-specific.")
    if "/kaggle/working" in full_text:
        notes.append("Notebook assumes writable Kaggle working storage for intermediate artifacts.")
    if "google.colab" in full_text:
        notes.append("Colab runtime detection is present; behavior may differ between Kaggle and Colab.")
    if any("pip install" in " ".join(cell["shell_commands"]) for cell in cell_analyses):
        notes.append("Dependency installation is embedded in notebook cells, so reproducibility depends on runtime package availability.")
    if any(cell["subprocess_calls"] for cell in cell_analyses):
        notes.append("subprocess-based installation or path manipulation introduces extra runtime coupling.")
    if errors:
        notes.append(f"Stored notebook outputs contain {len(errors)} execution error(s); treat those cells as unresolved at snapshot time.")
    if warnings:
        notes.append(f"Stored outputs include {len(warnings)} warning-like lines worth checking during reruns.")
    if not any(cell["cell_type"] == "markdown" for cell in cell_analyses):
        notes.append("Notebook contains no markdown commentary; intent must be inferred from code, comments, and outputs only.")
    if "YOLO(" in full_text and "segmentation_models_pytorch" in full_text:
        notes.append("Notebook depends on both object detection and segmentation stacks, increasing environment complexity.")
    if "torch.load" in full_text:
        notes.append("Checkpoint loading is embedded in the workflow; model file availability is a runtime prerequisite.")
    if not notes:
        notes.append("No special risk markers were inferred beyond the normal notebook-state caveats.")
    return notes


def enrich_notebook_differences(notebook_analyses: list[dict[str, Any]]) -> None:
    previous: dict[str, Any] | None = None
    for analysis in notebook_analyses:
        if previous is None:
            analysis["previous_diff"] = {
                "previous_name": None,
                "summary": "This is the first notebook in the mandated review order; no prior notebook exists for comparison.",
                "shared_cell_hashes": 0,
                "new_imports": [],
                "removed_imports": [],
                "new_models": [],
                "removed_models": [],
                "new_titles": [],
                "removed_titles": [],
            }
        else:
            current_hashes = set(analysis["cell_hashes"])
            previous_hashes = set(previous["cell_hashes"])
            current_titles = set(analysis["first_lines"])
            previous_titles = set(previous["first_lines"])
            current_imports = set(analysis["imports"])
            previous_imports = set(previous["imports"])
            current_models = set(analysis["model_references"])
            previous_models = set(previous["model_references"])

            analysis["previous_diff"] = {
                "previous_name": previous["source_name"],
                "summary": (
                    f"Compared with `{previous['source_name']}`, cell count changed from {previous['cell_count']} to {analysis['cell_count']}, "
                    f"stored output types changed from {sum(previous['output_type_counter'].values())} to {sum(analysis['output_type_counter'].values())}, "
                    f"and exact shared cell sources = {len(current_hashes & previous_hashes)}."
                ),
                "shared_cell_hashes": len(current_hashes & previous_hashes),
                "new_imports": sorted(current_imports - previous_imports),
                "removed_imports": sorted(previous_imports - current_imports),
                "new_models": sorted(current_models - previous_models),
                "removed_models": sorted(previous_models - current_models),
                "new_titles": sorted(current_titles - previous_titles),
                "removed_titles": sorted(previous_titles - current_titles),
            }
        previous = analysis


def analyze_model(path: Path, notebook_text_index: dict[str, str], used_slugs: set[str], manual_notes: dict[str, Any]) -> dict[str, Any]:
    ordered_index = model_review_order(path)
    slug = unique_slug(normalize_name(path.stem), used_slugs)
    load_summary = inspect_checkpoint(path)
    references = referencing_notebooks(path, notebook_text_index)
    archive_summary = inspect_zip_archive(path)

    return {
        "review_order": ordered_index,
        "source_name": path.name,
        "source_path": path,
        "report_name": f"{slug}.md",
        "size_bytes": path.stat().st_size,
        "modified_utc": utc_mtime(path),
        "sha256": sha256_file(path),
        "archive_summary": archive_summary,
        "references": references,
        "load_summary": load_summary,
        "manual_summary": manual_notes.get("manual_summary", []),
        "manual_risks": manual_notes.get("manual_risks", []),
        "editorial_status": "model-reviewed",
        "editorial_cell_note_count": 0,
        "editorial_output_note_count": 0,
        "summary_status": "n/a",
        "open_questions_count": 0,
        "confidence": "n/a",
        "delta_notes_count": 0,
        "editorial_complete": "yes",
    }


def inspect_checkpoint(path: Path) -> dict[str, Any]:
    try:
        import torch  # type: ignore
    except Exception as exc:  # pragma: no cover - environment-level fallback
        return {
            "status": "unavailable",
            "safe_load_strategy": "torch import failed in current environment",
            "error": f"{type(exc).__name__}: {exc}",
        }

    if path.name == "best.pt":
        return inspect_best_pt(path)

    try:
        obj = torch.load(path, map_location="cpu", weights_only=True)
        return summarize_loaded_object(obj, safe_load_strategy="torch.load(map_location='cpu', weights_only=True)")
    except Exception as exc:
        return {
            "status": "failed",
            "safe_load_strategy": "torch.load(map_location='cpu', weights_only=True)",
            "error": f"{type(exc).__name__}: {exc}",
        }


def inspect_best_pt(path: Path) -> dict[str, Any]:
    try:
        import torch  # type: ignore
    except Exception as exc:  # pragma: no cover - environment-level fallback
        return {
            "status": "unavailable",
            "safe_load_strategy": "torch import failed before best.pt inspection",
            "error": f"{type(exc).__name__}: {exc}",
        }

    try:
        torch.load(path, map_location="cpu", weights_only=True)
        obj = torch.load(path, map_location="cpu", weights_only=True)
        return summarize_loaded_object(obj, safe_load_strategy="torch.load(map_location='cpu', weights_only=True)")
    except Exception as initial_error:
        fallback = try_best_pt_with_temp_ultralytics(path)
        if fallback["status"] == "loaded":
            return fallback
        return {
            "status": "failed",
            "safe_load_strategy": (
                "Attempted torch.load(map_location='cpu', weights_only=True); "
                "then temporary venv with ultralytics safe-globals allowlist."
            ),
            "error": f"{type(initial_error).__name__}: {initial_error}",
            "fallback": fallback,
        }


def try_best_pt_with_temp_ultralytics(path: Path) -> dict[str, Any]:
    helper_code = textwrap.dedent(
        f"""
        import json
        import torch
        from torch.serialization import add_safe_globals
        from ultralytics import YOLO
        try:
            from ultralytics.nn.tasks import DetectionModel, SegmentationModel, ClassificationModel, PoseModel, OBBModel, RTDETRDetectionModel
            safe = [DetectionModel, SegmentationModel, ClassificationModel, PoseModel, OBBModel, RTDETRDetectionModel]
        except Exception:
            from ultralytics.nn.tasks import DetectionModel
            safe = [DetectionModel]
        add_safe_globals(safe)
        path = r\"{str(path)}\"

        PARAMETER_TERMS = {{'weight', 'bias', 'running_mean', 'running_var', 'num_batches_tracked'}}

        def family_name(key):
            parts = key.split('.')
            collected = []
            for part in parts:
                if part.isdigit():
                    continue
                if part in PARAMETER_TERMS and collected:
                    break
                collected.append(part)
                if len(collected) == 2:
                    break
            return '.'.join(collected) or parts[0]

        def state_dict_summary(state_dict):
            families = {{}}
            for key, value in state_dict.items():
                fam = family_name(key)
                entry = families.setdefault(fam, {{'count': 0, 'sample_keys': [], 'sample_tensors': []}})
                entry['count'] += 1
                if len(entry['sample_keys']) < 3:
                    entry['sample_keys'].append(key)
                if hasattr(value, 'shape') and len(entry['sample_tensors']) < 2:
                    entry['sample_tensors'].append({{
                        'key': key,
                        'shape': list(value.shape),
                        'dtype': str(value.dtype),
                    }})
            total_keys = len(state_dict)
            total_tensors = sum(1 for value in state_dict.values() if hasattr(value, 'shape'))
            total_parameters = int(sum(int(value.numel()) for value in state_dict.values() if hasattr(value, 'numel')))
            return {{
                'key_count': total_keys,
                'tensor_count': total_tensors,
                'parameter_count': total_parameters,
                'families': families,
            }}

        def summarize(obj):
            summary = {{'python_type': type(obj).__name__}}
            if hasattr(obj, 'state_dict'):
                sd = obj.state_dict()
                summary['state_dict'] = state_dict_summary(sd)
                if hasattr(obj, 'yaml') and isinstance(obj.yaml, dict):
                    summary['yaml_keys'] = list(obj.yaml.keys())[:30]
            elif isinstance(obj, dict):
                summary['top_level_keys'] = list(obj.keys())[:50]
                if obj and all(hasattr(v, 'shape') or isinstance(v, (int, float, str, bool)) for v in obj.values()):
                    tensor_values = {{k: v for k, v in obj.items() if hasattr(v, 'shape')}}
                    if tensor_values:
                        summary['state_dict'] = state_dict_summary(tensor_values)
            return summary

        results = []
        try:
            yolo = YOLO(path)
            yolo_summary = summarize(yolo.model)
            yolo_summary['loader'] = 'ultralytics.YOLO'
            yolo_summary['task'] = getattr(yolo, 'task', None)
            names = getattr(yolo.model, 'names', None)
            if isinstance(names, dict):
                yolo_summary['class_names'] = names
            results.append(yolo_summary)
        except Exception as yolo_error:
            results.append({{'loader': 'ultralytics.YOLO', 'error': str(yolo_error)}})

        try:
            obj = torch.load(path, map_location='cpu', weights_only=True)
            torch_summary = summarize(obj)
            torch_summary['loader'] = 'torch.load(weights_only=True)'
            results.append(torch_summary)
        except Exception as weights_error:
            results.append({{'loader': 'torch.load(weights_only=True)', 'error': str(weights_error)}})

        try:
            obj = torch.load(path, map_location='cpu', weights_only=False)
            torch_full_summary = summarize(obj)
            torch_full_summary['loader'] = 'torch.load(weights_only=False)'
            results.append(torch_full_summary)
        except Exception as full_error:
            results.append({{'loader': 'torch.load(weights_only=False)', 'error': str(full_error)}})

        print(json.dumps(results))
        """
    ).strip()

    with tempfile.TemporaryDirectory(prefix="file-audit-ultralytics-") as temp_dir:
        temp_path = Path(temp_dir)
        venv_dir = temp_path / "venv"
        helper_path = temp_path / "inspect_best_pt.py"
        helper_path.write_text(helper_code, encoding="utf-8")

        try:
            subprocess.run([sys.executable, "-m", "venv", "--system-site-packages", str(venv_dir)], check=True, capture_output=True, text=True)
            venv_python = venv_dir / ("Scripts" if os.name == "nt" else "bin") / ("python.exe" if os.name == "nt" else "python")
            install = subprocess.run(
                [str(venv_python), "-m", "pip", "install", "--disable-pip-version-check", "ultralytics==8.3.241"],
                check=False,
                capture_output=True,
                text=True,
            )
            if install.returncode != 0:
                return {
                    "status": "failed",
                    "safe_load_strategy": "Temporary venv with system site packages and pip install ultralytics==8.3.241",
                    "error": excerpt_text((install.stderr or install.stdout or "").strip(), 400),
                }
            inspect = subprocess.run([str(venv_python), str(helper_path)], check=False, capture_output=True, text=True)
            if inspect.returncode != 0:
                return {
                    "status": "failed",
                    "safe_load_strategy": "Temporary venv with ultralytics safe-globals allowlist",
                    "error": excerpt_text((inspect.stderr or inspect.stdout or "").strip(), 400),
                }
            payload = json.loads(inspect.stdout)
            successful = next((item for item in payload if 'state_dict' in item), None)
            if successful is not None:
                return {
                    "status": "loaded",
                    "safe_load_strategy": (
                        "Temporary trusted venv created with --system-site-packages; "
                        "installed ultralytics==8.3.241; attempted ultralytics.YOLO plus torch.load "
                        "with allowlisted ultralytics task models."
                    ),
                    "object_summary": successful,
                    "attempt_log": payload,
                }
            return {
                "status": "failed",
                "safe_load_strategy": "Temporary trusted venv with ultralytics helper attempts",
                "error": "No helper attempt produced a state_dict summary.",
                "attempt_log": payload,
            }
        except Exception as exc:
            return {
                "status": "failed",
                "safe_load_strategy": "Temporary trusted venv workflow for best.pt",
                "error": f"{type(exc).__name__}: {exc}",
            }


def summarize_loaded_object(obj: Any, safe_load_strategy: str) -> dict[str, Any]:
    summary = {
        "status": "loaded",
        "safe_load_strategy": safe_load_strategy,
        "python_type": type(obj).__name__,
    }

    if is_state_dict_like(obj):
        summary["state_dict"] = summarize_state_dict(obj)
        summary["top_level_keys"] = list(obj.keys())[:50]
        return summary

    if isinstance(obj, dict):
        summary["top_level_keys"] = list(obj.keys())[:50]
        top_level = {}
        for key, value in obj.items():
            top_level[key] = summarize_arbitrary_value(value)
        summary["top_level_summary"] = top_level
        return summary

    if hasattr(obj, "state_dict"):
        state_dict = obj.state_dict()
        summary["state_dict"] = summarize_state_dict(state_dict)
    return summary


def summarize_arbitrary_value(value: Any) -> dict[str, Any]:
    result = {"python_type": type(value).__name__}
    if isinstance(value, (int, float, str, bool)) or value is None:
        result["value"] = value
        return result
    if is_state_dict_like(value):
        result["state_dict"] = summarize_state_dict(value)
        return result
    if isinstance(value, dict):
        result["keys"] = list(value.keys())[:50]
        if "state" in value and isinstance(value["state"], dict):
            result["state_entries"] = len(value["state"])
        if "param_groups" in value and isinstance(value["param_groups"], list):
            result["param_group_count"] = len(value["param_groups"])
        return result
    if isinstance(value, list):
        result["length"] = len(value)
        return result
    if hasattr(value, "shape"):
        result["shape"] = list(value.shape)
        result["dtype"] = str(value.dtype)
        return result
    return result


def is_state_dict_like(obj: Any) -> bool:
    if not isinstance(obj, dict) or not obj:
        return False
    tensor_like = 0
    checked = 0
    for value in obj.values():
        checked += 1
        if hasattr(value, "shape") and hasattr(value, "dtype"):
            tensor_like += 1
        if checked >= 12:
            break
    return tensor_like == checked and checked > 0


def summarize_state_dict(state_dict: dict[str, Any]) -> dict[str, Any]:
    families: dict[str, dict[str, Any]] = {}
    total_parameters = 0
    tensor_count = 0
    for key, value in state_dict.items():
        family = infer_key_family(key)
        entry = families.setdefault(family, {"count": 0, "sample_keys": [], "sample_tensors": []})
        entry["count"] += 1
        if len(entry["sample_keys"]) < 3:
            entry["sample_keys"].append(key)
        if hasattr(value, "numel"):
            total_parameters += int(value.numel())
            tensor_count += 1
        if hasattr(value, "shape") and len(entry["sample_tensors"]) < 2:
            entry["sample_tensors"].append({"key": key, "shape": list(value.shape), "dtype": str(value.dtype)})
    return {
        "key_count": len(state_dict),
        "tensor_count": tensor_count,
        "parameter_count": total_parameters,
        "families": families,
    }


def infer_key_family(key: str) -> str:
    parts = key.split(".")
    collected = []
    for part in parts:
        if part.isdigit():
            continue
        if part in PARAMETER_TERMS and collected:
            break
        collected.append(part)
        if len(collected) == 2:
            break
    return ".".join(collected) if collected else parts[0]


def inspect_zip_archive(path: Path) -> dict[str, Any]:
    summary = {"is_zip_archive": zipfile.is_zipfile(path)}
    if not summary["is_zip_archive"]:
        return summary
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
    summary["entry_count"] = len(names)
    summary["sample_entries"] = names[:20]
    return summary


def referencing_notebooks(path: Path, notebook_text_index: dict[str, str]) -> list[str]:
    matches = []
    basename = path.name
    for notebook_name, text in notebook_text_index.items():
        if basename in text:
            matches.append(notebook_name)
    return matches


def notebook_review_order(path: Path) -> int:
    if path.name == f"{NOTEBOOK_PATTERN}.ipynb":
        return 1
    match = re.fullmatch(rf"{re.escape(NOTEBOOK_PATTERN)} \((\d+)\)\.ipynb", path.name)
    if not match:
        raise ValueError(f"Unexpected notebook name: {path.name}")
    return int(match.group(1)) + 1


def model_review_order(path: Path) -> int:
    model_names = [model.name for model in ordered_models(ROOT)]
    return len(ordered_notebooks(ROOT)) + model_names.index(path.name) + 1


def unique_slug(base: str, used: set[str]) -> str:
    candidate = base
    suffix = 2
    while candidate in used:
        candidate = f"{base}-{suffix}"
        suffix += 1
    used.add(candidate)
    return candidate


def normalize_name(name: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9._-]+", "-", name.replace(" ", "-"))
    normalized = re.sub(r"-{2,}", "-", normalized).strip("-")
    return normalized.lower()


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def utc_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat()


def render_notebook_report(analysis: dict[str, Any], all_notebooks: list[dict[str, Any]]) -> str:
    previous_diff = analysis["previous_diff"]
    lines = [
        f"# File Audit: `{analysis['source_name']}`",
        "",
        "## File Identity",
        "",
        kv_table(
            [
                ("Review order", str(analysis["review_order"])),
                ("Original path", analysis["source_name"]),
                ("Report path", f"docs/file-audit/notebooks/{analysis['report_name']}"),
                ("SHA-256", analysis["sha256"]),
                ("Size (bytes)", f"{analysis['size_bytes']:,}"),
                ("Modified (UTC)", analysis["modified_utc"]),
                ("Inferred role", analysis["inferred_role"]),
            ]
        ),
        "",
        "## Notebook Metadata",
        "",
        kv_table(
            [
                ("nbformat", str(analysis["nbformat"])),
                ("nbformat_minor", str(analysis["nbformat_minor"])),
                ("Cell count", str(analysis["cell_count"])),
                ("Code cells", str(analysis["code_cells"])),
                ("Markdown cells", str(analysis["markdown_cells"])),
                ("Raw cells", str(analysis["raw_cells"])),
                ("Extracted image outputs", str(analysis["image_output_count"])),
                ("Editorial cell notes", str(analysis["editorial_cell_note_count"])),
                ("Editorial output notes", str(analysis["editorial_output_note_count"])),
                ("Interpretation confidence", analysis["confidence"]),
                ("Open questions", str(analysis["open_questions_count"])),
                ("Editorial complete", analysis["editorial_complete"]),
                ("Kernel", json.dumps(analysis["kernelspec"], ensure_ascii=False) or "None"),
                ("Language info", json.dumps(analysis["language_info"], ensure_ascii=False) or "None"),
            ]
        ),
        "",
        "## Dependencies",
        "",
        bullet_block("Imports", analysis["imports"]),
        "",
        bullet_block("Packages requested via pip/install commands", analysis["pip_packages"]),
        "",
        "## Hard-Coded Paths And External Environment Markers",
        "",
        bullet_block("Environment markers", analysis["environment_flags"]),
        "",
        bullet_block("Literal paths / artifacts", analysis["paths"]),
        "",
        "## Symbols Defined",
        "",
        bullet_block("Functions", analysis["functions"]),
        "",
        bullet_block("Classes", analysis["classes"]),
        "",
        bullet_block("Constants / assigned names", analysis["constants"]),
        "",
        "## File Operations And Model Loads",
        "",
        bullet_block("File reads", analysis["file_reads"]),
        "",
        bullet_block("File writes", analysis["file_writes"]),
        "",
        bullet_block("Shell commands", analysis["shell_commands"]),
        "",
        bullet_block("subprocess calls", analysis["subprocess_calls"]),
        "",
        bullet_block("Model loads", analysis["model_loads"]),
        "",
        bullet_block("Model saves", analysis["model_saves"]),
        "",
        bullet_block("Model existence probes", analysis["model_probes"]),
        "",
        "## Stored Output Inventory",
        "",
        bullet_block("Output types", counter_lines(analysis["output_type_counter"])),
        "",
        bullet_block("MIME types", counter_lines(analysis["mime_counter"])),
        "",
        bullet_block("Exceptions captured in outputs", analysis["error_summaries"]),
        "",
        bullet_block("Warnings / warning-like lines", analysis["warning_messages"]),
    ]

    lines.extend(
        [
            "",
            "## Observed Dependency Summary",
            "",
            bullet_block("Referenced checkpoints", analysis["dependency_summary"]["referenced_checkpoints"]),
            "",
            bullet_block("Referenced datasets", analysis["dependency_summary"]["referenced_datasets"]),
            "",
            bullet_block("External files", analysis["dependency_summary"]["external_files"]),
            "",
            bullet_block("Required runtime assumptions", analysis["dependency_summary"]["runtime_assumptions"]),
            "",
            bullet_block("Outputs created or updated", analysis["dependency_summary"]["outputs_created"]),
            "",
            "## Phase 1 Closure Status",
            "",
            kv_table(
                [
                    ("Notebook summary", analysis["summary_status"]),
                    ("Editorial cell coverage", f"{analysis['editorial_cell_note_count']}/{analysis['cell_count']}"),
                    ("Editorial output translations", str(analysis["editorial_output_note_count"])),
                    ("Delta notes", str(analysis["delta_notes_count"])),
                    ("Open questions", str(analysis["open_questions_count"])),
                    ("Confidence", analysis["confidence"]),
                    ("Editorial complete", analysis["editorial_complete"]),
                ]
            ),
            "",
            "## Manual Interpretation",
            "",
            "Observed facts are listed in the structural sections above. The bullets below are editorial interpretation and historical inference.",
            "",
        ]
    )
    if analysis["notebook_summary"]:
        lines.extend([bullet_block("Notebook summary", analysis["notebook_summary"]), ""])
    if analysis["delta_notes"]:
        lines.extend([bullet_block("Delta notes", analysis["delta_notes"]), ""])
    lines.extend([bullet_block("Open questions", analysis["open_questions"]), ""])

    lines.extend(["## Differences Vs Previous Notebook In Review Order", ""])

    if previous_diff["previous_name"] is None:
        lines.extend(["- " + previous_diff["summary"], ""])
    else:
        lines.extend(
            [
                f"- Previous notebook: `{previous_diff['previous_name']}`",
                f"- {previous_diff['summary']}",
                f"- New imports: {join_inline(previous_diff['new_imports'])}",
                f"- Removed imports: {join_inline(previous_diff['removed_imports'])}",
                f"- New model refs: {join_inline(previous_diff['new_models'])}",
                f"- Removed model refs: {join_inline(previous_diff['removed_models'])}",
                f"- New first-line titles: {join_inline(previous_diff['new_titles'])}",
                f"- Removed first-line titles: {join_inline(previous_diff['removed_titles'])}",
                "",
            ]
        )

    lines.extend(
        [
            "## Risks And Notes",
            "",
        ]
    )
    lines.extend(f"- {note}" for note in analysis["notes"])
    lines.extend(["", "## Cell-By-Cell Audit", ""])

    for cell in analysis["cell_analyses"]:
        lines.extend(render_cell_section(cell))
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def render_cell_section(cell: dict[str, Any]) -> list[str]:
    lines = [f"### Cell {cell['index']}", ""]
    lines.append(
        kv_table(
            [
                ("Cell type", cell["cell_type"]),
                ("Execution count", str(cell["execution_count"])),
                ("First non-empty line", inline_code(cell["first_line"]) if cell["first_line"] else "None"),
                ("Role summary", cell["source_summary"]),
            ]
        )
    )
    if cell["editorial_note"]:
        lines.extend(["", bullet_block("Editorial interpretation", [cell["editorial_note"]])])
    lines.extend(
        [
            "",
            bullet_block("Imports", cell["imports"]),
            "",
            bullet_block("Functions defined", cell["functions"]),
            "",
            bullet_block("Classes defined", cell["classes"]),
            "",
            bullet_block("Constants / bindings", [f"{key} = {value}" for key, value in sorted(cell["constant_bindings"].items())] or cell["constants"]),
            "",
            bullet_block("Paths mentioned", cell["paths"]),
            "",
            bullet_block("File reads", cell["file_reads"]),
            "",
            bullet_block("File writes", cell["file_writes"]),
            "",
            bullet_block("Shell commands", cell["shell_commands"]),
            "",
            bullet_block("subprocess calls", cell["subprocess_calls"]),
            "",
            bullet_block("Model loads", cell["model_loads"]),
            "",
            bullet_block("Model saves", cell["model_saves"]),
            "",
            bullet_block("Model existence probes", cell["model_probes"]),
            "",
            bullet_block("Stored outputs", cell["output_items"]),
            "",
            bullet_block("Exceptions", cell["exceptions"]),
            "",
            bullet_block("Warnings", cell["warnings"]),
        ]
    )
    if cell["output_artifacts"]:
        lines.extend(["", bullet_block("Output artifacts", cell["output_artifacts"])])
    if cell["output_notes"]:
        lines.extend(["", bullet_block("Output interpretation", cell["output_notes"])])
    return lines


def render_model_report(analysis: dict[str, Any]) -> str:
    load_summary = analysis["load_summary"]
    lines = [
        f"# File Audit: `{analysis['source_name']}`",
        "",
        "## File Identity",
        "",
        kv_table(
            [
                ("Review order", str(analysis["review_order"])),
                ("Original path", analysis["source_name"]),
                ("Report path", f"docs/file-audit/models/{analysis['report_name']}"),
                ("SHA-256", analysis["sha256"]),
                ("Size (bytes)", f"{analysis['size_bytes']:,}"),
                ("Modified (UTC)", analysis["modified_utc"]),
            ]
        ),
        "",
        "## Archive Layout",
        "",
        bullet_block(
            "Archive summary",
            [
                f"is_zip_archive={analysis['archive_summary'].get('is_zip_archive')}",
                f"entry_count={analysis['archive_summary'].get('entry_count', 'n/a')}",
            ]
            + [f"sample entry: {entry}" for entry in analysis["archive_summary"].get("sample_entries", [])],
        ),
        "",
        "## Referencing Notebooks",
        "",
        bullet_block("Notebook references", analysis["references"]),
        "",
        "## Safe Load Strategy",
        "",
        bullet_block("Strategy", [load_summary.get("safe_load_strategy", "None")]),
        "",
    ]

    if analysis["manual_summary"]:
        lines.extend(
            [
                "## Manual Interpretation",
                "",
                bullet_block("Analyst notes", analysis["manual_summary"]),
                "",
            ]
        )

    if load_summary.get("status") == "loaded":
        lines.extend(render_model_summary(load_summary))
    else:
        lines.extend(
            [
                bullet_block("Load status", [load_summary.get("status", "failed")]),
                "",
                bullet_block("Error", [load_summary.get("error", "None")]),
                "",
            ]
        )
        if load_summary.get("fallback"):
            fallback = load_summary["fallback"]
            lines.extend(
                [
                    "## Fallback Attempt",
                    "",
                    bullet_block("Fallback status", [fallback.get("status", "failed")]),
                    "",
                    bullet_block("Fallback strategy", [fallback.get("safe_load_strategy", "None")]),
                    "",
                    bullet_block("Fallback error", [fallback.get("error", "None")]),
                    "",
                ]
            )
            if fallback.get("attempt_log"):
                lines.extend(
                    [
                        bullet_block("Fallback attempt log", [json.dumps(item, ensure_ascii=False) for item in fallback["attempt_log"]]),
                        "",
                    ]
                )

    if analysis["manual_risks"]:
        lines.extend(
            [
                "## Inspection Limits And Risks",
                "",
                bullet_block("Notes", analysis["manual_risks"]),
                "",
            ]
        )

    return "\n".join(lines).strip() + "\n"


def render_model_summary(load_summary: dict[str, Any]) -> list[str]:
    lines = [
        bullet_block("Load status", [load_summary.get("status", "loaded")]),
        "",
        bullet_block("Python type", [load_summary.get("python_type", load_summary.get("object_summary", {}).get("python_type", "unknown"))]),
        "",
    ]
    state_dict = load_summary.get("state_dict")
    if state_dict is None and "object_summary" in load_summary:
        state_dict = load_summary["object_summary"].get("state_dict")
    top_level_keys = load_summary.get("top_level_keys")
    if top_level_keys is None and "object_summary" in load_summary:
        top_level_keys = load_summary["object_summary"].get("top_level_keys")
    if top_level_keys:
        lines.extend([bullet_block("Top-level keys", top_level_keys), ""])
    top_level_summary = load_summary.get("top_level_summary")
    if top_level_summary:
        lines.extend([bullet_block("Top-level value summary", [f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in top_level_summary.items()]), ""])
    if state_dict:
        lines.extend(
            [
                "## State Dict Summary",
                "",
                kv_table(
                    [
                        ("Key count", str(state_dict.get("key_count", "n/a"))),
                        ("Tensor count", str(state_dict.get("tensor_count", "n/a"))),
                        ("Parameter count", f"{state_dict.get('parameter_count', 'n/a'):,}" if isinstance(state_dict.get("parameter_count"), int) else str(state_dict.get("parameter_count", "n/a"))),
                    ]
                ),
                "",
                "### Prefix Families",
                "",
            ]
        )
        for family, family_summary in sorted(state_dict.get("families", {}).items()):
            lines.append(f"#### `{family}`")
            lines.append("")
            lines.append(f"- Key count: {family_summary.get('count')}")
            lines.append(f"- Sample keys: {join_inline(family_summary.get('sample_keys', []))}")
            for sample in family_summary.get("sample_tensors", []):
                lines.append(f"- Sample tensor: `{sample['key']}` shape={sample['shape']} dtype={sample['dtype']}")
            lines.append("")
    if load_summary.get("attempt_log"):
        lines.extend(
            [
                "## Loader Attempt Log",
                "",
                bullet_block("Attempt records", [json.dumps(item, ensure_ascii=False) for item in load_summary["attempt_log"]]),
                "",
            ]
        )
    return lines


def write_readme(notebooks: list[dict[str, Any]], models: list[dict[str, Any]], manifest_rows: list[dict[str, str]]) -> None:
    notebook_groups = group_notebooks_by_family(notebooks)
    chronology = build_chronology(notebooks)
    notebooks_with_questions = sum(1 for notebook in notebooks if notebook["open_questions_count"] > 0)
    confidence_counts = Counter(notebook["confidence"] for notebook in notebooks)
    lines = [
        "# File Audit Index",
        "",
        "This directory contains a deterministic file-by-file audit for every notebook and every checkpoint found in the project root at generation time.",
        "",
        "## Audit Scope",
        "",
        f"- Notebook files: {len(notebooks)}",
        f"- Model files: {len(models)}",
        f"- Total audited files: {len(manifest_rows)}",
        "- Inspection mode: static notebook JSON analysis + stored output inspection + read-only checkpoint inspection.",
        f"- Extracted notebook image outputs: {sum(notebook['image_output_count'] for notebook in notebooks)}",
        f"- Notebooks with full cell review: {sum(1 for notebook in notebooks if notebook['editorial_status'] == 'cell-reviewed')}/{len(notebooks)}",
        f"- Image/HTML outputs with manual translations: {sum(notebook['editorial_output_note_count'] for notebook in notebooks)}",
        f"- Models with manual interpretation: {sum(1 for model in models if model['manual_summary'])}/{len(models)}",
        f"- Notebooks with unresolved open questions: {notebooks_with_questions}/{len(notebooks)}",
        f"- Interpretation confidence split: high={confidence_counts.get('high', 0)}, medium={confidence_counts.get('medium', 0)}, low={confidence_counts.get('low', 0)}",
        "- Manifest: [manifest.csv](manifest.csv)",
        "- Extracted image artifacts: [image-outputs/](image-outputs/)",
        "- Checkpoint companion summary: [checkpoint-companion-summary.md](checkpoint-companion-summary.md)",
        "- Phase 2 synthesis seed: [../final_synthesis_outline.md](../final_synthesis_outline.md)",
        "",
        "## Phase 1 Closure Standard",
        "",
        "- A notebook is Phase-1 complete only when a notebook summary exists, every source cell has exactly one editorial note, output translations remain preserved, delta notes exist, open questions are tracked, a confidence level is assigned, and the manifest marks the notebook as editorially complete.",
        "- Observed facts remain in the structural sections of each report; the manual layer is reserved for editorial interpretation, historical framing, and unresolved questions.",
        "",
        "## Completion Table",
        "",
        "| Review order | Source file | Type | Report | Status | Editorial | Confidence | Complete |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    for row in manifest_rows:
        lines.append(
            f"| {row['review_order']} | `{row['source_name']}` | {row['entry_type']} | [{row['report_path']}]({row['report_path']}) | {row['status']} | {row['editorial_status']} | {row['confidence']} | {row['editorial_complete']} |"
        )

    lines.extend(["", "## Notebook Families", ""])
    for family, family_notebooks in notebook_groups.items():
        lines.append(f"### {family}")
        lines.append("")
        for analysis in family_notebooks:
            report = f"notebooks/{analysis['report_name']}"
            lines.append(f"- [{analysis['source_name']}]({report})")
        lines.append("")

    lines.extend(["## Model Reports", ""])
    for analysis in models:
        lines.append(f"- [{analysis['source_name']}](models/{analysis['report_name']})")

    lines.extend(["", "## Short Evolution Timeline", ""])
    for item in chronology:
        lines.append(f"- {item}")

    lines.extend(["", "## Snapshot Characteristics", ""])
    lines.append("- Almost every notebook is code-only; markdown documentation is effectively absent.")
    lines.append("- Kaggle-specific paths and dependency bootstrap steps recur throughout the notebook series.")
    lines.append("- Later notebooks increasingly consolidate around YOLO + segmentation inference pipelines and checkpoint loading.")
    lines.append("- Image-bearing notebooks now include explicit prose translations tied to extracted PNG artifacts instead of only figure-size placeholders.")
    lines.append("- The audit reports intentionally preserve per-file detail even when multiple notebook revisions are near-duplicates.")

    (OUTPUT_ROOT / "README.md").write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def compact_items(items: list[str], limit: int) -> list[str]:
    return dedupe_preserve_order([item for item in items if item])[:limit]


def extract_checkpoint_basenames(values: list[str]) -> list[str]:
    results = []
    pattern = re.compile(r"([A-Za-z0-9_./() -]+\.(?:pt|pth))", re.IGNORECASE)
    for value in values:
        for match in pattern.findall(str(value)):
            basename = Path(match.strip(" `\"'")).name
            if basename.lower().endswith((".pt", ".pth")):
                results.append(basename)
    return dedupe_preserve_order(results)


def summarize_dataset_dependencies(paths: list[str], file_reads: list[str]) -> list[str]:
    candidates = []
    for item in paths + file_reads:
        lowered = item.lower()
        if (
            "/kaggle/input" in lowered
            or lowered.endswith((".csv", ".parquet", ".json", ".hea", ".mat", ".dat", ".wfdb"))
        ):
            candidates.append(item)
    return compact_items(candidates, limit=8)


def summarize_runtime_assumptions(
    imports: list[str],
    shell_commands: list[str],
    environment_flags: list[str],
    paths: list[str],
) -> list[str]:
    assumptions = []
    if shell_commands:
        assumptions.append("Assumes in-notebook shell execution is allowed for package installation or environment repair.")
    if any("pip install" in command for command in shell_commands):
        assumptions.append("Assumes in-notebook dependency installation is permitted.")
    if any("/kaggle/input" in path for path in paths):
        assumptions.append("Assumes Kaggle input mounts are available.")
    if any(path.lower().endswith(".whl") for path in paths):
        assumptions.append("Assumes offline wheel files are available under the input mounts.")
    if "YOLO loader" in environment_flags:
        assumptions.append("Assumes ultralytics/YOLO is available for lead localization.")
    if "torch.load" in environment_flags:
        assumptions.append("Assumes PyTorch checkpoint loading is available.")
    if "segmentation_models_pytorch" in imports or "segmentation_models_pytorch" in environment_flags:
        assumptions.append("Assumes segmentation_models_pytorch is available for segmentation model construction.")
    if any("/kaggle/working" in path for path in paths):
        assumptions.append("Assumes a writable working directory such as /kaggle/working exists.")
    return dedupe_preserve_order(assumptions)


def build_checkpoint_companion_entries(notebooks: list[dict[str, Any]], models: list[dict[str, Any]]) -> list[dict[str, Any]]:
    audited_lookup = {model["source_name"]: model for model in models}
    references: defaultdict[str, set[str]] = defaultdict(set)

    for notebook in notebooks:
        checkpoint_refs = extract_checkpoint_basenames(
            notebook["model_references"] + notebook["paths"] + notebook["file_reads"] + notebook["file_writes"] + notebook["model_saves"]
        )
        for ref in checkpoint_refs:
            references[ref].add(notebook["source_name"])

    all_checkpoints = sorted(set(references) | set(audited_lookup))
    entries = []
    for checkpoint_name in all_checkpoints:
        model = audited_lookup.get(checkpoint_name)
        entries.append(
            {
                "checkpoint_name": checkpoint_name,
                "notebooks": sorted(references.get(checkpoint_name, set())),
                "audited_model": model,
                "interpreted_role": interpret_checkpoint_role(checkpoint_name, model),
                "development_phase": infer_checkpoint_phase(checkpoint_name, model),
                "confidence": infer_checkpoint_confidence(checkpoint_name, model),
            }
        )
    return entries


def interpret_checkpoint_role(checkpoint_name: str, model: dict[str, Any] | None) -> str:
    if model and model.get("manual_summary"):
        return str(model["manual_summary"][0])

    lowered = checkpoint_name.lower()
    if checkpoint_name == "best.pt":
        return "Primary YOLO lead-detector artifact used to localize the 12 ECG lead regions before segmentation."
    if "phase10" in lowered and "deeplab" in lowered:
        return "DeepLabV3+ ensemble competitor for the phase-10 trace-mask objective."
    if "phase10" in lowered and "efficientnet" in lowered:
        return "EfficientNet-B3 ensemble competitor for the phase-10 trace-mask objective."
    if "phase10" in lowered:
        return "Primary phase-10 segmentation checkpoint reused across many later notebooks."
    if "phase9" in lowered and "checkpoint" in lowered:
        return "Full resumable EfficientNet-B3 phase-9 training checkpoint with optimizer and EMA state."
    if "phase9" in lowered and "effb3" in lowered:
        return "Inference-oriented EfficientNet-B3 export from the phase-9 DDP branch."
    if "phase2" in lowered:
        return "Intermediate hardening-phase segmentation checkpoint referenced by the geometry and quality-boost notebooks."
    if "real_data" in lowered:
        return "Real-data fine-tuning checkpoint from the early synthetic-to-real adaptation branch."
    if lowered.startswith("temp_effnet_base"):
        return "Bootstrap EfficientNet base weights used as an initializer before the explicit phase-10 competitor training begins."
    if lowered.startswith("temp_deeplab_base"):
        return "Bootstrap DeepLab base weights used as an initializer before the explicit phase-10 competitor training begins."
    return "Checkpoint referenced by notebooks, but its exact historical role remains partly implicit in code rather than in explicit prose."


def infer_checkpoint_phase(checkpoint_name: str, model: dict[str, Any] | None) -> str:
    lowered = checkpoint_name.lower()
    if checkpoint_name == "best.pt":
        return "Lead detector deployment branch"
    if "phase10" in lowered:
        return "Phase 10 pseudo-label / real-image fine-tuning era"
    if "phase9" in lowered:
        return "Phase 9 EfficientNet-B3 DDP era"
    if "phase2" in lowered:
        return "Phase 2 hardening era"
    if "real_data" in lowered:
        return "Early real-data adaptation branch"
    if lowered.startswith("temp_"):
        return "Ensemble bootstrap initialization"
    if model and model.get("source_name"):
        return "Bundled checkpoint artifact"
    return "Unclassified experimental reference"


def infer_checkpoint_confidence(checkpoint_name: str, model: dict[str, Any] | None) -> str:
    lowered = checkpoint_name.lower()
    if model and model.get("manual_summary"):
        if "duplicate" in " ".join(model.get("manual_risks", [])).lower():
            return "medium"
        return "high"
    if lowered.startswith("temp_"):
        return "low"
    if any(term in lowered for term in ["phase10", "phase9", "phase2", "best.pt", "real_data"]):
        return "medium"
    return "low"


def write_checkpoint_companion_summary(notebooks: list[dict[str, Any]], models: list[dict[str, Any]]) -> None:
    entries = build_checkpoint_companion_entries(notebooks, models)
    lines = [
        "# Checkpoint Companion Summary",
        "",
        "This is the Phase 1 closure cross-reference for checkpoints mentioned across the notebook series. It is intentionally lighter than the full model reports and is meant to support later synthesis work.",
        "",
    ]
    for entry in entries:
        lines.extend(
            [
                f"## `{entry['checkpoint_name']}`",
                "",
                f"- Audited artifact in bundle: {'yes' if entry['audited_model'] else 'no'}",
                f"- Referencing notebooks: {join_inline(entry['notebooks'])}",
                f"- Interpreted role: {entry['interpreted_role']}",
                f"- Development phase: {entry['development_phase']}",
                f"- Interpretation confidence: {entry['confidence']}",
            ]
        )
        if entry["audited_model"]:
            lines.append(f"- Model report: [models/{entry['audited_model']['report_name']}](models/{entry['audited_model']['report_name']})")
        lines.append("")
    CHECKPOINT_COMPANION_OUTPUT.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def write_synthesis_outline(notebooks: list[dict[str, Any]], models: list[dict[str, Any]]) -> None:
    lines = [
        "# Phase 2 Synthesis Seed",
        "",
        "This file is a scaffold for Phase 2 synthesis only. It is not the final narrative and should not be treated as a completed cross-notebook analysis.",
        "",
        "## Project Timeline Headings",
        "",
        "- Early monolithic exploration: main notebook.",
        "- Compact proof-of-concept consolidation: notebook (1).",
        "- Synthetic-to-real staged research pipeline: notebooks (2) through (6).",
        "- Architecture hardening and combat-detector era: notebooks (7) through (9).",
        "- Compact deployment and robustness iteration: notebooks (10) through (41).",
        "- Ensemble and competitor checkpoint branch: notebook (42) and its compact descendants (43) through (48).",
        "- EfficientNet-B3 integration and modular finalization: notebooks (49) through (56).",
        "",
        "## Renderer Evolution",
        "",
        "- Track how the renderer moves from synthetic data generation into a persistent qualitative debugging surface in compact deployment notebooks.",
        "- Record when the renderer stops being a training dependency and becomes primarily an interpretation and quality-control tool.",
        "",
        "## Model Evolution",
        "",
        "- Baseline synthetic segmentation branch.",
        "- Real-data and pseudo-label fine-tuning branch.",
        "- Phase-7 and phase-8 architecture and optimization experiments.",
        "- Phase-10 dominant checkpoint reuse.",
        "- EfficientNet-B3 and DeepLabV3+ competitor branch from notebook (42).",
        "- EfficientNet-B3 deployment integration in notebooks (49) through (56).",
        "",
        "## Inference Evolution",
        "",
        "- Viterbi and dynamic-programming signal extraction prototypes.",
        "- Geometry and calibration-aware reconstruction.",
        "- YOLO-assisted lead localization.",
        "- Compact no-internet deployment shells.",
        "- Ensemble and checkpoint-routing inference variants.",
        "- Modular final execution flow in notebook (56).",
        "",
        "## Checkpoint Map",
        "",
        f"- Primary cross-reference: [file-audit/checkpoint-companion-summary.md](file-audit/checkpoint-companion-summary.md)",
        "- Confirm which checkpoints are bundled artifacts versus notebook-only references before writing Phase 2 lineage claims.",
        "",
        "## Terminology Glossary Seed",
        "",
        "| Term | Working definition for synthesis |",
        "| --- | --- |",
        "| notebook | One saved `.ipynb` revision in the ordered development chain. |",
        "| revision | A notebook that changes the immediately prior workflow in the sequence. |",
        "| phase | The project-local stage label used in checkpoint or cell naming, such as phase 2, phase 7, phase 8, phase 9, or phase 10. |",
        "| experiment | A bounded branch of notebook work that tests a new model, loss, calibration strategy, or inference policy. |",
        "| checkpoint | A saved `.pt` or `.pth` artifact used for detector or segmentation reuse. |",
        "| renderer | The code path that rasterizes synthetic ECG signals or provides visual debugging views of masks and recovered traces. |",
        "| teacher | A model or prior pipeline whose outputs are used to guide another stage, often through pseudo-label generation. |",
        "| student | The model trained or fine-tuned using synthetic labels, pseudo-labels, or inherited checkpoint knowledge. |",
        "| pseudo-labeling | Generating approximate supervision from existing models or heuristic pipelines on real images. |",
        "| lead detector | The YOLO-based localization model that finds ECG lead regions on a page before segmentation. |",
        "| segmentation | Predicting a foreground trace mask from an ECG crop or lead image. |",
        "| trace extraction | Turning a predicted mask or probability map into a one-dimensional ECG waveform. |",
        "| post-processing | Any path-cleaning, smoothing, gating, calibration, or formatting step applied after raw model output. |",
        "| calibration | Estimating paper grid spacing, scale, and orientation so extracted signals can be mapped back to plausible physical units. |",
        "| inference pipeline | The end-to-end chain that loads inputs, localizes leads, segments traces, extracts waveforms, and writes submission output. |",
        "",
        "## Phase 2 Preparation Notes",
        "",
        "- Use notebook-level open questions and confidence levels as synthesis risk markers instead of assuming every revision is equally certain.",
        "- Treat the structural sections in the audit reports as observed facts and the manual interpretation sections as higher-level inference.",
        "- Reconcile checkpoint lineage with the companion summary before writing any final timeline claims.",
    ]
    SYNTHESIS_OUTLINE_OUTPUT.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def group_notebooks_by_family(notebooks: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for analysis in notebooks:
        groups[analysis["inferred_role"]].append(analysis)
    return dict(sorted(groups.items(), key=lambda item: (len(item[1]) * -1, item[0].lower())))


def build_chronology(notebooks: list[dict[str, Any]]) -> list[str]:
    timeline = []
    current_role = None
    start_name = None
    last_name = None
    count = 0
    for analysis in notebooks:
        role = analysis["inferred_role"]
        if role != current_role:
            if current_role is not None:
                timeline.append(f"`{start_name}` -> `{last_name}` ({count} notebook(s)): {current_role}")
            current_role = role
            start_name = analysis["source_name"]
            count = 0
        last_name = analysis["source_name"]
        count += 1
    if current_role is not None and start_name is not None and last_name is not None:
        timeline.append(f"`{start_name}` -> `{last_name}` ({count} notebook(s)): {current_role}")
    return timeline


def kv_table(rows: list[tuple[str, str]]) -> str:
    lines = ["| Field | Value |", "| --- | --- |"]
    for key, value in rows:
        lines.append(f"| {escape_md(key)} | {escape_md(value)} |")
    return "\n".join(lines)


def bullet_block(title: str, items: list[str]) -> str:
    if not items:
        return f"**{title}**\n\n- None"
    lines = [f"**{title}**", ""]
    for item in items:
        lines.append(f"- {item}")
    return "\n".join(lines)


def counter_lines(counter_dict: dict[str, int]) -> list[str]:
    if not counter_dict:
        return []
    return [f"{key}: {value}" for key, value in sorted(counter_dict.items(), key=lambda item: (-item[1], item[0]))]


def join_inline(items: list[str]) -> str:
    return ", ".join(f"`{item}`" for item in items) if items else "None"


def inline_code(value: str) -> str:
    if not value:
        return "None"
    return f"`{value}`"


def escape_md(value: str) -> str:
    return value.replace("|", "\\|")


def dedupe_preserve_order(values: list[str]) -> list[str]:
    seen = set()
    result = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


if __name__ == "__main__":
    main()

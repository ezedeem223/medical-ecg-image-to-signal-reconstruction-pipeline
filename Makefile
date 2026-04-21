PYTHON ?= python

.PHONY: install install-dev lint test run validate

install:
	$(PYTHON) -m pip install -e .
	$(PYTHON) -m pip install -r requirements.txt

install-dev:
	$(PYTHON) -m pip install -e .
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m pip install -r requirements-dev.txt

lint:
	ruff check .

test:
	pytest

run:
	$(PYTHON) -m ecg_digitizer.cli run --config configs/runtime.default.yaml

validate:
	$(PYTHON) -m ecg_digitizer.cli validate --config configs/runtime.default.yaml --submission results/submission.csv

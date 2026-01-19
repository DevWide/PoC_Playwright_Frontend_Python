# =========================
# Project configuration
# =========================
VENV=venv
PYTHON=python
PIP=$(VENV)/bin/pip
ACTIVATE=. $(VENV)/bin/activate

# =========================
# Targets
# =========================

.PHONY: help install test test-ci clean

help:
	@echo "Available commands:"
	@echo "  make install   - Create venv and install dependencies"
	@echo "  make test      - Run tests locally (headed)"
	@echo "  make test-ci   - Run tests for CI (headless)"
	@echo "  make clean     - Remove virtual environment and cache"

# -------------------------
# Setup environment
# -------------------------
install:
	$(PYTHON) -m venv $(VENV)
	$(ACTIVATE) && pip install --upgrade pip
	$(ACTIVATE) && pip install -r requirements.txt
	$(ACTIVATE) && playwright install --with-deps

# -------------------------
# Run tests (local)
# -------------------------
test:
	$(ACTIVATE) && pytest --cache-clear

# -------------------------
# Run tests (CI)
# -------------------------
test-ci:	
	ENV=prod HEADLESS=true pytest --cache-clear

# -------------------------
# Clean project
# -------------------------
clean:
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -rf __pycache__

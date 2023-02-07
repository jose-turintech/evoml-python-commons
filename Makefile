# Makefile related to main project
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────

SHELL := bash

# --------------------------------------------------------------------------------------------------------------------
# --- CONFIGURATION
# --------------------------------------------------------------------------------------------------------------------

# Building
PYTHON ?= python3.8
BUILDTOOL ?= wheel  # expected: {wheel,nuitka}


# --------------------------------------------------------------------------------------------------------------------
# --- PATHS
# --------------------------------------------------------------------------------------------------------------------

MK_FILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
ROOT_PATH := $(realpath $(dir $(MK_FILE_PATH)))

SETUP_PATH = $(ROOT_PATH)/setup
SETUP_CONF_PATH = $(ROOT_PATH)/setup.cfg
TOML_CONF_PATH = $(ROOT_PATH)/pyproject.toml

MAKEFILE_PATH = $(SETUP_PATH)/Makefile

SRC_PATH = $(ROOT_PATH)/src
TESTS_PATH = $(ROOT_PATH)/tests

LINT_PATHS = $(SRC_PATH) $(TESTS_PATH)

# Temporary files to check improvements evolution
CHECK_FILE = $(ROOT_PATH)/docs/check.log
CHECK_BEFORE_FILE = $(ROOT_PATH)/docs/check_before.log


# --------------------------------------------------------------------------------------------------------------------
# --- OPTIONS
# --------------------------------------------------------------------------------------------------------------------

.PHONY: clean-pyc clean-build docs

help: ## This help.
	@echo " Usage: make <task>"
	@echo "   task options:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "	\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# --------------- Main

clean: clean-build clean-dist clean-pyc clean-lint clean-test

clean-dist: ## Remove 'dist' folder.
	@rm -fr dist/

clean-build: ## Remove construction artifacts, except 'dist' folder.
	@find $(ROOT_PATH) -name 'build' -exec rm -rf {} +
	@find $(ROOT_PATH) -name '*.egg-info' -exec rm -rf {} +

clean-pyc: ## Remove Python file artifacts.
	@find $(ROOT_PATH) -name '*.pyc' -exec rm -f {} +
	@find $(ROOT_PATH) -name '*.pyo' -exec rm -f {} +
	@find $(ROOT_PATH) -name '*~' -exec rm -f {} +

clean-lint: # Remove the temporary files generated when executing the tests.
	@find $(ROOT_PATH) -name '.mypy_cache' -exec rm -rf {} +

clean-test: # Remove the temporary files generated when executing the tests.
	@find $(ROOT_PATH) -name '.pytest_cache' -exec rm -rf {} +
	@find $(ROOT_PATH) -name '.coverage*' ! -name ".coveragerc" -exec rm -rf {} +

lint: ## Check style with flake8 and pylint.
	@echo ""
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@echo "─── Checking the project code style [flake8]"
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@flake8 --config=$(SETUP_CONF_PATH) $(LINT_PATHS) || echo

	@echo ""
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@echo "─── Checking the project code style [pylint]"
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@pylint --rcfile=$(SETUP_CONF_PATH) $(LINT_PATHS) || echo

	@$(MAKE) -s clean-lint

test: ## Run tests quickly with the default Python.
	@PYTHONPATH=$(SRC_PATH) pytest -rfs $(TESTS_PATH) || true
	@$(MAKE) -s clean-test

type-check: ## Run type checking using mypy.
	@echo ""
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@echo "─── Checking the project code style [mypy]"
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@mypy $(LINT_PATHS) --config-file $(SETUP_CONF_PATH) || true
	@$(MAKE) -s clean-lint

format-check: ## Run format checks using black.
	@black $(LINT_PATHS) --check --diff --verbose --config $(TOML_CONF_PATH) || true

format-apply: ## Apply the black format to all the code.
	@black $(LINT_PATHS) --verbose --config $(TOML_CONF_PATH) || true

check-all: ## Run all clean code checks.
	@$(MAKE) -s format-apply
	@$(MAKE) -s lint
	@$(MAKE) -s type-check
	@$(MAKE) -s test

check-all-file: ## Run all clean code checks and save the result to a file.
	@mv $(CHECK_FILE) $(CHECK_BEFORE_FILE) | true
	@$(MAKE) -s check-all 2>&1 | tee $(CHECK_FILE)

# --------------- Setup

req-install: ## Install all the requirements in the activated local environment.
	@make -s -f $(MAKEFILE_PATH) install-req

req-install-prod: ## Install the production required libraries in the activated local environment.
	@make -s -f $(MAKEFILE_PATH) install-req-prod

req-remove: ## Uninstall all the libraries installed in the Python environment.
	@make -s -f $(MAKEFILE_PATH) remove-req

req-clean: ## Remove all items from the pip cache.
	@make -s -f $(MAKEFILE_PATH) cache-purge

# --------------- Package

package: clean ## Package the library as a .whl file.
	@echo ""
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@echo "─── Setup bdist_$(BUILDTOOL)"
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@PYTHONPATH=$(SRC_PATH) python setup.py bdist_$(BUILDTOOL)
	@$(MAKE) -s clean-build
	@echo ""
	@ls -l dist
	@echo ""


.DEFAULT_GOAL := help
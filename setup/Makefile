# Makefile related to requirements
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
SHELL := bash

# --------------------------------------------------------------------------------------------------------------------
# --- REQUIREMENTS
# --------------------------------------------------------------------------------------------------------------------

MK_FILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
SETUP_PATH := $(realpath $(dir $(MK_FILE_PATH)))

REQ_DIST =
REQ_FILES = requirements.txt
REQ_FILES_DEV = requirements_develop.txt

REQ_FREEZE = $(SETUP_PATH)/requirements_freeze.txt
REQ_PIPDEPTREE = $(SETUP_PATH)/requirements_pipdeptree.txt


# --------------------------------------------------------------------------------------------------------------------
# --- OPTIONS
# --------------------------------------------------------------------------------------------------------------------

# HELP. This will output the help for each task
.PHONY: help

help: ## This help.
	@echo " Usage: make <task>"
	@echo "   task options:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "	\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install-req-prod: ## Install the production required libraries in the activated local environment.
	@echo "──────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@echo "─── Install requirements: $(REQ_DIST) $(REQ_FILES)"
	@echo "──────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@$(foreach var,$(REQ_DIST),pip install -U $(var) || (echo "install failed $?");)
	@$(foreach var,$(REQ_FILES),pip install -U -r $(SETUP_PATH)/$(var) || (echo "install failed $?");)
	pip freeze > $(REQ_FREEZE)

install-req: install-req-prod ## Install all the requirements in the activated local environment.
	@echo "──────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@echo "─── Install requirements: $(REQ_FILES_DEV)"
	@echo "──────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@$(foreach var,$(REQ_FILES_DEV),pip install -U -r $(SETUP_PATH)/$(var) || (echo "install failed $?");)
	pip freeze > $(REQ_FREEZE)
	pipdeptree > $(REQ_PIPDEPTREE)

remove-req: ## Uninstall all the libraries installed in the Python environment.
	@echo "──────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@echo "─── Delete all previously installed libraries: $(REQ_FILES) $(REQ_DIST) $(REQ_FILES_DEV)"
	@echo "──────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@$(foreach var,$(REQ_FILES),pip uninstall -r $(SETUP_PATH)/$(var) -y || (echo "uninstall failed $?");)
	@$(foreach var,$(REQ_FILES_DEV),pip uninstall -r $(SETUP_PATH)/$(var) -y || (echo "uninstall failed $?");)
	@$(foreach var,$(REQ_DIST),pip uninstall $(var) -y || (echo "uninstall failed $?");)
	@pip freeze | grep -v "certifi" | awk '{print $$1}' | xargs pip uninstall -y || (echo "uninstall failed $?")
	@pip freeze > $(REQ_FREEZE)
	@rm $(REQ_PIPDEPTREE)

cache-purge:  ## Remove all items from the pip cache.
	@echo "──────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@echo "─── Remove all items from the pip cache."
	@echo "──────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@pip cache purge


.DEFAULT_GOAL := help

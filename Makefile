# The directory of this file
DIR := $(shell echo $(shell cd "$(shell  dirname "${BASH_SOURCE[0]}" )" && pwd ))

# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help: ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

.PHONY: venv
venv: ## Create venv
	python3 -m venv .venv

.PHONY: bootstrap
bootstrap: ## Install dependencies
	./.venv/bin/pip3 install -r requirements.txt

.PHONY: install
install: ## Install package
	./.venv/bin/python3 setup.py install

.PHONY: test
test: ## Run unittests
	./.venv/bin/pytest test/


.PHONY: cli_help
cli_help: ## Use package
	./.venv/bin/python3 -m joplin_db --help

.PHONY: doc
doc: ## Build documentation
	.venv/bin/sphinx-build -b html doc doc/_build/html

.PHONY: install install-dev clean check format test api build docker

## Install for production
install:
	@echo ">> Installing dependencies"
	@uv pip install --upgrade pip
	@uv pip install -e .

## Install for development 
install-dev: install
	@uv pip install -e ".[dev]"

## Delete all temporary files
clean:
	@rm -rf .ipynb_checkpoints
	@rm -rf **/.ipynb_checkpoints
	@rm -rf .pytest_cache
	@rm -rf **/.pytest_cache
	@rm -rf __pycache__
	@rm -rf **/__pycache__
	@rm -rf build
	@rm -rf dist

## Run checks (ruff + test)
check:
	@python -m ruff check . 
	@python -m ruff format --check . 

## Format files using black
format:
	@python -m ruff check . --fix
	@python -m ruff format .

## Run tests
test:
	@python -m pytest --cov=src --cov-report xml --log-level=WARNING --disable-pytest-warnings

## Run api
api:
	@python -m uvicorn src.{{cookiecutter.project_slug}}.api.main:app --reload

## Build using pip-tools
build:
	@uv pip install --upgrade pip
	@uv pip install --upgrade pip-tools
	@uv pip compile pyproject.toml -o requirements.txt
	@uv pip compile pyproject.toml --extra dev -o requirements-dev.txt

## Build the docker image
docker:
	docker build -f Dockerfile -t {{cookiecutter.project_slug}} .

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available commands:$$(tput sgr0)"
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')


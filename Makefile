.DEFAULT_GOAL := help

# for setup

STAGED := $(shell git diff --cached --name-only --diff-filter=ACMR -- 'src/***.py' | sed 's| |\\ |g')

TAG_NAME ?= $(shell git log -1 --format=%h)

format:
	brunette . --config=setup.cfg
	isort .

lint:
	PYTHONPATH=src pytest src --pylint --flake8 --mypy

lint-all:
	PYTHONPATH=src pytest src --pylint --flake8 --mypy --cache-clear

lint-staged:
ifdef STAGED
	PYTHONPATH=src pytest $(STAGED) --pylint --flake8 --mypy --cache-clear
else
	@echo "No Staged Python File in the src folder"
endif


# Usages:
utest:
	PYTHONPATH=src pytest test/$(target) -vv --cov=src --cov-config=.coveragerc --cov-report=html --cov-report=term-missing --cov-fail-under=100
	coverage-badge -fo coverage.svg

setup-dev:
	pip install -r "requirements.txt"
	pre-commit install

tree:
	tree -I "*data|.pkl|*.png|*.txt|$(shell cat .gitignore | tr -s '\n' '|' )"
help:
	@echo "Usage: make [target]"
	@echo
	@echo "Available targets:"
	@echo "  format:"
	@echo "    Format the code"
	@echo "  lint:"
	@echo "    Lint the code with caching"
	@echo "  lint-all:"
	@echo "    Lint the code without caching"
	@echo "  lint-staged:"
	@echo "    Lint the code staged by git"
	@echo "  utest:"
	@echo "    Run unit tests"
	@echo "  setup:"
	@echo "    Install the dependencies"
	@echo "  setup-dev:"
	@echo "    Install the dependencies for development"
	@echo "  clean:"
	@echo "    Clean the data folder"
	@echo "  tree:"
	@echo "    Show the directory tree"
	@echo
	@echo "  help:"
	@echo "    Show this help message"

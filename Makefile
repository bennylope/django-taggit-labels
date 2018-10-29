.PHONY: clean-pyc clean-build docs clean

TOX_NAME=tox  # alternative: detox
MODULE_NAME=taggit_labels
TEST_FLAGS=--verbose
COVER_FLAGS=--cov=taggit_labels

install:  ## Install all requirements including for testing
	pip install -r requirements-dev.txt

install-quiet:  ## Same as install but pipes all output to /dev/null
	pip install -r requirements-dev.txt > /dev/null

clean: clean-build clean-pyc clean-test-all  ## Remove all artifacts

clean-build:  ## Remove build artifacts
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info

clean-pyc:  ## Remove Python file artifacts
	-@find . -name '*.pyc' -follow -print0 | xargs -0 rm -f &> /dev/null
	-@find . -name '*.pyo' -follow -print0 | xargs -0 rm -f &> /dev/null
	-@find . -name '__pycache__' -type d -follow -print0 | xargs -0 rm -rf &> /dev/null

clean-test:  ## Remove test and coverage artifacts
	rm -rf .coverage coverage*
	rm -rf tests/.coverage test/coverage*
	rm -rf htmlcov/

clean-test-all: clean-test  ## remove all test-related artifacts including tox
	rm -rf .tox/

lint:  ## Check style with flake8
	flake8 ${MODULE_NAME}

test:  ## Run tests quickly with the default Python
	py.test ${TEST_FLAGS}

test-coverage: clean-test  ## Run tests with coverage report
	-py.test ${COVER_FLAGS} ${TEST_FLAGS}
	@exit_code=$?
	@-coverage html
	@exit ${exit_code}

test-all:  ## Run tests on every Python version with tox
	tox

check: clean-build clean-pyc clean-test lint test-coverage  ## Run all necessary steps to check validity of project

build: clean  ## Create distribution files for release
	python setup.py sdist bdist_wheel

release: build  ## Create distribution files and publish to PyPI
	python setup.py check -r -s
	twine upload dist/*

sdist: clean  ##sdist Create source distribution only
	python setup.py sdist
	ls -l dist

docs:
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

help:
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


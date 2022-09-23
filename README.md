# CellML Validation tools

This repository hosts:

- A large set of CellML models that each either exemplify or break a rule in the CellML 1.0 specification
- XML validation tools (DTD, Schema, RelaxNG) for CellML 1.0
- Code to apply each validation method to each model file, and generate a report showing the results.

Please note that this repo is still under development, meaning the validation tools have not yet been fully tested.

The goal is to extend the 1.0 tests and tools to 1.1, and then 2.0.

## CellML 2.0

* [A very brief overview of CellML 2.0](cellml_2_0/cellml_2_0_quick.md)
* [A condensed list of CellML 2.0 rules](cellml_2_0/cellml_2_0_rules.md)
* [An XSLT document to transform 1.0/1.1 models to 2.0](cellml_2_0/cellml_1_to_2.xsl) by [various authors](https://github.com/cellml/cellml1to2)

## CellML 1.1

* [A very brief overview of CellML 1.1](cellml_1_1/cellml_1_1_quick.md)
* [An XSLT document to transform 1.0 models to 1.1](cellml_1_1/cellml_1_0_to_1_1.xsl)
* [A Markdown version of the CellML 1.1 spec](cellml_1_1/cellml_1_1_spec.md)
* [A document showing the changes from 1.0](cellml_1_1/cellml_1_1_changes.md)

Older files:

* [CellML 1.1 Schema](cellml_1_1/todo/cellml_1_1.xsd) by Andrew Miller, Auckland Bioengineering Institute

## CellML 1.0

* [A very brief overview of CellML 1.0](cellml_1_0/cellml_1_0_quick.md)
* [The CellML 1.0 test set](models_1_0)
* [CellML 1.0 XML Schema](cellml_1_0/cellml_1_0.xsd)
* [CellML 1.0 DTD](cellml_1_0/cellml_1_0.dtd) - based on the version by Warren Hedley
* [CellML 1.0 RELAX NG schema (XML syntax)](cellml_1_0/cellml_1_0.rng) translated from the compact syntax version by Jonathan Cooper
* [CellML 1.0 RELAX NG schema (compact syntax)](cellml_1_0/cellml_1_0.rnc) written by Jonathan Cooper
* [A Markdown version of the CellML 1.0 spec](cellml_1_0/cellml_1_0_spec.md)

Older files:

* [CellML 1.0 XML Schema](cellml_1_0/deprecated/cellml_1_0_simple.xsd) written by Autumn Cuellar, Auckland Bioengineering Institute
* [CellML 1.0 DTD](cellml_1_0/deprecated/cellml_1_0.dtd) by Warren Hedley, Auckland Bioengineering Institute

## The `check` utility

The `check` directory contains a Python module that can validate or convert CellML files, and which contains unit tests for various tools.

### Installation

1. Create a virtual environment for python 3: `$ virtualenv venv -p python3` and activate it with `$ source venv/bin/activate`
2. Install the requirements using pip: `$ pip install -r requirements.txt`

To add validation tools:
- Use `pip` to install Myokit
- Use `pip` to install cellmlmanip
- Download and install OpenCOR, and update `check/opencor_validation.py` with the path to your OpenCOR installation.

### Command-line use

To validate a single file use e.g.
```
python -m check schema_1_0 path/to/file.cellml
```

To convert a CellML file using XSLT use e.g.
```
python -m check xslt_1_to_2 original.cellml converted.cellml
```

For a full list of options use
```
python -m check
```

### Unit tests

The `check/tests` directory contains `pytest` tests that run all the test files through the supported validation tools, check the result, and generate reports (see below).
Dependening on how you look at it, this constitutes a test of the test files, of the tools, or both.

To run the full test suite type
```
pytest
```
To get more test output, use `$ pytest -v` or even `$ pytest -v -s --log-cli-level=INFO`.

Test output should consist of `passes` (the validator is correct, and we expected this) and `xfails` (the validator is wrong, and we expected this).
An error or `fail` result indicates the test is behaving in an unexpected way (suggesting that the `check` module should be updated).
For a full guide to interpreting the results, see the docstrings for `assert_valid` and `assert_invalid` in `check/tests/shared.py`.

## Reports

The full suite of tests have been run on several validation and simulation tools.
[Reports of the test results can be viewed here](reports/README.md).


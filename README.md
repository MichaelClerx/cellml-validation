# CellML Validation tools

This repository hosts:

- A large set of CellML models that each either exemplify or break a rule in the CellML 1.0 specification
- XML validation tools (DTD, Schema, RelaxNG) for CellML 1.0
- Code to apply each validation method to each model file, and generate a report showing the results.

Please note that this repo is still under development, meaning the validation tools have not yet been fully tested.

The goal is to extend the 1.0 tests and tools to 1.1, and then 2.0.

## CellML 2.0 (Draft)

* To-do

## CellML 1.1

* [A Markdown version of the CellML 1.1 spec](cellml_1_1/cellml_1_1_spec.md)

* Older files:
  * [CellML 1.1 Schema](cellml_1_1/todo/cellml_1_1.xsd) by Andrew Miller, Auckland Bioengineering Institute

## CellML 1.0

* [A very brief overview of CellML 1.0](cellml_1_0/cellml_1_0_quick.md)
* [A Markdown version of the CellML 1.0 spec](cellml_1_0/cellml_1_0_spec.md)
* [The CellML 1.0 test set](models_1_0)
* [CellML 1.0 XML Schema](cellml_1_0/cellml_1_0.xsd)
* [CellML 1.0 DTD](cellml_1_0/cellml_1_0.dtd) - based on the version by Warren Hedley
* [CellML 1.0 RELAX NG schema (XML syntax)](cellml_1_0/cellml_1_0.rng) translated from the compact syntax version by Jonathan Cooper
* [CellML 1.0 RELAX NG schema (compact syntax)](cellml_1_0/cellml_1_0.rnc) written by Jonathan Cooper

* Older files:
  * [CellML 1.0 XML Schema](cellml_1_0/deprecated/cellml_1_0_simple.xsd) written by Autumn Cuellar, Auckland Bioengineering Institute
  * [CellML 1.0 DTD](cellml_1_0/deprecated/cellml_1_0.dtd) by Warren Hedley, Auckland Bioengineering Institute

## Tests

The `check` directory contains a Python module that can run the test files through various validation tools.
Dependening on how you look at it, this constitutes a test of the test files, of the tools, or both.

- Installation
  1. Create a virtual environment for python 3: `$ virtualenv venv -p python3` and activate it with `$ source venc/bin/activate`
  2. Install the requirements using pip: `$ pip install -r requirements.txt`
- To validate a single file use e.g.
  ```
  python -m check schema_1_0 models_1_0/valid/empty-model.cellml
  ```
  To see more options simply type
  ```
  python -m check
  ```
- To run the full test suite type
  ```
  pytest
  ```
  To get more test output, use `$ pytest -v` or even `$ pytest -v -s --log-cli-level=INFO`.
- Running all tests generates reports of which test files pass and fail with different validation tools.
  [A list of pre-rendered reports can be viewed here](reports/README.md).


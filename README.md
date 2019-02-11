# CellML Validation tools

This repository is intended to host tests for the various validation tools for CellML.

Disclaimers:

1. XML technologies like Schema, DTD, RelaxNG, and Schematron can only provide *partial* validation for CellML files.
2. This repo is still under development, meaning the validation tools have not yet been fully tested.

## CellML 2.0 (Draft)

* To-do

## CellML 1.1

* Older files:
  * [CellML 1.1 Schema](cellml_1_1/todo/cellml_1_1.xsd) by Andrew Miller, Auckland Bioengineering Institute

## CellML 1.0

* [A very brief overview of CellML 1.0](cellml_1_0/README.md)
* [The CellML 1.0 test set](models_1_0)
* [CellML 1.0 XML Schema](cellml_1_0/cellml_1_0.xsd)
* [CellML 1.0 DTD](cellml_1_0/cellml_1_0.dtd) - based on the version by Warren Hedley
* [CellML 1.0 RELAX NG schema (XML syntax)(cellml_1_0/cellml_1_0.rng) translated from the compact version by Jonathan Cooper
* [CellML 1.0 RELAX NG schema (compact syntax)](cellml_1_0/cellml_1_0.rnc) written by Jonathan Cooper

* Older files:
  * [CellML 1.0 XML Schema](cellml_1_0/deprecated/cellml_1_0_simple.xsd) written by Autumn Cuellar, Auckland Bioengineering Institute
  * [CellML 1.0 DTD](cellml_1_0/todo/cellml_1_0.dtd) by Warren Hedley, Auckland Bioengineering Institute
 

## Tests

The validation files themselves can be tested using the following steps:

1. Create a virtual environment for python 3: `$ virtualenv venv -p python3` and activate it with `$ source venc/bin/activate`
2. Install the requirements using pip: `$ pip install -r requirements.txt`
3. Run the tests using pytest: `$ pytest`

To get more test output, use `$ pytest -v` or even `$ pytest -v -s --log-cli-level=INFO`.

To validate a single file, use e.g. `$ python -m check schema_1_0 models_1_0/valid/empty-model.cellml`.


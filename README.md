# CellML Validation tools

This repository is intended to host tests for the various validation tools for CellML.

Disclaimers:

1. Schema/DTD/RelaxNG can only provide *partial* validation for CellML files.
2. This repo is still under development, meaning the validation tools have not yet been fully tested.

## CellML 2.0 (Draft)

* To-do

## CellML 1.1

* Older files:
  * [CellML 1.1 Schema](cellml_1_1/todo/cellml_1_1.xsd) by Andrew Miller, Auckland Bioengineering Institute

## CellML 1.0

* [CellML 1.0 XML Schema](cellml_1_0/cellml_1_0.xsd)
* Older files:
  * [CellML 1.0 XML Schema](cellml_1_0/deprecated/cellml_1_0_simple.xsd) written by Autumn Cuellar, Auckland Bioengineering Institute
  * [CellML 1.0 DTD](cellml_1_0/todo/cellml_1_0.dtd) by Warren Hedley, Auckland Bioengineering Institute
  * [RELAX NG schema](cellml_1_0/todo/cellml1.0.rnc) for CellML 1.0 written by Jonathan Cooper

## Tests

The validation files themselves can be tested using the following steps:

1. Create a virtual environment for python 3: `$ virtualenv venv -p python3` and activate it with `$ source venc/bin/activate`
2. Install the requirements using pip: `$ pip install -r requirements.txt`
3. Run the tests using pytest: `$ pytest`

To get more test output, use `$ pytest -v` or even `$ pytest -v -s --log-cli-level=INFO`.

To validate a single file, use e.g. `$ python -m check schema_1_0 models_1_0/valid/empty-model.cellml`.

## CellML 1.0 document structure

Elements are shown with their attributes in brackets.
Required elements/attributes are indicated in italics.

- model(*name*)
  - units(*name*,base_units)
    - unit(*units*,prefix,exponent,multiplier,offset)
  - component(*name*)
    - units --> see above
    - variable(*name*,*units*,(initial_value,public_interface,private_interface)
    - reaction(reversible)
      - *variable_ref*(*variable*)
        - *role*(*role*,delta_variable,direction_stoichiometry)
          - mathml:math
    - mathml:math
  - group()
    - *relationship_ref*(*relationship*,name)
    - *component_ref*(*component*)
      - component_ref --> see above
  - connection()
    - *map_components*(*component_1*,*component_2*)
    - *map_variables*(*variable_1*,*variable_2*)


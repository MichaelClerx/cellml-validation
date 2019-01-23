# CellML 1.0

This directory contains validation files for CellML 1.0.

A quick reference for the kind of thing you find a CellML 1.0 document is given below.

## Outline of CellML 1.0 structure

Elements are shown with their attributes in brackets.
Required elements/attributes are indicated in italics.

- model(*name*)
  - units(*name*,base_units)
    - unit(*units*,prefix,exponent,multiplier,offset)
  - component(*name*)
    - units --> see above
    - variable(*name*,*units*,initial_value,public_interface,private_interface)
    - reaction(reversible)
      - *variable_ref*(*variable*)
        - *role*(*role*,delta_variable,direction,stoichiometry)
          - mathml:math
    - mathml:math
  - group()
    - *relationship_ref*(*relationship*,name)
    - *component_ref*(*component*)
      - component_ref --> see above
  - connection()
    - *map_components*(*component_1*,*component_2*)
    - *map_variables*(*variable_1*,*variable_2*)


## List of elements and attributes

### Elements:

- component
- component_ref
- connection
- group
- map_components
- map_variables
- mathml:math
- model
- reaction
- relationship_ref
- role
- unit
- units
- variable
- variable_ref

In addition, the document can contain anything from the `rdf` namespace, and in fact elements from a namspace other than `cellml`, `cmeta`, `rdf` and `mathml` can appear at any position in the document.

### Attributes:

- base_units
- cmeta:id
- component_1
- component_2
- delta_variable
- direction
- exponent
- initial_value
- multiplier
- name
- offset
- prefix
- private_interface
- public_interface
- relationship
- reversible
- role
- stoichiometry
- units
- variable
- variable_1
- variable_2

In addition, the document can contain anything from the `rdf` namespace, and attributes from a namespace other than `cellml`, `cmeta`, `rdf` and `mathml` can appear at any position in the document.

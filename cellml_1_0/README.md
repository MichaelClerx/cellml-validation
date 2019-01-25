# CellML 1.0

This directory contains validation files for CellML 1.0.

A quick-and-dirty reference is given below.

## These things exist in CellML:

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

In addition, the document can contain any element from the `rdf` namespace, and all elements are allowed to have a `cmeta:id` attribute.
Finally, all CellML elements are allowed contain _any elements and attributes from any namespace_ other than `cellml`, `cmeta`, `rdf` and `mathml`.

## Grouping & public/private interfaces

1. Containment means nothing
2. Encapsulation means parent/child relationships, which affect how connections are made.

![Encapsulation example](encapsulation.svg)

In CellML, components can't refer to each other's values.
Instead, if a component X wants to use a value from Y, it defines a _new variable_ in X and gives it an interface of "in". It then makes a _connection_ to the variable in Y, which must have an interface of "out".

- Connections can only be made between siblings, or between parent and child.
- Sibling connections are governed by the _public_ interfaces.
- Parent-child relationships are defined by the _parent's private_ interface, and the _child's public interface_.

Note that CellML refers to children as "components in the encapsulated set".
The following things follow from the rules above:

- There are no relationsips that are private on both ends.
- A parent can obtain a variable from a child (via the parent's private interface "in") and then share it with a sibling (via the parent's public interface "out").
- A parent can obtain a variable from a sibling (via the parent's public interface "in") and then share it with its children (via the parent's private interface "out").

Because a variable can only get its value from one source, CellML has additional rules saying:

- A variable with an "in" interface can't be changed by its component's maths (or reactions).
- A variable with an "in" interface can only be mapped to a single other variable with an "out" interface.
- A variable cannot have public _and_ private interface "in".
  
The third rule doesn't seem strictly necessary (as the second rule already prevents any abuse), but is present in CellML 1.0 anyway.


## Lists

### Elements

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

### Attributes

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

### Relationship types

- containment
- encapsulation

### Interface types

- in
- out
- none

### Predefined units

- ampere
- becquerel
- candela
- celsius
- coulomb
- dimensionless
- farad
- gram
- gray
- henry
- hertz
- joule
- katal
- kelvin
- kilogram
- liter
- litre
- lumen
- lux
- meter
- metre
- mole
- newton
- ohm
- pascal
- radian
- second
- siemens
- sievert
- steradian
- tesla
- volt
- watt
- weber

### Unit prefixes

- yotta
- zetta
- exa
- peta
- tera
- giga
- mega
- kilo
- hecta
- deka
- deci
- centi
- milli
- micro
- nano
- pico
- femto
- atto
- zepto
- yocto

### Reaction directions

- forward
- backward
- both

### Species roles

- reactant
- product
- activator
- catalyst
- inhibitor
- modifier
- rate

### Values for `base_units` and `reversible`

- yes
- no

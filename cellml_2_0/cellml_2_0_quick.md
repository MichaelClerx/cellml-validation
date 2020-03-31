# CellML 2.0 Quick Reference

## These things exist in CellML 2.0:

Elements are shown with their attributes in brackets.
Required elements/attributes are indicated in italics.

- model(*name*)
  - units(*name*)
    - unit(*units*, prefix, multiplier, exponent)
  - component(*name*)
    - variable(*name*, *units*, interface, initial_value)
    - reset(*variable*, *test_variable*, *order*)
      - *test_value*
        - *mathml:math*
      - *reset_value*
        - *mathml:math*
    - mathml:math
      - All mathml:cn elements must have a cellml:units attribute
  - encapsulation
    - component_ref(*component*)
      - component_ref(*component*)
        - ...
  - connection(*component_1*, *component_2*)
    - *map_variables*(*variable_1*, *variable_2*)
  - import(*xlink:href*)
    - units(*name*, *units_ref*)
    - component(*name*, *component_ref*)

All CellML 2.0 elements can also contain an `id` attribute.
  
## Encapsulation & public/private interfaces

Encapsulation means parent/child relationships, which affect how connections are made.

![Encapsulation example](encapsulation.svg)

There are three rules:

1. Only components that have sibling or parent-child relationships can be connected.
2. Connections between siblings are governed by the public interface.
3. In parent-child relationships, the parent uses the private interface and the child uses the public interface.

## Identifiers

Identifiers must start with at least one letter, and only contain letters, numbers, and underscores.

## Lists

### Elements

- component
- component_ref
- connection
- encapsulation
- import
- model
- reset
- reset_value
- test_value
- unit
- units
- variable
- variable_1
- variable_2

### Attributes

- component
- component_1
- component_2
- component_ref
- exponent
- initial_value
- interface
- map_variables
- multiplier
- name
- order
- prefix
- test_variable
- units
- units_ref
- variable

### Namespaces

```
cellml="http://www.cellml.org/cellml/2.0#"
mathml="http://www.w3.org/1998/Math/MathML"
```

### Predefined units

- ampere
- becquerel
- candela
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
- litre
- lumen
- lux
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
- deca
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

### Interface types

- `public`
- `private`
- `public_and_private`
- `none` (default)

### MathML subset

CellML 2.0 documents can use MathML, but must only elements from the Supported MathML Elements set.

#### MathML basics

- `<cn>`, `<ci>`, `<apply>`, `<eq>`, `<sep />`
- Every `<cn>` must have a `cellml:units` attribute
- The `type` of a `<cn>` must be either `real` or `e-notation`
- Every `<ci>` must refer to a variable from the same component

#### Arithmetic

- Basic 1: `<plus>`, `<minus>`, `<times>`, `<divide>`
- Basic 2: `<power>`, `<root>`, `<exp>`, `<ln>`, `<log>`, `<logbase>`
- Non-smooth: `<abs>`, `<floor>`, `<ceiling>`, `<rem>`
- N-ary comparison: `<max>`, `<min>`

#### Calculus

- First order: `<diff>`, `<bvar>`
- Higher order: `<degree>`

#### Trig functions

- Basic: `<sin>`, `<cos>`, `<tan>`, `<arcsin>`, `<arccos>`, `<arctan>`
- Hyperbolic: `<sinh>`, `<cosh>`, `<tanh>`, `<arcsinh>`, `<arccosh>`, `<arctanh>`
- Redundant `<sec>`, `<csc>`, `<cot>`, `<arcsec>`, `<arccsc>`, `<arccot>`
- Hyperbolic redundant: `<sech>`, `<csch>`, `<coth>`, `<arcsech>`, `<arccsch>`, `<arccoth>`

#### Logic and Piecewise

- Piecewise: `<piecewise>`, `<piece>`, `<otherwise>`
- Relations: `<eq>`, `<neq>`, `<gt>`, `<lt>`, `<geq>`, `<leq>`
- Logical operators: `<and>`, `<or>`, `<xor>`, `<not>`
- Logical constants: `<true>`, `<false>`

Note 1: `<eq>` is a relation in CellML, so the statement `x = 5` is treated as fact about `x`, not an assignment.

Note 2: The `<otherwise>` element is not required.
This means that you can write a statement like `x = (y > 0) ? 1 : undefined`.
The CellML spec doesn't define what implementations should do for these cases.

Note 3: Variables can never have the value `true` or `false`.

#### Constants

- `<pi>`
- `<exponentiale>`
- `<notanumber>`
- `<infinity>`


# CellML 1.0 Quick Reference

## These things exist in CellML 1.0:

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
            - All mathml:cn's must have an attribute cellml:units
    - mathml:math --> see above
  - group()
    - *relationship_ref*(*relationship*,name)
    - *component_ref*(*component*)
      - component_ref --> see above
  - connection()
    - *map_components*(*component_1*,*component_2*)
    - *map_variables*(*variable_1*,*variable_2*)

Note that (contrary to what the spec says), most attributes listed above are _not_ in the CellML 1.0 namespace.
The only attribute in the CellML 1.0 namespace is the `cellml:units` attribute, which appears _only_ inside `mathml:cn` elements.

All CellML 1.0 elements can also contain:
 - any element from the `rdf` namespace
 - a `cmeta:id` attribute.
 - _Any elements and attributes from any namespace_ other than `cellml`, `cmeta`, `mathml`, and `rdf`.

## Grouping & public/private interfaces

1. Containment means nothing
2. Encapsulation means parent/child relationships, which affect how connections are made.

![Encapsulation example](encapsulation.svg)

In CellML 1.0, components can't refer to each other's variables.
Instead, if a component X wants to use a value from Y, it defines a _new variable_ in X and gives it an interface of "in". It then makes a _connection_ to the variable in Y, which must have an interface of "out".

- Connections can only be made between siblings, or between parent and child.
- Sibling connections are governed by the _public_ interfaces.
- Parent-child relationships are defined by the _parent's private_ interface, and the _child's public interface_.

Note that CellML 1.0 refers to children as "components in the encapsulated set".
The following things follow from the rules above:

- There are no relationsips that are private on both ends.
- A parent can obtain a variable from a child (via the parent's private interface "in") and then share it with a sibling (via the parent's public interface "out").
- A parent can obtain a variable from a sibling (via the parent's public interface "in") and then share it with its children (via the parent's private interface "out").

Because a variable can only get its value from one source, CellML 1.0 has additional rules saying:

- A variable with an "in" interface can't be changed by its component's maths (or reactions).
- A variable with an "in" interface can only be mapped to a single other variable with an "out" interface.
- A variable cannot have public _and_ private interface "in".

The third rule doesn't seem strictly necessary (as the second rule already prevents any abuse), but is present in CellML 1.0 anyway.

Finally, users can add their own relationship types by using a `relationship` attribute on the `relationship_ref` element from any namespace other than cellml, mathml, cmeta, or rdf. In this case its value is unrestricted and there are no rules for the relationship's interpretation.

## Identifiers

CellML 1.0 defines identifiers as strings matching `('_')* ( letter | digit ) ( letter | '_' | digit )*`.
Note that this includes strings such as "0", "12", and "3e4".

## Real numbers

CellML 1.0 does not define a notation for real numbers, but presumably this should be something compatible with the MathML `real` number type.

## Units and unit conversion

### Empty units elements

It's unclear from the spec whether a `<units>` element that's not a base unit can be empty, and implementers have disagreed.

CellML 2.0 explicitly allows it, but as a way to define base units (removing the need for the `base_units` attribute).

In these tests we've assumed that empty units elements with `base_units="no"` are not allowed in CellML 1.0.

### Unit checking and conversion

Units come into play in two places in CellML 1.0: (1) when connecting variables; and (2) when writing equations.

#### Units of connected variables

Variables that are connected by `map_variables` elements need not necessarily have the same units.
If the units differ only by a scaling factor and/or offset, they may be convertible, and section 3.5.1 of the CellML 1.0 spec suggests that CellML processing software should do so.
The spec does **not** seem to say that having incompatible units on either side of a connection renders a model invalid.

#### Units inside equations

All variables and numbers that appear in equations must have units associated with them.
While the spec suggests these can be used to check the equations dimensionality, it also states (in 5.2.7) that "_CellML processing software is free to ignore units in mathematics and assume that equations are consistent_".
No rules exist saying that having invalid units in equations renders a model invalid.

Finally, there is no concept of unit conversion _within_ equations (e.g. to make equations like `x = 1V + 1mV` work), and in fact doing so would violate the rule quoted above.

#### Meter and metre

Technically, table 2 defines both meter and metre as base units, implying you can't convert between metres and meters.
This is pointed out in the [errata to 1.1](https://www.cellml.org/specifications/cellml_1.1/errata).
In these tests we assume they are simply aliases.

## MathML and the CellML subset

CellML 1.0 documents can use all of content MathML's capabilities.
However, CellML 1.0 software only needs to be able to handle "the CellML subset".
Documents using only this set are called "valid CellML subset documents".

### MathML basics

- `<cn>`, `<ci>`, `<apply>`, `<eq>`
- CellML adds the rule that every `<cn>` must have a `cellml:units` attribute

The Content MathML 2 spec has several types of number, which the CellML spec does not make any statements about.
They are:
- `real`, possibly in a non-decimal base.
- `integer`, possibly in a non-decimal base.
- `rational`, this uses the `<sep>` element and so is not in the CellML subset.
- `complex-cartesian` and `complex-polar`, the spec makes no statements, but it seems unlikely CellML subset compliant software needs to handle these.
- `constant`, this allows you to add unnamed constants.
- `e-notation`, this was added in later versions, it uses the `<sep>` element and so is outside of the CellML subset but very useful!

Going by the rules for `initial_value` attributes, it would seem CellML variables are real numbers.
Presumably, integers should be treated as reals then.
Although the spec makes no statement, it seems that `constant` introduces new variables and so shouldn't be allowed.
Finally, `<cn>` has additional attributes `definitionURL` and `encoding`, which the spec makes no statement about but are presumably not part of the subset.

The contents of a `<cn>` must be numbers, possibly a sign (`-`) and a period (`.`).
The default type is real and

### Arithmetic

- Basic 1: `<plus>`, `<minus>`, `<times>`, `<divide>`
- Basic 2: `<power>`, `<root>`, `<exp>`, `<ln>`, `<log>`, `<logbase>`
- Non-smooth: `<abs>`, `<floor>`, `<ceiling>`
- Non-negative integer only: `<factorial>`

Note that the factorial element is slightly troublesome for CellML: There is no concept of integers in CellML, yet factorial operates on integers exclusively.
In addition, values for x factorial quickly become larger than fit in most number types.

### Calculus

- First order: `<diff>`, `<bvar>`
- Higher order: `<degree>`

### Trig functions

- Basic: `<sin>`, `<cos>`, `<tan>`, `<arcsin>`, `<arccos>`, `<arctan>`
- Hyperbolic: `<sinh>`, `<cosh>`, `<tanh>`, `<arcsinh>`, `<arccosh>`, `<arctanh>`
- Redundant `<sec>`, `<csc>`, `<cot>`, `<arcsec>`, `<arccsc>`, `<arccot>`
- Hyperbolic redundant: `<sech>`, `<csch>`, `<coth>`, `<arcsech>`, `<arccsch>`, `<arccoth>`

### Logic and Piecewise
- Piecewise: `<piecewise>`, `<piece>`, `<otherwise>`
- Relations: `<eq>`, `<neq>`, `<gt>`, `<lt>`, `<geq>`, `<leq>`
- Logical operators: `<and>`, `<or>`, `<xor>`, `<not>`
- Logical constants: `<true>`, `<false>`

Note 1: `<eq>` is a relation in CellML, so the statement `x = 5` is treated as fact about `x`, not an assignment.

Note 2: The `<otherwise>` element is not required.
This means that you can write a statement like `x = (y > 0) ? 1 : undefined`.
The CellML spec doesn't define what implementations should do for these cases.

Note 3: Variables can never have the value `true` or `false`.
In light of this, it's a bit unclear what allowing `<true>` and `<false>` is intended to achieve, other than writing things like "if((x == 1) == true)".

### Constants

- `<pi>`
- `<exponentiale>`
- `<notanumber>`, `<infinity>`

### Semantics and annotation

- `<semantics>`, `<annotation>`, `<annotation-xml>`

It's allowed to wrap a bit of Content MathML in a `<semantics>` element, which looks something like this:
```
<semantics>
  <apply>
    <eq /><ci>x</ci><cn cellml:units="dimensionless">1</cn>
  </apply>
  <annotation>
    X is a really great variable.
  </annotation>
</semantics>
```
There can be multiple `<annotation>` elements (for non-xml annotation) or `<annotation-xml>` elements (for xml annotation).
I have personally never seen these in a model.

## Namespaces

|= prefix  |= namespace                                  |
|----------|---------------------------------------------|
| `cellml` | http://www.cellml.org/cellml/1.0            |
| `cmeta`  | http://www.cellml.org/metadata/1.0#         |
| `mathml` | http://www.w3.org/1998/Math/MathML          |
| `rdf`    | http://www.w3.org/1999/02/22-rdf-syntax-ns# |

### Namespace confusion

In XML, elements can specify a namespace just for themselves (`<ns:element xmlns:ns="http://example.org" />`) or for themselves and all their children (`<element xmlns="http://example.org" />`).
Attributes are not in a namespace unless explicitly stated using the `namespace:attribute="attribute_value"` syntax.
In general, attributes do not _need_ to be namespaced, because they are already uniquely identifiable from their namespaced parent element.
The one case where namespaced attributes are useful is when they appear in an element from a different namespace.
For example, in `<mathml:cn cellml:units="volt">1</mathml:cn>` we have a MathML element using a CellML attribute.

The spec unfortunately gets this wrong (2001 is early days for XML namespaces), and consistently refers to attributes in the `cellml` namespace, when what is meant is un-namespaced attributes.
Similarly, rule 8.4.1 mentions a `mathml:id` attribute (which doesn't exist), when wat is meant is an unnamespaced `id` attribute.

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

### Predefined units

With base units in **bold**.

- **ampere**
- becquerel
- **candela**
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
- **kelvin**
- **kilogram**
- liter
- litre
- lumen
- lux
- **meter**
- **metre**
- **mole**
- newton
- ohm
- pascal
- radian
- **second**
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

### Relationship types

- containment
- encapsulation

(Note that a relationship may also be defined in an extension namespace, in which case any value is allowable).

### Interface types

- in
- out
- none

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


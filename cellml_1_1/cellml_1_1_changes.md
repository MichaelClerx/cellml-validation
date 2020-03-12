# Changes between CellML 1.1 and 1.0

The namespace is updated to

    2.2.2 xmlns:cellml="http://www.cellml.org/cellml/1.1#"

The xlink namespace is added to the list of non-extension namespaces

    2.2.2 xmlns:xlink="http://www.w3.org/1999/xlink"

The rules for identifiers are changed:

    2.4.1 identifiers consist of numbers, letters, and underscores
    2.4.1 identifiers must contain at least one letter
    2.4.1 identifiers may not start with number

Models can now contain `<import>` elements

    3.4.1.1 A model can contain <import> elements

The rules for `<component>` now cover "model components" (defined locally) and "import components".

The numbering of rules for models has changed, and there are new rules for "import component" (a `<component>` element that's a child of an `<import>`).

    3.4.2.1.1 --> Now specifically about model components
    3.4.2.1.2 An import component cannot have children (except rdf:RDF)
    3.4.2.1.3 A component must have a name attribute (used to be 3.4.2.1.2)
    3.4.2.1.4 An import component have a component_ref attribute
    3.4.2.2.1 A component name must be an identifier
    3.4.2.2.2 A component name must be unique (over model _and_ import components)
    3.4.2.3 A component_ref must equal the name of a component in the imported model (directly or via an import)
    3.4.2.4 A model component must not have a component_ref attribute

Initial values can now be variables

    3.4.3.7 An initial value can be a number or a local variable name

Units can now be imported

    5.4.1.1.1 Models can contain `<units>` elements
    5.4.1.1.1 Components can contain `<units>` elements
    5.4.1.1.1 Imports can contain `<units>` elements
    5.4.1.1.2 Units elements must have a name attribute
    5.4.1.1.3 A model units or a component units may have a base_units attribute
    5.4.1.1.4 A model or component units with base_units="yes" must be empty (except for `<rdf:RDF>`)
    5.4.1.1.5 A model or component units with base_units="no" may only contain `<unit>` or `<rdf:RDF>` elements
    5.4.1.1.6 An import units must have a units_ref attribute
    5.4.1.1.7 An import units must be empty (except for `<rdf:RDF>`)

    5.4.1.2.1 A name attribute must be an identifier
    5.4.1.2.2 A name attribute can't shadow a standard unit
    5.4.1.2.3 Model units names and import units names must be unique (shared namespace)
    5.4.1.2.3 Component units must be unique within the component (but can shadow model or import units)

    5.4.1.3.1 A base_units attribute must be yes or no
    5.4.1.3.2 A base units attribute defaults to no
    
    5.4.1.4 An import units may not have a base_units attribute

    5.4.2.1 The units_ref attribute must equal the name of a model units in the imported model
    5.4.2.2 A model units or component units may not have a units_ref attribute
    
The unit element numbering has changed

    5.4.3 used to be 5.4.2
    
Imports were introduced

    9.4.1.1.1 An `<import>` element can contain only `<component>`, `<units>`, and `<rdf:RDF>` elements
    9.4.1.1.2 An `<import>` element must define an `xlink:href` attribute
    
    9.4.1.2.1 A model must not directly or indirectly import itself.
    9.4.1.2.2 Component units cannot be imported

    9.4.1.3 An `xlink:href` attribute must be a valid URI.
    
    9.5.1 Imported units may depend on other units in the source model (but these do get imported too).
    
    9.5.2.2 If imported components are connected, their connections are imported too.
    9.5.2.3 If imported components have encapsulated components, these are imported too, along with their connections (note that each component is a tree, cousins can't interact!).
    9.5.2.4 Component units may depend on other units in the source model (but these do not get imported too).
    

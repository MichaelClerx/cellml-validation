# Condensed CellML 2.0 rules

This is a selection of rules from CellML 2.0 used as a basis for the CellML 2.0 test set.

## General document rules

- 1.2.1.1 CellML documents must be well-formed XML 1.1.
- 1.2.2.2 Elements and attributes can only appear where the spec explicitly allows them.
- 1.2.3.2 CellML elements must not contain character items other than whitespace.
- 1.2.4.1 All elements must be either in the CellML or the MathML namespace.
- 1.2.4.2 Unless explicitly stated otherwise, attributes are unnamespaced.
- 1.2.5 Every element in the CellML namespace may contain an id attribute.

- 1.3.1.1 Identifiers are only letters, numbers, or underscores.
- 1.3.1.1 Identifiers must begin with a letter.

- 1.3.2.1 Integer strings are base ten.
- 1.3.2.2 Integer string may start with `+` or `-`.
- 1.3.2.3 Integer strings can only contain optional sign, plus one or more digits.

- 1.3.3.1 Basic real number strings are base ten.
- 1.3.3.2 Basic real number strings may start with `+` or `-`.
- 1.3.3.3 Basic real number strings may contain a `.`.
- 1.3.3.4 Basic real number strings can only contain an optional `+` or `-.`, an optional `.`, and one or more digits.

- 1.3.4.2 Real number strings are a basic real number string, optionally followed by an exponent.
- 1.3.4.4 The exponent is `e` or `E`, followed by an integer string.

## Elements

- 2.1 The top-level element must be a `<model>`.

- 2.1.1 A `model` must have a `name` attribute.
- 2.1.1 A `model` `name` must be an identifier.
- 2.1.2.1 A `model` may contain one or more `component` elements.
- 2.1.2.2 A `model` may contain one or more `connection` elements.
- 2.1.2.3 A `model` may contain an `encapsulation` element.
- 2.1.2.4 A `model` may contain one or more `import` elements.
- 2.1.2.5 A `model` may contain one or more `units` elements.
- 2.1.3 A `model` must not contain more than one `encapsulation` element.

- 2.2.1 An `import` must have an `xlink:href` attribute.
- 2.2.1 An `import` `xlink:href` must be a [valid xlink locator](https://www.w3.org/TR/2001/REC-xlink-20010627/#link-locators).
- 2.2.2.1 An `import` may contain one or more `import units` elements.
- 2.2.2.2 An `import` may contain one or more `import component` elements.
- 2.2.3 The imported model must be different from the importing model.

- 2.3.1 An `import units` element (`<units>`) must have a `name` attribute.
- 2.3.1 An `import units` `name` must be an identifier.
- 2.3.1 An `import units` `name` must not match the `name` of any other `units` or `import units`.
- 2.3.2 An `import units` must have a `units_ref` attribute.
- 2.3.2 An `import units` units_ref` must be an identifier.
- 2.3.2 An `import units` units_ref` must match the `name` of a `units` or `import units` in the imported model.
- Missing rule: An `import units` `name` must not match the name of a built-in unit.

- 2.4.1 An `import component` element (`<component>`) must have a `name` attribute.
- 2.4.1 An `import component` `name` must be an identifier.
- 2.4.1 An `import component` `name` must not match the `name` of any other `component` or `import component`.
- 2.4.2 An `import component` must have a `component_ref` attribute.
- 2.4.2 An `import component` `component_ref` must be an identifier.
- 2.4.2 An `import component` `component_ref` must match the name of a `component` or `import component` in the imported model.

- 2.5.1 A `units` must have a `name` attribute.
- 2.5.1 A `units` `name` must be an identifier.
- 2.5.1 A `units` `name` must not match the `name` of any other `units` or `import units`.
- 2.5.2 A `units` `name` must not match the name of a built-in unit.
- 2.5.3 A `units` may contain one or more `unit` elements.

- 2.6.1 A `unit` must have a `units` attribute.
- 2.6.1 A `unit` `units` must be a valid units reference.
- 2.6.1.2 A unit definition must not be cyclical.
- 2.6.2.1 A `units` may have a `prefix` attribute.
- 2.6.2.1 A `units` `prefix` must be an integer string or a prefix string.
- 2.6.2.2 A `units` may have a `multiplier` attribute.
- 2.6.2.2 A `units` `multiplier` must be a real number string.
- 2.6.2.3 A `units` may have an `exponent` attribute.
- 2.6.2.3 A `units` `exponent` must be a real number string.

- 2.7.1 A `component` must have a `name` attribute.
- 2.7.1 A `component` `name` must be an identifier.
- 2.7.1 A `component` `name` must not match the `name` of any other `component` or `import component`.
- 2.7.2.1 A `component` may contain one or more `mathml:math` elements.
- 2.7.2.2 A `component` may contain one or more `reset` elements.
- 2.7.2.3 A `component` may contain one or more `variable` elements.

- 2.8.1.1 A `variable` must have a `name` attribute.
- 2.8.1.1 A `variable` `name` must be an identifier.
- 2.8.1.1 A `variable` `name` must be unique within the component.
- 2.8.1.2 A `variable` must have a `units` attribute.
- 2.8.1.2 A `variable` `units` must be a valid units reference.
- 2.8.2.1 A `variable` may have an `interface` attribute.
- 2.8.2.1 A `variable` `interface` must be "public", "private", "public_and_private", or "none".
- 2.8.2.2 A `variable` may have an `initial_value` attribute.
- 2.8.2.2 A `variable` `initial_value` must be a number of the name of a local variable.

- 2.9.1.1 A `reset` must have a `variable` attribute.
- 2.9.1.1 A `reset` `variable` must match the name of a `variable` in the same component.
- 2.9.1.2 A `reset` must have a `test_variable` attribute.
- 2.9.1.2 A `reset` `test_variable` must match the name of a `variable` in the same component.
- 2.9.1.3 A `reset` must have an `order` attribute.
- 2.9.1.3 A `reset` `order` must be an integer string.
- 2.9.1.3 A `reset` `order` must be unique for all resets on the same variable (including connected variables).
- 2.9.2.1 A `reset` must contain exactly one `reset_value` element.
- 2.9.2.2 A `reset` must contain exactly one `test_value` element.

- 2.10.1 A `test_value` must contain exactly one `mathml:math` element.

- 2.11.1 A `reset_value` must contain exactly one `mathml:math` element.

- 2.12.1 A `mathml:math` must contain content MathML.
- 2.12.2 Only elements from the supported subset are allowed.
- 2.12.3 All `mathml:ci` elements must contain the name of a `variable` in the same component.
- 2.12.4 All `mathml:cn` elements must have a `cellml:units` attribute.
- 2.12.4 The value of a `cellml:units` attribute must be a valid units reference.
- 2.12.5 All `mathml:cn` elements must be of type "real" or "e-notation".
- 2.12.5 All `mathml:cn` elements must be base ten.

- 2.13.1 An `encapsulation` may contain one or more `component_ref` elements.

- 2.14.1 A `component_ref` must have a `component` attribute.
- 2.14.1 A `component_ref` `component` must match the name of a `component` or an `import component`.
- 2.14.1 A `component_ref` `component` must be unique.
- 2.14.2 A `component_ref` may contain further `component_ref` elements.

- 2.15.1 A `connection` must have a `component_1` attribute.
- 2.15.1 A `connection` `component_1` must match the name of a `component` or `import component`.
- 2.15.2 A `connection` must have a `component_2` attribute.
- 2.15.2 A `connection` `component_2` must match the name of a `component` or `import component`.
- 2.15.3 A `connection` `component_1` and `component_2` cannot have the same value.
- 2.15.4 For any two components, there can be at most one `connection`.
- 2.15.5 A `connection` may contain one or more `map_variables` elements.

- 2.16.1 A `map_variables` must have a `variable_1` attribute.
- 2.16.1 A `map_variables` `variable_1` must match the name of a `variable` in component_1.
- 2.16.2 A `map_variables` must have a `variable_2` attribute.
- 2.16.2 A `map_variables` `variable_2` must match the name of a `variable` in component_2.
- 2.16.3 The pair (`variable_1`, `variable_2`) must be unique within the `connection`.

## Interpretation

- 3.1.1 Each `import units` or `import components` creates a distinct infoset.
- 3.1.2 A units reference in an import element is resolved within its infoset.
- 3.1.3.1 Connections can be made from local to imported components.
- 3.1.3.2 Connections to child components in the imported model are maintained, connections to sibiling and/or parents are not.

- 3.2.1 A units reference must be an identifier.
- 3.2.2 A units reference must be the name of units defined or imported in the model, or one of the built-in units.

- 3.3.1.1 The `prefix` attribute has default value 0.
- 3.3.1.1 If the `prefix` is an integer, the "prefix value" is that integer.
- 3.3.1.1 If the `prefix` is a string, the "prefix value" is given by the prefix values table.
- 3.3.1.2 The `exponent` attribute has default value 1.
- 3.3.1.3 The `multiplier` attribute has default value 1.
- 3.3.3.1 Empty units elements define a new base unit (with exponent 1)

- 3.10.4 Connections cannot connect two variables twice.
- 3.10.5 The connection network must not contain any cycles.
- 3.10.7.1 Connections between sibling components use the public interface.
- 3.10.7.2 In parent-child relations, the parent variable uses the private interface.
- 3.10.7.2 In parent-child relations, the child variable uses the public interface.
- 3.10.9 Connected variables must have compatible units.
- 3.10.10 If two units differ by a scaling factor, this must be taken into account when evaluating the model's mathematics.

- Missing rule: Variables can't have value `true` or `false`

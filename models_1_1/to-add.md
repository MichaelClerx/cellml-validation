# Tests yet to be added

New elements: `<import>`.
New attributes: no new CellML imports, although there are now rules for `xlink:href`.

## Valid

- [ ] 2.4.3.import_with_extensions
- [ ] 2.4.3.xlink_href_in_import
- [ ] 3.4.1.1.model_with_import
- [ ] 3.4.3.7.variable_with_initial_value_variable --> And add to invalid 1.0

## Invalid

- [ ] xlink is no longer valid anywhere
- [ ] 2.4.3.bad_cmeta_attribute_in_import
- [ ] 2.4.3.bad_rdf_element_in_import
- [ ] 2.4.3.cmeta_element_in_import
- [ ] 2.4.3.mathml_attribute_in_import
- [ ] 2.4.3.rdf_attribute_in_import
- [ ] 2.4.4.text_in_import
- [ ] 3.4.2.1.component_with_import (2 cases: in model & in import)
- [ ] 3.4.3.1.variable_with_import
- [ ] import_with_import
- [ ] units_with_import (2 cases: in model & in import)
- [ ] unit with import
- [ ] reaction with import
- [ ] variable_ref with import
- [ ] role with import
- [ ] math with import? Or general case "cellml in math"
- [ ] group_with_import
- [ ] relationship_ref_with_import
- [ ] component_ref_with_import (and nested?)
- [ ] connection_with_import
- [ ] map_components_with_import
- [ ] map_variables_with_import

## Sections

3.2.1/3.4.1 <import> in model
3.2.2/3.4.2 <component> in import
3.2.4 connection to imported variables
5.4.1 <units> in import
5.4.2 units_ref rules
9 Importing models

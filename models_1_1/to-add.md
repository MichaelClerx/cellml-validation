# Tests yet to be added

New elements: `<import>`.
New attributes: no new CellML imports, although there are now rules for `xlink:href`.

## Valid

- [ ] 2.4.3.import_with_extensions
- [ ] 2.4.3.xlink_href_in_import
- [ ] 3.4.1.1.model_with_import
- [ ] 3.4.3.7.variable_with_initial_value_variable --> And add to invalid 1.0
- [ ] 3.4.3.7 same but with 1 or 2 imported components
- [ ] 5.? Unit shadowing: Component overrides model unit
- [ ] 6.x connections to imported components (and interfaces etc.)
- [ ] 6.x unit conversion to imported components/units
- [ ] imported relationship
- [ ] 8.4.1_cmeta_id_in_import
- [ ] 8.4.1_cmeta_id_in_import_component
- [ ] 8.4.1_cmeta_id_in_import_units
- [ ] 8.4.1_cmeta_id_in imported elements (component, units, variables, connections?)
- [ ] 8.4.2_rdf_in_import
- [ ] 8.4.2_rdf_in_import_component
- [ ] 8.4.2_rdf_in_import_units
- [ ] duplicate_connections w imports
- [ ] overdefined w imports
- [ ] unit_checking_consistent w imports
- [ ] unit_checking_inconsistent w imports
- [ ] unit_conversion_convertible w imports


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
- [ ] 3.4.4.1_connection_with_import
- [ ] 3.4.5.1_map_components_with_import
- [ ] 3.4.6.1_map_variables_with_import
- [ ] 3.4.x some invalid interfaces, relationships etc. w imports
- [ ] 4.4.2 some invalid ci references w imports
- [ ] 4.4.3.2 some invalid cn units references w imports
- [ ] 5.4.1.1_units_with_import
- [ ] 5.4.1.2 duplicate names etc w imports
- [ ] 5.4.2.1_unit_with_import
- [ ] 5.4.2.2 unit cycle w imports
- [ ] 6.4.1.1_group_with_import
- [ ] 6.4.2.1_relationship_ref_with_import
- [ ] 6.4.2.5 relationship ref duplicate w imports?
- [ ] 6.4.3.1_component_ref_with_import
- [ ] 6.4.3.2_component_ref errors w imports
- [ ] 6.4.3.3_component_ref errors w imports
- [ ] 7.4.1.1_reaction_with_import
- [ ] 7.4.2.1_variable_ref_with_import
- [ ] 7.4.3.1_role_with_import
- [ ] 8.4.1 duplicate cmeta ids in imported elements

## Sections

3.2.1/3.4.1 <import> in model
3.2.2/3.4.2 <component> in import
3.2.4 connection to imported variables
5.4.1 <units> in import
5.4.2 units_ref rules
9 Importing models

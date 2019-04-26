# DTD Validation - CellML 1.0

Performance:
* 280 out of 316 valid files passed
* 253 out of 447 invalid files detected

Issues:
* 36 valid files failed to parse
* 194 invalid files passed validation
* 0 invalid files failed validation for the wrong reason

## 0.0

`0.0.root_namespace_1`: Valid file passed OK

`0.0.root_namespace_2`: Valid file passed OK

❌ `0.0.root_node_namespace_wrong`: Invalid file passed validation

❌ `0.0.root_node_not_model`: Invalid file passed validation

`0.0.root_node_two_elements`: Error in invalid file detected

`0.0.root_node_two_models`: Error in invalid file detected


### 0.1

❌ `0.1.real_number_invalid_1`: Invalid file passed validation

❌ `0.1.real_number_invalid_2`: Invalid file passed validation

❌ `0.1.real_number_invalid_3`: Invalid file passed validation

❌ `0.1.real_number_invalid_4`: Invalid file passed validation

❌ `0.1.real_number_invalid_5`: Invalid file passed validation

❌ `0.1.real_number_invalid_6`: Invalid file passed validation

`0.1.real_numbers`: Valid file passed OK

`0.1.real_numbers_extreme`: Valid file passed OK


### 0.2

`0.2.component_name_same_as_model`: Valid file passed OK

`0.2.variable_name_same_as_model`: Valid file passed OK


## 2.4.1

❌ `2.4.1.identifier_empty`: Invalid file passed validation

❌ `2.4.1.identifier_only_underscore`: Invalid file passed validation

❌ `2.4.1.identifier_unexpected_character_1`: Invalid file passed validation

❌ `2.4.1.identifier_unexpected_character_2`: Invalid file passed validation

❌ `2.4.1.identifier_unexpected_character_unicode`: Invalid file passed validation

`2.4.1.valid_identifiers`: Valid file passed OK


#### 2.4.2

`2.4.2.imaginary_attributes_1`: Error in invalid file detected

`2.4.2.imaginary_attributes_2`: Error in invalid file detected

`2.4.2.imaginary_elements`: Error in invalid file detected


#### 2.4.3

`2.4.3.cellml_attributes_inside_extensions`: Error in invalid file detected

`2.4.3.cellml_elements_inside_extensions`: Error in invalid file detected

❌ `2.4.3.component_ref_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 11: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (fruit:orange fruit:pear )
  * Error on line 11: No declaration for attribute banana of element component_ref
  * Error on line 12: No declaration for element orange
  * Error on line 12: No declaration for attribute peel of element orange
  * Error on line 13: No declaration for element clementine
  * Error on line 15: No declaration for element pear

❌ `2.4.3.component_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 6: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (fruit:orange fruit:pear )
  * Error on line 6: No declaration for attribute banana of element component
  * Error on line 7: No declaration for element orange
  * Error on line 7: No declaration for attribute peel of element orange
  * Error on line 8: No declaration for element clementine
  * Error on line 10: No declaration for element pear

❌ `2.4.3.connection_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 6: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (fruit:orange fruit:pear map_components map_variables )
  * Error on line 6: No declaration for attribute x_a_day of element connection
  * Error on line 7: No declaration for element orange
  * Error on line 7: No declaration for attribute peel of element orange
  * Error on line 8: No declaration for element clementine
  * Error on line 10: No declaration for element pear

❌ `2.4.3.group_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 8: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (fruit:orange fruit:pear relationship_ref component_ref )
  * Error on line 8: No declaration for attribute banana of element group
  * Error on line 9: No declaration for element orange
  * Error on line 9: No declaration for attribute peel of element orange
  * Error on line 10: No declaration for element clementine
  * Error on line 12: No declaration for element pear

❌ `2.4.3.map_components_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 7: Element map_components was declared EMPTY this one has content
  * Error on line 7: No declaration for attribute x_a_day of element map_components
  * Error on line 8: No declaration for element orange
  * Error on line 8: No declaration for attribute peel of element orange
  * Error on line 9: No declaration for element clementine
  * Error on line 11: No declaration for element pear

❌ `2.4.3.map_variables_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 8: Element map_variables was declared EMPTY this one has content
  * Error on line 8: No declaration for attribute x_a_day of element map_variables
  * Error on line 9: No declaration for element orange
  * Error on line 9: No declaration for attribute peel of element orange
  * Error on line 10: No declaration for element clementine
  * Error on line 12: No declaration for element pear

❌ `2.4.3.model_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 6: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (fruit:orange fruit:pear )
  * Error on line 6: No declaration for attribute x_a_day of element model
  * Error on line 6: No declaration for attribute xmlns:fruit of element model
  * Error on line 7: No declaration for element orange
  * Error on line 7: No declaration for attribute peel of element orange
  * Error on line 8: No declaration for element clementine
  * Error on line 10: No declaration for element pear

❌ `2.4.3.reaction_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (fruit:orange fruit:pear variable_ref )
  * Error on line 8: No declaration for attribute x_a_day of element reaction
  * Error on line 9: No declaration for element orange
  * Error on line 9: No declaration for attribute peel of element orange
  * Error on line 10: No declaration for element clementine
  * Error on line 12: No declaration for element pear

❌ `2.4.3.relationship_ref_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 9: Element relationship_ref was declared EMPTY this one has content
  * Error on line 9: No declaration for attribute banana of element relationship_ref
  * Error on line 10: No declaration for element orange
  * Error on line 10: No declaration for attribute peel of element orange
  * Error on line 11: No declaration for element clementine
  * Error on line 13: No declaration for element pear

❌ `2.4.3.role_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (fruit:orange fruit:pear )
  * Error on line 10: No declaration for attribute x_a_day of element role
  * Error on line 11: No declaration for element orange
  * Error on line 11: No declaration for attribute peel of element orange
  * Error on line 12: No declaration for element clementine
  * Error on line 14: No declaration for element pear

❌ `2.4.3.unit_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 7: Element unit was declared EMPTY this one has content
  * Error on line 7: No declaration for attribute x_a_day of element unit
  * Error on line 8: No declaration for element orange
  * Error on line 8: No declaration for attribute peel of element orange
  * Error on line 9: No declaration for element clementine
  * Error on line 11: No declaration for element pear

❌ `2.4.3.units_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 6: Element units content does not follow the DTD, expecting (unit)*, got (unit fruit:orange fruit:pear )
  * Error on line 6: No declaration for attribute x_a_day of element units
  * Error on line 8: No declaration for element orange
  * Error on line 8: No declaration for attribute peel of element orange
  * Error on line 9: No declaration for element clementine
  * Error on line 11: No declaration for element pear
  * Error on line 14: Element units content does not follow the DTD, expecting (unit)*, got (unit fruit:orange fruit:pear )
  * Error on line 14: No declaration for attribute x_a_day of element units
  * Error on line 16: No declaration for element orange
  * Error on line 16: No declaration for attribute peel of element orange
  * Error on line 17: No declaration for element clementine
  * Error on line 19: No declaration for element pear

❌ `2.4.3.variable_ref_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (fruit:orange fruit:pear role )
  * Error on line 9: No declaration for attribute x_a_day of element variable_ref
  * Error on line 10: No declaration for element orange
  * Error on line 10: No declaration for attribute peel of element orange
  * Error on line 11: No declaration for element clementine
  * Error on line 13: No declaration for element pear

❌ `2.4.3.variable_with_extensions`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 7: Element variable was declared EMPTY this one has content
  * Error on line 7: No declaration for attribute x_a_day of element variable
  * Error on line 8: No declaration for element orange
  * Error on line 8: No declaration for attribute peel of element orange
  * Error on line 9: No declaration for element clementine
  * Error on line 11: No declaration for element pear


#### 2.4.4

`2.4.4.model_linux_line_breaks`: Valid file passed OK

`2.4.4.model_windows_line_breaks`: Valid file passed OK

`2.4.4.model_with_spaces`: Valid file passed OK

`2.4.4.model_with_tabs`: Valid file passed OK

`2.4.4.text_in_component`: Error in invalid file detected

`2.4.4.text_in_component_ref`: Error in invalid file detected

`2.4.4.text_in_connection`: Error in invalid file detected

`2.4.4.text_in_group`: Error in invalid file detected

`2.4.4.text_in_map_components`: Error in invalid file detected

`2.4.4.text_in_map_variables`: Error in invalid file detected

`2.4.4.text_in_model`: Error in invalid file detected

`2.4.4.text_in_reaction`: Error in invalid file detected

`2.4.4.text_in_relationship_ref`: Error in invalid file detected

`2.4.4.text_in_role`: Error in invalid file detected

`2.4.4.text_in_unit`: Error in invalid file detected

`2.4.4.text_in_units_1`: Error in invalid file detected

`2.4.4.text_in_units_2`: Error in invalid file detected

`2.4.4.text_in_variable`: Error in invalid file detected

`2.4.4.text_in_variable_ref`: Error in invalid file detected


### 2.5.1

❌ `2.5.1.identifiers_are_case_sensitive`: Invalid file passed validation


#### 2.5.2

`2.5.2.attribute_in_cellml_namespace`: Error in invalid file detected


## 3.4.1.1

`3.4.1.1.model_child_order_1`: Valid file passed OK

`3.4.1.1.model_child_order_2`: Valid file passed OK

`3.4.1.1.model_empty`: Valid file passed OK

`3.4.1.1.model_name_missing`: Error in invalid file detected

`3.4.1.1.model_with_component_ref`: Error in invalid file detected

`3.4.1.1.model_with_components`: Valid file passed OK

`3.4.1.1.model_with_connections`: Valid file passed OK

`3.4.1.1.model_with_groups`: Valid file passed OK

`3.4.1.1.model_with_map_components`: Error in invalid file detected

`3.4.1.1.model_with_map_variables`: Error in invalid file detected

`3.4.1.1.model_with_math`: Error in invalid file detected

`3.4.1.1.model_with_model`: Error in invalid file detected

`3.4.1.1.model_with_one_component`: Valid file passed OK

`3.4.1.1.model_with_one_connection`: Valid file passed OK

`3.4.1.1.model_with_one_group`: Valid file passed OK

`3.4.1.1.model_with_one_units`: Valid file passed OK

`3.4.1.1.model_with_reaction`: Error in invalid file detected

`3.4.1.1.model_with_relationship_ref`: Error in invalid file detected

`3.4.1.1.model_with_role`: Error in invalid file detected

`3.4.1.1.model_with_unit`: Error in invalid file detected

`3.4.1.1.model_with_units`: Valid file passed OK

`3.4.1.1.model_with_variable`: Error in invalid file detected

`3.4.1.1.model_with_variable_ref`: Error in invalid file detected


##### 3.4.1.2

❌ `3.4.1.2.model_name_invalid`: Invalid file passed validation


#### 3.4.2.1

`3.4.2.1.component_child_order_1`: Valid file passed OK

`3.4.2.1.component_child_order_2`: Valid file passed OK

`3.4.2.1.component_empty`: Valid file passed OK

`3.4.2.1.component_name_missing`: Error in invalid file detected

`3.4.2.1.component_with_component`: Error in invalid file detected

`3.4.2.1.component_with_component_ref`: Error in invalid file detected

`3.4.2.1.component_with_connection`: Error in invalid file detected

`3.4.2.1.component_with_group`: Error in invalid file detected

`3.4.2.1.component_with_map_components`: Error in invalid file detected

`3.4.2.1.component_with_map_variables`: Error in invalid file detected

`3.4.2.1.component_with_maths`: Valid file passed OK

`3.4.2.1.component_with_model`: Error in invalid file detected

`3.4.2.1.component_with_one_math`: Valid file passed OK

`3.4.2.1.component_with_one_reaction`: Valid file passed OK

`3.4.2.1.component_with_one_units`: Valid file passed OK

`3.4.2.1.component_with_one_variable`: Valid file passed OK

`3.4.2.1.component_with_reactions`: Valid file passed OK

`3.4.2.1.component_with_relationship_ref`: Error in invalid file detected

`3.4.2.1.component_with_role`: Error in invalid file detected

`3.4.2.1.component_with_unit`: Error in invalid file detected

`3.4.2.1.component_with_units`: Valid file passed OK

`3.4.2.1.component_with_variable_ref`: Error in invalid file detected

`3.4.2.1.component_with_variables`: Valid file passed OK


##### 3.4.2.2

❌ `3.4.2.2.component_name_duplicate`: Invalid file passed validation

❌ `3.4.2.2.component_name_invalid`: Invalid file passed validation


#### 3.4.3.1

`3.4.3.1.variable_name_missing`: Error in invalid file detected

`3.4.3.1.variable_units_missing`: Error in invalid file detected

`3.4.3.1.variable_with_component`: Error in invalid file detected

`3.4.3.1.variable_with_component_ref`: Error in invalid file detected

`3.4.3.1.variable_with_connection`: Error in invalid file detected

`3.4.3.1.variable_with_group`: Error in invalid file detected

`3.4.3.1.variable_with_initial_value`: Valid file passed OK

`3.4.3.1.variable_with_interfaces`: Valid file passed OK

`3.4.3.1.variable_with_map_components`: Error in invalid file detected

`3.4.3.1.variable_with_map_variables`: Error in invalid file detected

`3.4.3.1.variable_with_math`: Error in invalid file detected

`3.4.3.1.variable_with_model`: Error in invalid file detected

`3.4.3.1.variable_with_reaction`: Error in invalid file detected

`3.4.3.1.variable_with_relationship_ref`: Error in invalid file detected

`3.4.3.1.variable_with_role`: Error in invalid file detected

`3.4.3.1.variable_with_unit`: Error in invalid file detected

`3.4.3.1.variable_with_units`: Error in invalid file detected

`3.4.3.1.variable_with_variable`: Error in invalid file detected

`3.4.3.1.variable_with_variable_ref`: Error in invalid file detected

`3.4.3.1.variable_without_initial_value`: Valid file passed OK


##### 3.4.3.2

❌ `3.4.3.2.variable_name_duplicate`: Invalid file passed validation

❌ `3.4.3.2.variable_name_invalid`: Invalid file passed validation

`3.4.3.2.variable_name_same_as_cousin`: Valid file passed OK

`3.4.3.2.variable_name_same_as_parent`: Valid file passed OK


##### 3.4.3.3

`3.4.3.3.variable_units_component`: Valid file passed OK

`3.4.3.3.variable_units_model`: Valid file passed OK

❌ `3.4.3.3.variable_units_other_component`: Invalid file passed validation

`3.4.3.3.variable_units_predefined`: Valid file passed OK

❌ `3.4.3.3.variable_units_unknown`: Invalid file passed validation


##### 3.4.3.4

`3.4.3.4.variable_interface_public_invalid`: Error in invalid file detected


##### 3.4.3.5

`3.4.3.5.variable_interface_private_invalid`: Error in invalid file detected


##### 3.4.3.6

❌ `3.4.3.6.variable_interfaces_both_in`: Invalid file passed validation


##### 3.4.3.7

❌ `3.4.3.7.variable_initial_value_empty`: Invalid file passed validation

❌ `3.4.3.7.variable_initial_value_invalid`: Invalid file passed validation


##### 3.4.3.8

❌ `3.4.3.8.variable_interfaces_private_in_and_initial`: Invalid file passed validation

❌ `3.4.3.8.variable_interfaces_public_in_and_initial`: Invalid file passed validation


#### 3.4.4.1

`3.4.4.1.connection_empty`: Error in invalid file detected

`3.4.4.1.connection_map_components_missing`: Error in invalid file detected

`3.4.4.1.connection_map_components_multiple`: Error in invalid file detected

`3.4.4.1.connection_map_variables_missing_1`: Error in invalid file detected

`3.4.4.1.connection_map_variables_missing_2`: Error in invalid file detected

`3.4.4.1.connection_only_extensions`: Error in invalid file detected

`3.4.4.1.connection_with_component`: Error in invalid file detected

`3.4.4.1.connection_with_component_ref`: Error in invalid file detected

`3.4.4.1.connection_with_connection`: Error in invalid file detected

`3.4.4.1.connection_with_group`: Error in invalid file detected

`3.4.4.1.connection_with_map_variables`: Valid file passed OK

`3.4.4.1.connection_with_math`: Error in invalid file detected

`3.4.4.1.connection_with_model`: Error in invalid file detected

`3.4.4.1.connection_with_name_attribute`: Error in invalid file detected

`3.4.4.1.connection_with_one_map_variables`: Valid file passed OK

`3.4.4.1.connection_with_reaction`: Error in invalid file detected

`3.4.4.1.connection_with_relationship_ref`: Error in invalid file detected

`3.4.4.1.connection_with_role`: Error in invalid file detected

`3.4.4.1.connection_with_unit`: Error in invalid file detected

`3.4.4.1.connection_with_units`: Error in invalid file detected

`3.4.4.1.connection_with_variable`: Error in invalid file detected

`3.4.4.1.connection_with_variable_ref`: Error in invalid file detected


#### 3.4.5.1

`3.4.5.1.connection_any_order_1`: Valid file passed OK

`3.4.5.1.connection_any_order_2`: Valid file passed OK

`3.4.5.1.map_components_component_1_missing`: Error in invalid file detected

`3.4.5.1.map_components_component_2_missing`: Error in invalid file detected

`3.4.5.1.map_components_with_component`: Error in invalid file detected

`3.4.5.1.map_components_with_component_ref`: Error in invalid file detected

`3.4.5.1.map_components_with_connection`: Error in invalid file detected

`3.4.5.1.map_components_with_group`: Error in invalid file detected

`3.4.5.1.map_components_with_map_components`: Error in invalid file detected

`3.4.5.1.map_components_with_map_variables`: Error in invalid file detected

`3.4.5.1.map_components_with_math`: Error in invalid file detected

`3.4.5.1.map_components_with_model`: Error in invalid file detected

`3.4.5.1.map_components_with_reaction`: Error in invalid file detected

`3.4.5.1.map_components_with_relationship_ref`: Error in invalid file detected

`3.4.5.1.map_components_with_role`: Error in invalid file detected

`3.4.5.1.map_components_with_unit`: Error in invalid file detected

`3.4.5.1.map_components_with_units`: Error in invalid file detected

`3.4.5.1.map_components_with_variable`: Error in invalid file detected

`3.4.5.1.map_components_with_variable_ref`: Error in invalid file detected


##### 3.4.5.2

❌ `3.4.5.2.map_components_component_1_nonexistent`: Invalid file passed validation


##### 3.4.5.3

❌ `3.4.5.3.map_components_component_2_nonexistent`: Invalid file passed validation


##### 3.4.5.4

❌ `3.4.5.4.map_components_component_1_equals_2`: Invalid file passed validation

❌ `3.4.5.4.map_components_duplicate`: Invalid file passed validation

❌ `3.4.5.4.map_components_duplicate_mirrored`: Invalid file passed validation


#### 3.4.6.1

`3.4.6.1.map_variables_variable_1_missing`: Error in invalid file detected

`3.4.6.1.map_variables_variable_2_missing`: Error in invalid file detected

`3.4.6.1.map_variables_with_component`: Error in invalid file detected

`3.4.6.1.map_variables_with_component_ref`: Error in invalid file detected

`3.4.6.1.map_variables_with_connection`: Error in invalid file detected

`3.4.6.1.map_variables_with_group`: Error in invalid file detected

`3.4.6.1.map_variables_with_map_components`: Error in invalid file detected

`3.4.6.1.map_variables_with_map_variables`: Error in invalid file detected

`3.4.6.1.map_variables_with_math`: Error in invalid file detected

`3.4.6.1.map_variables_with_model`: Error in invalid file detected

`3.4.6.1.map_variables_with_reaction`: Error in invalid file detected

`3.4.6.1.map_variables_with_relationship_ref`: Error in invalid file detected

`3.4.6.1.map_variables_with_role`: Error in invalid file detected

`3.4.6.1.map_variables_with_unit`: Error in invalid file detected

`3.4.6.1.map_variables_with_units`: Error in invalid file detected

`3.4.6.1.map_variables_with_variable`: Error in invalid file detected

`3.4.6.1.map_variables_with_variable_ref`: Error in invalid file detected


##### 3.4.6.2

❌ `3.4.6.2.map_variables_variable_1_nonexistent`: Invalid file passed validation


##### 3.4.6.3

❌ `3.4.6.3.map_variables_variable_2_nonexistent`: Invalid file passed validation


##### 3.4.6.4

`3.4.6.4.map_variables_chain_down`: Valid file passed OK

`3.4.6.4.map_variables_chain_up`: Valid file passed OK

❌ `3.4.6.4.map_variables_child_multiple_out_1`: Invalid file passed validation

❌ `3.4.6.4.map_variables_child_multiple_out_2`: Invalid file passed validation

❌ `3.4.6.4.map_variables_child_out_to_out_1`: Invalid file passed validation

❌ `3.4.6.4.map_variables_child_out_to_out_2`: Invalid file passed validation

❌ `3.4.6.4.map_variables_child_private_in`: Invalid file passed validation

❌ `3.4.6.4.map_variables_child_private_out`: Invalid file passed validation

❌ `3.4.6.4.map_variables_hidden_aunt_1`: Invalid file passed validation

❌ `3.4.6.4.map_variables_hidden_aunt_2`: Invalid file passed validation

❌ `3.4.6.4.map_variables_hidden_cousins_1`: Invalid file passed validation

❌ `3.4.6.4.map_variables_hidden_cousins_2`: Invalid file passed validation

❌ `3.4.6.4.map_variables_hidden_cousins_3`: Invalid file passed validation

❌ `3.4.6.4.map_variables_hidden_cousins_4`: Invalid file passed validation

❌ `3.4.6.4.map_variables_hidden_grandchild_1`: Invalid file passed validation

❌ `3.4.6.4.map_variables_hidden_grandchild_2`: Invalid file passed validation

❌ `3.4.6.4.map_variables_hidden_grandparent_1`: Invalid file passed validation

❌ `3.4.6.4.map_variables_hidden_grandparent_2`: Invalid file passed validation

❌ `3.4.6.4.map_variables_hidden_niece_1`: Invalid file passed validation

❌ `3.4.6.4.map_variables_hidden_niece_2`: Invalid file passed validation

`3.4.6.4.map_variables_nested_sibling_connection`: Valid file passed OK

❌ `3.4.6.4.map_variables_nested_sibling_private_in`: Invalid file passed validation

❌ `3.4.6.4.map_variables_nested_sibling_private_in_and_out`: Invalid file passed validation

❌ `3.4.6.4.map_variables_nested_sibling_private_out`: Invalid file passed validation

`3.4.6.4.map_variables_parent_connection_1`: Valid file passed OK

`3.4.6.4.map_variables_parent_connection_2`: Valid file passed OK

❌ `3.4.6.4.map_variables_parent_in_to_in_1`: Invalid file passed validation

❌ `3.4.6.4.map_variables_parent_in_to_in_2`: Invalid file passed validation

`3.4.6.4.map_variables_parent_multiple_1`: Valid file passed OK

`3.4.6.4.map_variables_parent_multiple_2`: Valid file passed OK

❌ `3.4.6.4.map_variables_parent_multiple_out`: Invalid file passed validation

❌ `3.4.6.4.map_variables_parent_out_to_out_1`: Invalid file passed validation

❌ `3.4.6.4.map_variables_parent_out_to_out_2`: Invalid file passed validation

❌ `3.4.6.4.map_variables_parent_public_in`: Invalid file passed validation

❌ `3.4.6.4.map_variables_parent_public_out`: Invalid file passed validation

`3.4.6.4.map_variables_sibling_connection_1`: Valid file passed OK

`3.4.6.4.map_variables_sibling_connection_2`: Valid file passed OK

`3.4.6.4.map_variables_sibling_connection_3`: Valid file passed OK

❌ `3.4.6.4.map_variables_sibling_in_to_in`: Invalid file passed validation

`3.4.6.4.map_variables_sibling_multiple_1`: Valid file passed OK

`3.4.6.4.map_variables_sibling_multiple_2`: Valid file passed OK

❌ `3.4.6.4.map_variables_sibling_multiple_out_1`: Invalid file passed validation

❌ `3.4.6.4.map_variables_sibling_multiple_out_2`: Invalid file passed validation

`3.4.6.4.map_variables_sibling_mutual`: Valid file passed OK

❌ `3.4.6.4.map_variables_sibling_out_to_out`: Invalid file passed validation

❌ `3.4.6.4.map_variables_sibling_private_in_1`: Invalid file passed validation

❌ `3.4.6.4.map_variables_sibling_private_in_2`: Invalid file passed validation

❌ `3.4.6.4.map_variables_sibling_private_in_and_out`: Invalid file passed validation

❌ `3.4.6.4.map_variables_sibling_private_out_1`: Invalid file passed validation

❌ `3.4.6.4.map_variables_sibling_private_out_2`: Invalid file passed validation

`3.4.6.4.map_variables_talking_aunt`: Valid file passed OK

`3.4.6.4.map_variables_talking_cousins`: Valid file passed OK

`3.4.6.4.map_variables_talking_niece`: Valid file passed OK


## 4.2

`4.2.3_1.mathml_basics`: Valid file passed OK

`4.2.3_2.1.mathml_numbers_real`: Valid file passed OK

`4.2.3_2.2.mathml_numbers_integer`: Valid file passed OK

`4.2.3_2.3.mathml_numbers_real_base`: Valid file passed OK

`4.2.3_2.4.mathml_numbers_integer_base`: Valid file passed OK

`4.2.3_2.5.mathml_numbers_e_notation`: Valid file passed OK

`4.2.3_2.6.mathml_numbers_rational`: Valid file passed OK

`4.2.3_3.1_mathml_arithmetic_binary`: Valid file passed OK

`4.2.3_3.2_mathml_arithmetic_n_ary`: Valid file passed OK

`4.2.3_3.2_mathml_arithmetic_unary`: Valid file passed OK

`4.2.3_4.1_mathml_functions_basic`: Valid file passed OK

`4.2.3_4.2_mathml_functions_non_smooth`: Valid file passed OK

`4.2.3_4.3_mathml_functions_factorial`: Valid file passed OK

`4.2.3_4.4_mathml_functions_trig`: Valid file passed OK

`4.2.3_4.5_mathml_functions_trig_hyperbolic`: Valid file passed OK

`4.2.3_4.6_mathml_functions_trig_redundant`: Valid file passed OK

`4.2.3_4.7_mathml_functions_trig_redundant_hyperbolic`: Valid file passed OK

`4.2.3_5.1_mathml_derivatives`: Valid file passed OK

`4.2.3_5.2_mathml_derivatives_degree`: Valid file passed OK

`4.2.3_5.3_mathml_derivatives_with_units`: Valid file passed OK

`4.2.3_5.4_mathml_derivatives_with_units_degree`: Valid file passed OK

`4.2.3_6.1_mathml_logic_one_piece`: Valid file passed OK

`4.2.3_6.2_mathml_logic_two_pieces`: Valid file passed OK

`4.2.3_6.3_mathml_logic_no_otherwise`: Valid file passed OK

`4.2.3_6.4_mathml_logic_comparisons`: Valid file passed OK

`4.2.3_6.5_mathml_logic_unary_operators`: Valid file passed OK

`4.2.3_6.6_mathml_logic_binary_operators`: Valid file passed OK

`4.2.3_6.7_mathml_logic_constants`: Valid file passed OK

`4.2.3_7.1_mathml_pi`: Valid file passed OK

`4.2.3_7.2_mathml_e`: Valid file passed OK

`4.2.3_7.3_mathml_nan_inf`: Valid file passed OK

`4.2.3_8.1_annotation`: Valid file passed OK

`4.2.3_8.2_annotation_xml`: Valid file passed OK


### 4.4.1

`4.4.1.math_not_math_component`: Error in invalid file detected

`4.4.1.math_not_math_reaction`: Error in invalid file detected


#### 4.4.2

`4.4.2.ci_no_whitespace`: Valid file passed OK

❌ `4.4.2.ci_non_local_aunt`: Invalid file passed validation

❌ `4.4.2.ci_non_local_child`: Invalid file passed validation

❌ `4.4.2.ci_non_local_cousin`: Invalid file passed validation

❌ `4.4.2.ci_non_local_nested_sibling`: Invalid file passed validation

❌ `4.4.2.ci_non_local_niece`: Invalid file passed validation

❌ `4.4.2.ci_non_local_parent`: Invalid file passed validation

❌ `4.4.2.ci_non_local_sibling`: Invalid file passed validation

❌ `4.4.2.ci_nonexistent`: Invalid file passed validation

`4.4.2.ci_whitespace_1`: Valid file passed OK

`4.4.2.ci_whitespace_2`: Valid file passed OK

`4.4.2.ci_whitespace_3`: Valid file passed OK


#### 4.4.3.1

`4.4.3.1.cn_component_units`: Valid file passed OK

`4.4.3.1.cn_model_units`: Valid file passed OK

`4.4.3.1.cn_predefined_units`: Valid file passed OK

`4.4.3.1.cn_units_missing`: Error in invalid file detected


##### 4.4.3.2

❌ `4.4.3.2.cn_units_nonexistent_1`: Invalid file passed validation

❌ `4.4.3.2.cn_units_nonexistent_2`: Invalid file passed validation

❌ `4.4.3.2.cn_units_parent_component`: Invalid file passed validation


#### 4.4.4

❌ `4.4.4.modify_nonexistent`: Invalid file passed validation

❌ `4.4.4.modify_private_in`: Invalid file passed validation

`4.4.4.modify_private_out`: Valid file passed OK

❌ `4.4.4.modify_public_in`: Invalid file passed validation

`4.4.4.modify_public_out`: Valid file passed OK


### 4.5.1

`4.5.1.ordering_not_significant`: Valid file passed OK

`4.algebraic_model`: Valid file passed OK

`4.algebraic_ode_model`: Valid file passed OK

❌ `4.math_and_initial_value`: Invalid file passed validation

❌ `4.math_overdefined`: Invalid file passed validation


## 5.2.2

❌ `5.2.2.unit_deca`: Invalid file passed validation


#### 5.2.7

`5.2.7.unit_checking_arithmetic`: Valid file passed OK

`5.2.7.unit_checking_comparisons`: Valid file passed OK

`5.2.7.unit_checking_derivatives`: Valid file passed OK

`5.2.7.unit_checking_derivatives_degree`: Valid file passed OK

`5.2.7.unit_checking_dimensionless`: Valid file passed OK

`5.2.7.unit_checking_functions_factorial`: Valid file passed OK

`5.2.7.unit_checking_functions_non_smooth`: Valid file passed OK

`5.2.7.unit_checking_functions_power_and_root`: Valid file passed OK

`5.2.7.unit_checking_internal_mismatch_1`: Valid file passed OK

`5.2.7.unit_checking_internal_mismatch_2`: Valid file passed OK

`5.2.7.unit_checking_internal_mismatch_3`: Valid file passed OK

`5.2.7.unit_checking_internal_mismatch_4`: Valid file passed OK

`5.2.7.unit_checking_name_differs`: Valid file passed OK

`5.2.7.unit_checking_piecewise`: Valid file passed OK

`5.2.7.unit_checking_piecewise_multi_unit`: Valid file passed OK

`5.2.7.unit_checking_repeated_unit`: Valid file passed OK

`5.2.7.unit_conversion_different_names_same_unit`: Valid file passed OK

`5.2.7.unit_conversion_dimensionless_exponent`: Valid file passed OK

`5.2.7.unit_conversion_dimensionless_multiplier_1`: Valid file passed OK

`5.2.7.unit_conversion_dimensionless_multiplier_2`: Valid file passed OK

`5.2.7.unit_conversion_dimensionless_offset`: Valid file passed OK

`5.2.7.unit_conversion_inconvertible_1`: Valid file passed OK

`5.2.7.unit_conversion_less_obvious`: Valid file passed OK

`5.2.7.unit_conversion_multiplier`: Valid file passed OK

`5.2.7.unit_conversion_new_base_units`: Valid file passed OK

`5.2.7.unit_conversion_offset`: Valid file passed OK

`5.2.7.unit_conversion_prefix`: Valid file passed OK


### 5.4.1.1

`5.4.1.1.units_base_units`: Valid file passed OK

❌ `5.4.1.1.units_base_units_with_children`: Invalid file passed validation

`5.4.1.1.units_empty_1`: Valid file passed OK

`5.4.1.1.units_empty_2`: Valid file passed OK

`5.4.1.1.units_name_missing`: Error in invalid file detected

`5.4.1.1.units_with_component`: Error in invalid file detected

`5.4.1.1.units_with_component_ref`: Error in invalid file detected

`5.4.1.1.units_with_connection`: Error in invalid file detected

`5.4.1.1.units_with_group`: Error in invalid file detected

`5.4.1.1.units_with_map_components`: Error in invalid file detected

`5.4.1.1.units_with_map_variables`: Error in invalid file detected

`5.4.1.1.units_with_math`: Error in invalid file detected

`5.4.1.1.units_with_model`: Error in invalid file detected

`5.4.1.1.units_with_reaction`: Error in invalid file detected

`5.4.1.1.units_with_relationship_ref`: Error in invalid file detected

`5.4.1.1.units_with_role`: Error in invalid file detected

`5.4.1.1.units_with_unit_children`: Valid file passed OK

`5.4.1.1.units_with_units`: Error in invalid file detected

`5.4.1.1.units_with_variable`: Error in invalid file detected

`5.4.1.1.units_with_variable_ref`: Error in invalid file detected


##### 5.4.1.2

❌ `5.4.1.2.units_name_duplicate_1`: Invalid file passed validation

❌ `5.4.1.2.units_name_duplicate_2`: Invalid file passed validation

❌ `5.4.1.2.units_name_invalid`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_ampere`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_becquerel`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_candela`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_celsius`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_component_ampere`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_coulomb`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_dimensionless`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_farad`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_gram`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_gray`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_henry`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_hertz`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_joule`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_katal`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_kelvin`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_kilogram`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_liter`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_litre`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_lumen`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_lux`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_meter`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_metre`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_mole`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_newton`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_ohm`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_pascal`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_radian`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_second`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_siemens`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_sievert`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_steradian`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_tesla`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_volt`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_watt`: Invalid file passed validation

❌ `5.4.1.2.units_name_predefined_weber`: Invalid file passed validation

`5.4.1.2.units_names_and_other_names`: Valid file passed OK

`5.4.1.2.units_shadowing_1`: Valid file passed OK

`5.4.1.2.units_shadowing_2`: Valid file passed OK


##### 5.4.1.3

`5.4.1.3.units_base_units_invalid`: Error in invalid file detected


#### 5.4.2.1

`5.4.2.1.unit_offset_non_zero`: Valid file passed OK

`5.4.2.1.unit_offset_zero`: Valid file passed OK

`5.4.2.1.unit_prefix_exponent_multiplier`: Valid file passed OK

`5.4.2.1.unit_units_missing`: Error in invalid file detected

`5.4.2.1.unit_with_component`: Error in invalid file detected

`5.4.2.1.unit_with_component_ref`: Error in invalid file detected

`5.4.2.1.unit_with_connection`: Error in invalid file detected

`5.4.2.1.unit_with_group`: Error in invalid file detected

`5.4.2.1.unit_with_map_components`: Error in invalid file detected

`5.4.2.1.unit_with_map_variables`: Error in invalid file detected

`5.4.2.1.unit_with_math`: Error in invalid file detected

`5.4.2.1.unit_with_model`: Error in invalid file detected

`5.4.2.1.unit_with_reaction`: Error in invalid file detected

`5.4.2.1.unit_with_relationship_ref`: Error in invalid file detected

`5.4.2.1.unit_with_role`: Error in invalid file detected

`5.4.2.1.unit_with_unit`: Error in invalid file detected

`5.4.2.1.unit_with_units`: Error in invalid file detected

`5.4.2.1.unit_with_variable`: Error in invalid file detected

`5.4.2.1.unit_with_variable_ref`: Error in invalid file detected


##### 5.4.2.2

❌ `5.4.2.2.unit_cycle_1`: Invalid file passed validation

❌ `5.4.2.2.unit_cycle_2`: Invalid file passed validation

❌ `5.4.2.2.unit_cycle_3`: Invalid file passed validation

❌ `5.4.2.2.unit_units_invalid`: Invalid file passed validation

`5.4.2.2.unit_units_local_1`: Valid file passed OK

`5.4.2.2.unit_units_local_2`: Valid file passed OK


##### 5.4.2.3

`5.4.2.3.unit_prefix_integer`: Valid file passed OK

`5.4.2.3.unit_prefix_named`: Valid file passed OK

❌ `5.4.2.3.unit_prefix_real`: Invalid file passed validation

❌ `5.4.2.3.unit_prefix_real_int`: Invalid file passed validation

❌ `5.4.2.3.unit_prefix_spaces`: Invalid file passed validation

❌ `5.4.2.3.unit_prefix_unknown`: Invalid file passed validation


##### 5.4.2.4

❌ `5.4.2.4.unit_exponent_invalid`: Invalid file passed validation


##### 5.4.2.5

❌ `5.4.2.5.unit_multiplier_invalid`: Invalid file passed validation


##### 5.4.2.6

❌ `5.4.2.6.unit_offset_invalid`: Invalid file passed validation


##### 5.4.2.7

❌ `5.4.2.7.unit_offset_and_exponent`: Invalid file passed validation

❌ `5.4.2.7.unit_offset_and_siblings_1`: Invalid file passed validation

❌ `5.4.2.7.unit_offset_and_siblings_2`: Invalid file passed validation

`5.4.2.7.unit_offset_non_zero_and_exponent_one`: Valid file passed OK

`5.4.2.7.unit_offset_zero_and_exponent`: Valid file passed OK

`5.4.2.7.unit_offset_zero_and_siblings`: Valid file passed OK


### 5.5.2

`5.5.2.boolean_arithmetic_divide`: Valid file passed OK

`5.5.2.boolean_arithmetic_minus`: Valid file passed OK

`5.5.2.boolean_arithmetic_plus`: Valid file passed OK

`5.5.2.boolean_arithmetic_power_1`: Valid file passed OK

`5.5.2.boolean_arithmetic_power_2`: Valid file passed OK

`5.5.2.boolean_arithmetic_root_1`: Valid file passed OK

`5.5.2.boolean_arithmetic_root_2`: Valid file passed OK

`5.5.2.boolean_arithmetic_times`: Valid file passed OK

`5.5.2.boolean_compare_eq_operand_error`: Valid file passed OK

`5.5.2.boolean_compare_geq_operand_error`: Valid file passed OK

`5.5.2.boolean_compare_gt_operand_error`: Valid file passed OK

`5.5.2.boolean_compare_leq_operand_error`: Valid file passed OK

`5.5.2.boolean_compare_lt_operand_error`: Valid file passed OK

`5.5.2.boolean_compare_neq_operand_error`: Valid file passed OK

`5.5.2.boolean_derivatives_1`: Valid file passed OK

`5.5.2.boolean_derivatives_2`: Valid file passed OK

`5.5.2.boolean_function_abs`: Valid file passed OK

`5.5.2.boolean_function_ceiling`: Valid file passed OK

`5.5.2.boolean_function_exp`: Valid file passed OK

`5.5.2.boolean_function_factorial`: Valid file passed OK

`5.5.2.boolean_function_floor`: Valid file passed OK

`5.5.2.boolean_function_ln`: Valid file passed OK

`5.5.2.boolean_function_log_1`: Valid file passed OK

`5.5.2.boolean_function_log_2`: Valid file passed OK

`5.5.2.boolean_logic_and_operand_error`: Valid file passed OK

`5.5.2.boolean_logic_not_operand_error`: Valid file passed OK

`5.5.2.boolean_logic_or_operand_error`: Valid file passed OK

`5.5.2.boolean_logic_xor_operand_error`: Valid file passed OK

`5.5.2.boolean_trig_arccos`: Valid file passed OK

`5.5.2.boolean_trig_arccosh`: Valid file passed OK

`5.5.2.boolean_trig_arccot`: Valid file passed OK

`5.5.2.boolean_trig_arccoth`: Valid file passed OK

`5.5.2.boolean_trig_arccsc`: Valid file passed OK

`5.5.2.boolean_trig_arccsch`: Valid file passed OK

`5.5.2.boolean_trig_arcsec`: Valid file passed OK

`5.5.2.boolean_trig_arcsech`: Valid file passed OK

`5.5.2.boolean_trig_arcsin`: Valid file passed OK

`5.5.2.boolean_trig_arcsinh`: Valid file passed OK

`5.5.2.boolean_trig_arctan`: Valid file passed OK

`5.5.2.boolean_trig_arctanh`: Valid file passed OK

`5.5.2.boolean_trig_cos`: Valid file passed OK

`5.5.2.boolean_trig_cosh`: Valid file passed OK

`5.5.2.boolean_trig_cot`: Valid file passed OK

`5.5.2.boolean_trig_coth`: Valid file passed OK

`5.5.2.boolean_trig_csc`: Valid file passed OK

`5.5.2.boolean_trig_csch`: Valid file passed OK

`5.5.2.boolean_trig_sec`: Valid file passed OK

`5.5.2.boolean_trig_sech`: Valid file passed OK

`5.5.2.boolean_trig_sin`: Valid file passed OK

`5.5.2.boolean_trig_sinh`: Valid file passed OK

`5.5.2.boolean_trig_tan`: Valid file passed OK

`5.5.2.boolean_trig_tanh`: Valid file passed OK

`5.5.2.boolean_variable_1`: Valid file passed OK

`5.5.2.boolean_variable_2`: Valid file passed OK

`5.5.2.boolean_variable_3`: Valid file passed OK


## 6.4.1.1

❌ `6.4.1.1.group_component_ref_missing_1`: Invalid file passed validation

`6.4.1.1.group_component_ref_missing_2`: Error in invalid file detected

`6.4.1.1.group_component_ref_multiple`: Valid file passed OK

`6.4.1.1.group_component_ref_single`: Valid file passed OK

`6.4.1.1.group_empty`: Error in invalid file detected

`6.4.1.1.group_only_extensions`: Error in invalid file detected

❌ `6.4.1.1.group_relationship_ref_missing_1`: Invalid file passed validation

`6.4.1.1.group_relationship_ref_missing_2`: Error in invalid file detected

`6.4.1.1.group_with_component`: Error in invalid file detected

`6.4.1.1.group_with_connection`: Error in invalid file detected

`6.4.1.1.group_with_group`: Error in invalid file detected

`6.4.1.1.group_with_map_components`: Error in invalid file detected

`6.4.1.1.group_with_map_variables`: Error in invalid file detected

`6.4.1.1.group_with_math`: Error in invalid file detected

`6.4.1.1.group_with_model`: Error in invalid file detected

`6.4.1.1.group_with_reaction`: Error in invalid file detected

`6.4.1.1.group_with_role`: Error in invalid file detected

`6.4.1.1.group_with_unit`: Error in invalid file detected

`6.4.1.1.group_with_units`: Error in invalid file detected

`6.4.1.1.group_with_variable`: Error in invalid file detected

`6.4.1.1.group_with_variable_ref`: Error in invalid file detected

`6.4.1.group_child_order_1`: Valid file passed OK

`6.4.1.group_child_order_2`: Valid file passed OK


#### 6.4.2.1

❌ `6.4.2.1.relationship_ref_name`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:family of element model

`6.4.2.1.relationship_ref_relationship_1`: Valid file passed OK

❌ `6.4.2.1.relationship_ref_relationship_2`: Valid file failed validation
* Returned: 
  * Error on line 6: No declaration for attribute xmlns:family of element model
  * Error on line 10: No declaration for attribute relationship of element relationship_ref

`6.4.2.1.relationship_ref_relationship_missing`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_component`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_component_ref`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_connection`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_group`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_map_components`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_map_variables`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_math`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_model`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_reaction`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_relationship_ref`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_role`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_unit`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_units`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_variable`: Error in invalid file detected

`6.4.2.1.relationship_ref_with_variable_ref`: Error in invalid file detected


##### 6.4.2.2

❌ `6.4.2.2.relationship_ref_relationship_invalid`: Invalid file passed validation


##### 6.4.2.3

❌ `6.4.2.3.relationship_ref_name_invalid`: Invalid file passed validation

❌ `6.4.2.3.relationship_ref_name_not_unique_model_wide`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:family of element model


##### 6.4.2.4

❌ `6.4.2.4.relationship_ref_encapsulation_duplicate`: Invalid file passed validation

❌ `6.4.2.4.relationship_ref_encapsulation_named`: Invalid file passed validation


##### 6.4.2.5

❌ `6.4.2.5.relationship_ref_duplicate_named`: Invalid file passed validation

❌ `6.4.2.5.relationship_ref_duplicate_unnamed_1`: Invalid file passed validation

❌ `6.4.2.5.relationship_ref_duplicate_unnamed_2`: Invalid file passed validation

❌ `6.4.2.5.relationship_ref_multiple_1`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model

❌ `6.4.2.5.relationship_ref_multiple_2`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model

❌ `6.4.2.5.relationship_ref_multiple_3`: Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model


#### 6.4.3.1

`6.4.3.1.component_ref_component_missing`: Error in invalid file detected

`6.4.3.1.component_ref_nesting`: Valid file passed OK

`6.4.3.1.component_ref_with_component`: Error in invalid file detected

`6.4.3.1.component_ref_with_connection`: Error in invalid file detected

`6.4.3.1.component_ref_with_group`: Error in invalid file detected

`6.4.3.1.component_ref_with_map_components`: Error in invalid file detected

`6.4.3.1.component_ref_with_map_variables`: Error in invalid file detected

`6.4.3.1.component_ref_with_math`: Error in invalid file detected

`6.4.3.1.component_ref_with_model`: Error in invalid file detected

`6.4.3.1.component_ref_with_reaction`: Error in invalid file detected

`6.4.3.1.component_ref_with_relationship_ref`: Error in invalid file detected

`6.4.3.1.component_ref_with_role`: Error in invalid file detected

`6.4.3.1.component_ref_with_unit`: Error in invalid file detected

`6.4.3.1.component_ref_with_units`: Error in invalid file detected

`6.4.3.1.component_ref_with_variable`: Error in invalid file detected

`6.4.3.1.component_ref_with_variable_ref`: Error in invalid file detected


##### 6.4.3.2

❌ `6.4.3.2.component_ref_children_declared_twice_1`: Invalid file passed validation

❌ `6.4.3.2.component_ref_children_declared_twice_2`: Invalid file passed validation

❌ `6.4.3.2.component_ref_children_declared_twice_3`: Invalid file passed validation

❌ `6.4.3.2.component_ref_cycle_1`: Invalid file passed validation

❌ `6.4.3.2.component_ref_cycle_2`: Invalid file passed validation

❌ `6.4.3.2.component_ref_cycle_3`: Invalid file passed validation

❌ `6.4.3.2.component_ref_cycle_4`: Invalid file passed validation

❌ `6.4.3.2.component_ref_duplicate_child_1`: Invalid file passed validation

❌ `6.4.3.2.component_ref_duplicate_child_2`: Invalid file passed validation

❌ `6.4.3.2.component_ref_no_children_containment`: Invalid file passed validation

❌ `6.4.3.2.component_ref_no_children_encapsulation`: Invalid file passed validation

❌ `6.4.3.2.component_ref_no_children_extension`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:fruit of element model
  * Error on line 11: No declaration for attribute relationship of element relationship_ref

`6.4.3.2.component_ref_overlapping_containment`: Valid file passed OK

❌ `6.4.3.2.component_ref_overlapping_encapsulation`: Invalid file passed validation

`6.4.3.2.component_ref_split_named`: Valid file passed OK

`6.4.3.2.component_ref_split_unnamed_1`: Valid file passed OK

`6.4.3.2.component_ref_split_unnamed_2`: Valid file passed OK


##### 6.4.3.3

❌ `6.4.3.3.component_ref_component_invalid`: Invalid file passed validation

❌ `6.4.3.3.component_ref_component_nonexistent_1`: Invalid file passed validation

❌ `6.4.3.3.component_ref_component_nonexistent_2`: Invalid file passed validation


## 7.4.1.1

`7.4.1.1.reaction_variable_ref_missing`: Error in invalid file detected

`7.4.1.1.reaction_with_component`: Error in invalid file detected

`7.4.1.1.reaction_with_component_ref`: Error in invalid file detected

`7.4.1.1.reaction_with_connection`: Error in invalid file detected

`7.4.1.1.reaction_with_group`: Error in invalid file detected

`7.4.1.1.reaction_with_map_components`: Error in invalid file detected

`7.4.1.1.reaction_with_map_variables`: Error in invalid file detected

`7.4.1.1.reaction_with_math`: Error in invalid file detected

`7.4.1.1.reaction_with_model`: Error in invalid file detected

`7.4.1.1.reaction_with_reaction`: Error in invalid file detected

`7.4.1.1.reaction_with_relationship_ref`: Error in invalid file detected

`7.4.1.1.reaction_with_role`: Error in invalid file detected

`7.4.1.1.reaction_with_unit`: Error in invalid file detected

`7.4.1.1.reaction_with_units`: Error in invalid file detected

`7.4.1.1.reaction_with_variable`: Error in invalid file detected


##### 7.4.1.2

`7.4.1.2.reaction_reversible_invalid`: Error in invalid file detected

`7.4.1.2.reaction_reversible_no`: Valid file passed OK

`7.4.1.2.reaction_reversible_yes`: Valid file passed OK


##### 7.4.1.3

❌ `7.4.1.3.reaction_encapsulating_delta_variable`: Invalid file passed validation


#### 7.4.2.1

`7.4.2.1.variable_ref_role_missing`: Error in invalid file detected

`7.4.2.1.variable_ref_variable_missing`: Error in invalid file detected

`7.4.2.1.variable_ref_with_component`: Error in invalid file detected

`7.4.2.1.variable_ref_with_component_ref`: Error in invalid file detected

`7.4.2.1.variable_ref_with_connection`: Error in invalid file detected

`7.4.2.1.variable_ref_with_group`: Error in invalid file detected

`7.4.2.1.variable_ref_with_map_components`: Error in invalid file detected

`7.4.2.1.variable_ref_with_map_variables`: Error in invalid file detected

`7.4.2.1.variable_ref_with_math`: Error in invalid file detected

`7.4.2.1.variable_ref_with_model`: Error in invalid file detected

`7.4.2.1.variable_ref_with_reaction`: Error in invalid file detected

`7.4.2.1.variable_ref_with_relationship_ref`: Error in invalid file detected

`7.4.2.1.variable_ref_with_unit`: Error in invalid file detected

`7.4.2.1.variable_ref_with_units`: Error in invalid file detected

`7.4.2.1.variable_ref_with_variable`: Error in invalid file detected

`7.4.2.1.variable_ref_with_variable_ref`: Error in invalid file detected


##### 7.4.2.2

❌ `7.4.2.2.variable_ref_variable_duplicate`: Invalid file passed validation

❌ `7.4.2.2.variable_ref_variable_hidden`: Invalid file passed validation

❌ `7.4.2.2.variable_ref_variable_nonexistent`: Invalid file passed validation


#### 7.4.3.1

`7.4.3.1.role_role_missing`: Error in invalid file detected

`7.4.3.1.role_with_component`: Error in invalid file detected

`7.4.3.1.role_with_component_ref`: Error in invalid file detected

`7.4.3.1.role_with_connection`: Error in invalid file detected

`7.4.3.1.role_with_group`: Error in invalid file detected

`7.4.3.1.role_with_map_components`: Error in invalid file detected

`7.4.3.1.role_with_map_variables`: Error in invalid file detected

`7.4.3.1.role_with_model`: Error in invalid file detected

`7.4.3.1.role_with_reaction`: Error in invalid file detected

`7.4.3.1.role_with_relationship_ref`: Error in invalid file detected

`7.4.3.1.role_with_role`: Error in invalid file detected

`7.4.3.1.role_with_unit`: Error in invalid file detected

`7.4.3.1.role_with_units`: Error in invalid file detected

`7.4.3.1.role_with_variable`: Error in invalid file detected

`7.4.3.1.role_with_variable_ref`: Error in invalid file detected


##### 7.4.3.2

`7.4.3.2.role_role_invalid`: Error in invalid file detected


##### 7.4.3.3

❌ `7.4.3.3.reaction_multiple_rates`: Invalid file passed validation

❌ `7.4.3.3.role_rate_with_delta_variable`: Invalid file passed validation

❌ `7.4.3.3.role_rate_with_multiple_roles`: Invalid file passed validation

❌ `7.4.3.3.role_rate_with_stoichiometry`: Invalid file passed validation


##### 7.4.3.4

`7.4.3.4.role_direction_invalid`: Error in invalid file detected


##### 7.4.3.5

❌ `7.4.3.5.role_direction_both_irreversible`: Invalid file passed validation

❌ `7.4.3.5.role_direction_both_product`: Invalid file passed validation

❌ `7.4.3.5.role_direction_both_rate`: Invalid file passed validation

❌ `7.4.3.5.role_direction_both_reactant`: Invalid file passed validation

❌ `7.4.3.5.role_direction_reverse_irreversible`: Invalid file passed validation

❌ `7.4.3.5.role_direction_reverse_product`: Invalid file passed validation

❌ `7.4.3.5.role_direction_reverse_rate`: Invalid file passed validation

❌ `7.4.3.5.role_direction_reverse_reactant`: Invalid file passed validation

❌ `7.4.3.5.role_direction_role_duplicate`: Invalid file passed validation


##### 7.4.3.6

❌ `7.4.3.6.role_stoichiometry_invalid`: Invalid file passed validation


##### 7.4.3.7

❌ `7.4.3.7.role_delta_variable_duplicate_1`: Invalid file passed validation

❌ `7.4.3.7.role_delta_variable_duplicate_2`: Invalid file passed validation

❌ `7.4.3.7.role_delta_variable_nonexistent_1`: Invalid file passed validation

❌ `7.4.3.7.role_delta_variable_nonexistent_2`: Invalid file passed validation


##### 7.4.3.8

❌ `7.4.3.8.role_delta_variable_activator`: Invalid file passed validation

❌ `7.4.3.8.role_delta_variable_catalyst`: Invalid file passed validation

❌ `7.4.3.8.role_delta_variable_inhibitor`: Invalid file passed validation

❌ `7.4.3.8.role_delta_variable_modifier`: Invalid file passed validation

❌ `7.4.3.8.role_delta_variable_with_rate_and_math`: Invalid file passed validation

❌ `7.4.3.8.role_delta_variable_with_stoichiometry_no_rate`: Invalid file passed validation

❌ `7.4.3.8.role_delta_variable_without_rate_or_math`: Invalid file passed validation


##### 7.4.3.9

❌ `7.4.3.9.role_math_not_relevant`: Invalid file passed validation

`7.4.3.reaction_all_roles_and_attributes`: Valid file passed OK

`7.4.3.reaction_reversible_no`: Valid file passed OK

`7.4.3.reaction_simple`: Valid file passed OK


## 8.4.1

`8.4.1.cmeta_id_duplicate`: Error in invalid file detected

`8.4.1.cmeta_id_in_component`: Valid file passed OK

`8.4.1.cmeta_id_in_component_ref`: Valid file passed OK

`8.4.1.cmeta_id_in_connection`: Valid file passed OK

`8.4.1.cmeta_id_in_group`: Valid file passed OK

`8.4.1.cmeta_id_in_map_components`: Valid file passed OK

`8.4.1.cmeta_id_in_map_variables`: Valid file passed OK

`8.4.1.cmeta_id_in_model`: Valid file passed OK

`8.4.1.cmeta_id_in_reaction`: Valid file passed OK

`8.4.1.cmeta_id_in_relationship_ref`: Valid file passed OK

`8.4.1.cmeta_id_in_role`: Valid file passed OK

`8.4.1.cmeta_id_in_unit`: Valid file passed OK

`8.4.1.cmeta_id_in_units_1`: Valid file passed OK

`8.4.1.cmeta_id_in_units_2`: Valid file passed OK

`8.4.1.cmeta_id_in_variable`: Valid file passed OK

`8.4.1.cmeta_id_in_variable_ref`: Valid file passed OK


#### 8.4.2

❌ `8.4.2.rdf_in_component`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 8: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (rdf:RDF )
  * Error on line 9: No declaration for element RDF
  * Error on line 9: No declaration for attribute about of element RDF
  * Error on line 10: No declaration for element description

❌ `8.4.2.rdf_in_component_ref`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 13: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (rdf:RDF )
  * Error on line 14: No declaration for element RDF
  * Error on line 14: No declaration for attribute about of element RDF
  * Error on line 15: No declaration for element description

❌ `8.4.2.rdf_in_connection`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 14: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables rdf:RDF )
  * Error on line 17: No declaration for element RDF
  * Error on line 17: No declaration for attribute about of element RDF
  * Error on line 18: No declaration for element description

❌ `8.4.2.rdf_in_group`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 10: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref rdf:RDF )
  * Error on line 15: No declaration for element RDF
  * Error on line 15: No declaration for attribute about of element RDF
  * Error on line 16: No declaration for element description

❌ `8.4.2.rdf_in_map_components`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 9: Element map_components was declared EMPTY this one has content
  * Error on line 10: No declaration for element RDF
  * Error on line 10: No declaration for attribute about of element RDF
  * Error on line 11: No declaration for element description

❌ `8.4.2.rdf_in_map_variables`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 16: Element map_variables was declared EMPTY this one has content
  * Error on line 17: No declaration for element RDF
  * Error on line 17: No declaration for attribute about of element RDF
  * Error on line 18: No declaration for element description

❌ `8.4.2.rdf_in_model`: Valid file failed validation
* Returned: 
  * Error on line 8: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (rdf:RDF )
  * Error on line 8: No declaration for attribute xmlns:rdf of element model
  * Error on line 8: No declaration for attribute xmlns:dc of element model
  * Error on line 9: No declaration for element RDF
  * Error on line 9: No declaration for attribute about of element RDF
  * Error on line 10: No declaration for element description

❌ `8.4.2.rdf_in_reaction`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 10: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref rdf:RDF )
  * Error on line 14: No declaration for element RDF
  * Error on line 14: No declaration for attribute about of element RDF
  * Error on line 15: No declaration for element description

❌ `8.4.2.rdf_in_relationship_ref`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 11: Element relationship_ref was declared EMPTY this one has content
  * Error on line 12: No declaration for element RDF
  * Error on line 12: No declaration for attribute about of element RDF
  * Error on line 13: No declaration for element description

❌ `8.4.2.rdf_in_role`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 12: Element role content does not follow the DTD, expecting (math)?, got (rdf:RDF )
  * Error on line 13: No declaration for element RDF
  * Error on line 13: No declaration for attribute about of element RDF
  * Error on line 14: No declaration for element description

❌ `8.4.2.rdf_in_unit`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 9: Element unit was declared EMPTY this one has content
  * Error on line 10: No declaration for element RDF
  * Error on line 10: No declaration for attribute about of element RDF
  * Error on line 11: No declaration for element description

❌ `8.4.2.rdf_in_units_1`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 8: Element units content does not follow the DTD, expecting (unit)*, got (unit rdf:RDF )
  * Error on line 10: No declaration for element RDF
  * Error on line 10: No declaration for attribute about of element RDF
  * Error on line 11: No declaration for element description

❌ `8.4.2.rdf_in_units_2`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 9: Element units content does not follow the DTD, expecting (unit)*, got (unit rdf:RDF )
  * Error on line 11: No declaration for element RDF
  * Error on line 11: No declaration for attribute about of element RDF
  * Error on line 12: No declaration for element description

❌ `8.4.2.rdf_in_variable`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 9: Element variable was declared EMPTY this one has content
  * Error on line 10: No declaration for element RDF
  * Error on line 10: No declaration for attribute about of element RDF
  * Error on line 11: No declaration for element description

❌ `8.4.2.rdf_in_variable_ref`: Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 11: Element variable_ref content does not follow the DTD, expecting (role)+, got (rdf:RDF role )
  * Error on line 12: No declaration for element RDF
  * Error on line 12: No declaration for attribute about of element RDF
  * Error on line 13: No declaration for element description

`C.3.3.unit_checking_arithmetic_minus_operand_error_1`: Valid file passed OK

`C.3.3.unit_checking_arithmetic_minus_operand_error_2`: Valid file passed OK

`C.3.3.unit_checking_arithmetic_minus_operand_error_3`: Valid file passed OK

`C.3.3.unit_checking_arithmetic_plus_operand_error_1`: Valid file passed OK

`C.3.3.unit_checking_arithmetic_plus_operand_error_2`: Valid file passed OK

`C.3.3.unit_checking_arithmetic_plus_operand_error_3`: Valid file passed OK

`C.3.3.unit_checking_arithmetic_plus_operand_error_4`: Valid file passed OK

`C.3.3.unit_checking_arithmetic_power_operand_error`: Valid file passed OK

`C.3.3.unit_checking_arithmetic_root_operand_error`: Valid file passed OK

`C.3.3.unit_checking_compare_eq_operand_mismatch`: Valid file passed OK

`C.3.3.unit_checking_compare_geq_operand_mismatch`: Valid file passed OK

`C.3.3.unit_checking_compare_gt_operand_mismatch`: Valid file passed OK

`C.3.3.unit_checking_compare_leq_operand_mismatch`: Valid file passed OK

`C.3.3.unit_checking_compare_lt_operand_mismatch`: Valid file passed OK

`C.3.3.unit_checking_compare_neq_operand_mismatch`: Valid file passed OK

`C.3.3.unit_checking_derivative_operand_error`: Valid file passed OK

`C.3.3.unit_checking_function_exp_operand_error`: Valid file passed OK

`C.3.3.unit_checking_function_factorial_operand_error`: Valid file passed OK

`C.3.3.unit_checking_function_ln_operand_error`: Valid file passed OK

`C.3.3.unit_checking_function_log_operand_error_1`: Valid file passed OK

`C.3.3.unit_checking_function_log_operand_error_2`: Valid file passed OK

`C.3.3.unit_checking_trig_arccos_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_arccosh_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_arccot_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_arccoth_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_arccsc_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_arccsch_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_arcsec_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_arcsech_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_arcsin_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_arcsinh_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_arctan_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_arctanh_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_cos_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_cosh_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_cot_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_coth_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_csc_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_csch_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_sec_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_sech_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_sin_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_sinh_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_tan_operand_error`: Valid file passed OK

`C.3.3.unit_checking_trig_tanh_operand_error`: Valid file passed OK

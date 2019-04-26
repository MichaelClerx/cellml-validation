# DTD Validation - CellML 1.0

Performance:
* 69% according to spec (533 out of 763)
* 280 out of 316 valid files passed
* 253 out of 447 invalid files detected

Issues:
* 36 valid files failed to parse
* 194 invalid files passed validation
* 0 invalid files failed validation for the wrong reason

## 0.0

[0.0.root_namespace_1](../models_1_0/valid/0.0.root_namespace_1.cellml): Valid file passed OK

[0.0.root_namespace_2](../models_1_0/valid/0.0.root_namespace_2.cellml): Valid file passed OK

❌ [0.0.root_node_namespace_wrong](../models_1_0/invalid/0.0.root_node_namespace_wrong.cellml): Invalid file passed validation

❌ [0.0.root_node_not_model](../models_1_0/invalid/0.0.root_node_not_model.cellml): Invalid file passed validation

[0.0.root_node_two_elements](../models_1_0/invalid/0.0.root_node_two_elements.cellml): Error in invalid file detected

[0.0.root_node_two_models](../models_1_0/invalid/0.0.root_node_two_models.cellml): Error in invalid file detected


### 0.1

❌ [0.1.real_number_invalid_1](../models_1_0/invalid/0.1.real_number_invalid_1.cellml): Invalid file passed validation

❌ [0.1.real_number_invalid_2](../models_1_0/invalid/0.1.real_number_invalid_2.cellml): Invalid file passed validation

❌ [0.1.real_number_invalid_3](../models_1_0/invalid/0.1.real_number_invalid_3.cellml): Invalid file passed validation

❌ [0.1.real_number_invalid_4](../models_1_0/invalid/0.1.real_number_invalid_4.cellml): Invalid file passed validation

❌ [0.1.real_number_invalid_5](../models_1_0/invalid/0.1.real_number_invalid_5.cellml): Invalid file passed validation

❌ [0.1.real_number_invalid_6](../models_1_0/invalid/0.1.real_number_invalid_6.cellml): Invalid file passed validation

[0.1.real_numbers](../models_1_0/valid/0.1.real_numbers.cellml): Valid file passed OK

[0.1.real_numbers_extreme](../models_1_0/valid/0.1.real_numbers_extreme.cellml): Valid file passed OK


### 0.2

[0.2.component_name_same_as_model](../models_1_0/valid/0.2.component_name_same_as_model.cellml): Valid file passed OK

[0.2.variable_name_same_as_model](../models_1_0/valid/0.2.variable_name_same_as_model.cellml): Valid file passed OK


## 2.4.1

❌ [2.4.1.identifier_empty](../models_1_0/invalid/2.4.1.identifier_empty.cellml): Invalid file passed validation

❌ [2.4.1.identifier_only_underscore](../models_1_0/invalid/2.4.1.identifier_only_underscore.cellml): Invalid file passed validation

❌ [2.4.1.identifier_unexpected_character_1](../models_1_0/invalid/2.4.1.identifier_unexpected_character_1.cellml): Invalid file passed validation

❌ [2.4.1.identifier_unexpected_character_2](../models_1_0/invalid/2.4.1.identifier_unexpected_character_2.cellml): Invalid file passed validation

❌ [2.4.1.identifier_unexpected_character_unicode](../models_1_0/invalid/2.4.1.identifier_unexpected_character_unicode.cellml): Invalid file passed validation

[2.4.1.valid_identifiers](../models_1_0/valid/2.4.1.valid_identifiers.cellml): Valid file passed OK


#### 2.4.2

[2.4.2.imaginary_attributes_1](../models_1_0/invalid/2.4.2.imaginary_attributes_1.cellml): Error in invalid file detected

[2.4.2.imaginary_attributes_2](../models_1_0/invalid/2.4.2.imaginary_attributes_2.cellml): Error in invalid file detected

[2.4.2.imaginary_elements](../models_1_0/invalid/2.4.2.imaginary_elements.cellml): Error in invalid file detected


#### 2.4.3

[2.4.3.cellml_attributes_inside_extensions](../models_1_0/invalid/2.4.3.cellml_attributes_inside_extensions.cellml): Error in invalid file detected

[2.4.3.cellml_elements_inside_extensions](../models_1_0/invalid/2.4.3.cellml_elements_inside_extensions.cellml): Error in invalid file detected

❌ [2.4.3.component_ref_with_extensions](../models_1_0/valid/2.4.3.component_ref_with_extensions.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 11: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (fruit:orange fruit:pear )
  * Error on line 11: No declaration for attribute banana of element component_ref
  * Error on line 12: No declaration for element orange
  * Error on line 12: No declaration for attribute peel of element orange
  * Error on line 13: No declaration for element clementine
  * Error on line 15: No declaration for element pear

❌ [2.4.3.component_with_extensions](../models_1_0/valid/2.4.3.component_with_extensions.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 6: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (fruit:orange fruit:pear )
  * Error on line 6: No declaration for attribute banana of element component
  * Error on line 7: No declaration for element orange
  * Error on line 7: No declaration for attribute peel of element orange
  * Error on line 8: No declaration for element clementine
  * Error on line 10: No declaration for element pear

❌ [2.4.3.connection_with_extensions](../models_1_0/valid/2.4.3.connection_with_extensions.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 6: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (fruit:orange fruit:pear map_components map_variables )
  * Error on line 6: No declaration for attribute x_a_day of element connection
  * Error on line 7: No declaration for element orange
  * Error on line 7: No declaration for attribute peel of element orange
  * Error on line 8: No declaration for element clementine
  * Error on line 10: No declaration for element pear

❌ [2.4.3.group_with_extensions](../models_1_0/valid/2.4.3.group_with_extensions.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 8: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (fruit:orange fruit:pear relationship_ref component_ref )
  * Error on line 8: No declaration for attribute banana of element group
  * Error on line 9: No declaration for element orange
  * Error on line 9: No declaration for attribute peel of element orange
  * Error on line 10: No declaration for element clementine
  * Error on line 12: No declaration for element pear

❌ [2.4.3.map_components_with_extensions](../models_1_0/valid/2.4.3.map_components_with_extensions.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 7: Element map_components was declared EMPTY this one has content
  * Error on line 7: No declaration for attribute x_a_day of element map_components
  * Error on line 8: No declaration for element orange
  * Error on line 8: No declaration for attribute peel of element orange
  * Error on line 9: No declaration for element clementine
  * Error on line 11: No declaration for element pear

❌ [2.4.3.map_variables_with_extensions](../models_1_0/valid/2.4.3.map_variables_with_extensions.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 8: Element map_variables was declared EMPTY this one has content
  * Error on line 8: No declaration for attribute x_a_day of element map_variables
  * Error on line 9: No declaration for element orange
  * Error on line 9: No declaration for attribute peel of element orange
  * Error on line 10: No declaration for element clementine
  * Error on line 12: No declaration for element pear

❌ [2.4.3.model_with_extensions](../models_1_0/valid/2.4.3.model_with_extensions.cellml): Valid file failed validation
* Returned: 
  * Error on line 6: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (fruit:orange fruit:pear )
  * Error on line 6: No declaration for attribute x_a_day of element model
  * Error on line 6: No declaration for attribute xmlns:fruit of element model
  * Error on line 7: No declaration for element orange
  * Error on line 7: No declaration for attribute peel of element orange
  * Error on line 8: No declaration for element clementine
  * Error on line 10: No declaration for element pear

❌ [2.4.3.reaction_with_extensions](../models_1_0/valid/2.4.3.reaction_with_extensions.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (fruit:orange fruit:pear variable_ref )
  * Error on line 8: No declaration for attribute x_a_day of element reaction
  * Error on line 9: No declaration for element orange
  * Error on line 9: No declaration for attribute peel of element orange
  * Error on line 10: No declaration for element clementine
  * Error on line 12: No declaration for element pear

❌ [2.4.3.relationship_ref_with_extensions](../models_1_0/valid/2.4.3.relationship_ref_with_extensions.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 9: Element relationship_ref was declared EMPTY this one has content
  * Error on line 9: No declaration for attribute banana of element relationship_ref
  * Error on line 10: No declaration for element orange
  * Error on line 10: No declaration for attribute peel of element orange
  * Error on line 11: No declaration for element clementine
  * Error on line 13: No declaration for element pear

❌ [2.4.3.role_with_extensions](../models_1_0/valid/2.4.3.role_with_extensions.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (fruit:orange fruit:pear )
  * Error on line 10: No declaration for attribute x_a_day of element role
  * Error on line 11: No declaration for element orange
  * Error on line 11: No declaration for attribute peel of element orange
  * Error on line 12: No declaration for element clementine
  * Error on line 14: No declaration for element pear

❌ [2.4.3.unit_with_extensions](../models_1_0/valid/2.4.3.unit_with_extensions.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 7: Element unit was declared EMPTY this one has content
  * Error on line 7: No declaration for attribute x_a_day of element unit
  * Error on line 8: No declaration for element orange
  * Error on line 8: No declaration for attribute peel of element orange
  * Error on line 9: No declaration for element clementine
  * Error on line 11: No declaration for element pear

❌ [2.4.3.units_with_extensions](../models_1_0/valid/2.4.3.units_with_extensions.cellml): Valid file failed validation
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

❌ [2.4.3.variable_ref_with_extensions](../models_1_0/valid/2.4.3.variable_ref_with_extensions.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (fruit:orange fruit:pear role )
  * Error on line 9: No declaration for attribute x_a_day of element variable_ref
  * Error on line 10: No declaration for element orange
  * Error on line 10: No declaration for attribute peel of element orange
  * Error on line 11: No declaration for element clementine
  * Error on line 13: No declaration for element pear

❌ [2.4.3.variable_with_extensions](../models_1_0/valid/2.4.3.variable_with_extensions.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model
  * Error on line 7: Element variable was declared EMPTY this one has content
  * Error on line 7: No declaration for attribute x_a_day of element variable
  * Error on line 8: No declaration for element orange
  * Error on line 8: No declaration for attribute peel of element orange
  * Error on line 9: No declaration for element clementine
  * Error on line 11: No declaration for element pear


#### 2.4.4

[2.4.4.model_linux_line_breaks](../models_1_0/valid/2.4.4.model_linux_line_breaks.cellml): Valid file passed OK

[2.4.4.model_windows_line_breaks](../models_1_0/valid/2.4.4.model_windows_line_breaks.cellml): Valid file passed OK

[2.4.4.model_with_spaces](../models_1_0/valid/2.4.4.model_with_spaces.cellml): Valid file passed OK

[2.4.4.model_with_tabs](../models_1_0/valid/2.4.4.model_with_tabs.cellml): Valid file passed OK

[2.4.4.text_in_component](../models_1_0/invalid/2.4.4.text_in_component.cellml): Error in invalid file detected

[2.4.4.text_in_component_ref](../models_1_0/invalid/2.4.4.text_in_component_ref.cellml): Error in invalid file detected

[2.4.4.text_in_connection](../models_1_0/invalid/2.4.4.text_in_connection.cellml): Error in invalid file detected

[2.4.4.text_in_group](../models_1_0/invalid/2.4.4.text_in_group.cellml): Error in invalid file detected

[2.4.4.text_in_map_components](../models_1_0/invalid/2.4.4.text_in_map_components.cellml): Error in invalid file detected

[2.4.4.text_in_map_variables](../models_1_0/invalid/2.4.4.text_in_map_variables.cellml): Error in invalid file detected

[2.4.4.text_in_model](../models_1_0/invalid/2.4.4.text_in_model.cellml): Error in invalid file detected

[2.4.4.text_in_reaction](../models_1_0/invalid/2.4.4.text_in_reaction.cellml): Error in invalid file detected

[2.4.4.text_in_relationship_ref](../models_1_0/invalid/2.4.4.text_in_relationship_ref.cellml): Error in invalid file detected

[2.4.4.text_in_role](../models_1_0/invalid/2.4.4.text_in_role.cellml): Error in invalid file detected

[2.4.4.text_in_unit](../models_1_0/invalid/2.4.4.text_in_unit.cellml): Error in invalid file detected

[2.4.4.text_in_units_1](../models_1_0/invalid/2.4.4.text_in_units_1.cellml): Error in invalid file detected

[2.4.4.text_in_units_2](../models_1_0/invalid/2.4.4.text_in_units_2.cellml): Error in invalid file detected

[2.4.4.text_in_variable](../models_1_0/invalid/2.4.4.text_in_variable.cellml): Error in invalid file detected

[2.4.4.text_in_variable_ref](../models_1_0/invalid/2.4.4.text_in_variable_ref.cellml): Error in invalid file detected


### 2.5.1

❌ [2.5.1.identifiers_are_case_sensitive](../models_1_0/invalid/2.5.1.identifiers_are_case_sensitive.cellml): Invalid file passed validation


#### 2.5.2

[2.5.2.attribute_in_cellml_namespace](../models_1_0/invalid/2.5.2.attribute_in_cellml_namespace.cellml): Error in invalid file detected


## 3.4.1.1

[3.4.1.1.model_child_order_1](../models_1_0/valid/3.4.1.1.model_child_order_1.cellml): Valid file passed OK

[3.4.1.1.model_child_order_2](../models_1_0/valid/3.4.1.1.model_child_order_2.cellml): Valid file passed OK

[3.4.1.1.model_empty](../models_1_0/valid/3.4.1.1.model_empty.cellml): Valid file passed OK

[3.4.1.1.model_name_missing](../models_1_0/invalid/3.4.1.1.model_name_missing.cellml): Error in invalid file detected

[3.4.1.1.model_with_component_ref](../models_1_0/invalid/3.4.1.1.model_with_component_ref.cellml): Error in invalid file detected

[3.4.1.1.model_with_components](../models_1_0/valid/3.4.1.1.model_with_components.cellml): Valid file passed OK

[3.4.1.1.model_with_connections](../models_1_0/valid/3.4.1.1.model_with_connections.cellml): Valid file passed OK

[3.4.1.1.model_with_groups](../models_1_0/valid/3.4.1.1.model_with_groups.cellml): Valid file passed OK

[3.4.1.1.model_with_map_components](../models_1_0/invalid/3.4.1.1.model_with_map_components.cellml): Error in invalid file detected

[3.4.1.1.model_with_map_variables](../models_1_0/invalid/3.4.1.1.model_with_map_variables.cellml): Error in invalid file detected

[3.4.1.1.model_with_math](../models_1_0/invalid/3.4.1.1.model_with_math.cellml): Error in invalid file detected

[3.4.1.1.model_with_model](../models_1_0/invalid/3.4.1.1.model_with_model.cellml): Error in invalid file detected

[3.4.1.1.model_with_one_component](../models_1_0/valid/3.4.1.1.model_with_one_component.cellml): Valid file passed OK

[3.4.1.1.model_with_one_connection](../models_1_0/valid/3.4.1.1.model_with_one_connection.cellml): Valid file passed OK

[3.4.1.1.model_with_one_group](../models_1_0/valid/3.4.1.1.model_with_one_group.cellml): Valid file passed OK

[3.4.1.1.model_with_one_units](../models_1_0/valid/3.4.1.1.model_with_one_units.cellml): Valid file passed OK

[3.4.1.1.model_with_reaction](../models_1_0/invalid/3.4.1.1.model_with_reaction.cellml): Error in invalid file detected

[3.4.1.1.model_with_relationship_ref](../models_1_0/invalid/3.4.1.1.model_with_relationship_ref.cellml): Error in invalid file detected

[3.4.1.1.model_with_role](../models_1_0/invalid/3.4.1.1.model_with_role.cellml): Error in invalid file detected

[3.4.1.1.model_with_unit](../models_1_0/invalid/3.4.1.1.model_with_unit.cellml): Error in invalid file detected

[3.4.1.1.model_with_units](../models_1_0/valid/3.4.1.1.model_with_units.cellml): Valid file passed OK

[3.4.1.1.model_with_variable](../models_1_0/invalid/3.4.1.1.model_with_variable.cellml): Error in invalid file detected

[3.4.1.1.model_with_variable_ref](../models_1_0/invalid/3.4.1.1.model_with_variable_ref.cellml): Error in invalid file detected


##### 3.4.1.2

❌ [3.4.1.2.model_name_invalid](../models_1_0/invalid/3.4.1.2.model_name_invalid.cellml): Invalid file passed validation


#### 3.4.2.1

[3.4.2.1.component_child_order_1](../models_1_0/valid/3.4.2.1.component_child_order_1.cellml): Valid file passed OK

[3.4.2.1.component_child_order_2](../models_1_0/valid/3.4.2.1.component_child_order_2.cellml): Valid file passed OK

[3.4.2.1.component_empty](../models_1_0/valid/3.4.2.1.component_empty.cellml): Valid file passed OK

[3.4.2.1.component_name_missing](../models_1_0/invalid/3.4.2.1.component_name_missing.cellml): Error in invalid file detected

[3.4.2.1.component_with_component](../models_1_0/invalid/3.4.2.1.component_with_component.cellml): Error in invalid file detected

[3.4.2.1.component_with_component_ref](../models_1_0/invalid/3.4.2.1.component_with_component_ref.cellml): Error in invalid file detected

[3.4.2.1.component_with_connection](../models_1_0/invalid/3.4.2.1.component_with_connection.cellml): Error in invalid file detected

[3.4.2.1.component_with_group](../models_1_0/invalid/3.4.2.1.component_with_group.cellml): Error in invalid file detected

[3.4.2.1.component_with_map_components](../models_1_0/invalid/3.4.2.1.component_with_map_components.cellml): Error in invalid file detected

[3.4.2.1.component_with_map_variables](../models_1_0/invalid/3.4.2.1.component_with_map_variables.cellml): Error in invalid file detected

[3.4.2.1.component_with_maths](../models_1_0/valid/3.4.2.1.component_with_maths.cellml): Valid file passed OK

[3.4.2.1.component_with_model](../models_1_0/invalid/3.4.2.1.component_with_model.cellml): Error in invalid file detected

[3.4.2.1.component_with_one_math](../models_1_0/valid/3.4.2.1.component_with_one_math.cellml): Valid file passed OK

[3.4.2.1.component_with_one_reaction](../models_1_0/valid/3.4.2.1.component_with_one_reaction.cellml): Valid file passed OK

[3.4.2.1.component_with_one_units](../models_1_0/valid/3.4.2.1.component_with_one_units.cellml): Valid file passed OK

[3.4.2.1.component_with_one_variable](../models_1_0/valid/3.4.2.1.component_with_one_variable.cellml): Valid file passed OK

[3.4.2.1.component_with_reactions](../models_1_0/valid/3.4.2.1.component_with_reactions.cellml): Valid file passed OK

[3.4.2.1.component_with_relationship_ref](../models_1_0/invalid/3.4.2.1.component_with_relationship_ref.cellml): Error in invalid file detected

[3.4.2.1.component_with_role](../models_1_0/invalid/3.4.2.1.component_with_role.cellml): Error in invalid file detected

[3.4.2.1.component_with_unit](../models_1_0/invalid/3.4.2.1.component_with_unit.cellml): Error in invalid file detected

[3.4.2.1.component_with_units](../models_1_0/valid/3.4.2.1.component_with_units.cellml): Valid file passed OK

[3.4.2.1.component_with_variable_ref](../models_1_0/invalid/3.4.2.1.component_with_variable_ref.cellml): Error in invalid file detected

[3.4.2.1.component_with_variables](../models_1_0/valid/3.4.2.1.component_with_variables.cellml): Valid file passed OK


##### 3.4.2.2

❌ [3.4.2.2.component_name_duplicate](../models_1_0/invalid/3.4.2.2.component_name_duplicate.cellml): Invalid file passed validation

❌ [3.4.2.2.component_name_invalid](../models_1_0/invalid/3.4.2.2.component_name_invalid.cellml): Invalid file passed validation


#### 3.4.3.1

[3.4.3.1.variable_name_missing](../models_1_0/invalid/3.4.3.1.variable_name_missing.cellml): Error in invalid file detected

[3.4.3.1.variable_units_missing](../models_1_0/invalid/3.4.3.1.variable_units_missing.cellml): Error in invalid file detected

[3.4.3.1.variable_with_component](../models_1_0/invalid/3.4.3.1.variable_with_component.cellml): Error in invalid file detected

[3.4.3.1.variable_with_component_ref](../models_1_0/invalid/3.4.3.1.variable_with_component_ref.cellml): Error in invalid file detected

[3.4.3.1.variable_with_connection](../models_1_0/invalid/3.4.3.1.variable_with_connection.cellml): Error in invalid file detected

[3.4.3.1.variable_with_group](../models_1_0/invalid/3.4.3.1.variable_with_group.cellml): Error in invalid file detected

[3.4.3.1.variable_with_initial_value](../models_1_0/valid/3.4.3.1.variable_with_initial_value.cellml): Valid file passed OK

[3.4.3.1.variable_with_interfaces](../models_1_0/valid/3.4.3.1.variable_with_interfaces.cellml): Valid file passed OK

[3.4.3.1.variable_with_map_components](../models_1_0/invalid/3.4.3.1.variable_with_map_components.cellml): Error in invalid file detected

[3.4.3.1.variable_with_map_variables](../models_1_0/invalid/3.4.3.1.variable_with_map_variables.cellml): Error in invalid file detected

[3.4.3.1.variable_with_math](../models_1_0/invalid/3.4.3.1.variable_with_math.cellml): Error in invalid file detected

[3.4.3.1.variable_with_model](../models_1_0/invalid/3.4.3.1.variable_with_model.cellml): Error in invalid file detected

[3.4.3.1.variable_with_reaction](../models_1_0/invalid/3.4.3.1.variable_with_reaction.cellml): Error in invalid file detected

[3.4.3.1.variable_with_relationship_ref](../models_1_0/invalid/3.4.3.1.variable_with_relationship_ref.cellml): Error in invalid file detected

[3.4.3.1.variable_with_role](../models_1_0/invalid/3.4.3.1.variable_with_role.cellml): Error in invalid file detected

[3.4.3.1.variable_with_unit](../models_1_0/invalid/3.4.3.1.variable_with_unit.cellml): Error in invalid file detected

[3.4.3.1.variable_with_units](../models_1_0/invalid/3.4.3.1.variable_with_units.cellml): Error in invalid file detected

[3.4.3.1.variable_with_variable](../models_1_0/invalid/3.4.3.1.variable_with_variable.cellml): Error in invalid file detected

[3.4.3.1.variable_with_variable_ref](../models_1_0/invalid/3.4.3.1.variable_with_variable_ref.cellml): Error in invalid file detected

[3.4.3.1.variable_without_initial_value](../models_1_0/valid/3.4.3.1.variable_without_initial_value.cellml): Valid file passed OK


##### 3.4.3.2

❌ [3.4.3.2.variable_name_duplicate](../models_1_0/invalid/3.4.3.2.variable_name_duplicate.cellml): Invalid file passed validation

❌ [3.4.3.2.variable_name_invalid](../models_1_0/invalid/3.4.3.2.variable_name_invalid.cellml): Invalid file passed validation

[3.4.3.2.variable_name_same_as_cousin](../models_1_0/valid/3.4.3.2.variable_name_same_as_cousin.cellml): Valid file passed OK

[3.4.3.2.variable_name_same_as_parent](../models_1_0/valid/3.4.3.2.variable_name_same_as_parent.cellml): Valid file passed OK


##### 3.4.3.3

[3.4.3.3.variable_units_component](../models_1_0/valid/3.4.3.3.variable_units_component.cellml): Valid file passed OK

[3.4.3.3.variable_units_model](../models_1_0/valid/3.4.3.3.variable_units_model.cellml): Valid file passed OK

❌ [3.4.3.3.variable_units_other_component](../models_1_0/invalid/3.4.3.3.variable_units_other_component.cellml): Invalid file passed validation

[3.4.3.3.variable_units_predefined](../models_1_0/valid/3.4.3.3.variable_units_predefined.cellml): Valid file passed OK

❌ [3.4.3.3.variable_units_unknown](../models_1_0/invalid/3.4.3.3.variable_units_unknown.cellml): Invalid file passed validation


##### 3.4.3.4

[3.4.3.4.variable_interface_public_invalid](../models_1_0/invalid/3.4.3.4.variable_interface_public_invalid.cellml): Error in invalid file detected


##### 3.4.3.5

[3.4.3.5.variable_interface_private_invalid](../models_1_0/invalid/3.4.3.5.variable_interface_private_invalid.cellml): Error in invalid file detected


##### 3.4.3.6

❌ [3.4.3.6.variable_interfaces_both_in](../models_1_0/invalid/3.4.3.6.variable_interfaces_both_in.cellml): Invalid file passed validation


##### 3.4.3.7

❌ [3.4.3.7.variable_initial_value_empty](../models_1_0/invalid/3.4.3.7.variable_initial_value_empty.cellml): Invalid file passed validation

❌ [3.4.3.7.variable_initial_value_invalid](../models_1_0/invalid/3.4.3.7.variable_initial_value_invalid.cellml): Invalid file passed validation


##### 3.4.3.8

❌ [3.4.3.8.variable_interfaces_private_in_and_initial](../models_1_0/invalid/3.4.3.8.variable_interfaces_private_in_and_initial.cellml): Invalid file passed validation

❌ [3.4.3.8.variable_interfaces_public_in_and_initial](../models_1_0/invalid/3.4.3.8.variable_interfaces_public_in_and_initial.cellml): Invalid file passed validation


#### 3.4.4.1

[3.4.4.1.connection_empty](../models_1_0/invalid/3.4.4.1.connection_empty.cellml): Error in invalid file detected

[3.4.4.1.connection_map_components_missing](../models_1_0/invalid/3.4.4.1.connection_map_components_missing.cellml): Error in invalid file detected

[3.4.4.1.connection_map_components_multiple](../models_1_0/invalid/3.4.4.1.connection_map_components_multiple.cellml): Error in invalid file detected

[3.4.4.1.connection_map_variables_missing_1](../models_1_0/invalid/3.4.4.1.connection_map_variables_missing_1.cellml): Error in invalid file detected

[3.4.4.1.connection_map_variables_missing_2](../models_1_0/invalid/3.4.4.1.connection_map_variables_missing_2.cellml): Error in invalid file detected

[3.4.4.1.connection_only_extensions](../models_1_0/invalid/3.4.4.1.connection_only_extensions.cellml): Error in invalid file detected

[3.4.4.1.connection_with_component](../models_1_0/invalid/3.4.4.1.connection_with_component.cellml): Error in invalid file detected

[3.4.4.1.connection_with_component_ref](../models_1_0/invalid/3.4.4.1.connection_with_component_ref.cellml): Error in invalid file detected

[3.4.4.1.connection_with_connection](../models_1_0/invalid/3.4.4.1.connection_with_connection.cellml): Error in invalid file detected

[3.4.4.1.connection_with_group](../models_1_0/invalid/3.4.4.1.connection_with_group.cellml): Error in invalid file detected

[3.4.4.1.connection_with_map_variables](../models_1_0/valid/3.4.4.1.connection_with_map_variables.cellml): Valid file passed OK

[3.4.4.1.connection_with_math](../models_1_0/invalid/3.4.4.1.connection_with_math.cellml): Error in invalid file detected

[3.4.4.1.connection_with_model](../models_1_0/invalid/3.4.4.1.connection_with_model.cellml): Error in invalid file detected

[3.4.4.1.connection_with_name_attribute](../models_1_0/invalid/3.4.4.1.connection_with_name_attribute.cellml): Error in invalid file detected

[3.4.4.1.connection_with_one_map_variables](../models_1_0/valid/3.4.4.1.connection_with_one_map_variables.cellml): Valid file passed OK

[3.4.4.1.connection_with_reaction](../models_1_0/invalid/3.4.4.1.connection_with_reaction.cellml): Error in invalid file detected

[3.4.4.1.connection_with_relationship_ref](../models_1_0/invalid/3.4.4.1.connection_with_relationship_ref.cellml): Error in invalid file detected

[3.4.4.1.connection_with_role](../models_1_0/invalid/3.4.4.1.connection_with_role.cellml): Error in invalid file detected

[3.4.4.1.connection_with_unit](../models_1_0/invalid/3.4.4.1.connection_with_unit.cellml): Error in invalid file detected

[3.4.4.1.connection_with_units](../models_1_0/invalid/3.4.4.1.connection_with_units.cellml): Error in invalid file detected

[3.4.4.1.connection_with_variable](../models_1_0/invalid/3.4.4.1.connection_with_variable.cellml): Error in invalid file detected

[3.4.4.1.connection_with_variable_ref](../models_1_0/invalid/3.4.4.1.connection_with_variable_ref.cellml): Error in invalid file detected


#### 3.4.5.1

[3.4.5.1.connection_any_order_1](../models_1_0/valid/3.4.5.1.connection_any_order_1.cellml): Valid file passed OK

[3.4.5.1.connection_any_order_2](../models_1_0/valid/3.4.5.1.connection_any_order_2.cellml): Valid file passed OK

[3.4.5.1.map_components_component_1_missing](../models_1_0/invalid/3.4.5.1.map_components_component_1_missing.cellml): Error in invalid file detected

[3.4.5.1.map_components_component_2_missing](../models_1_0/invalid/3.4.5.1.map_components_component_2_missing.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_component](../models_1_0/invalid/3.4.5.1.map_components_with_component.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_component_ref](../models_1_0/invalid/3.4.5.1.map_components_with_component_ref.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_connection](../models_1_0/invalid/3.4.5.1.map_components_with_connection.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_group](../models_1_0/invalid/3.4.5.1.map_components_with_group.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_map_components](../models_1_0/invalid/3.4.5.1.map_components_with_map_components.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_map_variables](../models_1_0/invalid/3.4.5.1.map_components_with_map_variables.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_math](../models_1_0/invalid/3.4.5.1.map_components_with_math.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_model](../models_1_0/invalid/3.4.5.1.map_components_with_model.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_reaction](../models_1_0/invalid/3.4.5.1.map_components_with_reaction.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_relationship_ref](../models_1_0/invalid/3.4.5.1.map_components_with_relationship_ref.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_role](../models_1_0/invalid/3.4.5.1.map_components_with_role.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_unit](../models_1_0/invalid/3.4.5.1.map_components_with_unit.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_units](../models_1_0/invalid/3.4.5.1.map_components_with_units.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_variable](../models_1_0/invalid/3.4.5.1.map_components_with_variable.cellml): Error in invalid file detected

[3.4.5.1.map_components_with_variable_ref](../models_1_0/invalid/3.4.5.1.map_components_with_variable_ref.cellml): Error in invalid file detected


##### 3.4.5.2

❌ [3.4.5.2.map_components_component_1_nonexistent](../models_1_0/invalid/3.4.5.2.map_components_component_1_nonexistent.cellml): Invalid file passed validation


##### 3.4.5.3

❌ [3.4.5.3.map_components_component_2_nonexistent](../models_1_0/invalid/3.4.5.3.map_components_component_2_nonexistent.cellml): Invalid file passed validation


##### 3.4.5.4

❌ [3.4.5.4.map_components_component_1_equals_2](../models_1_0/invalid/3.4.5.4.map_components_component_1_equals_2.cellml): Invalid file passed validation

❌ [3.4.5.4.map_components_duplicate](../models_1_0/invalid/3.4.5.4.map_components_duplicate.cellml): Invalid file passed validation

❌ [3.4.5.4.map_components_duplicate_mirrored](../models_1_0/invalid/3.4.5.4.map_components_duplicate_mirrored.cellml): Invalid file passed validation


#### 3.4.6.1

[3.4.6.1.map_variables_variable_1_missing](../models_1_0/invalid/3.4.6.1.map_variables_variable_1_missing.cellml): Error in invalid file detected

[3.4.6.1.map_variables_variable_2_missing](../models_1_0/invalid/3.4.6.1.map_variables_variable_2_missing.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_component](../models_1_0/invalid/3.4.6.1.map_variables_with_component.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_component_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_component_ref.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_connection](../models_1_0/invalid/3.4.6.1.map_variables_with_connection.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_group](../models_1_0/invalid/3.4.6.1.map_variables_with_group.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_map_components](../models_1_0/invalid/3.4.6.1.map_variables_with_map_components.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_map_variables](../models_1_0/invalid/3.4.6.1.map_variables_with_map_variables.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_math](../models_1_0/invalid/3.4.6.1.map_variables_with_math.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_model](../models_1_0/invalid/3.4.6.1.map_variables_with_model.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_reaction](../models_1_0/invalid/3.4.6.1.map_variables_with_reaction.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_relationship_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_relationship_ref.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_role](../models_1_0/invalid/3.4.6.1.map_variables_with_role.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_unit](../models_1_0/invalid/3.4.6.1.map_variables_with_unit.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_units](../models_1_0/invalid/3.4.6.1.map_variables_with_units.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_variable](../models_1_0/invalid/3.4.6.1.map_variables_with_variable.cellml): Error in invalid file detected

[3.4.6.1.map_variables_with_variable_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_variable_ref.cellml): Error in invalid file detected


##### 3.4.6.2

❌ [3.4.6.2.map_variables_variable_1_nonexistent](../models_1_0/invalid/3.4.6.2.map_variables_variable_1_nonexistent.cellml): Invalid file passed validation


##### 3.4.6.3

❌ [3.4.6.3.map_variables_variable_2_nonexistent](../models_1_0/invalid/3.4.6.3.map_variables_variable_2_nonexistent.cellml): Invalid file passed validation


##### 3.4.6.4

[3.4.6.4.map_variables_chain_down](../models_1_0/valid/3.4.6.4.map_variables_chain_down.cellml): Valid file passed OK

[3.4.6.4.map_variables_chain_up](../models_1_0/valid/3.4.6.4.map_variables_chain_up.cellml): Valid file passed OK

❌ [3.4.6.4.map_variables_child_multiple_out_1](../models_1_0/invalid/3.4.6.4.map_variables_child_multiple_out_1.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_child_multiple_out_2](../models_1_0/invalid/3.4.6.4.map_variables_child_multiple_out_2.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_child_out_to_out_1](../models_1_0/invalid/3.4.6.4.map_variables_child_out_to_out_1.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_child_out_to_out_2](../models_1_0/invalid/3.4.6.4.map_variables_child_out_to_out_2.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_child_private_in](../models_1_0/invalid/3.4.6.4.map_variables_child_private_in.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_child_private_out](../models_1_0/invalid/3.4.6.4.map_variables_child_private_out.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_hidden_aunt_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_aunt_1.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_hidden_aunt_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_aunt_2.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_hidden_cousins_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_1.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_hidden_cousins_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_2.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_hidden_cousins_3](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_3.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_hidden_cousins_4](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_4.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_hidden_grandchild_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandchild_1.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_hidden_grandchild_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandchild_2.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_hidden_grandparent_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandparent_1.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_hidden_grandparent_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandparent_2.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_hidden_niece_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_niece_1.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_hidden_niece_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_niece_2.cellml): Invalid file passed validation

[3.4.6.4.map_variables_nested_sibling_connection](../models_1_0/valid/3.4.6.4.map_variables_nested_sibling_connection.cellml): Valid file passed OK

❌ [3.4.6.4.map_variables_nested_sibling_private_in](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_in.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_nested_sibling_private_in_and_out](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_in_and_out.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_nested_sibling_private_out](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_out.cellml): Invalid file passed validation

[3.4.6.4.map_variables_parent_connection_1](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_1.cellml): Valid file passed OK

[3.4.6.4.map_variables_parent_connection_2](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_2.cellml): Valid file passed OK

❌ [3.4.6.4.map_variables_parent_in_to_in_1](../models_1_0/invalid/3.4.6.4.map_variables_parent_in_to_in_1.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_parent_in_to_in_2](../models_1_0/invalid/3.4.6.4.map_variables_parent_in_to_in_2.cellml): Invalid file passed validation

[3.4.6.4.map_variables_parent_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_1.cellml): Valid file passed OK

[3.4.6.4.map_variables_parent_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_2.cellml): Valid file passed OK

❌ [3.4.6.4.map_variables_parent_multiple_out](../models_1_0/invalid/3.4.6.4.map_variables_parent_multiple_out.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_parent_out_to_out_1](../models_1_0/invalid/3.4.6.4.map_variables_parent_out_to_out_1.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_parent_out_to_out_2](../models_1_0/invalid/3.4.6.4.map_variables_parent_out_to_out_2.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_parent_public_in](../models_1_0/invalid/3.4.6.4.map_variables_parent_public_in.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_parent_public_out](../models_1_0/invalid/3.4.6.4.map_variables_parent_public_out.cellml): Invalid file passed validation

[3.4.6.4.map_variables_sibling_connection_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_1.cellml): Valid file passed OK

[3.4.6.4.map_variables_sibling_connection_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_2.cellml): Valid file passed OK

[3.4.6.4.map_variables_sibling_connection_3](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_3.cellml): Valid file passed OK

❌ [3.4.6.4.map_variables_sibling_in_to_in](../models_1_0/invalid/3.4.6.4.map_variables_sibling_in_to_in.cellml): Invalid file passed validation

[3.4.6.4.map_variables_sibling_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_1.cellml): Valid file passed OK

[3.4.6.4.map_variables_sibling_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_2.cellml): Valid file passed OK

❌ [3.4.6.4.map_variables_sibling_multiple_out_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_multiple_out_1.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_sibling_multiple_out_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_multiple_out_2.cellml): Invalid file passed validation

[3.4.6.4.map_variables_sibling_mutual](../models_1_0/valid/3.4.6.4.map_variables_sibling_mutual.cellml): Valid file passed OK

❌ [3.4.6.4.map_variables_sibling_out_to_out](../models_1_0/invalid/3.4.6.4.map_variables_sibling_out_to_out.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_sibling_private_in_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_1.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_sibling_private_in_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_2.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_sibling_private_in_and_out](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_and_out.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_sibling_private_out_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_out_1.cellml): Invalid file passed validation

❌ [3.4.6.4.map_variables_sibling_private_out_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_out_2.cellml): Invalid file passed validation

[3.4.6.4.map_variables_talking_aunt](../models_1_0/valid/3.4.6.4.map_variables_talking_aunt.cellml): Valid file passed OK

[3.4.6.4.map_variables_talking_cousins](../models_1_0/valid/3.4.6.4.map_variables_talking_cousins.cellml): Valid file passed OK

[3.4.6.4.map_variables_talking_niece](../models_1_0/valid/3.4.6.4.map_variables_talking_niece.cellml): Valid file passed OK


## 4.2

[4.2.3_1.mathml_basics](../models_1_0/valid/4.2.3_1.mathml_basics.cellml): Valid file passed OK

[4.2.3_2.1.mathml_numbers_real](../models_1_0/numbers/4.2.3_2.1.mathml_numbers_real.cellml): Valid file passed OK

[4.2.3_2.2.mathml_numbers_integer](../models_1_0/numbers/4.2.3_2.2.mathml_numbers_integer.cellml): Valid file passed OK

[4.2.3_2.3.mathml_numbers_real_base](../models_1_0/numbers/4.2.3_2.3.mathml_numbers_real_base.cellml): Valid file passed OK

[4.2.3_2.4.mathml_numbers_integer_base](../models_1_0/numbers/4.2.3_2.4.mathml_numbers_integer_base.cellml): Valid file passed OK

[4.2.3_2.5.mathml_numbers_e_notation](../models_1_0/numbers/4.2.3_2.5.mathml_numbers_e_notation.cellml): Valid file passed OK

[4.2.3_2.6.mathml_numbers_rational](../models_1_0/numbers/4.2.3_2.6.mathml_numbers_rational.cellml): Valid file passed OK

[4.2.3_3.1_mathml_arithmetic_binary](../models_1_0/valid/4.2.3_3.1_mathml_arithmetic_binary.cellml): Valid file passed OK

[4.2.3_3.2_mathml_arithmetic_n_ary](../models_1_0/valid/4.2.3_3.2_mathml_arithmetic_n_ary.cellml): Valid file passed OK

[4.2.3_3.2_mathml_arithmetic_unary](../models_1_0/valid/4.2.3_3.2_mathml_arithmetic_unary.cellml): Valid file passed OK

[4.2.3_4.1_mathml_functions_basic](../models_1_0/valid/4.2.3_4.1_mathml_functions_basic.cellml): Valid file passed OK

[4.2.3_4.2_mathml_functions_non_smooth](../models_1_0/valid/4.2.3_4.2_mathml_functions_non_smooth.cellml): Valid file passed OK

[4.2.3_4.3_mathml_functions_factorial](../models_1_0/valid/4.2.3_4.3_mathml_functions_factorial.cellml): Valid file passed OK

[4.2.3_4.4_mathml_functions_trig](../models_1_0/valid/4.2.3_4.4_mathml_functions_trig.cellml): Valid file passed OK

[4.2.3_4.5_mathml_functions_trig_hyperbolic](../models_1_0/valid/4.2.3_4.5_mathml_functions_trig_hyperbolic.cellml): Valid file passed OK

[4.2.3_4.6_mathml_functions_trig_redundant](../models_1_0/valid/4.2.3_4.6_mathml_functions_trig_redundant.cellml): Valid file passed OK

[4.2.3_4.7_mathml_functions_trig_redundant_hyperbolic](../models_1_0/valid/4.2.3_4.7_mathml_functions_trig_redundant_hyperbolic.cellml): Valid file passed OK

[4.2.3_5.1_mathml_derivatives](../models_1_0/valid/4.2.3_5.1_mathml_derivatives.cellml): Valid file passed OK

[4.2.3_5.2_mathml_derivatives_degree](../models_1_0/valid/4.2.3_5.2_mathml_derivatives_degree.cellml): Valid file passed OK

[4.2.3_5.3_mathml_derivatives_with_units](../models_1_0/valid/4.2.3_5.3_mathml_derivatives_with_units.cellml): Valid file passed OK

[4.2.3_5.4_mathml_derivatives_with_units_degree](../models_1_0/valid/4.2.3_5.4_mathml_derivatives_with_units_degree.cellml): Valid file passed OK

[4.2.3_6.1_mathml_logic_one_piece](../models_1_0/valid/4.2.3_6.1_mathml_logic_one_piece.cellml): Valid file passed OK

[4.2.3_6.2_mathml_logic_two_pieces](../models_1_0/valid/4.2.3_6.2_mathml_logic_two_pieces.cellml): Valid file passed OK

[4.2.3_6.3_mathml_logic_no_otherwise](../models_1_0/valid/4.2.3_6.3_mathml_logic_no_otherwise.cellml): Valid file passed OK

[4.2.3_6.4_mathml_logic_comparisons](../models_1_0/valid/4.2.3_6.4_mathml_logic_comparisons.cellml): Valid file passed OK

[4.2.3_6.5_mathml_logic_unary_operators](../models_1_0/valid/4.2.3_6.5_mathml_logic_unary_operators.cellml): Valid file passed OK

[4.2.3_6.6_mathml_logic_binary_operators](../models_1_0/valid/4.2.3_6.6_mathml_logic_binary_operators.cellml): Valid file passed OK

[4.2.3_6.7_mathml_logic_constants](../models_1_0/valid/4.2.3_6.7_mathml_logic_constants.cellml): Valid file passed OK

[4.2.3_7.1_mathml_pi](../models_1_0/valid/4.2.3_7.1_mathml_pi.cellml): Valid file passed OK

[4.2.3_7.2_mathml_e](../models_1_0/valid/4.2.3_7.2_mathml_e.cellml): Valid file passed OK

[4.2.3_7.3_mathml_nan_inf](../models_1_0/valid/4.2.3_7.3_mathml_nan_inf.cellml): Valid file passed OK

[4.2.3_8.1_annotation](../models_1_0/valid/4.2.3_8.1_annotation.cellml): Valid file passed OK

[4.2.3_8.2_annotation_xml](../models_1_0/valid/4.2.3_8.2_annotation_xml.cellml): Valid file passed OK


### 4.4.1

[4.4.1.math_not_math_component](../models_1_0/invalid/4.4.1.math_not_math_component.cellml): Error in invalid file detected

[4.4.1.math_not_math_reaction](../models_1_0/invalid/4.4.1.math_not_math_reaction.cellml): Error in invalid file detected


#### 4.4.2

[4.4.2.ci_no_whitespace](../models_1_0/valid/4.4.2.ci_no_whitespace.cellml): Valid file passed OK

❌ [4.4.2.ci_non_local_aunt](../models_1_0/invalid/4.4.2.ci_non_local_aunt.cellml): Invalid file passed validation

❌ [4.4.2.ci_non_local_child](../models_1_0/invalid/4.4.2.ci_non_local_child.cellml): Invalid file passed validation

❌ [4.4.2.ci_non_local_cousin](../models_1_0/invalid/4.4.2.ci_non_local_cousin.cellml): Invalid file passed validation

❌ [4.4.2.ci_non_local_nested_sibling](../models_1_0/invalid/4.4.2.ci_non_local_nested_sibling.cellml): Invalid file passed validation

❌ [4.4.2.ci_non_local_niece](../models_1_0/invalid/4.4.2.ci_non_local_niece.cellml): Invalid file passed validation

❌ [4.4.2.ci_non_local_parent](../models_1_0/invalid/4.4.2.ci_non_local_parent.cellml): Invalid file passed validation

❌ [4.4.2.ci_non_local_sibling](../models_1_0/invalid/4.4.2.ci_non_local_sibling.cellml): Invalid file passed validation

❌ [4.4.2.ci_nonexistent](../models_1_0/invalid/4.4.2.ci_nonexistent.cellml): Invalid file passed validation

[4.4.2.ci_whitespace_1](../models_1_0/valid/4.4.2.ci_whitespace_1.cellml): Valid file passed OK

[4.4.2.ci_whitespace_2](../models_1_0/valid/4.4.2.ci_whitespace_2.cellml): Valid file passed OK

[4.4.2.ci_whitespace_3](../models_1_0/valid/4.4.2.ci_whitespace_3.cellml): Valid file passed OK


#### 4.4.3.1

[4.4.3.1.cn_component_units](../models_1_0/valid/4.4.3.1.cn_component_units.cellml): Valid file passed OK

[4.4.3.1.cn_model_units](../models_1_0/valid/4.4.3.1.cn_model_units.cellml): Valid file passed OK

[4.4.3.1.cn_predefined_units](../models_1_0/valid/4.4.3.1.cn_predefined_units.cellml): Valid file passed OK

[4.4.3.1.cn_units_missing](../models_1_0/invalid/4.4.3.1.cn_units_missing.cellml): Error in invalid file detected


##### 4.4.3.2

❌ [4.4.3.2.cn_units_nonexistent_1](../models_1_0/invalid/4.4.3.2.cn_units_nonexistent_1.cellml): Invalid file passed validation

❌ [4.4.3.2.cn_units_nonexistent_2](../models_1_0/invalid/4.4.3.2.cn_units_nonexistent_2.cellml): Invalid file passed validation

❌ [4.4.3.2.cn_units_parent_component](../models_1_0/invalid/4.4.3.2.cn_units_parent_component.cellml): Invalid file passed validation


#### 4.4.4

❌ [4.4.4.modify_nonexistent](../models_1_0/invalid/4.4.4.modify_nonexistent.cellml): Invalid file passed validation

❌ [4.4.4.modify_private_in](../models_1_0/invalid/4.4.4.modify_private_in.cellml): Invalid file passed validation

[4.4.4.modify_private_out](../models_1_0/valid/4.4.4.modify_private_out.cellml): Valid file passed OK

❌ [4.4.4.modify_public_in](../models_1_0/invalid/4.4.4.modify_public_in.cellml): Invalid file passed validation

[4.4.4.modify_public_out](../models_1_0/valid/4.4.4.modify_public_out.cellml): Valid file passed OK


### 4.5.1

[4.5.1.ordering_not_significant](../models_1_0/valid/4.5.1.ordering_not_significant.cellml): Valid file passed OK

[4.algebraic_model](../models_1_0/valid/4.algebraic_model.cellml): Valid file passed OK

[4.algebraic_ode_model](../models_1_0/valid/4.algebraic_ode_model.cellml): Valid file passed OK

❌ [4.math_and_initial_value](../models_1_0/invalid/4.math_and_initial_value.cellml): Invalid file passed validation

❌ [4.math_overdefined](../models_1_0/invalid/4.math_overdefined.cellml): Invalid file passed validation


## 5.2.2

❌ [5.2.2.unit_deca](../models_1_0/unit_deca/5.2.2.unit_deca.cellml): Invalid file passed validation


#### 5.2.7

[5.2.7.unit_checking_arithmetic](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_arithmetic.cellml): Valid file passed OK

[5.2.7.unit_checking_comparisons](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_comparisons.cellml): Valid file passed OK

[5.2.7.unit_checking_derivatives](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_derivatives.cellml): Valid file passed OK

[5.2.7.unit_checking_derivatives_degree](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_derivatives_degree.cellml): Valid file passed OK

[5.2.7.unit_checking_dimensionless](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_dimensionless.cellml): Valid file passed OK

[5.2.7.unit_checking_functions_factorial](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_functions_factorial.cellml): Valid file passed OK

[5.2.7.unit_checking_functions_non_smooth](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_functions_non_smooth.cellml): Valid file passed OK

[5.2.7.unit_checking_functions_power_and_root](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_functions_power_and_root.cellml): Valid file passed OK

[5.2.7.unit_checking_internal_mismatch_1](../models_1_0/unit_checking_inconsistent/5.2.7.unit_checking_internal_mismatch_1.cellml): Valid file passed OK

[5.2.7.unit_checking_internal_mismatch_2](../models_1_0/unit_checking_inconsistent/5.2.7.unit_checking_internal_mismatch_2.cellml): Valid file passed OK

[5.2.7.unit_checking_internal_mismatch_3](../models_1_0/unit_checking_inconsistent/5.2.7.unit_checking_internal_mismatch_3.cellml): Valid file passed OK

[5.2.7.unit_checking_internal_mismatch_4](../models_1_0/unit_checking_inconsistent/5.2.7.unit_checking_internal_mismatch_4.cellml): Valid file passed OK

[5.2.7.unit_checking_name_differs](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_name_differs.cellml): Valid file passed OK

[5.2.7.unit_checking_piecewise](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_piecewise.cellml): Valid file passed OK

[5.2.7.unit_checking_piecewise_multi_unit](../models_1_0/unit_checking_inconsistent/5.2.7.unit_checking_piecewise_multi_unit.cellml): Valid file passed OK

[5.2.7.unit_checking_repeated_unit](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_repeated_unit.cellml): Valid file passed OK

[5.2.7.unit_conversion_different_names_same_unit](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_different_names_same_unit.cellml): Valid file passed OK

[5.2.7.unit_conversion_dimensionless_exponent](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_dimensionless_exponent.cellml): Valid file passed OK

[5.2.7.unit_conversion_dimensionless_multiplier_1](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_dimensionless_multiplier_1.cellml): Valid file passed OK

[5.2.7.unit_conversion_dimensionless_multiplier_2](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_dimensionless_multiplier_2.cellml): Valid file passed OK

[5.2.7.unit_conversion_dimensionless_offset](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_dimensionless_offset.cellml): Valid file passed OK

[5.2.7.unit_conversion_inconvertible_1](../models_1_0/unit_conversion_inconvertible/5.2.7.unit_conversion_inconvertible_1.cellml): Valid file passed OK

[5.2.7.unit_conversion_less_obvious](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_less_obvious.cellml): Valid file passed OK

[5.2.7.unit_conversion_multiplier](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_multiplier.cellml): Valid file passed OK

[5.2.7.unit_conversion_new_base_units](../models_1_0/unit_conversion_inconvertible/5.2.7.unit_conversion_new_base_units.cellml): Valid file passed OK

[5.2.7.unit_conversion_offset](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_offset.cellml): Valid file passed OK

[5.2.7.unit_conversion_prefix](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_prefix.cellml): Valid file passed OK


### 5.4.1.1

[5.4.1.1.units_base_units](../models_1_0/valid/5.4.1.1.units_base_units.cellml): Valid file passed OK

❌ [5.4.1.1.units_base_units_with_children](../models_1_0/invalid/5.4.1.1.units_base_units_with_children.cellml): Invalid file passed validation

[5.4.1.1.units_empty_1](../models_1_0/valid/5.4.1.1.units_empty_1.cellml): Valid file passed OK

[5.4.1.1.units_empty_2](../models_1_0/valid/5.4.1.1.units_empty_2.cellml): Valid file passed OK

[5.4.1.1.units_name_missing](../models_1_0/invalid/5.4.1.1.units_name_missing.cellml): Error in invalid file detected

[5.4.1.1.units_with_component](../models_1_0/invalid/5.4.1.1.units_with_component.cellml): Error in invalid file detected

[5.4.1.1.units_with_component_ref](../models_1_0/invalid/5.4.1.1.units_with_component_ref.cellml): Error in invalid file detected

[5.4.1.1.units_with_connection](../models_1_0/invalid/5.4.1.1.units_with_connection.cellml): Error in invalid file detected

[5.4.1.1.units_with_group](../models_1_0/invalid/5.4.1.1.units_with_group.cellml): Error in invalid file detected

[5.4.1.1.units_with_map_components](../models_1_0/invalid/5.4.1.1.units_with_map_components.cellml): Error in invalid file detected

[5.4.1.1.units_with_map_variables](../models_1_0/invalid/5.4.1.1.units_with_map_variables.cellml): Error in invalid file detected

[5.4.1.1.units_with_math](../models_1_0/invalid/5.4.1.1.units_with_math.cellml): Error in invalid file detected

[5.4.1.1.units_with_model](../models_1_0/invalid/5.4.1.1.units_with_model.cellml): Error in invalid file detected

[5.4.1.1.units_with_reaction](../models_1_0/invalid/5.4.1.1.units_with_reaction.cellml): Error in invalid file detected

[5.4.1.1.units_with_relationship_ref](../models_1_0/invalid/5.4.1.1.units_with_relationship_ref.cellml): Error in invalid file detected

[5.4.1.1.units_with_role](../models_1_0/invalid/5.4.1.1.units_with_role.cellml): Error in invalid file detected

[5.4.1.1.units_with_unit_children](../models_1_0/valid/5.4.1.1.units_with_unit_children.cellml): Valid file passed OK

[5.4.1.1.units_with_units](../models_1_0/invalid/5.4.1.1.units_with_units.cellml): Error in invalid file detected

[5.4.1.1.units_with_variable](../models_1_0/invalid/5.4.1.1.units_with_variable.cellml): Error in invalid file detected

[5.4.1.1.units_with_variable_ref](../models_1_0/invalid/5.4.1.1.units_with_variable_ref.cellml): Error in invalid file detected


##### 5.4.1.2

❌ [5.4.1.2.units_name_duplicate_1](../models_1_0/invalid/5.4.1.2.units_name_duplicate_1.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_duplicate_2](../models_1_0/invalid/5.4.1.2.units_name_duplicate_2.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_invalid](../models_1_0/invalid/5.4.1.2.units_name_invalid.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_ampere](../models_1_0/invalid/5.4.1.2.units_name_predefined_ampere.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_becquerel](../models_1_0/invalid/5.4.1.2.units_name_predefined_becquerel.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_candela](../models_1_0/invalid/5.4.1.2.units_name_predefined_candela.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_celsius](../models_1_0/invalid/5.4.1.2.units_name_predefined_celsius.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_component_ampere](../models_1_0/invalid/5.4.1.2.units_name_predefined_component_ampere.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_coulomb](../models_1_0/invalid/5.4.1.2.units_name_predefined_coulomb.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_dimensionless](../models_1_0/invalid/5.4.1.2.units_name_predefined_dimensionless.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_farad](../models_1_0/invalid/5.4.1.2.units_name_predefined_farad.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_gram](../models_1_0/invalid/5.4.1.2.units_name_predefined_gram.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_gray](../models_1_0/invalid/5.4.1.2.units_name_predefined_gray.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_henry](../models_1_0/invalid/5.4.1.2.units_name_predefined_henry.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_hertz](../models_1_0/invalid/5.4.1.2.units_name_predefined_hertz.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_joule](../models_1_0/invalid/5.4.1.2.units_name_predefined_joule.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_katal](../models_1_0/invalid/5.4.1.2.units_name_predefined_katal.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_kelvin](../models_1_0/invalid/5.4.1.2.units_name_predefined_kelvin.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_kilogram](../models_1_0/invalid/5.4.1.2.units_name_predefined_kilogram.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_liter](../models_1_0/invalid/5.4.1.2.units_name_predefined_liter.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_litre](../models_1_0/invalid/5.4.1.2.units_name_predefined_litre.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_lumen](../models_1_0/invalid/5.4.1.2.units_name_predefined_lumen.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_lux](../models_1_0/invalid/5.4.1.2.units_name_predefined_lux.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_meter](../models_1_0/invalid/5.4.1.2.units_name_predefined_meter.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_metre](../models_1_0/invalid/5.4.1.2.units_name_predefined_metre.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_mole](../models_1_0/invalid/5.4.1.2.units_name_predefined_mole.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_newton](../models_1_0/invalid/5.4.1.2.units_name_predefined_newton.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_ohm](../models_1_0/invalid/5.4.1.2.units_name_predefined_ohm.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_pascal](../models_1_0/invalid/5.4.1.2.units_name_predefined_pascal.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_radian](../models_1_0/invalid/5.4.1.2.units_name_predefined_radian.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_second](../models_1_0/invalid/5.4.1.2.units_name_predefined_second.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_siemens](../models_1_0/invalid/5.4.1.2.units_name_predefined_siemens.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_sievert](../models_1_0/invalid/5.4.1.2.units_name_predefined_sievert.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_steradian](../models_1_0/invalid/5.4.1.2.units_name_predefined_steradian.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_tesla](../models_1_0/invalid/5.4.1.2.units_name_predefined_tesla.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_volt](../models_1_0/invalid/5.4.1.2.units_name_predefined_volt.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_watt](../models_1_0/invalid/5.4.1.2.units_name_predefined_watt.cellml): Invalid file passed validation

❌ [5.4.1.2.units_name_predefined_weber](../models_1_0/invalid/5.4.1.2.units_name_predefined_weber.cellml): Invalid file passed validation

[5.4.1.2.units_names_and_other_names](../models_1_0/valid/5.4.1.2.units_names_and_other_names.cellml): Valid file passed OK

[5.4.1.2.units_shadowing_1](../models_1_0/valid/5.4.1.2.units_shadowing_1.cellml): Valid file passed OK

[5.4.1.2.units_shadowing_2](../models_1_0/valid/5.4.1.2.units_shadowing_2.cellml): Valid file passed OK


##### 5.4.1.3

[5.4.1.3.units_base_units_invalid](../models_1_0/invalid/5.4.1.3.units_base_units_invalid.cellml): Error in invalid file detected


#### 5.4.2.1

[5.4.2.1.unit_offset_non_zero](../models_1_0/valid/5.4.2.1.unit_offset_non_zero.cellml): Valid file passed OK

[5.4.2.1.unit_offset_zero](../models_1_0/valid/5.4.2.1.unit_offset_zero.cellml): Valid file passed OK

[5.4.2.1.unit_prefix_exponent_multiplier](../models_1_0/valid/5.4.2.1.unit_prefix_exponent_multiplier.cellml): Valid file passed OK

[5.4.2.1.unit_units_missing](../models_1_0/invalid/5.4.2.1.unit_units_missing.cellml): Error in invalid file detected

[5.4.2.1.unit_with_component](../models_1_0/invalid/5.4.2.1.unit_with_component.cellml): Error in invalid file detected

[5.4.2.1.unit_with_component_ref](../models_1_0/invalid/5.4.2.1.unit_with_component_ref.cellml): Error in invalid file detected

[5.4.2.1.unit_with_connection](../models_1_0/invalid/5.4.2.1.unit_with_connection.cellml): Error in invalid file detected

[5.4.2.1.unit_with_group](../models_1_0/invalid/5.4.2.1.unit_with_group.cellml): Error in invalid file detected

[5.4.2.1.unit_with_map_components](../models_1_0/invalid/5.4.2.1.unit_with_map_components.cellml): Error in invalid file detected

[5.4.2.1.unit_with_map_variables](../models_1_0/invalid/5.4.2.1.unit_with_map_variables.cellml): Error in invalid file detected

[5.4.2.1.unit_with_math](../models_1_0/invalid/5.4.2.1.unit_with_math.cellml): Error in invalid file detected

[5.4.2.1.unit_with_model](../models_1_0/invalid/5.4.2.1.unit_with_model.cellml): Error in invalid file detected

[5.4.2.1.unit_with_reaction](../models_1_0/invalid/5.4.2.1.unit_with_reaction.cellml): Error in invalid file detected

[5.4.2.1.unit_with_relationship_ref](../models_1_0/invalid/5.4.2.1.unit_with_relationship_ref.cellml): Error in invalid file detected

[5.4.2.1.unit_with_role](../models_1_0/invalid/5.4.2.1.unit_with_role.cellml): Error in invalid file detected

[5.4.2.1.unit_with_unit](../models_1_0/invalid/5.4.2.1.unit_with_unit.cellml): Error in invalid file detected

[5.4.2.1.unit_with_units](../models_1_0/invalid/5.4.2.1.unit_with_units.cellml): Error in invalid file detected

[5.4.2.1.unit_with_variable](../models_1_0/invalid/5.4.2.1.unit_with_variable.cellml): Error in invalid file detected

[5.4.2.1.unit_with_variable_ref](../models_1_0/invalid/5.4.2.1.unit_with_variable_ref.cellml): Error in invalid file detected


##### 5.4.2.2

❌ [5.4.2.2.unit_cycle_1](../models_1_0/invalid/5.4.2.2.unit_cycle_1.cellml): Invalid file passed validation

❌ [5.4.2.2.unit_cycle_2](../models_1_0/invalid/5.4.2.2.unit_cycle_2.cellml): Invalid file passed validation

❌ [5.4.2.2.unit_cycle_3](../models_1_0/invalid/5.4.2.2.unit_cycle_3.cellml): Invalid file passed validation

❌ [5.4.2.2.unit_units_invalid](../models_1_0/invalid/5.4.2.2.unit_units_invalid.cellml): Invalid file passed validation

[5.4.2.2.unit_units_local_1](../models_1_0/valid/5.4.2.2.unit_units_local_1.cellml): Valid file passed OK

[5.4.2.2.unit_units_local_2](../models_1_0/valid/5.4.2.2.unit_units_local_2.cellml): Valid file passed OK


##### 5.4.2.3

[5.4.2.3.unit_prefix_integer](../models_1_0/valid/5.4.2.3.unit_prefix_integer.cellml): Valid file passed OK

[5.4.2.3.unit_prefix_named](../models_1_0/valid/5.4.2.3.unit_prefix_named.cellml): Valid file passed OK

❌ [5.4.2.3.unit_prefix_real](../models_1_0/invalid/5.4.2.3.unit_prefix_real.cellml): Invalid file passed validation

❌ [5.4.2.3.unit_prefix_real_int](../models_1_0/invalid/5.4.2.3.unit_prefix_real_int.cellml): Invalid file passed validation

❌ [5.4.2.3.unit_prefix_spaces](../models_1_0/invalid/5.4.2.3.unit_prefix_spaces.cellml): Invalid file passed validation

❌ [5.4.2.3.unit_prefix_unknown](../models_1_0/invalid/5.4.2.3.unit_prefix_unknown.cellml): Invalid file passed validation


##### 5.4.2.4

❌ [5.4.2.4.unit_exponent_invalid](../models_1_0/invalid/5.4.2.4.unit_exponent_invalid.cellml): Invalid file passed validation


##### 5.4.2.5

❌ [5.4.2.5.unit_multiplier_invalid](../models_1_0/invalid/5.4.2.5.unit_multiplier_invalid.cellml): Invalid file passed validation


##### 5.4.2.6

❌ [5.4.2.6.unit_offset_invalid](../models_1_0/invalid/5.4.2.6.unit_offset_invalid.cellml): Invalid file passed validation


##### 5.4.2.7

❌ [5.4.2.7.unit_offset_and_exponent](../models_1_0/invalid/5.4.2.7.unit_offset_and_exponent.cellml): Invalid file passed validation

❌ [5.4.2.7.unit_offset_and_siblings_1](../models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_1.cellml): Invalid file passed validation

❌ [5.4.2.7.unit_offset_and_siblings_2](../models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_2.cellml): Invalid file passed validation

[5.4.2.7.unit_offset_non_zero_and_exponent_one](../models_1_0/valid/5.4.2.7.unit_offset_non_zero_and_exponent_one.cellml): Valid file passed OK

[5.4.2.7.unit_offset_zero_and_exponent](../models_1_0/valid/5.4.2.7.unit_offset_zero_and_exponent.cellml): Valid file passed OK

[5.4.2.7.unit_offset_zero_and_siblings](../models_1_0/valid/5.4.2.7.unit_offset_zero_and_siblings.cellml): Valid file passed OK


### 5.5.2

[5.5.2.boolean_arithmetic_divide](../models_1_0/booleans/5.5.2.boolean_arithmetic_divide.cellml): Valid file passed OK

[5.5.2.boolean_arithmetic_minus](../models_1_0/booleans/5.5.2.boolean_arithmetic_minus.cellml): Valid file passed OK

[5.5.2.boolean_arithmetic_plus](../models_1_0/booleans/5.5.2.boolean_arithmetic_plus.cellml): Valid file passed OK

[5.5.2.boolean_arithmetic_power_1](../models_1_0/booleans/5.5.2.boolean_arithmetic_power_1.cellml): Valid file passed OK

[5.5.2.boolean_arithmetic_power_2](../models_1_0/booleans/5.5.2.boolean_arithmetic_power_2.cellml): Valid file passed OK

[5.5.2.boolean_arithmetic_root_1](../models_1_0/booleans/5.5.2.boolean_arithmetic_root_1.cellml): Valid file passed OK

[5.5.2.boolean_arithmetic_root_2](../models_1_0/booleans/5.5.2.boolean_arithmetic_root_2.cellml): Valid file passed OK

[5.5.2.boolean_arithmetic_times](../models_1_0/booleans/5.5.2.boolean_arithmetic_times.cellml): Valid file passed OK

[5.5.2.boolean_compare_eq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_eq_operand_error.cellml): Valid file passed OK

[5.5.2.boolean_compare_geq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_geq_operand_error.cellml): Valid file passed OK

[5.5.2.boolean_compare_gt_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_gt_operand_error.cellml): Valid file passed OK

[5.5.2.boolean_compare_leq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_leq_operand_error.cellml): Valid file passed OK

[5.5.2.boolean_compare_lt_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_lt_operand_error.cellml): Valid file passed OK

[5.5.2.boolean_compare_neq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_neq_operand_error.cellml): Valid file passed OK

[5.5.2.boolean_derivatives_1](../models_1_0/booleans/5.5.2.boolean_derivatives_1.cellml): Valid file passed OK

[5.5.2.boolean_derivatives_2](../models_1_0/booleans/5.5.2.boolean_derivatives_2.cellml): Valid file passed OK

[5.5.2.boolean_function_abs](../models_1_0/booleans/5.5.2.boolean_function_abs.cellml): Valid file passed OK

[5.5.2.boolean_function_ceiling](../models_1_0/booleans/5.5.2.boolean_function_ceiling.cellml): Valid file passed OK

[5.5.2.boolean_function_exp](../models_1_0/booleans/5.5.2.boolean_function_exp.cellml): Valid file passed OK

[5.5.2.boolean_function_factorial](../models_1_0/booleans/5.5.2.boolean_function_factorial.cellml): Valid file passed OK

[5.5.2.boolean_function_floor](../models_1_0/booleans/5.5.2.boolean_function_floor.cellml): Valid file passed OK

[5.5.2.boolean_function_ln](../models_1_0/booleans/5.5.2.boolean_function_ln.cellml): Valid file passed OK

[5.5.2.boolean_function_log_1](../models_1_0/booleans/5.5.2.boolean_function_log_1.cellml): Valid file passed OK

[5.5.2.boolean_function_log_2](../models_1_0/booleans/5.5.2.boolean_function_log_2.cellml): Valid file passed OK

[5.5.2.boolean_logic_and_operand_error](../models_1_0/booleans/5.5.2.boolean_logic_and_operand_error.cellml): Valid file passed OK

[5.5.2.boolean_logic_not_operand_error](../models_1_0/booleans/5.5.2.boolean_logic_not_operand_error.cellml): Valid file passed OK

[5.5.2.boolean_logic_or_operand_error](../models_1_0/booleans/5.5.2.boolean_logic_or_operand_error.cellml): Valid file passed OK

[5.5.2.boolean_logic_xor_operand_error](../models_1_0/booleans/5.5.2.boolean_logic_xor_operand_error.cellml): Valid file passed OK

[5.5.2.boolean_trig_arccos](../models_1_0/booleans/5.5.2.boolean_trig_arccos.cellml): Valid file passed OK

[5.5.2.boolean_trig_arccosh](../models_1_0/booleans/5.5.2.boolean_trig_arccosh.cellml): Valid file passed OK

[5.5.2.boolean_trig_arccot](../models_1_0/booleans/5.5.2.boolean_trig_arccot.cellml): Valid file passed OK

[5.5.2.boolean_trig_arccoth](../models_1_0/booleans/5.5.2.boolean_trig_arccoth.cellml): Valid file passed OK

[5.5.2.boolean_trig_arccsc](../models_1_0/booleans/5.5.2.boolean_trig_arccsc.cellml): Valid file passed OK

[5.5.2.boolean_trig_arccsch](../models_1_0/booleans/5.5.2.boolean_trig_arccsch.cellml): Valid file passed OK

[5.5.2.boolean_trig_arcsec](../models_1_0/booleans/5.5.2.boolean_trig_arcsec.cellml): Valid file passed OK

[5.5.2.boolean_trig_arcsech](../models_1_0/booleans/5.5.2.boolean_trig_arcsech.cellml): Valid file passed OK

[5.5.2.boolean_trig_arcsin](../models_1_0/booleans/5.5.2.boolean_trig_arcsin.cellml): Valid file passed OK

[5.5.2.boolean_trig_arcsinh](../models_1_0/booleans/5.5.2.boolean_trig_arcsinh.cellml): Valid file passed OK

[5.5.2.boolean_trig_arctan](../models_1_0/booleans/5.5.2.boolean_trig_arctan.cellml): Valid file passed OK

[5.5.2.boolean_trig_arctanh](../models_1_0/booleans/5.5.2.boolean_trig_arctanh.cellml): Valid file passed OK

[5.5.2.boolean_trig_cos](../models_1_0/booleans/5.5.2.boolean_trig_cos.cellml): Valid file passed OK

[5.5.2.boolean_trig_cosh](../models_1_0/booleans/5.5.2.boolean_trig_cosh.cellml): Valid file passed OK

[5.5.2.boolean_trig_cot](../models_1_0/booleans/5.5.2.boolean_trig_cot.cellml): Valid file passed OK

[5.5.2.boolean_trig_coth](../models_1_0/booleans/5.5.2.boolean_trig_coth.cellml): Valid file passed OK

[5.5.2.boolean_trig_csc](../models_1_0/booleans/5.5.2.boolean_trig_csc.cellml): Valid file passed OK

[5.5.2.boolean_trig_csch](../models_1_0/booleans/5.5.2.boolean_trig_csch.cellml): Valid file passed OK

[5.5.2.boolean_trig_sec](../models_1_0/booleans/5.5.2.boolean_trig_sec.cellml): Valid file passed OK

[5.5.2.boolean_trig_sech](../models_1_0/booleans/5.5.2.boolean_trig_sech.cellml): Valid file passed OK

[5.5.2.boolean_trig_sin](../models_1_0/booleans/5.5.2.boolean_trig_sin.cellml): Valid file passed OK

[5.5.2.boolean_trig_sinh](../models_1_0/booleans/5.5.2.boolean_trig_sinh.cellml): Valid file passed OK

[5.5.2.boolean_trig_tan](../models_1_0/booleans/5.5.2.boolean_trig_tan.cellml): Valid file passed OK

[5.5.2.boolean_trig_tanh](../models_1_0/booleans/5.5.2.boolean_trig_tanh.cellml): Valid file passed OK

[5.5.2.boolean_variable_1](../models_1_0/booleans/5.5.2.boolean_variable_1.cellml): Valid file passed OK

[5.5.2.boolean_variable_2](../models_1_0/booleans/5.5.2.boolean_variable_2.cellml): Valid file passed OK

[5.5.2.boolean_variable_3](../models_1_0/booleans/5.5.2.boolean_variable_3.cellml): Valid file passed OK


## 6.4.1.1

❌ [6.4.1.1.group_component_ref_missing_1](../models_1_0/invalid/6.4.1.1.group_component_ref_missing_1.cellml): Invalid file passed validation

[6.4.1.1.group_component_ref_missing_2](../models_1_0/invalid/6.4.1.1.group_component_ref_missing_2.cellml): Error in invalid file detected

[6.4.1.1.group_component_ref_multiple](../models_1_0/valid/6.4.1.1.group_component_ref_multiple.cellml): Valid file passed OK

[6.4.1.1.group_component_ref_single](../models_1_0/valid/6.4.1.1.group_component_ref_single.cellml): Valid file passed OK

[6.4.1.1.group_empty](../models_1_0/invalid/6.4.1.1.group_empty.cellml): Error in invalid file detected

[6.4.1.1.group_only_extensions](../models_1_0/invalid/6.4.1.1.group_only_extensions.cellml): Error in invalid file detected

❌ [6.4.1.1.group_relationship_ref_missing_1](../models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_1.cellml): Invalid file passed validation

[6.4.1.1.group_relationship_ref_missing_2](../models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_2.cellml): Error in invalid file detected

[6.4.1.1.group_with_component](../models_1_0/invalid/6.4.1.1.group_with_component.cellml): Error in invalid file detected

[6.4.1.1.group_with_connection](../models_1_0/invalid/6.4.1.1.group_with_connection.cellml): Error in invalid file detected

[6.4.1.1.group_with_group](../models_1_0/invalid/6.4.1.1.group_with_group.cellml): Error in invalid file detected

[6.4.1.1.group_with_map_components](../models_1_0/invalid/6.4.1.1.group_with_map_components.cellml): Error in invalid file detected

[6.4.1.1.group_with_map_variables](../models_1_0/invalid/6.4.1.1.group_with_map_variables.cellml): Error in invalid file detected

[6.4.1.1.group_with_math](../models_1_0/invalid/6.4.1.1.group_with_math.cellml): Error in invalid file detected

[6.4.1.1.group_with_model](../models_1_0/invalid/6.4.1.1.group_with_model.cellml): Error in invalid file detected

[6.4.1.1.group_with_reaction](../models_1_0/invalid/6.4.1.1.group_with_reaction.cellml): Error in invalid file detected

[6.4.1.1.group_with_role](../models_1_0/invalid/6.4.1.1.group_with_role.cellml): Error in invalid file detected

[6.4.1.1.group_with_unit](../models_1_0/invalid/6.4.1.1.group_with_unit.cellml): Error in invalid file detected

[6.4.1.1.group_with_units](../models_1_0/invalid/6.4.1.1.group_with_units.cellml): Error in invalid file detected

[6.4.1.1.group_with_variable](../models_1_0/invalid/6.4.1.1.group_with_variable.cellml): Error in invalid file detected

[6.4.1.1.group_with_variable_ref](../models_1_0/invalid/6.4.1.1.group_with_variable_ref.cellml): Error in invalid file detected

[6.4.1.group_child_order_1](../models_1_0/valid/6.4.1.group_child_order_1.cellml): Valid file passed OK

[6.4.1.group_child_order_2](../models_1_0/valid/6.4.1.group_child_order_2.cellml): Valid file passed OK


#### 6.4.2.1

❌ [6.4.2.1.relationship_ref_name](../models_1_0/valid/6.4.2.1.relationship_ref_name.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:family of element model

[6.4.2.1.relationship_ref_relationship_1](../models_1_0/valid/6.4.2.1.relationship_ref_relationship_1.cellml): Valid file passed OK

❌ [6.4.2.1.relationship_ref_relationship_2](../models_1_0/valid/6.4.2.1.relationship_ref_relationship_2.cellml): Valid file failed validation
* Returned: 
  * Error on line 6: No declaration for attribute xmlns:family of element model
  * Error on line 10: No declaration for attribute relationship of element relationship_ref

[6.4.2.1.relationship_ref_relationship_missing](../models_1_0/invalid/6.4.2.1.relationship_ref_relationship_missing.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_component](../models_1_0/invalid/6.4.2.1.relationship_ref_with_component.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_component_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_component_ref.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_connection](../models_1_0/invalid/6.4.2.1.relationship_ref_with_connection.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_group](../models_1_0/invalid/6.4.2.1.relationship_ref_with_group.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_map_components](../models_1_0/invalid/6.4.2.1.relationship_ref_with_map_components.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_map_variables](../models_1_0/invalid/6.4.2.1.relationship_ref_with_map_variables.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_math](../models_1_0/invalid/6.4.2.1.relationship_ref_with_math.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_model](../models_1_0/invalid/6.4.2.1.relationship_ref_with_model.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_reaction](../models_1_0/invalid/6.4.2.1.relationship_ref_with_reaction.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_relationship_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_relationship_ref.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_role](../models_1_0/invalid/6.4.2.1.relationship_ref_with_role.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_unit](../models_1_0/invalid/6.4.2.1.relationship_ref_with_unit.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_units](../models_1_0/invalid/6.4.2.1.relationship_ref_with_units.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_variable](../models_1_0/invalid/6.4.2.1.relationship_ref_with_variable.cellml): Error in invalid file detected

[6.4.2.1.relationship_ref_with_variable_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_variable_ref.cellml): Error in invalid file detected


##### 6.4.2.2

❌ [6.4.2.2.relationship_ref_relationship_invalid](../models_1_0/invalid/6.4.2.2.relationship_ref_relationship_invalid.cellml): Invalid file passed validation


##### 6.4.2.3

❌ [6.4.2.3.relationship_ref_name_invalid](../models_1_0/invalid/6.4.2.3.relationship_ref_name_invalid.cellml): Invalid file passed validation

❌ [6.4.2.3.relationship_ref_name_not_unique_model_wide](../models_1_0/valid/6.4.2.3.relationship_ref_name_not_unique_model_wide.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:family of element model


##### 6.4.2.4

❌ [6.4.2.4.relationship_ref_encapsulation_duplicate](../models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_duplicate.cellml): Invalid file passed validation

❌ [6.4.2.4.relationship_ref_encapsulation_named](../models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_named.cellml): Invalid file passed validation


##### 6.4.2.5

❌ [6.4.2.5.relationship_ref_duplicate_named](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_named.cellml): Invalid file passed validation

❌ [6.4.2.5.relationship_ref_duplicate_unnamed_1](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_unnamed_1.cellml): Invalid file passed validation

❌ [6.4.2.5.relationship_ref_duplicate_unnamed_2](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_unnamed_2.cellml): Invalid file passed validation

❌ [6.4.2.5.relationship_ref_multiple_1](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_1.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model

❌ [6.4.2.5.relationship_ref_multiple_2](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_2.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model

❌ [6.4.2.5.relationship_ref_multiple_3](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_3.cellml): Valid file failed validation
* Returned: 
  * Error on line 5: No declaration for attribute xmlns:fruit of element model


#### 6.4.3.1

[6.4.3.1.component_ref_component_missing](../models_1_0/invalid/6.4.3.1.component_ref_component_missing.cellml): Error in invalid file detected

[6.4.3.1.component_ref_nesting](../models_1_0/valid/6.4.3.1.component_ref_nesting.cellml): Valid file passed OK

[6.4.3.1.component_ref_with_component](../models_1_0/invalid/6.4.3.1.component_ref_with_component.cellml): Error in invalid file detected

[6.4.3.1.component_ref_with_connection](../models_1_0/invalid/6.4.3.1.component_ref_with_connection.cellml): Error in invalid file detected

[6.4.3.1.component_ref_with_group](../models_1_0/invalid/6.4.3.1.component_ref_with_group.cellml): Error in invalid file detected

[6.4.3.1.component_ref_with_map_components](../models_1_0/invalid/6.4.3.1.component_ref_with_map_components.cellml): Error in invalid file detected

[6.4.3.1.component_ref_with_map_variables](../models_1_0/invalid/6.4.3.1.component_ref_with_map_variables.cellml): Error in invalid file detected

[6.4.3.1.component_ref_with_math](../models_1_0/invalid/6.4.3.1.component_ref_with_math.cellml): Error in invalid file detected

[6.4.3.1.component_ref_with_model](../models_1_0/invalid/6.4.3.1.component_ref_with_model.cellml): Error in invalid file detected

[6.4.3.1.component_ref_with_reaction](../models_1_0/invalid/6.4.3.1.component_ref_with_reaction.cellml): Error in invalid file detected

[6.4.3.1.component_ref_with_relationship_ref](../models_1_0/invalid/6.4.3.1.component_ref_with_relationship_ref.cellml): Error in invalid file detected

[6.4.3.1.component_ref_with_role](../models_1_0/invalid/6.4.3.1.component_ref_with_role.cellml): Error in invalid file detected

[6.4.3.1.component_ref_with_unit](../models_1_0/invalid/6.4.3.1.component_ref_with_unit.cellml): Error in invalid file detected

[6.4.3.1.component_ref_with_units](../models_1_0/invalid/6.4.3.1.component_ref_with_units.cellml): Error in invalid file detected

[6.4.3.1.component_ref_with_variable](../models_1_0/invalid/6.4.3.1.component_ref_with_variable.cellml): Error in invalid file detected

[6.4.3.1.component_ref_with_variable_ref](../models_1_0/invalid/6.4.3.1.component_ref_with_variable_ref.cellml): Error in invalid file detected


##### 6.4.3.2

❌ [6.4.3.2.component_ref_children_declared_twice_1](../models_1_0/invalid/6.4.3.2.component_ref_children_declared_twice_1.cellml): Invalid file passed validation

❌ [6.4.3.2.component_ref_children_declared_twice_2](../models_1_0/invalid/6.4.3.2.component_ref_children_declared_twice_2.cellml): Invalid file passed validation

❌ [6.4.3.2.component_ref_children_declared_twice_3](../models_1_0/invalid/6.4.3.2.component_ref_children_declared_twice_3.cellml): Invalid file passed validation

❌ [6.4.3.2.component_ref_cycle_1](../models_1_0/invalid/6.4.3.2.component_ref_cycle_1.cellml): Invalid file passed validation

❌ [6.4.3.2.component_ref_cycle_2](../models_1_0/invalid/6.4.3.2.component_ref_cycle_2.cellml): Invalid file passed validation

❌ [6.4.3.2.component_ref_cycle_3](../models_1_0/invalid/6.4.3.2.component_ref_cycle_3.cellml): Invalid file passed validation

❌ [6.4.3.2.component_ref_cycle_4](../models_1_0/invalid/6.4.3.2.component_ref_cycle_4.cellml): Invalid file passed validation

❌ [6.4.3.2.component_ref_duplicate_child_1](../models_1_0/invalid/6.4.3.2.component_ref_duplicate_child_1.cellml): Invalid file passed validation

❌ [6.4.3.2.component_ref_duplicate_child_2](../models_1_0/invalid/6.4.3.2.component_ref_duplicate_child_2.cellml): Invalid file passed validation

❌ [6.4.3.2.component_ref_no_children_containment](../models_1_0/invalid/6.4.3.2.component_ref_no_children_containment.cellml): Invalid file passed validation

❌ [6.4.3.2.component_ref_no_children_encapsulation](../models_1_0/invalid/6.4.3.2.component_ref_no_children_encapsulation.cellml): Invalid file passed validation

❌ [6.4.3.2.component_ref_no_children_extension](../models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:fruit of element model
  * Error on line 11: No declaration for attribute relationship of element relationship_ref

[6.4.3.2.component_ref_overlapping_containment](../models_1_0/valid/6.4.3.2.component_ref_overlapping_containment.cellml): Valid file passed OK

❌ [6.4.3.2.component_ref_overlapping_encapsulation](../models_1_0/invalid/6.4.3.2.component_ref_overlapping_encapsulation.cellml): Invalid file passed validation

[6.4.3.2.component_ref_split_named](../models_1_0/valid/6.4.3.2.component_ref_split_named.cellml): Valid file passed OK

[6.4.3.2.component_ref_split_unnamed_1](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_1.cellml): Valid file passed OK

[6.4.3.2.component_ref_split_unnamed_2](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_2.cellml): Valid file passed OK


##### 6.4.3.3

❌ [6.4.3.3.component_ref_component_invalid](../models_1_0/invalid/6.4.3.3.component_ref_component_invalid.cellml): Invalid file passed validation

❌ [6.4.3.3.component_ref_component_nonexistent_1](../models_1_0/invalid/6.4.3.3.component_ref_component_nonexistent_1.cellml): Invalid file passed validation

❌ [6.4.3.3.component_ref_component_nonexistent_2](../models_1_0/invalid/6.4.3.3.component_ref_component_nonexistent_2.cellml): Invalid file passed validation


## 7.4.1.1

[7.4.1.1.reaction_variable_ref_missing](../models_1_0/invalid/7.4.1.1.reaction_variable_ref_missing.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_component](../models_1_0/invalid/7.4.1.1.reaction_with_component.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_component_ref](../models_1_0/invalid/7.4.1.1.reaction_with_component_ref.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_connection](../models_1_0/invalid/7.4.1.1.reaction_with_connection.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_group](../models_1_0/invalid/7.4.1.1.reaction_with_group.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_map_components](../models_1_0/invalid/7.4.1.1.reaction_with_map_components.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_map_variables](../models_1_0/invalid/7.4.1.1.reaction_with_map_variables.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_math](../models_1_0/invalid/7.4.1.1.reaction_with_math.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_model](../models_1_0/invalid/7.4.1.1.reaction_with_model.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_reaction](../models_1_0/invalid/7.4.1.1.reaction_with_reaction.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_relationship_ref](../models_1_0/invalid/7.4.1.1.reaction_with_relationship_ref.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_role](../models_1_0/invalid/7.4.1.1.reaction_with_role.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_unit](../models_1_0/invalid/7.4.1.1.reaction_with_unit.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_units](../models_1_0/invalid/7.4.1.1.reaction_with_units.cellml): Error in invalid file detected

[7.4.1.1.reaction_with_variable](../models_1_0/invalid/7.4.1.1.reaction_with_variable.cellml): Error in invalid file detected


##### 7.4.1.2

[7.4.1.2.reaction_reversible_invalid](../models_1_0/invalid/7.4.1.2.reaction_reversible_invalid.cellml): Error in invalid file detected

[7.4.1.2.reaction_reversible_no](../models_1_0/valid/7.4.1.2.reaction_reversible_no.cellml): Valid file passed OK

[7.4.1.2.reaction_reversible_yes](../models_1_0/valid/7.4.1.2.reaction_reversible_yes.cellml): Valid file passed OK


##### 7.4.1.3

❌ [7.4.1.3.reaction_encapsulating_delta_variable](../models_1_0/invalid/7.4.1.3.reaction_encapsulating_delta_variable.cellml): Invalid file passed validation


#### 7.4.2.1

[7.4.2.1.variable_ref_role_missing](../models_1_0/invalid/7.4.2.1.variable_ref_role_missing.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_variable_missing](../models_1_0/invalid/7.4.2.1.variable_ref_variable_missing.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_component](../models_1_0/invalid/7.4.2.1.variable_ref_with_component.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_component_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_component_ref.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_connection](../models_1_0/invalid/7.4.2.1.variable_ref_with_connection.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_group](../models_1_0/invalid/7.4.2.1.variable_ref_with_group.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_map_components](../models_1_0/invalid/7.4.2.1.variable_ref_with_map_components.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_map_variables](../models_1_0/invalid/7.4.2.1.variable_ref_with_map_variables.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_math](../models_1_0/invalid/7.4.2.1.variable_ref_with_math.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_model](../models_1_0/invalid/7.4.2.1.variable_ref_with_model.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_reaction](../models_1_0/invalid/7.4.2.1.variable_ref_with_reaction.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_relationship_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_relationship_ref.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_unit](../models_1_0/invalid/7.4.2.1.variable_ref_with_unit.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_units](../models_1_0/invalid/7.4.2.1.variable_ref_with_units.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_variable](../models_1_0/invalid/7.4.2.1.variable_ref_with_variable.cellml): Error in invalid file detected

[7.4.2.1.variable_ref_with_variable_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_variable_ref.cellml): Error in invalid file detected


##### 7.4.2.2

❌ [7.4.2.2.variable_ref_variable_duplicate](../models_1_0/invalid/7.4.2.2.variable_ref_variable_duplicate.cellml): Invalid file passed validation

❌ [7.4.2.2.variable_ref_variable_hidden](../models_1_0/invalid/7.4.2.2.variable_ref_variable_hidden.cellml): Invalid file passed validation

❌ [7.4.2.2.variable_ref_variable_nonexistent](../models_1_0/invalid/7.4.2.2.variable_ref_variable_nonexistent.cellml): Invalid file passed validation


#### 7.4.3.1

[7.4.3.1.role_role_missing](../models_1_0/invalid/7.4.3.1.role_role_missing.cellml): Error in invalid file detected

[7.4.3.1.role_with_component](../models_1_0/invalid/7.4.3.1.role_with_component.cellml): Error in invalid file detected

[7.4.3.1.role_with_component_ref](../models_1_0/invalid/7.4.3.1.role_with_component_ref.cellml): Error in invalid file detected

[7.4.3.1.role_with_connection](../models_1_0/invalid/7.4.3.1.role_with_connection.cellml): Error in invalid file detected

[7.4.3.1.role_with_group](../models_1_0/invalid/7.4.3.1.role_with_group.cellml): Error in invalid file detected

[7.4.3.1.role_with_map_components](../models_1_0/invalid/7.4.3.1.role_with_map_components.cellml): Error in invalid file detected

[7.4.3.1.role_with_map_variables](../models_1_0/invalid/7.4.3.1.role_with_map_variables.cellml): Error in invalid file detected

[7.4.3.1.role_with_model](../models_1_0/invalid/7.4.3.1.role_with_model.cellml): Error in invalid file detected

[7.4.3.1.role_with_reaction](../models_1_0/invalid/7.4.3.1.role_with_reaction.cellml): Error in invalid file detected

[7.4.3.1.role_with_relationship_ref](../models_1_0/invalid/7.4.3.1.role_with_relationship_ref.cellml): Error in invalid file detected

[7.4.3.1.role_with_role](../models_1_0/invalid/7.4.3.1.role_with_role.cellml): Error in invalid file detected

[7.4.3.1.role_with_unit](../models_1_0/invalid/7.4.3.1.role_with_unit.cellml): Error in invalid file detected

[7.4.3.1.role_with_units](../models_1_0/invalid/7.4.3.1.role_with_units.cellml): Error in invalid file detected

[7.4.3.1.role_with_variable](../models_1_0/invalid/7.4.3.1.role_with_variable.cellml): Error in invalid file detected

[7.4.3.1.role_with_variable_ref](../models_1_0/invalid/7.4.3.1.role_with_variable_ref.cellml): Error in invalid file detected


##### 7.4.3.2

[7.4.3.2.role_role_invalid](../models_1_0/invalid/7.4.3.2.role_role_invalid.cellml): Error in invalid file detected


##### 7.4.3.3

❌ [7.4.3.3.reaction_multiple_rates](../models_1_0/invalid/7.4.3.3.reaction_multiple_rates.cellml): Invalid file passed validation

❌ [7.4.3.3.role_rate_with_delta_variable](../models_1_0/invalid/7.4.3.3.role_rate_with_delta_variable.cellml): Invalid file passed validation

❌ [7.4.3.3.role_rate_with_multiple_roles](../models_1_0/invalid/7.4.3.3.role_rate_with_multiple_roles.cellml): Invalid file passed validation

❌ [7.4.3.3.role_rate_with_stoichiometry](../models_1_0/invalid/7.4.3.3.role_rate_with_stoichiometry.cellml): Invalid file passed validation


##### 7.4.3.4

[7.4.3.4.role_direction_invalid](../models_1_0/invalid/7.4.3.4.role_direction_invalid.cellml): Error in invalid file detected


##### 7.4.3.5

❌ [7.4.3.5.role_direction_both_irreversible](../models_1_0/invalid/7.4.3.5.role_direction_both_irreversible.cellml): Invalid file passed validation

❌ [7.4.3.5.role_direction_both_product](../models_1_0/invalid/7.4.3.5.role_direction_both_product.cellml): Invalid file passed validation

❌ [7.4.3.5.role_direction_both_rate](../models_1_0/invalid/7.4.3.5.role_direction_both_rate.cellml): Invalid file passed validation

❌ [7.4.3.5.role_direction_both_reactant](../models_1_0/invalid/7.4.3.5.role_direction_both_reactant.cellml): Invalid file passed validation

❌ [7.4.3.5.role_direction_reverse_irreversible](../models_1_0/invalid/7.4.3.5.role_direction_reverse_irreversible.cellml): Invalid file passed validation

❌ [7.4.3.5.role_direction_reverse_product](../models_1_0/invalid/7.4.3.5.role_direction_reverse_product.cellml): Invalid file passed validation

❌ [7.4.3.5.role_direction_reverse_rate](../models_1_0/invalid/7.4.3.5.role_direction_reverse_rate.cellml): Invalid file passed validation

❌ [7.4.3.5.role_direction_reverse_reactant](../models_1_0/invalid/7.4.3.5.role_direction_reverse_reactant.cellml): Invalid file passed validation

❌ [7.4.3.5.role_direction_role_duplicate](../models_1_0/invalid/7.4.3.5.role_direction_role_duplicate.cellml): Invalid file passed validation


##### 7.4.3.6

❌ [7.4.3.6.role_stoichiometry_invalid](../models_1_0/invalid/7.4.3.6.role_stoichiometry_invalid.cellml): Invalid file passed validation


##### 7.4.3.7

❌ [7.4.3.7.role_delta_variable_duplicate_1](../models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_1.cellml): Invalid file passed validation

❌ [7.4.3.7.role_delta_variable_duplicate_2](../models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_2.cellml): Invalid file passed validation

❌ [7.4.3.7.role_delta_variable_nonexistent_1](../models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_1.cellml): Invalid file passed validation

❌ [7.4.3.7.role_delta_variable_nonexistent_2](../models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_2.cellml): Invalid file passed validation


##### 7.4.3.8

❌ [7.4.3.8.role_delta_variable_activator](../models_1_0/invalid/7.4.3.8.role_delta_variable_activator.cellml): Invalid file passed validation

❌ [7.4.3.8.role_delta_variable_catalyst](../models_1_0/invalid/7.4.3.8.role_delta_variable_catalyst.cellml): Invalid file passed validation

❌ [7.4.3.8.role_delta_variable_inhibitor](../models_1_0/invalid/7.4.3.8.role_delta_variable_inhibitor.cellml): Invalid file passed validation

❌ [7.4.3.8.role_delta_variable_modifier](../models_1_0/invalid/7.4.3.8.role_delta_variable_modifier.cellml): Invalid file passed validation

❌ [7.4.3.8.role_delta_variable_with_rate_and_math](../models_1_0/invalid/7.4.3.8.role_delta_variable_with_rate_and_math.cellml): Invalid file passed validation

❌ [7.4.3.8.role_delta_variable_with_stoichiometry_no_rate](../models_1_0/invalid/7.4.3.8.role_delta_variable_with_stoichiometry_no_rate.cellml): Invalid file passed validation

❌ [7.4.3.8.role_delta_variable_without_rate_or_math](../models_1_0/invalid/7.4.3.8.role_delta_variable_without_rate_or_math.cellml): Invalid file passed validation


##### 7.4.3.9

❌ [7.4.3.9.role_math_not_relevant](../models_1_0/invalid/7.4.3.9.role_math_not_relevant.cellml): Invalid file passed validation

[7.4.3.reaction_all_roles_and_attributes](../models_1_0/valid/7.4.3.reaction_all_roles_and_attributes.cellml): Valid file passed OK

[7.4.3.reaction_reversible_no](../models_1_0/valid/7.4.3.reaction_reversible_no.cellml): Valid file passed OK

[7.4.3.reaction_simple](../models_1_0/valid/7.4.3.reaction_simple.cellml): Valid file passed OK


## 8.4.1

[8.4.1.cmeta_id_duplicate](../models_1_0/invalid/8.4.1.cmeta_id_duplicate.cellml): Error in invalid file detected

[8.4.1.cmeta_id_in_component](../models_1_0/valid/8.4.1.cmeta_id_in_component.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_component_ref](../models_1_0/valid/8.4.1.cmeta_id_in_component_ref.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_connection](../models_1_0/valid/8.4.1.cmeta_id_in_connection.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_group](../models_1_0/valid/8.4.1.cmeta_id_in_group.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_map_components](../models_1_0/valid/8.4.1.cmeta_id_in_map_components.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_map_variables](../models_1_0/valid/8.4.1.cmeta_id_in_map_variables.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_model](../models_1_0/valid/8.4.1.cmeta_id_in_model.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_reaction](../models_1_0/valid/8.4.1.cmeta_id_in_reaction.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_relationship_ref](../models_1_0/valid/8.4.1.cmeta_id_in_relationship_ref.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_role](../models_1_0/valid/8.4.1.cmeta_id_in_role.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_unit](../models_1_0/valid/8.4.1.cmeta_id_in_unit.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_units_1](../models_1_0/valid/8.4.1.cmeta_id_in_units_1.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_units_2](../models_1_0/valid/8.4.1.cmeta_id_in_units_2.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_variable](../models_1_0/valid/8.4.1.cmeta_id_in_variable.cellml): Valid file passed OK

[8.4.1.cmeta_id_in_variable_ref](../models_1_0/valid/8.4.1.cmeta_id_in_variable_ref.cellml): Valid file passed OK


#### 8.4.2

❌ [8.4.2.rdf_in_component](../models_1_0/valid/8.4.2.rdf_in_component.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 8: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (rdf:RDF )
  * Error on line 9: No declaration for element RDF
  * Error on line 9: No declaration for attribute about of element RDF
  * Error on line 10: No declaration for element description

❌ [8.4.2.rdf_in_component_ref](../models_1_0/valid/8.4.2.rdf_in_component_ref.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 13: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (rdf:RDF )
  * Error on line 14: No declaration for element RDF
  * Error on line 14: No declaration for attribute about of element RDF
  * Error on line 15: No declaration for element description

❌ [8.4.2.rdf_in_connection](../models_1_0/valid/8.4.2.rdf_in_connection.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 14: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables rdf:RDF )
  * Error on line 17: No declaration for element RDF
  * Error on line 17: No declaration for attribute about of element RDF
  * Error on line 18: No declaration for element description

❌ [8.4.2.rdf_in_group](../models_1_0/valid/8.4.2.rdf_in_group.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 10: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref rdf:RDF )
  * Error on line 15: No declaration for element RDF
  * Error on line 15: No declaration for attribute about of element RDF
  * Error on line 16: No declaration for element description

❌ [8.4.2.rdf_in_map_components](../models_1_0/valid/8.4.2.rdf_in_map_components.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 9: Element map_components was declared EMPTY this one has content
  * Error on line 10: No declaration for element RDF
  * Error on line 10: No declaration for attribute about of element RDF
  * Error on line 11: No declaration for element description

❌ [8.4.2.rdf_in_map_variables](../models_1_0/valid/8.4.2.rdf_in_map_variables.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 16: Element map_variables was declared EMPTY this one has content
  * Error on line 17: No declaration for element RDF
  * Error on line 17: No declaration for attribute about of element RDF
  * Error on line 18: No declaration for element description

❌ [8.4.2.rdf_in_model](../models_1_0/valid/8.4.2.rdf_in_model.cellml): Valid file failed validation
* Returned: 
  * Error on line 8: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (rdf:RDF )
  * Error on line 8: No declaration for attribute xmlns:rdf of element model
  * Error on line 8: No declaration for attribute xmlns:dc of element model
  * Error on line 9: No declaration for element RDF
  * Error on line 9: No declaration for attribute about of element RDF
  * Error on line 10: No declaration for element description

❌ [8.4.2.rdf_in_reaction](../models_1_0/valid/8.4.2.rdf_in_reaction.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 10: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref rdf:RDF )
  * Error on line 14: No declaration for element RDF
  * Error on line 14: No declaration for attribute about of element RDF
  * Error on line 15: No declaration for element description

❌ [8.4.2.rdf_in_relationship_ref](../models_1_0/valid/8.4.2.rdf_in_relationship_ref.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 11: Element relationship_ref was declared EMPTY this one has content
  * Error on line 12: No declaration for element RDF
  * Error on line 12: No declaration for attribute about of element RDF
  * Error on line 13: No declaration for element description

❌ [8.4.2.rdf_in_role](../models_1_0/valid/8.4.2.rdf_in_role.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 12: Element role content does not follow the DTD, expecting (math)?, got (rdf:RDF )
  * Error on line 13: No declaration for element RDF
  * Error on line 13: No declaration for attribute about of element RDF
  * Error on line 14: No declaration for element description

❌ [8.4.2.rdf_in_unit](../models_1_0/valid/8.4.2.rdf_in_unit.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 9: Element unit was declared EMPTY this one has content
  * Error on line 10: No declaration for element RDF
  * Error on line 10: No declaration for attribute about of element RDF
  * Error on line 11: No declaration for element description

❌ [8.4.2.rdf_in_units_1](../models_1_0/valid/8.4.2.rdf_in_units_1.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 8: Element units content does not follow the DTD, expecting (unit)*, got (unit rdf:RDF )
  * Error on line 10: No declaration for element RDF
  * Error on line 10: No declaration for attribute about of element RDF
  * Error on line 11: No declaration for element description

❌ [8.4.2.rdf_in_units_2](../models_1_0/valid/8.4.2.rdf_in_units_2.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 9: Element units content does not follow the DTD, expecting (unit)*, got (unit rdf:RDF )
  * Error on line 11: No declaration for element RDF
  * Error on line 11: No declaration for attribute about of element RDF
  * Error on line 12: No declaration for element description

❌ [8.4.2.rdf_in_variable](../models_1_0/valid/8.4.2.rdf_in_variable.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 9: Element variable was declared EMPTY this one has content
  * Error on line 10: No declaration for element RDF
  * Error on line 10: No declaration for attribute about of element RDF
  * Error on line 11: No declaration for element description

❌ [8.4.2.rdf_in_variable_ref](../models_1_0/valid/8.4.2.rdf_in_variable_ref.cellml): Valid file failed validation
* Returned: 
  * Error on line 7: No declaration for attribute xmlns:rdf of element model
  * Error on line 7: No declaration for attribute xmlns:dc of element model
  * Error on line 11: Element variable_ref content does not follow the DTD, expecting (role)+, got (rdf:RDF role )
  * Error on line 12: No declaration for element RDF
  * Error on line 12: No declaration for attribute about of element RDF
  * Error on line 13: No declaration for element description

[C.3.3.unit_checking_arithmetic_minus_operand_error_1](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_minus_operand_error_1.cellml): Valid file passed OK

[C.3.3.unit_checking_arithmetic_minus_operand_error_2](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_minus_operand_error_2.cellml): Valid file passed OK

[C.3.3.unit_checking_arithmetic_minus_operand_error_3](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_minus_operand_error_3.cellml): Valid file passed OK

[C.3.3.unit_checking_arithmetic_plus_operand_error_1](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_plus_operand_error_1.cellml): Valid file passed OK

[C.3.3.unit_checking_arithmetic_plus_operand_error_2](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_plus_operand_error_2.cellml): Valid file passed OK

[C.3.3.unit_checking_arithmetic_plus_operand_error_3](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_plus_operand_error_3.cellml): Valid file passed OK

[C.3.3.unit_checking_arithmetic_plus_operand_error_4](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_plus_operand_error_4.cellml): Valid file passed OK

[C.3.3.unit_checking_arithmetic_power_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_power_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_arithmetic_root_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_root_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_compare_eq_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_eq_operand_mismatch.cellml): Valid file passed OK

[C.3.3.unit_checking_compare_geq_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_geq_operand_mismatch.cellml): Valid file passed OK

[C.3.3.unit_checking_compare_gt_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_gt_operand_mismatch.cellml): Valid file passed OK

[C.3.3.unit_checking_compare_leq_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_leq_operand_mismatch.cellml): Valid file passed OK

[C.3.3.unit_checking_compare_lt_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_lt_operand_mismatch.cellml): Valid file passed OK

[C.3.3.unit_checking_compare_neq_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_neq_operand_mismatch.cellml): Valid file passed OK

[C.3.3.unit_checking_derivative_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_derivative_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_function_exp_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_function_exp_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_function_factorial_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_function_factorial_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_function_ln_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_function_ln_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_function_log_operand_error_1](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_function_log_operand_error_1.cellml): Valid file passed OK

[C.3.3.unit_checking_function_log_operand_error_2](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_function_log_operand_error_2.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_arccos_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arccos_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_arccosh_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arccosh_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_arccot_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arccot_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_arccoth_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arccoth_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_arccsc_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arccsc_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_arccsch_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arccsch_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_arcsec_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arcsec_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_arcsech_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arcsech_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_arcsin_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arcsin_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_arcsinh_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arcsinh_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_arctan_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arctan_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_arctanh_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arctanh_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_cos_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_cos_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_cosh_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_cosh_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_cot_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_cot_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_coth_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_coth_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_csc_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_csc_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_csch_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_csch_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_sec_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_sec_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_sech_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_sech_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_sin_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_sin_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_sinh_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_sinh_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_tan_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_tan_operand_error.cellml): Valid file passed OK

[C.3.3.unit_checking_trig_tanh_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_tanh_operand_error.cellml): Valid file passed OK

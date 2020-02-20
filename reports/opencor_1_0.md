# OpenCOR / CellML API Validation - CellML 1.0

Performance:
* 88% according to spec (685 out of 770)
* 297 out of 317 valid files passed
* 388 out of 453 invalid files detected

Issues:
* 20 valid files failed validation
* 57 invalid files passed validation
* 8 invalid files failed validation for the wrong reason

Results per category

(Valid passed, invalid failed, valid failed, invalid passed, invalid failed for wrong reason, percent classified correctly according to spec)

|Category|V Pass|I Fail|🔴 V Fail|🔵 I Pass|🔶 I Bad|Score|
|-|-|-|-|-|-|-|
|[0. Not mentioned in spec](#0-not-mentioned-in-spec)|6|10|0|0|0|100%|
|[2. Fundamentals](#2-fundamentals)|18|22|1|5|0|86%|
|[3. Model structure](#3-model-structure)|50|153|0|0|0|100%|
|[4. Mathematics](#4-mathematics)|40|14|5|5|0|84%|
|[5. Units](#5-units)|90|74|10|4|8|88%|
|[6. Grouping](#6-grouping)|16|65|1|13|0|85%|
|[7. Reactions](#7-reactions)|5|50|0|29|0|65%|
|[8. Metadata framework](#8-metadata-framework)|30|0|0|1|0|96%|
|[C. Advanced units functionality](#c-advanced-units-functionality)|42|0|3|0|0|93%|


---

## 0. Not mentioned in spec

### 0.0

[0.0.root_namespace_1](../models_1_0/valid/0.0.root_namespace_1.cellml): Valid file passed validation.

[0.0.root_namespace_2](../models_1_0/valid/0.0.root_namespace_2.cellml): Valid file passed validation.

[0.0.root_node_namespace_wrong](../models_1_0/invalid/0.0.root_node_namespace_wrong.cellml): Error detected correctly.
* Expected: ```model is not CellML (wrong namespace)```
* Output: ```[Error] [0:0] The model could not be loaded (model is not CellML (wrong namespace)).```

[0.0.root_node_not_model](../models_1_0/invalid/0.0.root_node_not_model.cellml): Error detected correctly.
* Expected: ```model is not CellML (wrong element name)```
* Output: ```[Error] [0:0] The model could not be loaded (model is not CellML (wrong element name)).```

[0.0.root_node_two_elements](../models_1_0/invalid/0.0.root_node_two_elements.cellml): Error detected correctly.
* Expected: ```The model could not be loaded (badxml```
* Output: ```[Error] [0:0] The model could not be loaded (badxml/6/0//).```

[0.0.root_node_two_models](../models_1_0/invalid/0.0.root_node_two_models.cellml): Error detected correctly.
* Expected: ```The model could not be loaded (badxml```
* Output: ```[Error] [0:0] The model could not be loaded (badxml/6/0//).```


---

### 0.1

[0.1.real_number_invalid_1](../models_1_0/invalid/0.1.real_number_invalid_1.cellml): Error detected correctly.
* Expected: ```Expected a real number, but didn't get one in a valid format```
* Output: ```[Error] [4:20] Expected a real number, but didn't get one in a valid format.```

[0.1.real_number_invalid_2](../models_1_0/invalid/0.1.real_number_invalid_2.cellml): Error detected correctly.
* Expected: ```Expected a real number, but didn't get one in a valid format```
* Output: ```[Error] [4:20] Expected a real number, but didn't get one in a valid format.```

[0.1.real_number_invalid_3](../models_1_0/invalid/0.1.real_number_invalid_3.cellml): Error detected correctly.
* Expected: ```Expected a real number, but didn't get one in a valid format```
* Output: ```[Error] [4:20] Expected a real number, but didn't get one in a valid format.```

[0.1.real_number_invalid_4](../models_1_0/invalid/0.1.real_number_invalid_4.cellml): Error detected correctly.
* Expected: ```Expected a real number, but didn't get one in a valid format```
* Output: ```[Error] [4:20] Expected a real number, but didn't get one in a valid format.```

[0.1.real_number_invalid_5](../models_1_0/invalid/0.1.real_number_invalid_5.cellml): Error detected correctly.
* Expected: ```Expected a real number, but didn't get one in a valid format```
* Output:
  * ```[Error] [4:6] Variable has initial_value attribute which is a CellML identifier which does not name a variable in the same component.```
  * ```[Error] [4:20] Expected a real number, but didn't get one in a valid format.```

[0.1.real_number_invalid_6](../models_1_0/invalid/0.1.real_number_invalid_6.cellml): Error detected correctly.
* Expected: ```Expected a real number, but didn't get one in a valid format```
* Output:
  * ```[Error] [4:6] Variable has initial_value attribute which is a CellML identifier which does not name a variable in the same component.```
  * ```[Error] [4:20] Expected a real number, but didn't get one in a valid format.```

[0.1.real_numbers](../models_1_0/valid/0.1.real_numbers.cellml): Valid file passed validation.

[0.1.real_numbers_extreme](../models_1_0/valid/0.1.real_numbers_extreme.cellml): Valid file passed validation.


---

### 0.2

[0.2.component_name_same_as_model](../models_1_0/valid/0.2.component_name_same_as_model.cellml): Valid file passed validation.

[0.2.variable_name_same_as_model](../models_1_0/valid/0.2.variable_name_same_as_model.cellml): Valid file passed validation.


---

## 2. Fundamentals

#### 2.4.1

[2.4.1.identifier_empty](../models_1_0/invalid/2.4.1.identifier_empty.cellml): Error detected correctly.
* Expected: ```A valid CellML identifier must contain at least one letter```
* Output: ```[Error] [3:9] A valid CellML identifier must contain at least one letter (section 2.4.1).```

[2.4.1.identifier_only_underscore](../models_1_0/invalid/2.4.1.identifier_only_underscore.cellml): Error detected correctly.
* Expected: ```A valid CellML identifier must contain at least one letter```
* Output: ```[Error] [3:9] A valid CellML identifier must contain at least one letter (section 2.4.1).```

[2.4.1.identifier_unexpected_character_1](../models_1_0/invalid/2.4.1.identifier_unexpected_character_1.cellml): Error detected correctly.
* Expected: ```A valid CellML identifier must only contain alphanumeric characters```
* Output: ```[Error] [3:9] A valid CellML identifier must only contain alphanumeric characters from the US-ASCII character set and the underscore character (section 2.4.1).```

🔵 [2.4.1.identifier_unexpected_character_2](../models_1_0/invalid/2.4.1.identifier_unexpected_character_2.cellml): **Error not detected.**

🔵 [2.4.1.identifier_unexpected_character_unicode](../models_1_0/invalid/2.4.1.identifier_unexpected_character_unicode.cellml): **Error not detected.**

🔴 [2.4.1.valid_identifiers](../models_1_0/valid/2.4.1.valid_identifiers.cellml): **Valid file failed validation.**
* Output:
  * ```[Error] [13:9] A valid CellML identifier must contain at least one letter (section 2.4.1).```
  * ```[Error] [15:9] A valid CellML identifier must contain at least one letter (section 2.4.1).```


---

#### 2.4.2

[2.4.2.imaginary_attributes_1](../models_1_0/invalid/2.4.2.imaginary_attributes_1.cellml): Error detected correctly.
* Expected: ```Unexpected attribute fruit found```
* Output: ```[Error] [2:258] Unexpected attribute fruit found - not valid here.```

[2.4.2.imaginary_attributes_2](../models_1_0/invalid/2.4.2.imaginary_attributes_2.cellml): Error detected correctly.
* Expected: ```Unexpected attribute fruit found```
* Output: ```[Error] [2:321] Unexpected attribute fruit found - not valid here.```

[2.4.2.imaginary_elements](../models_1_0/invalid/2.4.2.imaginary_elements.cellml): Error detected correctly.
* Expected: ```Unexpected element fruit found```
* Output: ```[Error] [3:4] Unexpected element fruit found - not valid here.```


---

#### 2.4.3

🔵 [2.4.3.cellml_attributes_inside_extensions](../models_1_0/invalid/2.4.3.cellml_attributes_inside_extensions.cellml): **Error not detected.**
* Output: ```[Warning] [3:4] Attribute name in namespace http://www.cellml.org/cellml/1.0#is not allowed in extension elements.```

🔵 [2.4.3.cellml_elements_inside_extensions](../models_1_0/invalid/2.4.3.cellml_elements_inside_extensions.cellml): **Error not detected.**
* Output: ```[Warning] [3:4] Element cellml:component in namespace http://www.cellml.org/cellml/1.0#is not allowed in extension elements.```

[2.4.3.component_ref_with_extensions](../models_1_0/valid/2.4.3.component_ref_with_extensions.cellml): Valid file passed validation.

[2.4.3.component_with_extensions](../models_1_0/valid/2.4.3.component_with_extensions.cellml): Valid file passed validation.

[2.4.3.connection_with_extensions](../models_1_0/valid/2.4.3.connection_with_extensions.cellml): Valid file passed validation.

[2.4.3.group_with_extensions](../models_1_0/valid/2.4.3.group_with_extensions.cellml): Valid file passed validation.

[2.4.3.map_components_with_extensions](../models_1_0/valid/2.4.3.map_components_with_extensions.cellml): Valid file passed validation.

[2.4.3.map_variables_with_extensions](../models_1_0/valid/2.4.3.map_variables_with_extensions.cellml): Valid file passed validation.

[2.4.3.model_with_extensions](../models_1_0/valid/2.4.3.model_with_extensions.cellml): Valid file passed validation.

[2.4.3.reaction_with_extensions](../models_1_0/valid/2.4.3.reaction_with_extensions.cellml): Valid file passed validation.

[2.4.3.relationship_ref_with_extensions](../models_1_0/valid/2.4.3.relationship_ref_with_extensions.cellml): Valid file passed validation.

[2.4.3.role_with_extensions](../models_1_0/valid/2.4.3.role_with_extensions.cellml): Valid file passed validation.

[2.4.3.unit_with_extensions](../models_1_0/valid/2.4.3.unit_with_extensions.cellml): Valid file passed validation.

[2.4.3.units_with_extensions](../models_1_0/valid/2.4.3.units_with_extensions.cellml): Valid file passed validation.

[2.4.3.variable_ref_with_extensions](../models_1_0/valid/2.4.3.variable_ref_with_extensions.cellml): Valid file passed validation.

[2.4.3.variable_with_extensions](../models_1_0/valid/2.4.3.variable_with_extensions.cellml): Valid file passed validation.


---

#### 2.4.4

[2.4.4.model_linux_line_breaks](../models_1_0/valid/2.4.4.model_linux_line_breaks.cellml): Valid file passed validation.

[2.4.4.model_windows_line_breaks](../models_1_0/valid/2.4.4.model_windows_line_breaks.cellml): Valid file passed validation.

[2.4.4.model_with_spaces](../models_1_0/valid/2.4.4.model_with_spaces.cellml): Valid file passed validation.

[2.4.4.model_with_tabs](../models_1_0/valid/2.4.4.model_with_tabs.cellml): Valid file passed validation.

[2.4.4.text_in_component](../models_1_0/invalid/2.4.4.text_in_component.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [3:4] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_component_ref](../models_1_0/invalid/2.4.4.text_in_component_ref.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [8:8] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_connection](../models_1_0/invalid/2.4.4.text_in_connection.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [9:4] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_group](../models_1_0/invalid/2.4.4.text_in_group.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [5:4] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_map_components](../models_1_0/invalid/2.4.4.text_in_map_components.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [4:6] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_map_variables](../models_1_0/invalid/2.4.4.text_in_map_variables.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [11:6] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_model](../models_1_0/invalid/2.4.4.text_in_model.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [2:131] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_reaction](../models_1_0/invalid/2.4.4.text_in_reaction.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [5:6] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_relationship_ref](../models_1_0/invalid/2.4.4.text_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [6:6] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_role](../models_1_0/invalid/2.4.4.text_in_role.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [7:10] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_unit](../models_1_0/invalid/2.4.4.text_in_unit.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [4:6] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_units_1](../models_1_0/invalid/2.4.4.text_in_units_1.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [3:4] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_units_2](../models_1_0/invalid/2.4.4.text_in_units_2.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [4:6] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_variable](../models_1_0/invalid/2.4.4.text_in_variable.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [4:6] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```

[2.4.4.text_in_variable_ref](../models_1_0/invalid/2.4.4.text_in_variable_ref.cellml): Error detected correctly.
* Expected: ```any characters that occur immediately within elements in the CellML```
* Output: ```[Error] [6:8] Per section 2.4.4 of the CellML specification, any characters that occur immediately within elements in the CellML namespace must be either space (#x20) characters, carriage returns (#xA), line feeds (#xD), or tabs (#x9).```


---

#### 2.5.1

[2.5.1.identifiers_are_case_sensitive](../models_1_0/invalid/2.5.1.identifiers_are_case_sensitive.cellml): Error detected correctly.
* Expected: ```Invalid component referenced by component_1 attribute```
* Output:
  * ```[Error] [10:6] Component_1 attribute doesn't refer to a valid component.```
  * ```[Error] [10:6] Invalid component referenced by component_1 attribute.```


---

#### 2.5.2

🔵 [2.5.2.attribute_in_cellml_namespace](../models_1_0/invalid/2.5.2.attribute_in_cellml_namespace.cellml): **Error not detected.**


---

## 3. Model structure

##### 3.4.1.1

[3.4.1.1.model_child_order_1](../models_1_0/valid/3.4.1.1.model_child_order_1.cellml): Valid file passed validation.

[3.4.1.1.model_child_order_2](../models_1_0/valid/3.4.1.1.model_child_order_2.cellml): Valid file passed validation.

[3.4.1.1.model_empty](../models_1_0/valid/3.4.1.1.model_empty.cellml): Valid file passed validation.

[3.4.1.1.model_name_missing](../models_1_0/invalid/3.4.1.1.model_name_missing.cellml): Error detected correctly.
* Expected: ```name attribute is required```
* Output: ```[Error] [2:131] The CellML specification says the name attribute is required here.```

[3.4.1.1.model_with_component_ref](../models_1_0/invalid/3.4.1.1.model_with_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element component_ref```
* Output: ```[Error] [3:4] Unexpected element component_ref found - not valid here.```

[3.4.1.1.model_with_components](../models_1_0/valid/3.4.1.1.model_with_components.cellml): Valid file passed validation.

[3.4.1.1.model_with_connections](../models_1_0/valid/3.4.1.1.model_with_connections.cellml): Valid file passed validation.

[3.4.1.1.model_with_groups](../models_1_0/valid/3.4.1.1.model_with_groups.cellml): Valid file passed validation.

[3.4.1.1.model_with_map_components](../models_1_0/invalid/3.4.1.1.model_with_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected element map_components```
* Output: ```[Error] [5:4] Unexpected element map_components found - not valid here.```

[3.4.1.1.model_with_map_variables](../models_1_0/invalid/3.4.1.1.model_with_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected element map_variables```
* Output: ```[Error] [9:4] Unexpected element map_variables found - not valid here.```

[3.4.1.1.model_with_math](../models_1_0/invalid/3.4.1.1.model_with_math.cellml): Error detected correctly.
* Expected: ```Unexpected element math```
* Output: ```[Error] [6:4] Unexpected element math found - not valid here.```

[3.4.1.1.model_with_model](../models_1_0/invalid/3.4.1.1.model_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [3:4] Unexpected element model found - not valid here.```

[3.4.1.1.model_with_one_component](../models_1_0/valid/3.4.1.1.model_with_one_component.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_connection](../models_1_0/valid/3.4.1.1.model_with_one_connection.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_group](../models_1_0/valid/3.4.1.1.model_with_one_group.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_units](../models_1_0/valid/3.4.1.1.model_with_one_units.cellml): Valid file passed validation.

[3.4.1.1.model_with_reaction](../models_1_0/invalid/3.4.1.1.model_with_reaction.cellml): Error detected correctly.
* Expected: ```Unexpected element reaction```
* Output: ```[Error] [6:4] Unexpected element reaction found - not valid here.```

[3.4.1.1.model_with_relationship_ref](../models_1_0/invalid/3.4.1.1.model_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element relationship_ref```
* Output: ```[Error] [3:4] Unexpected element relationship_ref found - not valid here.```

[3.4.1.1.model_with_role](../models_1_0/invalid/3.4.1.1.model_with_role.cellml): Error detected correctly.
* Expected: ```Unexpected element role```
* Output: ```[Error] [3:4] Unexpected element role found - not valid here.```

[3.4.1.1.model_with_unit](../models_1_0/invalid/3.4.1.1.model_with_unit.cellml): Error detected correctly.
* Expected: ```Unexpected element unit```
* Output: ```[Error] [3:4] Unexpected element unit found - not valid here.```

[3.4.1.1.model_with_units](../models_1_0/valid/3.4.1.1.model_with_units.cellml): Valid file passed validation.

[3.4.1.1.model_with_variable](../models_1_0/invalid/3.4.1.1.model_with_variable.cellml): Error detected correctly.
* Expected: ```Unexpected element variable```
* Output: ```[Error] [3:4] Unexpected element variable found - not valid here.```

[3.4.1.1.model_with_variable_ref](../models_1_0/invalid/3.4.1.1.model_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element variable_ref```
* Output: ```[Error] [3:4] Unexpected element variable_ref found - not valid here.```


---

##### 3.4.1.2

[3.4.1.2.model_name_invalid](../models_1_0/invalid/3.4.1.2.model_name_invalid.cellml): Error detected correctly.
* Expected: ```A valid CellML identifier must contain at least one letter```
* Output: ```[Error] [2:258] A valid CellML identifier must contain at least one letter (section 2.4.1).```


---

##### 3.4.2.1

[3.4.2.1.component_child_order_1](../models_1_0/valid/3.4.2.1.component_child_order_1.cellml): Valid file passed validation.

[3.4.2.1.component_child_order_2](../models_1_0/valid/3.4.2.1.component_child_order_2.cellml): Valid file passed validation.

[3.4.2.1.component_empty](../models_1_0/valid/3.4.2.1.component_empty.cellml): Valid file passed validation.

[3.4.2.1.component_name_missing](../models_1_0/invalid/3.4.2.1.component_name_missing.cellml): Error detected correctly.
* Expected: ```name attribute is required```
* Output: ```[Error] [3:4] The CellML specification says the name attribute is required here.```

[3.4.2.1.component_with_component](../models_1_0/invalid/3.4.2.1.component_with_component.cellml): Error detected correctly.
* Expected: ```Unexpected element component```
* Output: ```[Error] [4:6] Unexpected element component found - not valid here.```

[3.4.2.1.component_with_component_ref](../models_1_0/invalid/3.4.2.1.component_with_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element component_ref```
* Output: ```[Error] [4:6] Unexpected element component_ref found - not valid here.```

[3.4.2.1.component_with_connection](../models_1_0/invalid/3.4.2.1.component_with_connection.cellml): Error detected correctly.
* Expected: ```Unexpected element connection```
* Output: ```[Error] [10:6] Unexpected element connection found - not valid here.```

[3.4.2.1.component_with_group](../models_1_0/invalid/3.4.2.1.component_with_group.cellml): Error detected correctly.
* Expected: ```Unexpected element group```
* Output: ```[Error] [4:6] Unexpected element group found - not valid here.```

[3.4.2.1.component_with_map_components](../models_1_0/invalid/3.4.2.1.component_with_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected element map_components```
* Output: ```[Error] [4:6] Unexpected element map_components found - not valid here.```

[3.4.2.1.component_with_map_variables](../models_1_0/invalid/3.4.2.1.component_with_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected element map_variables```
* Output: ```[Error] [4:6] Unexpected element map_variables found - not valid here.```

[3.4.2.1.component_with_maths](../models_1_0/valid/3.4.2.1.component_with_maths.cellml): Valid file passed validation.

[3.4.2.1.component_with_model](../models_1_0/invalid/3.4.2.1.component_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [4:6] Unexpected element model found - not valid here.```

[3.4.2.1.component_with_one_math](../models_1_0/valid/3.4.2.1.component_with_one_math.cellml): Valid file passed validation.

[3.4.2.1.component_with_one_reaction](../models_1_0/valid/3.4.2.1.component_with_one_reaction.cellml): Valid file passed validation.

[3.4.2.1.component_with_one_units](../models_1_0/valid/3.4.2.1.component_with_one_units.cellml): Valid file passed validation.

[3.4.2.1.component_with_one_variable](../models_1_0/valid/3.4.2.1.component_with_one_variable.cellml): Valid file passed validation.

[3.4.2.1.component_with_reactions](../models_1_0/valid/3.4.2.1.component_with_reactions.cellml): Valid file passed validation.

[3.4.2.1.component_with_relationship_ref](../models_1_0/invalid/3.4.2.1.component_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element relationship_ref```
* Output: ```[Error] [4:6] Unexpected element relationship_ref found - not valid here.```

[3.4.2.1.component_with_role](../models_1_0/invalid/3.4.2.1.component_with_role.cellml): Error detected correctly.
* Expected: ```Unexpected element role```
* Output: ```[Error] [4:6] Unexpected element role found - not valid here.```

[3.4.2.1.component_with_unit](../models_1_0/invalid/3.4.2.1.component_with_unit.cellml): Error detected correctly.
* Expected: ```Unexpected element unit```
* Output: ```[Error] [4:6] Unexpected element unit found - not valid here.```

[3.4.2.1.component_with_units](../models_1_0/valid/3.4.2.1.component_with_units.cellml): Valid file passed validation.

[3.4.2.1.component_with_variable_ref](../models_1_0/invalid/3.4.2.1.component_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element variable_ref```
* Output: ```[Error] [4:6] Unexpected element variable_ref found - not valid here.```

[3.4.2.1.component_with_variables](../models_1_0/valid/3.4.2.1.component_with_variables.cellml): Valid file passed validation.


---

##### 3.4.2.2

[3.4.2.2.component_name_duplicate](../models_1_0/invalid/3.4.2.2.component_name_duplicate.cellml): Error detected correctly.
* Expected: ```More than one component in the model named```
* Output: ```[Error] [4:4] More than one component in the model named c1.```

[3.4.2.2.component_name_invalid](../models_1_0/invalid/3.4.2.2.component_name_invalid.cellml): Error detected correctly.
* Expected: ```A valid CellML identifier must contain at least one letter```
* Output: ```[Error] [3:9] A valid CellML identifier must contain at least one letter (section 2.4.1).```


---

##### 3.4.3.1

[3.4.3.1.variable_name_missing](../models_1_0/invalid/3.4.3.1.variable_name_missing.cellml): Error detected correctly.
* Expected: ```name attribute is required```
* Output: ```[Error] [4:6] The CellML specification says the name attribute is required here.```

[3.4.3.1.variable_units_missing](../models_1_0/invalid/3.4.3.1.variable_units_missing.cellml): Error detected correctly.
* Expected: ```MUST define a units attribute```
* Output:
  * ```[Error] [4:6] Each  /  element MUST define a units attribute (section 3.4.3.1 / 5.4.3.1).```
  * ```[Error] [4:6] Invalid units on variable: .```

[3.4.3.1.variable_with_component](../models_1_0/invalid/3.4.3.1.variable_with_component.cellml): Error detected correctly.
* Expected: ```Unexpected element component```
* Output: ```[Error] [5:8] Unexpected element component found - not valid here.```

[3.4.3.1.variable_with_component_ref](../models_1_0/invalid/3.4.3.1.variable_with_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element component_ref```
* Output: ```[Error] [5:8] Unexpected element component_ref found - not valid here.```

[3.4.3.1.variable_with_connection](../models_1_0/invalid/3.4.3.1.variable_with_connection.cellml): Error detected correctly.
* Expected: ```Unexpected element connection```
* Output: ```[Error] [11:8] Unexpected element connection found - not valid here.```

[3.4.3.1.variable_with_group](../models_1_0/invalid/3.4.3.1.variable_with_group.cellml): Error detected correctly.
* Expected: ```Unexpected element group```
* Output: ```[Error] [5:8] Unexpected element group found - not valid here.```

[3.4.3.1.variable_with_initial_value](../models_1_0/valid/3.4.3.1.variable_with_initial_value.cellml): Valid file passed validation.

[3.4.3.1.variable_with_interfaces](../models_1_0/valid/3.4.3.1.variable_with_interfaces.cellml): Valid file passed validation.

[3.4.3.1.variable_with_map_components](../models_1_0/invalid/3.4.3.1.variable_with_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected element map_component```
* Output: ```[Error] [5:8] Unexpected element map_components found - not valid here.```

[3.4.3.1.variable_with_map_variables](../models_1_0/invalid/3.4.3.1.variable_with_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected element map_variables```
* Output: ```[Error] [5:8] Unexpected element map_variables found - not valid here.```

[3.4.3.1.variable_with_math](../models_1_0/invalid/3.4.3.1.variable_with_math.cellml): Error detected correctly.
* Expected: ```Unexpected element math```
* Output: ```[Error] [5:8] Unexpected element math found - not valid here.```

[3.4.3.1.variable_with_model](../models_1_0/invalid/3.4.3.1.variable_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [5:8] Unexpected element model found - not valid here.```

[3.4.3.1.variable_with_reaction](../models_1_0/invalid/3.4.3.1.variable_with_reaction.cellml): Error detected correctly.
* Expected: ```Unexpected element reaction```
* Output: ```[Error] [5:8] Unexpected element reaction found - not valid here.```

[3.4.3.1.variable_with_relationship_ref](../models_1_0/invalid/3.4.3.1.variable_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element relationship_ref```
* Output: ```[Error] [5:8] Unexpected element relationship_ref found - not valid here.```

[3.4.3.1.variable_with_role](../models_1_0/invalid/3.4.3.1.variable_with_role.cellml): Error detected correctly.
* Expected: ```Unexpected element role```
* Output: ```[Error] [5:8] Unexpected element role found - not valid here.```

[3.4.3.1.variable_with_unit](../models_1_0/invalid/3.4.3.1.variable_with_unit.cellml): Error detected correctly.
* Expected: ```Unexpected element unit```
* Output: ```[Error] [5:8] Unexpected element unit found - not valid here.```

[3.4.3.1.variable_with_units](../models_1_0/invalid/3.4.3.1.variable_with_units.cellml): Error detected correctly.
* Expected: ```Unexpected element units```
* Output: ```[Error] [5:8] Unexpected element units found - not valid here.```

[3.4.3.1.variable_with_variable](../models_1_0/invalid/3.4.3.1.variable_with_variable.cellml): Error detected correctly.
* Expected: ```Unexpected element variable```
* Output: ```[Error] [5:8] Unexpected element variable found - not valid here.```

[3.4.3.1.variable_with_variable_ref](../models_1_0/invalid/3.4.3.1.variable_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element variable_ref```
* Output: ```[Error] [5:8] Unexpected element variable_ref found - not valid here.```

[3.4.3.1.variable_without_initial_value](../models_1_0/valid/3.4.3.1.variable_without_initial_value.cellml): Valid file passed validation.


---

##### 3.4.3.2

[3.4.3.2.variable_name_duplicate](../models_1_0/invalid/3.4.3.2.variable_name_duplicate.cellml): Error detected correctly.
* Expected: ```There is more than one variable in the same component called```
* Output: ```[Error] [5:6] There is more than one variable in the same component called x.```

[3.4.3.2.variable_name_invalid](../models_1_0/invalid/3.4.3.2.variable_name_invalid.cellml): Error detected correctly.
* Expected: ```A valid CellML identifier must only contain alphanumeric```
* Output:
  * ```[Error] [4:11] A valid CellML identifier must only contain alphanumeric characters from the US-ASCII character set and the underscore character (section 2.4.1).```
  * ```[Error] [4:11] A valid CellML identifier must only contain alphanumeric characters from the US-ASCII character set and the underscore character (section 2.4.1).```
  * ```[Error] [4:11] A valid CellML identifier must only contain alphanumeric characters from the US-ASCII character set and the underscore character (section 2.4.1).```

[3.4.3.2.variable_name_same_as_cousin](../models_1_0/valid/3.4.3.2.variable_name_same_as_cousin.cellml): Valid file passed validation.

[3.4.3.2.variable_name_same_as_parent](../models_1_0/valid/3.4.3.2.variable_name_same_as_parent.cellml): Valid file passed validation.


---

##### 3.4.3.3

[3.4.3.3.variable_units_component](../models_1_0/valid/3.4.3.3.variable_units_component.cellml): Valid file passed validation.

[3.4.3.3.variable_units_model](../models_1_0/valid/3.4.3.3.variable_units_model.cellml): Valid file passed validation.

[3.4.3.3.variable_units_other_component](../models_1_0/invalid/3.4.3.3.variable_units_other_component.cellml): Error detected correctly.
* Expected: ```Invalid units on variable```
* Output: ```[Error] [4:6] Invalid units on variable: oranges.```

[3.4.3.3.variable_units_predefined](../models_1_0/valid/3.4.3.3.variable_units_predefined.cellml): Valid file passed validation.

[3.4.3.3.variable_units_unknown](../models_1_0/invalid/3.4.3.3.variable_units_unknown.cellml): Error detected correctly.
* Expected: ```Invalid units on variable```
* Output: ```[Error] [4:6] Invalid units on variable: oranges.```


---

##### 3.4.3.4

[3.4.3.4.variable_interface_public_invalid](../models_1_0/invalid/3.4.3.4.variable_interface_public_invalid.cellml): Error detected correctly.
* Expected: ```the value of the public_interface / private_interface attribute MUST```
* Output: ```[Error] [4:32] If present, the value of the public_interface / private_interface attribute MUST be "in", "out", or "none" (section 3.4.3.4 / 3.4.3.5).```


---

##### 3.4.3.5

[3.4.3.5.variable_interface_private_invalid](../models_1_0/invalid/3.4.3.5.variable_interface_private_invalid.cellml): Error detected correctly.
* Expected: ```the value of the public_interface / private_interface attribute MUST```
* Output: ```[Error] [4:33] If present, the value of the public_interface / private_interface attribute MUST be "in", "out", or "none" (section 3.4.3.4 / 3.4.3.5).```


---

##### 3.4.3.6

[3.4.3.6.variable_interfaces_both_in](../models_1_0/invalid/3.4.3.6.variable_interfaces_both_in.cellml): Error detected correctly.
* Expected: ```Cannot have two in interfaces on variable```
* Output: ```[Error] [4:6] Cannot have two in interfaces on variable.```


---

##### 3.4.3.7

[3.4.3.7.variable_initial_value_empty](../models_1_0/invalid/3.4.3.7.variable_initial_value_empty.cellml): Error detected correctly.
* Expected: ```Expected a real number```
* Output: ```[Error] [4:20] Expected a real number, but didn't get one in a valid format.```

[3.4.3.7.variable_initial_value_invalid](../models_1_0/invalid/3.4.3.7.variable_initial_value_invalid.cellml): Error detected correctly.
* Expected: ```Expected a real number```
* Output: ```[Error] [4:20] Expected a real number, but didn't get one in a valid format.```


---

##### 3.4.3.8

[3.4.3.8.variable_interfaces_private_in_and_initial](../models_1_0/invalid/3.4.3.8.variable_interfaces_private_in_and_initial.cellml): Error detected correctly.
* Expected: ```cannot have initial value```
* Output: ```[Error] [5:6] Variables with public or private interfaces of in cannot have initial value attributes.```

[3.4.3.8.variable_interfaces_public_in_and_initial](../models_1_0/invalid/3.4.3.8.variable_interfaces_public_in_and_initial.cellml): Error detected correctly.
* Expected: ```cannot have initial value```
* Output: ```[Error] [5:6] Variables with public or private interfaces of in cannot have initial value attributes.```


---

##### 3.4.4.1

[3.4.4.1.connection_empty](../models_1_0/invalid/3.4.4.1.connection_empty.cellml): Error detected correctly.
* Expected: ```element MUST contain at least one```
* Output:
  * ```[Error] [3:4] Each  element MUST contain at least one  element (section 3.4.4.1).```
  * ```[Error] [3:4] Each  element MUST contain exactly one  element (section 3.4.4.1).```

[3.4.4.1.connection_map_components_missing](../models_1_0/invalid/3.4.4.1.connection_map_components_missing.cellml): Error detected correctly.
* Expected: ```MUST contain exactly one```
* Output: ```[Error] [11:4] Each  element MUST contain exactly one  element (section 3.4.4.1).```

[3.4.4.1.connection_map_components_multiple](../models_1_0/invalid/3.4.4.1.connection_map_components_multiple.cellml): Error detected correctly.
* Expected: ```MUST contain exactly one```
* Output:
  * ```[Error] [16:6] Each  element MUST contain exactly one  element (section 3.4.4.1).```
  * ```[Error] [18:6] Variable_2 attribute doesn't refer to a valid variable.```

[3.4.4.1.connection_map_variables_missing_1](../models_1_0/invalid/3.4.4.1.connection_map_variables_missing_1.cellml): Error detected correctly.
* Expected: ```MUST contain at least one```
* Output: ```[Error] [9:4] Each  element MUST contain at least one  element (section 3.4.4.1).```

[3.4.4.1.connection_map_variables_missing_2](../models_1_0/invalid/3.4.4.1.connection_map_variables_missing_2.cellml): Error detected correctly.
* Expected: ```MUST contain at least one```
* Output: ```[Error] [9:4] Each  element MUST contain at least one  element (section 3.4.4.1).```

[3.4.4.1.connection_only_extensions](../models_1_0/invalid/3.4.4.1.connection_only_extensions.cellml): Error detected correctly.
* Expected: ```MUST contain at least one```
* Output:
  * ```[Error] [3:4] Each  element MUST contain at least one  element (section 3.4.4.1).```
  * ```[Error] [3:4] Each  element MUST contain exactly one  element (section 3.4.4.1).```

[3.4.4.1.connection_with_component](../models_1_0/invalid/3.4.4.1.connection_with_component.cellml): Error detected correctly.
* Expected: ```Unexpected element component```
* Output: ```[Error] [12:6] Unexpected element component found - not valid here.```

[3.4.4.1.connection_with_component_ref](../models_1_0/invalid/3.4.4.1.connection_with_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element component_ref```
* Output: ```[Error] [12:6] Unexpected element component_ref found - not valid here.```

[3.4.4.1.connection_with_connection](../models_1_0/invalid/3.4.4.1.connection_with_connection.cellml): Error detected correctly.
* Expected: ```Unexpected element connection```
* Output: ```[Error] [15:6] Unexpected element connection found - not valid here.```

[3.4.4.1.connection_with_group](../models_1_0/invalid/3.4.4.1.connection_with_group.cellml): Error detected correctly.
* Expected: ```Unexpected element group```
* Output: ```[Error] [12:6] Unexpected element group found - not valid here.```

[3.4.4.1.connection_with_map_variables](../models_1_0/valid/3.4.4.1.connection_with_map_variables.cellml): Valid file passed validation.

[3.4.4.1.connection_with_math](../models_1_0/invalid/3.4.4.1.connection_with_math.cellml): Error detected correctly.
* Expected: ```Unexpected element math```
* Output: ```[Error] [12:6] Unexpected element math found - not valid here.```

[3.4.4.1.connection_with_model](../models_1_0/invalid/3.4.4.1.connection_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [12:6] Unexpected element model found - not valid here.```

[3.4.4.1.connection_with_name_attribute](../models_1_0/invalid/3.4.4.1.connection_with_name_attribute.cellml): Error detected correctly.
* Expected: ```Unexpected attribute name```
* Output: ```[Error] [9:9] Unexpected attribute name found - not valid here.```

[3.4.4.1.connection_with_one_map_variables](../models_1_0/valid/3.4.4.1.connection_with_one_map_variables.cellml): Valid file passed validation.

[3.4.4.1.connection_with_reaction](../models_1_0/invalid/3.4.4.1.connection_with_reaction.cellml): Error detected correctly.
* Expected: ```Unexpected element reaction```
* Output: ```[Error] [12:6] Unexpected element reaction found - not valid here.```

[3.4.4.1.connection_with_relationship_ref](../models_1_0/invalid/3.4.4.1.connection_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element relationship_ref```
* Output: ```[Error] [12:6] Unexpected element relationship_ref found - not valid here.```

[3.4.4.1.connection_with_role](../models_1_0/invalid/3.4.4.1.connection_with_role.cellml): Error detected correctly.
* Expected: ```Unexpected element role```
* Output: ```[Error] [12:6] Unexpected element role found - not valid here.```

[3.4.4.1.connection_with_unit](../models_1_0/invalid/3.4.4.1.connection_with_unit.cellml): Error detected correctly.
* Expected: ```Unexpected element unit```
* Output: ```[Error] [12:6] Unexpected element unit found - not valid here.```

[3.4.4.1.connection_with_units](../models_1_0/invalid/3.4.4.1.connection_with_units.cellml): Error detected correctly.
* Expected: ```Unexpected element units```
* Output: ```[Error] [12:6] Unexpected element units found - not valid here.```

[3.4.4.1.connection_with_variable](../models_1_0/invalid/3.4.4.1.connection_with_variable.cellml): Error detected correctly.
* Expected: ```Unexpected element variable```
* Output: ```[Error] [12:6] Unexpected element variable found - not valid here.```

[3.4.4.1.connection_with_variable_ref](../models_1_0/invalid/3.4.4.1.connection_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element variable_ref```
* Output: ```[Error] [12:6] Unexpected element variable_ref found - not valid here.```


---

##### 3.4.5.1

[3.4.5.1.connection_any_order_1](../models_1_0/valid/3.4.5.1.connection_any_order_1.cellml): Valid file passed validation.

[3.4.5.1.connection_any_order_2](../models_1_0/valid/3.4.5.1.connection_any_order_2.cellml): Valid file passed validation.

[3.4.5.1.map_components_component_1_missing](../models_1_0/invalid/3.4.5.1.map_components_component_1_missing.cellml): Error detected correctly.
* Expected: ```element MUST define a component_1 attribute```
* Output: ```[Error] [4:6] Each  element MUST define a component_1 attribute (section 3.4.5.1).```

[3.4.5.1.map_components_component_2_missing](../models_1_0/invalid/3.4.5.1.map_components_component_2_missing.cellml): Error detected correctly.
* Expected: ```element MUST define a component_2 attribute```
* Output: ```[Error] [4:6] Each  element MUST define a component_2 attribute (section 3.4.5.1).```

[3.4.5.1.map_components_with_component](../models_1_0/invalid/3.4.5.1.map_components_with_component.cellml): Error detected correctly.
* Expected: ```Unexpected element component```
* Output: ```[Error] [5:8] Unexpected element component found - not valid here.```

[3.4.5.1.map_components_with_component_ref](../models_1_0/invalid/3.4.5.1.map_components_with_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element component_ref```
* Output: ```[Error] [5:8] Unexpected element component_ref found - not valid here.```

[3.4.5.1.map_components_with_connection](../models_1_0/invalid/3.4.5.1.map_components_with_connection.cellml): Error detected correctly.
* Expected: ```Unexpected element connection```
* Output: ```[Error] [5:8] Unexpected element connection found - not valid here.```

[3.4.5.1.map_components_with_group](../models_1_0/invalid/3.4.5.1.map_components_with_group.cellml): Error detected correctly.
* Expected: ```Unexpected element group```
* Output: ```[Error] [5:8] Unexpected element group found - not valid here.```

[3.4.5.1.map_components_with_map_components](../models_1_0/invalid/3.4.5.1.map_components_with_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected element map_components```
* Output: ```[Error] [5:8] Unexpected element map_components found - not valid here.```

[3.4.5.1.map_components_with_map_variables](../models_1_0/invalid/3.4.5.1.map_components_with_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected element map_variables```
* Output: ```[Error] [5:8] Unexpected element map_variables found - not valid here.```

[3.4.5.1.map_components_with_math](../models_1_0/invalid/3.4.5.1.map_components_with_math.cellml): Error detected correctly.
* Expected: ```Unexpected element math```
* Output: ```[Error] [5:8] Unexpected element math found - not valid here.```

[3.4.5.1.map_components_with_model](../models_1_0/invalid/3.4.5.1.map_components_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [5:8] Unexpected element model found - not valid here.```

[3.4.5.1.map_components_with_reaction](../models_1_0/invalid/3.4.5.1.map_components_with_reaction.cellml): Error detected correctly.
* Expected: ```Unexpected element reaction```
* Output: ```[Error] [5:8] Unexpected element reaction found - not valid here.```

[3.4.5.1.map_components_with_relationship_ref](../models_1_0/invalid/3.4.5.1.map_components_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element relationship_ref```
* Output: ```[Error] [5:8] Unexpected element relationship_ref found - not valid here.```

[3.4.5.1.map_components_with_role](../models_1_0/invalid/3.4.5.1.map_components_with_role.cellml): Error detected correctly.
* Expected: ```Unexpected element role```
* Output: ```[Error] [5:8] Unexpected element role found - not valid here.```

[3.4.5.1.map_components_with_unit](../models_1_0/invalid/3.4.5.1.map_components_with_unit.cellml): Error detected correctly.
* Expected: ```Unexpected element unit```
* Output: ```[Error] [5:8] Unexpected element unit found - not valid here.```

[3.4.5.1.map_components_with_units](../models_1_0/invalid/3.4.5.1.map_components_with_units.cellml): Error detected correctly.
* Expected: ```Unexpected element units```
* Output: ```[Error] [5:8] Unexpected element units found - not valid here.```

[3.4.5.1.map_components_with_variable](../models_1_0/invalid/3.4.5.1.map_components_with_variable.cellml): Error detected correctly.
* Expected: ```Unexpected element variable```
* Output: ```[Error] [5:8] Unexpected element variable found - not valid here.```

[3.4.5.1.map_components_with_variable_ref](../models_1_0/invalid/3.4.5.1.map_components_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element variable_ref```
* Output: ```[Error] [5:8] Unexpected element variable_ref found - not valid here.```


---

##### 3.4.5.2

[3.4.5.2.map_components_component_1_nonexistent](../models_1_0/invalid/3.4.5.2.map_components_component_1_nonexistent.cellml): Error detected correctly.
* Expected: ```Component_1 attribute doesn't refer to a valid component```
* Output:
  * ```[Error] [5:6] Component_1 attribute doesn't refer to a valid component.```
  * ```[Error] [5:6] Invalid component referenced by component_1 attribute.```


---

##### 3.4.5.3

[3.4.5.3.map_components_component_2_nonexistent](../models_1_0/invalid/3.4.5.3.map_components_component_2_nonexistent.cellml): Error detected correctly.
* Expected: ```Component_2 attribute doesn't refer to a valid component```
* Output:
  * ```[Error] [5:6] Component_2 attribute doesn't refer to a valid component.```
  * ```[Error] [5:6] Invalid component referenced by component_2 attribute.```


---

##### 3.4.5.4

[3.4.5.4.map_components_component_1_equals_2](../models_1_0/invalid/3.4.5.4.map_components_component_1_equals_2.cellml): Error detected correctly.
* Expected: ```Cannot connect a component to itself```
* Output:
  * ```[Error] [4:6] Cannot connect a component to itself.```
  * ```[Error] [4:6] It is not valid to map a component to itself.```
  * ```[Error] [5:6] Mapping variable_1 has public interface of out but variable_2 also has public interface of out.```

[3.4.5.4.map_components_duplicate](../models_1_0/invalid/3.4.5.4.map_components_duplicate.cellml): Error detected correctly.
* Expected: ```There is more than one connection element for the same pair```
* Output:
  * ```[Error] [8:6] The can only be a single connection element for each pair of components in the model.```
  * ```[Error] [8:6] There is more than one connection element for the same pair of components.```

[3.4.5.4.map_components_duplicate_mirrored](../models_1_0/invalid/3.4.5.4.map_components_duplicate_mirrored.cellml): Error detected correctly.
* Expected: ```There is more than one connection element for the same pair```
* Output:
  * ```[Error] [8:6] The can only be a single connection element for each pair of components in the model.```
  * ```[Error] [8:6] There is more than one connection element for the same pair of components.```


---

##### 3.4.6.1

[3.4.6.1.map_variables_variable_1_missing](../models_1_0/invalid/3.4.6.1.map_variables_variable_1_missing.cellml): Error detected correctly.
* Expected: ```MUST define a variable_1 attribute```
* Output:
  * ```[Error] [11:6] Each  element MUST define a variable_1 attribute (section 3.4.6.1).```
  * ```[Error] [11:6] Variable_1 attribute doesn't refer to a valid variable.```

[3.4.6.1.map_variables_variable_2_missing](../models_1_0/invalid/3.4.6.1.map_variables_variable_2_missing.cellml): Error detected correctly.
* Expected: ```MUST define a variable_2 attribute```
* Output:
  * ```[Error] [11:6] Each  element MUST define a variable_2 attribute (section 3.4.6.1).```
  * ```[Error] [11:6] Variable_2 attribute doesn't refer to a valid variable.```

[3.4.6.1.map_variables_with_component](../models_1_0/invalid/3.4.6.1.map_variables_with_component.cellml): Error detected correctly.
* Expected: ```Unexpected element component```
* Output: ```[Error] [6:8] Unexpected element component found - not valid here.```

[3.4.6.1.map_variables_with_component_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element component_ref```
* Output: ```[Error] [6:8] Unexpected element component_ref found - not valid here.```

[3.4.6.1.map_variables_with_connection](../models_1_0/invalid/3.4.6.1.map_variables_with_connection.cellml): Error detected correctly.
* Expected: ```Unexpected element connection```
* Output: ```[Error] [6:8] Unexpected element connection found - not valid here.```

[3.4.6.1.map_variables_with_group](../models_1_0/invalid/3.4.6.1.map_variables_with_group.cellml): Error detected correctly.
* Expected: ```Unexpected element group```
* Output: ```[Error] [6:8] Unexpected element group found - not valid here.```

[3.4.6.1.map_variables_with_map_components](../models_1_0/invalid/3.4.6.1.map_variables_with_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected element map_components```
* Output: ```[Error] [6:8] Unexpected element map_components found - not valid here.```

[3.4.6.1.map_variables_with_map_variables](../models_1_0/invalid/3.4.6.1.map_variables_with_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected element map_variables```
* Output: ```[Error] [6:8] Unexpected element map_variables found - not valid here.```

[3.4.6.1.map_variables_with_math](../models_1_0/invalid/3.4.6.1.map_variables_with_math.cellml): Error detected correctly.
* Expected: ```Unexpected element math```
* Output: ```[Error] [6:8] Unexpected element math found - not valid here.```

[3.4.6.1.map_variables_with_model](../models_1_0/invalid/3.4.6.1.map_variables_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [6:8] Unexpected element model found - not valid here.```

[3.4.6.1.map_variables_with_reaction](../models_1_0/invalid/3.4.6.1.map_variables_with_reaction.cellml): Error detected correctly.
* Expected: ```Unexpected element reaction```
* Output: ```[Error] [6:8] Unexpected element reaction found - not valid here.```

[3.4.6.1.map_variables_with_relationship_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element relationship_ref```
* Output: ```[Error] [6:8] Unexpected element relationship_ref found - not valid here.```

[3.4.6.1.map_variables_with_role](../models_1_0/invalid/3.4.6.1.map_variables_with_role.cellml): Error detected correctly.
* Expected: ```Unexpected element role```
* Output: ```[Error] [6:8] Unexpected element role found - not valid here.```

[3.4.6.1.map_variables_with_unit](../models_1_0/invalid/3.4.6.1.map_variables_with_unit.cellml): Error detected correctly.
* Expected: ```Unexpected element unit```
* Output: ```[Error] [6:8] Unexpected element unit found - not valid here.```

[3.4.6.1.map_variables_with_units](../models_1_0/invalid/3.4.6.1.map_variables_with_units.cellml): Error detected correctly.
* Expected: ```Unexpected element units```
* Output: ```[Error] [6:8] Unexpected element units found - not valid here.```

[3.4.6.1.map_variables_with_variable](../models_1_0/invalid/3.4.6.1.map_variables_with_variable.cellml): Error detected correctly.
* Expected: ```Unexpected element variable```
* Output: ```[Error] [6:8] Unexpected element variable found - not valid here.```

[3.4.6.1.map_variables_with_variable_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element variable_ref```
* Output: ```[Error] [6:8] Unexpected element variable_ref found - not valid here.```


---

##### 3.4.6.2

[3.4.6.2.map_variables_variable_1_nonexistent](../models_1_0/invalid/3.4.6.2.map_variables_variable_1_nonexistent.cellml): Error detected correctly.
* Expected: ```Variable_1 attribute doesn't refer to a valid variable```
* Output: ```[Error] [9:6] Variable_1 attribute doesn't refer to a valid variable.```


---

##### 3.4.6.3

[3.4.6.3.map_variables_variable_2_nonexistent](../models_1_0/invalid/3.4.6.3.map_variables_variable_2_nonexistent.cellml): Error detected correctly.
* Expected: ```Variable_2 attribute doesn't refer to a valid variable```
* Output: ```[Error] [9:6] Variable_2 attribute doesn't refer to a valid variable.```


---

##### 3.4.6.4

[3.4.6.4.map_variables_chain_down](../models_1_0/valid/3.4.6.4.map_variables_chain_down.cellml): Valid file passed validation.

[3.4.6.4.map_variables_chain_up](../models_1_0/valid/3.4.6.4.map_variables_chain_up.cellml): Valid file passed validation.

[3.4.6.4.map_variables_child_multiple_out_1](../models_1_0/invalid/3.4.6.4.map_variables_child_multiple_out_1.cellml): Error detected correctly.
* Expected: ```More than one connection to in interface of variable```
* Output: ```[Error] [6:6] More than one connection to in interface of variable.```

[3.4.6.4.map_variables_child_multiple_out_2](../models_1_0/invalid/3.4.6.4.map_variables_child_multiple_out_2.cellml): Error detected correctly.
* Expected: ```More than one connection to in interface of variable```
* Output: ```[Error] [6:6] More than one connection to in interface of variable.```

[3.4.6.4.map_variables_child_out_to_out_1](../models_1_0/invalid/3.4.6.4.map_variables_child_out_to_out_1.cellml): Error detected correctly.
* Expected: ```also has public interface of out```
* Output: ```[Error] [19:6] Mapping variable_1 has private interface of out but variable_2 also has public interface of out.```

[3.4.6.4.map_variables_child_out_to_out_2](../models_1_0/invalid/3.4.6.4.map_variables_child_out_to_out_2.cellml): Error detected correctly.
* Expected: ```also has public interface of out```
* Output: ```[Error] [19:6] Mapping variable_1 has private interface of out but variable_2 also has public interface of out.```

[3.4.6.4.map_variables_child_private_in](../models_1_0/invalid/3.4.6.4.map_variables_child_private_in.cellml): Error detected correctly.
* Expected: ```Mapping variable_2 which has public interface of none```
* Output: ```[Error] [19:6] Mapping variable_2 which has public interface of none.```

[3.4.6.4.map_variables_child_private_out](../models_1_0/invalid/3.4.6.4.map_variables_child_private_out.cellml): Error detected correctly.
* Expected: ```Mapping variable_2 which has public interface of none```
* Output: ```[Error] [19:6] Mapping variable_2 which has public interface of none.```

[3.4.6.4.map_variables_hidden_aunt_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_aunt_1.cellml): Error detected correctly.
* Expected: ```in the hidden set of each other```
* Output:
  * ```[Error] [24:6] Connection of components which are encapsulated in the hidden set of each other.```
  * ```[Error] [25:6] Mapping variable_2 which has private interface of none.```

[3.4.6.4.map_variables_hidden_aunt_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_aunt_2.cellml): Error detected correctly.
* Expected: ```in the hidden set of each other```
* Output:
  * ```[Error] [24:6] Connection of components which are encapsulated in the hidden set of each other.```
  * ```[Error] [25:6] Mapping variable_1 has public interface of out but variable_2 also has private interface of out.```
  * ```[Error] [25:6] Mapping variable_1 which has public interface of none.```
  * ```[Error] [25:6] Mapping variable_2 which has private interface of none.```

[3.4.6.4.map_variables_hidden_cousins_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_1.cellml): Error detected correctly.
* Expected: ```in the hidden set of each other```
* Output:
  * ```[Error] [26:6] Connection of components which are encapsulated in the hidden set of each other.```
  * ```[Error] [27:6] Mapping variable_2 which has private interface of none.```

[3.4.6.4.map_variables_hidden_cousins_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_2.cellml): Error detected correctly.
* Expected: ```in the hidden set of each other```
* Output:
  * ```[Error] [26:6] Connection of components which are encapsulated in the hidden set of each other.```
  * ```[Error] [27:6] Mapping variable_1 has public interface of out but variable_2 also has private interface of out.```
  * ```[Error] [27:6] Mapping variable_1 which has public interface of none.```
  * ```[Error] [27:6] Mapping variable_2 which has private interface of none.```

[3.4.6.4.map_variables_hidden_cousins_3](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_3.cellml): Error detected correctly.
* Expected: ```in the hidden set of each other```
* Output: ```[Error] [26:6] Connection of components which are encapsulated in the hidden set of each other.```

[3.4.6.4.map_variables_hidden_cousins_4](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_4.cellml): Error detected correctly.
* Expected: ```in the hidden set of each other```
* Output:
  * ```[Error] [26:6] Connection of components which are encapsulated in the hidden set of each other.```
  * ```[Error] [27:6] Mapping variable_1 which has public interface of none.```

[3.4.6.4.map_variables_hidden_grandchild_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandchild_1.cellml): Error detected correctly.
* Expected: ```in the hidden set of each other```
* Output:
  * ```[Error] [21:6] Connection of components which are encapsulated in the hidden set of each other.```
  * ```[Error] [22:6] Mapping variable_2 which has private interface of none.```

[3.4.6.4.map_variables_hidden_grandchild_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandchild_2.cellml): Error detected correctly.
* Expected: ```in the hidden set of each other```
* Output:
  * ```[Error] [21:6] Connection of components which are encapsulated in the hidden set of each other.```
  * ```[Error] [22:6] Mapping variable_1 has public interface of out but variable_2 also has private interface of out.```
  * ```[Error] [22:6] Mapping variable_1 which has public interface of none.```
  * ```[Error] [22:6] Mapping variable_2 which has private interface of none.```

[3.4.6.4.map_variables_hidden_grandparent_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandparent_1.cellml): Error detected correctly.
* Expected: ```in the hidden set of each other```
* Output:
  * ```[Error] [21:6] Connection of components which are encapsulated in the hidden set of each other.```
  * ```[Error] [22:6] Mapping variable_2 which has private interface of none.```

[3.4.6.4.map_variables_hidden_grandparent_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandparent_2.cellml): Error detected correctly.
* Expected: ```in the hidden set of each other```
* Output:
  * ```[Error] [21:6] Connection of components which are encapsulated in the hidden set of each other.```
  * ```[Error] [22:6] Mapping variable_1 has public interface of out but variable_2 also has private interface of out.```
  * ```[Error] [22:6] Mapping variable_1 which has public interface of none.```
  * ```[Error] [22:6] Mapping variable_2 which has private interface of none.```

[3.4.6.4.map_variables_hidden_niece_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_niece_1.cellml): Error detected correctly.
* Expected: ```in the hidden set of each other```
* Output:
  * ```[Error] [24:6] Connection of components which are encapsulated in the hidden set of each other.```
  * ```[Error] [25:6] Mapping variable_2 which has private interface of none.```

[3.4.6.4.map_variables_hidden_niece_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_niece_2.cellml): Error detected correctly.
* Expected: ```in the hidden set of each other```
* Output:
  * ```[Error] [24:6] Connection of components which are encapsulated in the hidden set of each other.```
  * ```[Error] [25:6] Mapping variable_1 has public interface of out but variable_2 also has private interface of out.```
  * ```[Error] [25:6] Mapping variable_1 which has public interface of none.```
  * ```[Error] [25:6] Mapping variable_2 which has private interface of none.```

[3.4.6.4.map_variables_nested_sibling_connection](../models_1_0/valid/3.4.6.4.map_variables_nested_sibling_connection.cellml): Valid file passed validation.

[3.4.6.4.map_variables_nested_sibling_private_in](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_in.cellml): Error detected correctly.
* Expected: ```public interface of none```
* Output: ```[Error] [19:6] Mapping variable_2 which has public interface of none.```

[3.4.6.4.map_variables_nested_sibling_private_in_and_out](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_in_and_out.cellml): Error detected correctly.
* Expected: ```also has public interface of out```
* Output:
  * ```[Error] [19:6] Mapping variable_1 has public interface of out but variable_2 also has public interface of out.```
  * ```[Error] [19:6] Mapping variable_1 which has public interface of none.```
  * ```[Error] [19:6] Mapping variable_2 which has public interface of none.```

[3.4.6.4.map_variables_nested_sibling_private_out](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_out.cellml): Error detected correctly.
* Expected: ```public interface of none```
* Output: ```[Error] [19:6] Mapping variable_1 which has public interface of none.```

[3.4.6.4.map_variables_parent_connection_1](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_connection_2](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_in_to_in_1](../models_1_0/invalid/3.4.6.4.map_variables_parent_in_to_in_1.cellml): Error detected correctly.
* Expected: ```also has public interface of in```
* Output: ```[Error] [19:6] Mapping variable_1 has private interface of in but variable_2 also has public interface of in.```

[3.4.6.4.map_variables_parent_in_to_in_2](../models_1_0/invalid/3.4.6.4.map_variables_parent_in_to_in_2.cellml): Error detected correctly.
* Expected: ```also has public interface of in```
* Output: ```[Error] [19:6] Mapping variable_1 has private interface of in but variable_2 also has public interface of in.```

[3.4.6.4.map_variables_parent_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_multiple_out](../models_1_0/invalid/3.4.6.4.map_variables_parent_multiple_out.cellml): Error detected correctly.
* Expected: ```More than one connection to in interface of variable```
* Output: ```[Error] [10:6] More than one connection to in interface of variable.```

[3.4.6.4.map_variables_parent_out_to_out_1](../models_1_0/invalid/3.4.6.4.map_variables_parent_out_to_out_1.cellml): Error detected correctly.
* Expected: ```also has public interface of out```
* Output: ```[Error] [19:6] Mapping variable_1 has private interface of out but variable_2 also has public interface of out.```

[3.4.6.4.map_variables_parent_out_to_out_2](../models_1_0/invalid/3.4.6.4.map_variables_parent_out_to_out_2.cellml): Error detected correctly.
* Expected: ```also has public interface of out```
* Output: ```[Error] [19:6] Mapping variable_1 has private interface of out but variable_2 also has public interface of out.```

[3.4.6.4.map_variables_parent_public_in](../models_1_0/invalid/3.4.6.4.map_variables_parent_public_in.cellml): Error detected correctly.
* Expected: ```has private interface of none```
* Output: ```[Error] [19:6] Mapping variable_1 which has private interface of none.```

[3.4.6.4.map_variables_parent_public_out](../models_1_0/invalid/3.4.6.4.map_variables_parent_public_out.cellml): Error detected correctly.
* Expected: ```has private interface of none```
* Output: ```[Error] [19:6] Mapping variable_1 which has private interface of none.```

[3.4.6.4.map_variables_sibling_connection_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_connection_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_connection_3](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_3.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_in_to_in](../models_1_0/invalid/3.4.6.4.map_variables_sibling_in_to_in.cellml): Error detected correctly.
* Expected: ```also has public interface of in```
* Output: ```[Error] [11:6] Mapping variable_1 has public interface of in but variable_2 also has public interface of in.```

[3.4.6.4.map_variables_sibling_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_multiple_out_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_multiple_out_1.cellml): Error detected correctly.
* Expected: ```More than one connection to in interface of variable```
* Output: ```[Error] [8:6] More than one connection to in interface of variable.```

[3.4.6.4.map_variables_sibling_multiple_out_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_multiple_out_2.cellml): Error detected correctly.
* Expected: ```More than one connection to in interface of variable```
* Output: ```[Error] [10:6] More than one connection to in interface of variable.```

[3.4.6.4.map_variables_sibling_mutual](../models_1_0/valid/3.4.6.4.map_variables_sibling_mutual.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_out_to_out](../models_1_0/invalid/3.4.6.4.map_variables_sibling_out_to_out.cellml): Error detected correctly.
* Expected: ```also has public interface of out```
* Output: ```[Error] [11:6] Mapping variable_1 has public interface of out but variable_2 also has public interface of out.```

[3.4.6.4.map_variables_sibling_private_in_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_1.cellml): Error detected correctly.
* Expected: ```public interface of none```
* Output: ```[Error] [11:6] Mapping variable_1 which has public interface of none.```

[3.4.6.4.map_variables_sibling_private_in_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_2.cellml): Error detected correctly.
* Expected: ```also has public interface of out```
* Output: ```[Error] [11:6] Mapping variable_1 has public interface of out but variable_2 also has public interface of out.```

[3.4.6.4.map_variables_sibling_private_in_and_out](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_and_out.cellml): Error detected correctly.
* Expected: ```public interface of none```
* Output:
  * ```[Error] [11:6] Mapping variable_1 has public interface of out but variable_2 also has public interface of out.```
  * ```[Error] [11:6] Mapping variable_1 which has public interface of none.```
  * ```[Error] [11:6] Mapping variable_2 which has public interface of none.```

[3.4.6.4.map_variables_sibling_private_out_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_out_1.cellml): Error detected correctly.
* Expected: ```public interface of none```
* Output: ```[Error] [11:6] Mapping variable_2 which has public interface of none.```

[3.4.6.4.map_variables_sibling_private_out_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_out_2.cellml): Error detected correctly.
* Expected: ```also has public interface of in```
* Output: ```[Error] [11:6] Mapping variable_1 has public interface of in but variable_2 also has public interface of in.```

[3.4.6.4.map_variables_talking_aunt](../models_1_0/valid/3.4.6.4.map_variables_talking_aunt.cellml): Valid file passed validation.

[3.4.6.4.map_variables_talking_cousins](../models_1_0/valid/3.4.6.4.map_variables_talking_cousins.cellml): Valid file passed validation.

[3.4.6.4.map_variables_talking_niece](../models_1_0/valid/3.4.6.4.map_variables_talking_niece.cellml): Valid file passed validation.


---

## 4. Mathematics

### 4.2

[4.2.3_1.mathml_basics](../models_1_0/valid/4.2.3_1.mathml_basics.cellml): Valid file passed validation.

[4.2.3_2.1.mathml_numbers_real](../models_1_0/numbers/4.2.3_2.1.mathml_numbers_real.cellml): Valid file passed validation.

[4.2.3_2.2.mathml_numbers_integer](../models_1_0/numbers/4.2.3_2.2.mathml_numbers_integer.cellml): Valid file passed validation.

🔴 [4.2.3_2.3.mathml_numbers_real_base](../models_1_0/numbers/4.2.3_2.3.mathml_numbers_real_base.cellml): **Valid file failed validation.**
* Output: ```[Error] [22:10] MathML cn element contains an invalid constant representation.```

🔴 [4.2.3_2.4.mathml_numbers_integer_base](../models_1_0/numbers/4.2.3_2.4.mathml_numbers_integer_base.cellml): **Valid file failed validation.**
* Output: ```[Error] [22:10] MathML cn element contains an invalid constant representation.```

[4.2.3_2.5.mathml_numbers_e_notation](../models_1_0/numbers/4.2.3_2.5.mathml_numbers_e_notation.cellml): Valid file passed validation.

🔴 [4.2.3_2.6.mathml_numbers_rational](../models_1_0/numbers/4.2.3_2.6.mathml_numbers_rational.cellml): **Valid file failed validation.**
* Output: ```[Error] [10:10] MathML cn elements without the attribute type=e-notation shouldn't have element children.```

[4.2.3_3.1_mathml_arithmetic_binary](../models_1_0/valid/4.2.3_3.1_mathml_arithmetic_binary.cellml): Valid file passed validation.

[4.2.3_3.2_mathml_arithmetic_n_ary](../models_1_0/valid/4.2.3_3.2_mathml_arithmetic_n_ary.cellml): Valid file passed validation.

[4.2.3_3.2_mathml_arithmetic_unary](../models_1_0/valid/4.2.3_3.2_mathml_arithmetic_unary.cellml): Valid file passed validation.

[4.2.3_4.1_mathml_functions_basic](../models_1_0/valid/4.2.3_4.1_mathml_functions_basic.cellml): Valid file passed validation.

[4.2.3_4.2_mathml_functions_non_smooth](../models_1_0/valid/4.2.3_4.2_mathml_functions_non_smooth.cellml): Valid file passed validation.

[4.2.3_4.3_mathml_functions_factorial](../models_1_0/valid/4.2.3_4.3_mathml_functions_factorial.cellml): Valid file passed validation.

[4.2.3_4.4_mathml_functions_trig](../models_1_0/valid/4.2.3_4.4_mathml_functions_trig.cellml): Valid file passed validation.

[4.2.3_4.5_mathml_functions_trig_hyperbolic](../models_1_0/valid/4.2.3_4.5_mathml_functions_trig_hyperbolic.cellml): Valid file passed validation.

[4.2.3_4.6_mathml_functions_trig_redundant](../models_1_0/valid/4.2.3_4.6_mathml_functions_trig_redundant.cellml): Valid file passed validation.

[4.2.3_4.7_mathml_functions_trig_redundant_hyperbolic](../models_1_0/valid/4.2.3_4.7_mathml_functions_trig_redundant_hyperbolic.cellml): Valid file passed validation.

[4.2.3_5.1_mathml_derivatives](../models_1_0/valid/4.2.3_5.1_mathml_derivatives.cellml): Valid file passed validation.

[4.2.3_5.2_mathml_derivatives_degree](../models_1_0/valid/4.2.3_5.2_mathml_derivatives_degree.cellml): Valid file passed validation.

[4.2.3_5.3_mathml_derivatives_with_units](../models_1_0/valid/4.2.3_5.3_mathml_derivatives_with_units.cellml): Valid file passed validation.

[4.2.3_5.4_mathml_derivatives_with_units_degree](../models_1_0/valid/4.2.3_5.4_mathml_derivatives_with_units_degree.cellml): Valid file passed validation.

[4.2.3_6.1_mathml_logic_one_piece](../models_1_0/valid/4.2.3_6.1_mathml_logic_one_piece.cellml): Valid file passed validation.

[4.2.3_6.2_mathml_logic_two_pieces](../models_1_0/valid/4.2.3_6.2_mathml_logic_two_pieces.cellml): Valid file passed validation.

[4.2.3_6.3_mathml_logic_no_otherwise](../models_1_0/valid/4.2.3_6.3_mathml_logic_no_otherwise.cellml): Valid file passed validation.

[4.2.3_6.4_mathml_logic_comparisons](../models_1_0/valid/4.2.3_6.4_mathml_logic_comparisons.cellml): Valid file passed validation.

[4.2.3_6.5_mathml_logic_unary_operators](../models_1_0/valid/4.2.3_6.5_mathml_logic_unary_operators.cellml): Valid file passed validation.

[4.2.3_6.6_mathml_logic_binary_operators](../models_1_0/valid/4.2.3_6.6_mathml_logic_binary_operators.cellml): Valid file passed validation.

[4.2.3_6.7_mathml_logic_constants](../models_1_0/valid/4.2.3_6.7_mathml_logic_constants.cellml): Valid file passed validation.

[4.2.3_7.1_mathml_pi](../models_1_0/valid/4.2.3_7.1_mathml_pi.cellml): Valid file passed validation.

[4.2.3_7.2_mathml_e](../models_1_0/valid/4.2.3_7.2_mathml_e.cellml): Valid file passed validation.

[4.2.3_7.3_mathml_nan_inf](../models_1_0/valid/4.2.3_7.3_mathml_nan_inf.cellml): Valid file passed validation.

🔴 [4.2.3_8.1_annotation](../models_1_0/valid/4.2.3_8.1_annotation.cellml): **Valid file failed validation.**
* Output:
  * ```[Error] [7:8] Text should not be present directly inside a MathML semantics element.```
  * ```[Error] [12:17] Text should not be present directly inside a MathML semantics element.```
  * ```[Error] [15:22] Text should not be present directly inside a MathML semantics element.```

🔴 [4.2.3_8.2_annotation_xml](../models_1_0/valid/4.2.3_8.2_annotation_xml.cellml): **Valid file failed validation.**
* Output:
  * ```[Error] [19:8] Text should not be present directly inside a MathML semantics element.```
  * ```[Error] [55:17] Text should not be present directly inside a MathML semantics element.```
  * ```[Error] [85:26] Text should not be present directly inside a MathML semantics element.```


---

#### 4.4.1

[4.4.1.math_not_math_component](../models_1_0/invalid/4.4.1.math_not_math_component.cellml): Error detected correctly.
* Expected: ```cake was not expected in this context```
* Output: ```[Error] [9:10] MathML element cake was not expected in this context.```

🔵 [4.4.1.math_not_math_reaction](../models_1_0/invalid/4.4.1.math_not_math_reaction.cellml): **Error not detected.**


---

#### 4.4.2

[4.4.2.ci_no_whitespace](../models_1_0/valid/4.4.2.ci_no_whitespace.cellml): Valid file passed validation.

[4.4.2.ci_non_local_aunt](../models_1_0/invalid/4.4.2.ci_non_local_aunt.cellml): Error detected correctly.
* Expected: ```ci element references variable which doesn't exist```
* Output: ```[Error] [13:12] MathML ci element references variable which doesn't exist.```

[4.4.2.ci_non_local_child](../models_1_0/invalid/4.4.2.ci_non_local_child.cellml): Error detected correctly.
* Expected: ```ci element references variable which doesn't exist```
* Output: ```[Error] [12:12] MathML ci element references variable which doesn't exist.```

[4.4.2.ci_non_local_cousin](../models_1_0/invalid/4.4.2.ci_non_local_cousin.cellml): Error detected correctly.
* Expected: ```ci element references variable which doesn't exist```
* Output: ```[Error] [13:12] MathML ci element references variable which doesn't exist.```

[4.4.2.ci_non_local_nested_sibling](../models_1_0/invalid/4.4.2.ci_non_local_nested_sibling.cellml): Error detected correctly.
* Expected: ```ci element references variable which doesn't exist```
* Output: ```[Error] [13:12] MathML ci element references variable which doesn't exist.```

[4.4.2.ci_non_local_niece](../models_1_0/invalid/4.4.2.ci_non_local_niece.cellml): Error detected correctly.
* Expected: ```ci element references variable which doesn't exist```
* Output: ```[Error] [16:12] MathML ci element references variable which doesn't exist.```

[4.4.2.ci_non_local_parent](../models_1_0/invalid/4.4.2.ci_non_local_parent.cellml): Error detected correctly.
* Expected: ```ci element references variable which doesn't exist```
* Output: ```[Error] [15:12] MathML ci element references variable which doesn't exist.```

[4.4.2.ci_non_local_sibling](../models_1_0/invalid/4.4.2.ci_non_local_sibling.cellml): Error detected correctly.
* Expected: ```ci element references variable which doesn't exist```
* Output: ```[Error] [15:12] MathML ci element references variable which doesn't exist.```

[4.4.2.ci_nonexistent](../models_1_0/invalid/4.4.2.ci_nonexistent.cellml): Error detected correctly.
* Expected: ```ci element references variable which doesn't exist```
* Output: ```[Error] [12:12] MathML ci element references variable which doesn't exist.```

[4.4.2.ci_whitespace_1](../models_1_0/valid/4.4.2.ci_whitespace_1.cellml): Valid file passed validation.

[4.4.2.ci_whitespace_2](../models_1_0/valid/4.4.2.ci_whitespace_2.cellml): Valid file passed validation.

[4.4.2.ci_whitespace_3](../models_1_0/valid/4.4.2.ci_whitespace_3.cellml): Valid file passed validation.


---

##### 4.4.3.1

[4.4.3.1.cn_component_units](../models_1_0/valid/4.4.3.1.cn_component_units.cellml): Valid file passed validation.

[4.4.3.1.cn_model_units](../models_1_0/valid/4.4.3.1.cn_model_units.cellml): Valid file passed validation.

[4.4.3.1.cn_predefined_units](../models_1_0/valid/4.4.3.1.cn_predefined_units.cellml): Valid file passed validation.

[4.4.3.1.cn_units_missing](../models_1_0/invalid/4.4.3.1.cn_units_missing.cellml): Error detected correctly.
* Expected: ```MathML cn elements must have CellML units attribute```
* Output: ```[Error] [9:10] MathML cn elements must have CellML units attribute.```


---

##### 4.4.3.2

[4.4.3.2.cn_units_nonexistent_1](../models_1_0/invalid/4.4.3.2.cn_units_nonexistent_1.cellml): Error detected correctly.
* Expected: ```MathML cn element has invalid units```
* Output: ```[Error] [11:12] MathML cn element has invalid units.```

[4.4.3.2.cn_units_nonexistent_2](../models_1_0/invalid/4.4.3.2.cn_units_nonexistent_2.cellml): Error detected correctly.
* Expected: ```MathML cn element has invalid units```
* Output: ```[Error] [13:12] MathML cn element has invalid units.```

[4.4.3.2.cn_units_parent_component](../models_1_0/invalid/4.4.3.2.cn_units_parent_component.cellml): Error detected correctly.
* Expected: ```MathML cn element has invalid units```
* Output: ```[Error] [17:12] MathML cn element has invalid units.```


---

#### 4.4.4

[4.4.4.modify_nonexistent](../models_1_0/invalid/4.4.4.modify_nonexistent.cellml): Error detected correctly.
* Expected: ```ci element references variable which doesn't exist```
* Output: ```[Error] [7:10] MathML ci element references variable which doesn't exist.```

🔵 [4.4.4.modify_private_in](../models_1_0/invalid/4.4.4.modify_private_in.cellml): **Error not detected.**

[4.4.4.modify_private_out](../models_1_0/valid/4.4.4.modify_private_out.cellml): Valid file passed validation.

🔵 [4.4.4.modify_public_in](../models_1_0/invalid/4.4.4.modify_public_in.cellml): **Error not detected.**

[4.4.4.modify_public_out](../models_1_0/valid/4.4.4.modify_public_out.cellml): Valid file passed validation.


---

#### 4.5.1

[4.5.1.ordering_not_significant](../models_1_0/valid/4.5.1.ordering_not_significant.cellml): Valid file passed validation.


---

[4.algebraic_model](../models_1_0/valid/4.algebraic_model.cellml): Valid file passed validation.

[4.algebraic_ode_model](../models_1_0/valid/4.algebraic_ode_model.cellml): Valid file passed validation.

🔵 [4.math_and_initial_value](../models_1_0/invalid/4.math_and_initial_value.cellml): **Error not detected.**

🔵 [4.math_overdefined](../models_1_0/invalid/4.math_overdefined.cellml): **Error not detected.**


---

## 5. Units

#### 5.2.2

🔶 [5.2.2.unit_deca](../models_1_0/unit_deca/5.2.2.unit_deca.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output:
  * ```terminate called after throwing an instance of 'iface::cellml_api::CellMLException'```
  * ```  what():  std::exception```


---

#### 5.2.7

[5.2.7.unit_checking_arithmetic](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_arithmetic.cellml): Valid file passed validation.

[5.2.7.unit_checking_comparisons](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_comparisons.cellml): Valid file passed validation.

[5.2.7.unit_checking_derivatives](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_derivatives.cellml): Valid file passed validation.

[5.2.7.unit_checking_derivatives_degree](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_derivatives_degree.cellml): Valid file passed validation.

[5.2.7.unit_checking_dimensionless](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_dimensionless.cellml): Valid file passed validation.

[5.2.7.unit_checking_functions_factorial](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_functions_factorial.cellml): Valid file passed validation.

[5.2.7.unit_checking_functions_non_smooth](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_functions_non_smooth.cellml): Valid file passed validation.

[5.2.7.unit_checking_functions_power_and_root](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_functions_power_and_root.cellml): Valid file passed validation.

[5.2.7.unit_checking_internal_mismatch_1](../models_1_0/unit_checking_inconsistent/5.2.7.unit_checking_internal_mismatch_1.cellml): Valid file passed validation.

[5.2.7.unit_checking_internal_mismatch_2](../models_1_0/unit_checking_inconsistent/5.2.7.unit_checking_internal_mismatch_2.cellml): Valid file passed validation.

[5.2.7.unit_checking_internal_mismatch_3](../models_1_0/unit_checking_inconsistent/5.2.7.unit_checking_internal_mismatch_3.cellml): Valid file passed validation.

[5.2.7.unit_checking_internal_mismatch_4](../models_1_0/unit_checking_inconsistent/5.2.7.unit_checking_internal_mismatch_4.cellml): Valid file passed validation.

[5.2.7.unit_checking_name_differs](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_name_differs.cellml): Valid file passed validation.

[5.2.7.unit_checking_piecewise](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_piecewise.cellml): Valid file passed validation.

[5.2.7.unit_checking_piecewise_multi_unit](../models_1_0/unit_checking_inconsistent/5.2.7.unit_checking_piecewise_multi_unit.cellml): Valid file passed validation.

[5.2.7.unit_checking_repeated_unit](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_repeated_unit.cellml): Valid file passed validation.

[5.2.7.unit_conversion_different_names_same_unit](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_different_names_same_unit.cellml): Valid file passed validation.

[5.2.7.unit_conversion_dimensionless_exponent](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_dimensionless_exponent.cellml): Valid file passed validation.

[5.2.7.unit_conversion_dimensionless_multiplier_1](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_dimensionless_multiplier_1.cellml): Valid file passed validation.

🔴 [5.2.7.unit_conversion_dimensionless_multiplier_2](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_dimensionless_multiplier_2.cellml): **Valid file failed validation.**
* Output: ```[Error] [21:6] Connection of two variables which have dimensionally inconsistent units.```

[5.2.7.unit_conversion_dimensionless_offset](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_dimensionless_offset.cellml): Valid file passed validation.

🔴 [5.2.7.unit_conversion_inconvertible_1](../models_1_0/unit_conversion_inconvertible/5.2.7.unit_conversion_inconvertible_1.cellml): **Valid file failed validation.**
* Output: ```[Error] [11:6] Connection of two variables which have dimensionally inconsistent units.```

🔴 [5.2.7.unit_conversion_less_obvious](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_less_obvious.cellml): **Valid file failed validation.**
* Output: ```[Error] [21:6] Connection of two variables which have dimensionally inconsistent units.```

🔴 [5.2.7.unit_conversion_multiplier](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_multiplier.cellml): **Valid file failed validation.**
* Output: ```[Error] [14:6] Connection of two variables which have dimensionally inconsistent units.```

🔴 [5.2.7.unit_conversion_new_base_units](../models_1_0/unit_conversion_inconvertible/5.2.7.unit_conversion_new_base_units.cellml): **Valid file failed validation.**
* Output: ```[Error] [12:6] Connection of two variables which have dimensionally inconsistent units.```

🔴 [5.2.7.unit_conversion_offset](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_offset.cellml): **Valid file failed validation.**
* Output: ```[Error] [23:6] Connection of two variables which have dimensionally inconsistent units.```

🔴 [5.2.7.unit_conversion_prefix](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_prefix.cellml): **Valid file failed validation.**
* Output: ```[Error] [17:6] Connection of two variables which have dimensionally inconsistent units.```


---

##### 5.4.1.1

[5.4.1.1.units_base_units](../models_1_0/valid/5.4.1.1.units_base_units.cellml): Valid file passed validation.

🔵 [5.4.1.1.units_base_units_with_children](../models_1_0/invalid/5.4.1.1.units_base_units_with_children.cellml): **Error not detected.**

[5.4.1.1.units_empty_1](../models_1_0/valid/5.4.1.1.units_empty_1.cellml): Valid file passed validation.

[5.4.1.1.units_empty_2](../models_1_0/valid/5.4.1.1.units_empty_2.cellml): Valid file passed validation.

[5.4.1.1.units_name_missing](../models_1_0/invalid/5.4.1.1.units_name_missing.cellml): Error detected correctly.
* Expected: ```the name attribute is required here```
* Output: ```[Error] [3:4] The CellML specification says the name attribute is required here.```

[5.4.1.1.units_with_component](../models_1_0/invalid/5.4.1.1.units_with_component.cellml): Error detected correctly.
* Expected: ```Unexpected element component```
* Output: ```[Error] [5:6] Unexpected element component found - not valid here.```

[5.4.1.1.units_with_component_ref](../models_1_0/invalid/5.4.1.1.units_with_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element component_ref```
* Output: ```[Error] [5:6] Unexpected element component_ref found - not valid here.```

[5.4.1.1.units_with_connection](../models_1_0/invalid/5.4.1.1.units_with_connection.cellml): Error detected correctly.
* Expected: ```Unexpected element connection```
* Output: ```[Error] [11:6] Unexpected element connection found - not valid here.```

[5.4.1.1.units_with_group](../models_1_0/invalid/5.4.1.1.units_with_group.cellml): Error detected correctly.
* Expected: ```Unexpected element group```
* Output: ```[Error] [5:6] Unexpected element group found - not valid here.```

[5.4.1.1.units_with_map_components](../models_1_0/invalid/5.4.1.1.units_with_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected element map_components```
* Output: ```[Error] [5:6] Unexpected element map_components found - not valid here.```

[5.4.1.1.units_with_map_variables](../models_1_0/invalid/5.4.1.1.units_with_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected element map_variables```
* Output: ```[Error] [5:6] Unexpected element map_variables found - not valid here.```

[5.4.1.1.units_with_math](../models_1_0/invalid/5.4.1.1.units_with_math.cellml): Error detected correctly.
* Expected: ```Unexpected element math```
* Output: ```[Error] [7:8] Unexpected element math found - not valid here.```

[5.4.1.1.units_with_model](../models_1_0/invalid/5.4.1.1.units_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [5:6] Unexpected element model found - not valid here.```

[5.4.1.1.units_with_reaction](../models_1_0/invalid/5.4.1.1.units_with_reaction.cellml): Error detected correctly.
* Expected: ```Unexpected element reaction```
* Output: ```[Error] [6:8] Unexpected element reaction found - not valid here.```

[5.4.1.1.units_with_relationship_ref](../models_1_0/invalid/5.4.1.1.units_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element relationship_ref```
* Output: ```[Error] [5:6] Unexpected element relationship_ref found - not valid here.```

[5.4.1.1.units_with_role](../models_1_0/invalid/5.4.1.1.units_with_role.cellml): Error detected correctly.
* Expected: ```Unexpected element role```
* Output: ```[Error] [5:6] Unexpected element role found - not valid here.```

[5.4.1.1.units_with_unit_children](../models_1_0/valid/5.4.1.1.units_with_unit_children.cellml): Valid file passed validation.

[5.4.1.1.units_with_units](../models_1_0/invalid/5.4.1.1.units_with_units.cellml): Error detected correctly.
* Expected: ```Unexpected element units```
* Output: ```[Error] [5:6] Unexpected element units found - not valid here.```

[5.4.1.1.units_with_variable](../models_1_0/invalid/5.4.1.1.units_with_variable.cellml): Error detected correctly.
* Expected: ```Unexpected element variable```
* Output: ```[Error] [6:8] Unexpected element variable found - not valid here.```

[5.4.1.1.units_with_variable_ref](../models_1_0/invalid/5.4.1.1.units_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element variable_ref```
* Output: ```[Error] [7:8] Unexpected element variable_ref found - not valid here.```


---

##### 5.4.1.2

[5.4.1.2.units_name_duplicate_1](../models_1_0/invalid/5.4.1.2.units_name_duplicate_1.cellml): Error detected correctly.
* Expected: ```More than one units in the model named```
* Output: ```[Error] [6:4] More than one units in the model named wooster.```

[5.4.1.2.units_name_duplicate_2](../models_1_0/invalid/5.4.1.2.units_name_duplicate_2.cellml): Error detected correctly.
* Expected: ```More than one units in the component named```
* Output: ```[Error] [7:6] More than one units in the component named wooster.```

[5.4.1.2.units_name_invalid](../models_1_0/invalid/5.4.1.2.units_name_invalid.cellml): Error detected correctly.
* Expected: ```A valid CellML identifier must contain at least one letter```
* Output: ```[Error] [3:9] A valid CellML identifier must contain at least one letter (section 2.4.1).```

[5.4.1.2.units_name_predefined_ampere](../models_1_0/invalid/5.4.1.2.units_name_predefined_ampere.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name ampere```
* Output: ```[Error] [3:4] Units in the model uses reserved name ampere.```

[5.4.1.2.units_name_predefined_becquerel](../models_1_0/invalid/5.4.1.2.units_name_predefined_becquerel.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name becquerel```
* Output: ```[Error] [3:4] Units in the model uses reserved name becquerel.```

[5.4.1.2.units_name_predefined_candela](../models_1_0/invalid/5.4.1.2.units_name_predefined_candela.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name candela```
* Output: ```[Error] [3:4] Units in the model uses reserved name candela.```

[5.4.1.2.units_name_predefined_celsius](../models_1_0/invalid/5.4.1.2.units_name_predefined_celsius.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name celsius```
* Output: ```[Error] [3:4] Units in the model uses reserved name celsius.```

[5.4.1.2.units_name_predefined_component_ampere](../models_1_0/invalid/5.4.1.2.units_name_predefined_component_ampere.cellml): Error detected correctly.
* Expected: ```Units in the component uses reserved name ampere```
* Output: ```[Error] [4:6] Units in the component uses reserved name ampere.```

[5.4.1.2.units_name_predefined_coulomb](../models_1_0/invalid/5.4.1.2.units_name_predefined_coulomb.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name coulomb```
* Output: ```[Error] [3:4] Units in the model uses reserved name coulomb.```

[5.4.1.2.units_name_predefined_dimensionless](../models_1_0/invalid/5.4.1.2.units_name_predefined_dimensionless.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name dimensionless```
* Output: ```[Error] [3:4] Units in the model uses reserved name dimensionless.```

[5.4.1.2.units_name_predefined_farad](../models_1_0/invalid/5.4.1.2.units_name_predefined_farad.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name farad```
* Output: ```[Error] [3:4] Units in the model uses reserved name farad.```

[5.4.1.2.units_name_predefined_gram](../models_1_0/invalid/5.4.1.2.units_name_predefined_gram.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name gram```
* Output: ```[Error] [3:4] Units in the model uses reserved name gram.```

[5.4.1.2.units_name_predefined_gray](../models_1_0/invalid/5.4.1.2.units_name_predefined_gray.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name gray```
* Output: ```[Error] [3:4] Units in the model uses reserved name gray.```

[5.4.1.2.units_name_predefined_henry](../models_1_0/invalid/5.4.1.2.units_name_predefined_henry.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name henry```
* Output: ```[Error] [3:4] Units in the model uses reserved name henry.```

[5.4.1.2.units_name_predefined_hertz](../models_1_0/invalid/5.4.1.2.units_name_predefined_hertz.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name hertz```
* Output: ```[Error] [3:4] Units in the model uses reserved name hertz.```

[5.4.1.2.units_name_predefined_joule](../models_1_0/invalid/5.4.1.2.units_name_predefined_joule.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name joule```
* Output: ```[Error] [3:4] Units in the model uses reserved name joule.```

[5.4.1.2.units_name_predefined_katal](../models_1_0/invalid/5.4.1.2.units_name_predefined_katal.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name katal```
* Output: ```[Error] [3:4] Units in the model uses reserved name katal.```

[5.4.1.2.units_name_predefined_kelvin](../models_1_0/invalid/5.4.1.2.units_name_predefined_kelvin.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name kelvin```
* Output: ```[Error] [3:4] Units in the model uses reserved name kelvin.```

[5.4.1.2.units_name_predefined_kilogram](../models_1_0/invalid/5.4.1.2.units_name_predefined_kilogram.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name kilogram```
* Output: ```[Error] [3:4] Units in the model uses reserved name kilogram.```

[5.4.1.2.units_name_predefined_liter](../models_1_0/invalid/5.4.1.2.units_name_predefined_liter.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name liter```
* Output: ```[Error] [3:4] Units in the model uses reserved name liter.```

[5.4.1.2.units_name_predefined_litre](../models_1_0/invalid/5.4.1.2.units_name_predefined_litre.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name litre```
* Output: ```[Error] [3:4] Units in the model uses reserved name litre.```

[5.4.1.2.units_name_predefined_lumen](../models_1_0/invalid/5.4.1.2.units_name_predefined_lumen.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name lumen```
* Output: ```[Error] [3:4] Units in the model uses reserved name lumen.```

[5.4.1.2.units_name_predefined_lux](../models_1_0/invalid/5.4.1.2.units_name_predefined_lux.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name lux```
* Output: ```[Error] [3:4] Units in the model uses reserved name lux.```

[5.4.1.2.units_name_predefined_meter](../models_1_0/invalid/5.4.1.2.units_name_predefined_meter.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name meter```
* Output: ```[Error] [3:4] Units in the model uses reserved name meter.```

[5.4.1.2.units_name_predefined_metre](../models_1_0/invalid/5.4.1.2.units_name_predefined_metre.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name metre```
* Output: ```[Error] [3:4] Units in the model uses reserved name metre.```

[5.4.1.2.units_name_predefined_mole](../models_1_0/invalid/5.4.1.2.units_name_predefined_mole.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name mole```
* Output: ```[Error] [3:4] Units in the model uses reserved name mole.```

[5.4.1.2.units_name_predefined_newton](../models_1_0/invalid/5.4.1.2.units_name_predefined_newton.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name newton```
* Output: ```[Error] [3:4] Units in the model uses reserved name newton.```

[5.4.1.2.units_name_predefined_ohm](../models_1_0/invalid/5.4.1.2.units_name_predefined_ohm.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name ohm```
* Output: ```[Error] [3:4] Units in the model uses reserved name ohm.```

[5.4.1.2.units_name_predefined_pascal](../models_1_0/invalid/5.4.1.2.units_name_predefined_pascal.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name pascal```
* Output: ```[Error] [3:4] Units in the model uses reserved name pascal.```

[5.4.1.2.units_name_predefined_radian](../models_1_0/invalid/5.4.1.2.units_name_predefined_radian.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name radian```
* Output: ```[Error] [3:4] Units in the model uses reserved name radian.```

[5.4.1.2.units_name_predefined_second](../models_1_0/invalid/5.4.1.2.units_name_predefined_second.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name second```
* Output: ```[Error] [3:4] Units in the model uses reserved name second.```

[5.4.1.2.units_name_predefined_siemens](../models_1_0/invalid/5.4.1.2.units_name_predefined_siemens.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name siemens```
* Output: ```[Error] [3:4] Units in the model uses reserved name siemens.```

[5.4.1.2.units_name_predefined_sievert](../models_1_0/invalid/5.4.1.2.units_name_predefined_sievert.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name sievert```
* Output: ```[Error] [3:4] Units in the model uses reserved name sievert.```

[5.4.1.2.units_name_predefined_steradian](../models_1_0/invalid/5.4.1.2.units_name_predefined_steradian.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name steradian```
* Output: ```[Error] [3:4] Units in the model uses reserved name steradian.```

[5.4.1.2.units_name_predefined_tesla](../models_1_0/invalid/5.4.1.2.units_name_predefined_tesla.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name tesla```
* Output: ```[Error] [3:4] Units in the model uses reserved name tesla.```

[5.4.1.2.units_name_predefined_volt](../models_1_0/invalid/5.4.1.2.units_name_predefined_volt.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name volt```
* Output: ```[Error] [3:4] Units in the model uses reserved name volt.```

[5.4.1.2.units_name_predefined_watt](../models_1_0/invalid/5.4.1.2.units_name_predefined_watt.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name watt```
* Output: ```[Error] [3:4] Units in the model uses reserved name watt.```

[5.4.1.2.units_name_predefined_weber](../models_1_0/invalid/5.4.1.2.units_name_predefined_weber.cellml): Error detected correctly.
* Expected: ```Units in the model uses reserved name weber```
* Output: ```[Error] [3:4] Units in the model uses reserved name weber.```

[5.4.1.2.units_names_and_other_names](../models_1_0/valid/5.4.1.2.units_names_and_other_names.cellml): Valid file passed validation.

[5.4.1.2.units_shadowing_1](../models_1_0/valid/5.4.1.2.units_shadowing_1.cellml): Valid file passed validation.

[5.4.1.2.units_shadowing_2](../models_1_0/valid/5.4.1.2.units_shadowing_2.cellml): Valid file passed validation.


---

##### 5.4.1.3

[5.4.1.3.units_base_units_invalid](../models_1_0/invalid/5.4.1.3.units_base_units_invalid.cellml): Error detected correctly.
* Expected: ```the value of the base_units attribute MUST be```
* Output: ```[Error] [3:15] If present, the value of the base_units attribute MUST be "yes" or "no" (section 5.4.1.3).```


---

##### 5.4.2.1

[5.4.2.1.unit_offset_non_zero](../models_1_0/valid/5.4.2.1.unit_offset_non_zero.cellml): Valid file passed validation.

[5.4.2.1.unit_offset_zero](../models_1_0/valid/5.4.2.1.unit_offset_zero.cellml): Valid file passed validation.

[5.4.2.1.unit_prefix_exponent_multiplier](../models_1_0/valid/5.4.2.1.unit_prefix_exponent_multiplier.cellml): Valid file passed validation.

[5.4.2.1.unit_prefix_exponent_multiplier_huge](../models_1_0/valid/5.4.2.1.unit_prefix_exponent_multiplier_huge.cellml): Valid file passed validation.

[5.4.2.1.unit_units_missing](../models_1_0/invalid/5.4.2.1.unit_units_missing.cellml): Error detected correctly.
* Expected: ```MUST define a units attribute```
* Output:
  * ```[Error] [2:143] Found a unit with no units attribute in units wooster; .```
  * ```[Warning] [2:143] Cannot perform any further checking of unit names due to problems processing the model units.```
  * ```[Error] [4:6] Each  /  element MUST define a units attribute (section 3.4.3.1 / 5.4.3.1).```

[5.4.2.1.unit_with_component](../models_1_0/invalid/5.4.2.1.unit_with_component.cellml): Error detected correctly.
* Expected: ```Unexpected element component```
* Output: ```[Error] [5:8] Unexpected element component found - not valid here.```

[5.4.2.1.unit_with_component_ref](../models_1_0/invalid/5.4.2.1.unit_with_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element component_ref```
* Output: ```[Error] [5:8] Unexpected element component_ref found - not valid here.```

[5.4.2.1.unit_with_connection](../models_1_0/invalid/5.4.2.1.unit_with_connection.cellml): Error detected correctly.
* Expected: ```Unexpected element connection```
* Output: ```[Error] [5:8] Unexpected element connection found - not valid here.```

[5.4.2.1.unit_with_group](../models_1_0/invalid/5.4.2.1.unit_with_group.cellml): Error detected correctly.
* Expected: ```Unexpected element group```
* Output: ```[Error] [5:8] Unexpected element group found - not valid here.```

[5.4.2.1.unit_with_map_components](../models_1_0/invalid/5.4.2.1.unit_with_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected element map_components```
* Output: ```[Error] [5:8] Unexpected element map_components found - not valid here.```

[5.4.2.1.unit_with_map_variables](../models_1_0/invalid/5.4.2.1.unit_with_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected element map_variables```
* Output: ```[Error] [5:8] Unexpected element map_variables found - not valid here.```

[5.4.2.1.unit_with_math](../models_1_0/invalid/5.4.2.1.unit_with_math.cellml): Error detected correctly.
* Expected: ```Unexpected element math```
* Output: ```[Error] [5:8] Unexpected element math found - not valid here.```

[5.4.2.1.unit_with_model](../models_1_0/invalid/5.4.2.1.unit_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [5:8] Unexpected element model found - not valid here.```

[5.4.2.1.unit_with_reaction](../models_1_0/invalid/5.4.2.1.unit_with_reaction.cellml): Error detected correctly.
* Expected: ```Unexpected element reaction```
* Output: ```[Error] [7:10] Unexpected element reaction found - not valid here.```

[5.4.2.1.unit_with_relationship_ref](../models_1_0/invalid/5.4.2.1.unit_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element relationship_ref```
* Output: ```[Error] [5:8] Unexpected element relationship_ref found - not valid here.```

[5.4.2.1.unit_with_role](../models_1_0/invalid/5.4.2.1.unit_with_role.cellml): Error detected correctly.
* Expected: ```Unexpected element role```
* Output: ```[Error] [5:8] Unexpected element role found - not valid here.```

[5.4.2.1.unit_with_unit](../models_1_0/invalid/5.4.2.1.unit_with_unit.cellml): Error detected correctly.
* Expected: ```Unexpected element unit```
* Output: ```[Error] [5:8] Unexpected element unit found - not valid here.```

[5.4.2.1.unit_with_units](../models_1_0/invalid/5.4.2.1.unit_with_units.cellml): Error detected correctly.
* Expected: ```Unexpected element units```
* Output: ```[Error] [5:8] Unexpected element units found - not valid here.```

[5.4.2.1.unit_with_variable](../models_1_0/invalid/5.4.2.1.unit_with_variable.cellml): Error detected correctly.
* Expected: ```Unexpected element variable```
* Output: ```[Error] [6:10] Unexpected element variable found - not valid here.```

[5.4.2.1.unit_with_variable_ref](../models_1_0/invalid/5.4.2.1.unit_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element variable_ref```
* Output: ```[Error] [7:10] Unexpected element variable_ref found - not valid here.```


---

##### 5.4.2.2

[5.4.2.2.unit_cycle_1](../models_1_0/invalid/5.4.2.2.unit_cycle_1.cellml): Error detected correctly.
* Expected: ```Units are defined circularly```
* Output:
  * ```[Error] [2:139] Units are defined circularly. One unit in the cycle is wooster; .```
  * ```[Warning] [2:139] Cannot perform any further checking of unit names due to problems processing the model units.```

[5.4.2.2.unit_cycle_2](../models_1_0/invalid/5.4.2.2.unit_cycle_2.cellml): Error detected correctly.
* Expected: ```Units are defined circularly```
* Output:
  * ```[Error] [2:150] Units are defined circularly. One unit in the cycle is fluther; .```
  * ```[Warning] [2:150] Cannot perform any further checking of unit names due to problems processing the model units.```

[5.4.2.2.unit_cycle_3](../models_1_0/invalid/5.4.2.2.unit_cycle_3.cellml): Error detected correctly.
* Expected: ```Units are defined circularly```
* Output:
  * ```[Error] [2:150] Units are defined circularly. One unit in the cycle is fluther; .```
  * ```[Warning] [2:150] Cannot perform any further checking of unit names due to problems processing the model units.```

[5.4.2.2.unit_units_invalid](../models_1_0/invalid/5.4.2.2.unit_units_invalid.cellml): Error detected correctly.
* Expected: ```units could not be found```
* Output:
  * ```[Error] [2:144] Units wooster references units ribbles but the latter units could not be found; .```
  * ```[Warning] [2:144] Cannot perform any further checking of unit names due to problems processing the model units.```

[5.4.2.2.unit_units_local_1](../models_1_0/valid/5.4.2.2.unit_units_local_1.cellml): Valid file passed validation.

[5.4.2.2.unit_units_local_2](../models_1_0/valid/5.4.2.2.unit_units_local_2.cellml): Valid file passed validation.


---

##### 5.4.2.3

[5.4.2.3.unit_prefix_integer](../models_1_0/valid/5.4.2.3.unit_prefix_integer.cellml): Valid file passed validation.

[5.4.2.3.unit_prefix_named](../models_1_0/valid/5.4.2.3.unit_prefix_named.cellml): Valid file passed validation.

🔶 [5.4.2.3.unit_prefix_real](../models_1_0/invalid/5.4.2.3.unit_prefix_real.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output:
  * ```terminate called after throwing an instance of 'iface::cellml_api::CellMLException'```
  * ```  what():  std::exception```

🔶 [5.4.2.3.unit_prefix_real_int](../models_1_0/invalid/5.4.2.3.unit_prefix_real_int.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output:
  * ```terminate called after throwing an instance of 'iface::cellml_api::CellMLException'```
  * ```  what():  std::exception```

🔶 [5.4.2.3.unit_prefix_spaces](../models_1_0/invalid/5.4.2.3.unit_prefix_spaces.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output:
  * ```terminate called after throwing an instance of 'iface::cellml_api::CellMLException'```
  * ```  what():  std::exception```

🔶 [5.4.2.3.unit_prefix_unknown](../models_1_0/invalid/5.4.2.3.unit_prefix_unknown.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output:
  * ```terminate called after throwing an instance of 'iface::cellml_api::CellMLException'```
  * ```  what():  std::exception```


---

##### 5.4.2.4

🔶 [5.4.2.4.unit_exponent_invalid](../models_1_0/invalid/5.4.2.4.unit_exponent_invalid.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output:
  * ```terminate called after throwing an instance of 'iface::cellml_api::CellMLException'```
  * ```  what():  std::exception```


---

##### 5.4.2.5

🔶 [5.4.2.5.unit_multiplier_invalid](../models_1_0/invalid/5.4.2.5.unit_multiplier_invalid.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output:
  * ```terminate called after throwing an instance of 'iface::cellml_api::CellMLException'```
  * ```  what():  std::exception```


---

##### 5.4.2.6

🔶 [5.4.2.6.unit_offset_invalid](../models_1_0/invalid/5.4.2.6.unit_offset_invalid.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output:
  * ```terminate called after throwing an instance of 'iface::cellml_api::CellMLException'```
  * ```  what():  std::exception```


---

##### 5.4.2.7

🔵 [5.4.2.7.unit_offset_and_exponent](../models_1_0/invalid/5.4.2.7.unit_offset_and_exponent.cellml): **Error not detected.**

🔵 [5.4.2.7.unit_offset_and_siblings_1](../models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_1.cellml): **Error not detected.**

🔵 [5.4.2.7.unit_offset_and_siblings_2](../models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_2.cellml): **Error not detected.**

[5.4.2.7.unit_offset_non_zero_and_exponent_one](../models_1_0/valid/5.4.2.7.unit_offset_non_zero_and_exponent_one.cellml): Valid file passed validation.

[5.4.2.7.unit_offset_zero_and_exponent](../models_1_0/valid/5.4.2.7.unit_offset_zero_and_exponent.cellml): Valid file passed validation.

[5.4.2.7.unit_offset_zero_and_siblings](../models_1_0/valid/5.4.2.7.unit_offset_zero_and_siblings.cellml): Valid file passed validation.


---

#### 5.5.2

[5.5.2.boolean_arithmetic_divide](../models_1_0/booleans/5.5.2.boolean_arithmetic_divide.cellml): Valid file passed validation.

[5.5.2.boolean_arithmetic_minus](../models_1_0/booleans/5.5.2.boolean_arithmetic_minus.cellml): Valid file passed validation.

[5.5.2.boolean_arithmetic_plus](../models_1_0/booleans/5.5.2.boolean_arithmetic_plus.cellml): Valid file passed validation.

[5.5.2.boolean_arithmetic_power_1](../models_1_0/booleans/5.5.2.boolean_arithmetic_power_1.cellml): Valid file passed validation.

🔴 [5.5.2.boolean_arithmetic_power_2](../models_1_0/booleans/5.5.2.boolean_arithmetic_power_2.cellml): **Valid file failed validation.**
* Output:
  * ```[Warning] [13:16] Expected all arguments to operator "eq" to have the same units.```
  * ```[Error] [15:18] Expected exponent to pow operator to be dimensionless.```

[5.5.2.boolean_arithmetic_root_1](../models_1_0/booleans/5.5.2.boolean_arithmetic_root_1.cellml): Valid file passed validation.

🔴 [5.5.2.boolean_arithmetic_root_2](../models_1_0/booleans/5.5.2.boolean_arithmetic_root_2.cellml): **Valid file failed validation.**
* Output:
  * ```[Error] [16:18] Degree qualifier should be in dimensionless units.```
  * ```[Warning] [16:18] Units validation results may be incorrect because the degree of root is not a constant.```
  * ```[Warning] [17:20] Units validation results may be incorrect because the degree of root is not a constant.```

[5.5.2.boolean_arithmetic_times](../models_1_0/booleans/5.5.2.boolean_arithmetic_times.cellml): Valid file passed validation.

[5.5.2.boolean_compare_eq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_eq_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_geq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_geq_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_gt_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_gt_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_leq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_leq_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_lt_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_lt_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_neq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_neq_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_derivatives_1](../models_1_0/booleans/5.5.2.boolean_derivatives_1.cellml): Valid file passed validation.

🔴 [5.5.2.boolean_derivatives_2](../models_1_0/booleans/5.5.2.boolean_derivatives_2.cellml): **Valid file failed validation.**
* Output:
  * ```[Error] [14:12] Degree qualifier should be in dimensionless units.```
  * ```[Warning] [14:12] Units validation results may be incorrect because the degree of differentiation is not a constant.```
  * ```[Warning] [15:14] Units validation results may be incorrect because the degree of differentiation is not a constant.```

[5.5.2.boolean_function_abs](../models_1_0/booleans/5.5.2.boolean_function_abs.cellml): Valid file passed validation.

[5.5.2.boolean_function_ceiling](../models_1_0/booleans/5.5.2.boolean_function_ceiling.cellml): Valid file passed validation.

[5.5.2.boolean_function_exp](../models_1_0/booleans/5.5.2.boolean_function_exp.cellml): Valid file passed validation.

[5.5.2.boolean_function_factorial](../models_1_0/booleans/5.5.2.boolean_function_factorial.cellml): Valid file passed validation.

[5.5.2.boolean_function_floor](../models_1_0/booleans/5.5.2.boolean_function_floor.cellml): Valid file passed validation.

[5.5.2.boolean_function_ln](../models_1_0/booleans/5.5.2.boolean_function_ln.cellml): Valid file passed validation.

[5.5.2.boolean_function_log_1](../models_1_0/booleans/5.5.2.boolean_function_log_1.cellml): Valid file passed validation.

[5.5.2.boolean_function_log_2](../models_1_0/booleans/5.5.2.boolean_function_log_2.cellml): Valid file passed validation.

[5.5.2.boolean_logic_and_operand_error](../models_1_0/booleans/5.5.2.boolean_logic_and_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_logic_not_operand_error](../models_1_0/booleans/5.5.2.boolean_logic_not_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_logic_or_operand_error](../models_1_0/booleans/5.5.2.boolean_logic_or_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_logic_xor_operand_error](../models_1_0/booleans/5.5.2.boolean_logic_xor_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arccos](../models_1_0/booleans/5.5.2.boolean_trig_arccos.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arccosh](../models_1_0/booleans/5.5.2.boolean_trig_arccosh.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arccot](../models_1_0/booleans/5.5.2.boolean_trig_arccot.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arccoth](../models_1_0/booleans/5.5.2.boolean_trig_arccoth.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arccsc](../models_1_0/booleans/5.5.2.boolean_trig_arccsc.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arccsch](../models_1_0/booleans/5.5.2.boolean_trig_arccsch.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arcsec](../models_1_0/booleans/5.5.2.boolean_trig_arcsec.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arcsech](../models_1_0/booleans/5.5.2.boolean_trig_arcsech.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arcsin](../models_1_0/booleans/5.5.2.boolean_trig_arcsin.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arcsinh](../models_1_0/booleans/5.5.2.boolean_trig_arcsinh.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arctan](../models_1_0/booleans/5.5.2.boolean_trig_arctan.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arctanh](../models_1_0/booleans/5.5.2.boolean_trig_arctanh.cellml): Valid file passed validation.

[5.5.2.boolean_trig_cos](../models_1_0/booleans/5.5.2.boolean_trig_cos.cellml): Valid file passed validation.

[5.5.2.boolean_trig_cosh](../models_1_0/booleans/5.5.2.boolean_trig_cosh.cellml): Valid file passed validation.

[5.5.2.boolean_trig_cot](../models_1_0/booleans/5.5.2.boolean_trig_cot.cellml): Valid file passed validation.

[5.5.2.boolean_trig_coth](../models_1_0/booleans/5.5.2.boolean_trig_coth.cellml): Valid file passed validation.

[5.5.2.boolean_trig_csc](../models_1_0/booleans/5.5.2.boolean_trig_csc.cellml): Valid file passed validation.

[5.5.2.boolean_trig_csch](../models_1_0/booleans/5.5.2.boolean_trig_csch.cellml): Valid file passed validation.

[5.5.2.boolean_trig_sec](../models_1_0/booleans/5.5.2.boolean_trig_sec.cellml): Valid file passed validation.

[5.5.2.boolean_trig_sech](../models_1_0/booleans/5.5.2.boolean_trig_sech.cellml): Valid file passed validation.

[5.5.2.boolean_trig_sin](../models_1_0/booleans/5.5.2.boolean_trig_sin.cellml): Valid file passed validation.

[5.5.2.boolean_trig_sinh](../models_1_0/booleans/5.5.2.boolean_trig_sinh.cellml): Valid file passed validation.

[5.5.2.boolean_trig_tan](../models_1_0/booleans/5.5.2.boolean_trig_tan.cellml): Valid file passed validation.

[5.5.2.boolean_trig_tanh](../models_1_0/booleans/5.5.2.boolean_trig_tanh.cellml): Valid file passed validation.

[5.5.2.boolean_variable_1](../models_1_0/booleans/5.5.2.boolean_variable_1.cellml): Valid file passed validation.

[5.5.2.boolean_variable_2](../models_1_0/booleans/5.5.2.boolean_variable_2.cellml): Valid file passed validation.

[5.5.2.boolean_variable_3](../models_1_0/booleans/5.5.2.boolean_variable_3.cellml): Valid file passed validation.


---

## 6. Grouping

##### 6.4.1.1

[6.4.1.1.group_component_ref_missing_1](../models_1_0/invalid/6.4.1.1.group_component_ref_missing_1.cellml): Error detected correctly.
* Expected: ```MUST contain at least one```
* Output: ```[Error] [5:4] A  element MUST contain at least one  element (section 6.4.1.1).```

[6.4.1.1.group_component_ref_missing_2](../models_1_0/invalid/6.4.1.1.group_component_ref_missing_2.cellml): Error detected correctly.
* Expected: ```MUST contain at least one```
* Output: ```[Error] [5:4] A  element MUST contain at least one  element (section 6.4.1.1).```

[6.4.1.1.group_component_ref_multiple](../models_1_0/valid/6.4.1.1.group_component_ref_multiple.cellml): Valid file passed validation.

[6.4.1.1.group_component_ref_single](../models_1_0/valid/6.4.1.1.group_component_ref_single.cellml): Valid file passed validation.

[6.4.1.1.group_empty](../models_1_0/invalid/6.4.1.1.group_empty.cellml): Error detected correctly.
* Expected: ```MUST contain at least one```
* Output:
  * ```[Error] [3:4] A  element MUST contain at least one  element (section 6.4.1.1).```
  * ```[Error] [3:4] A  element MUST contain at least one  element (section 6.4.1.1).```

[6.4.1.1.group_only_extensions](../models_1_0/invalid/6.4.1.1.group_only_extensions.cellml): Error detected correctly.
* Expected: ```MUST contain at least one```
* Output:
  * ```[Error] [3:4] A  element MUST contain at least one  element (section 6.4.1.1).```
  * ```[Error] [3:4] A  element MUST contain at least one  element (section 6.4.1.1).```
  * ```[Warning] [4:6] Element howareyou in namespace http://www.cellml.org/cellml/1.0#is not allowed in extension elements.```

[6.4.1.1.group_relationship_ref_missing_1](../models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_1.cellml): Error detected correctly.
* Expected: ```MUST contain at least one```
* Output: ```[Error] [5:4] A  element MUST contain at least one  element (section 6.4.1.1).```

[6.4.1.1.group_relationship_ref_missing_2](../models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_2.cellml): Error detected correctly.
* Expected: ```MUST contain at least one```
* Output: ```[Error] [5:4] A  element MUST contain at least one  element (section 6.4.1.1).```

[6.4.1.1.group_with_component](../models_1_0/invalid/6.4.1.1.group_with_component.cellml): Error detected correctly.
* Expected: ```Unexpected element component```
* Output: ```[Error] [10:6] Unexpected element component found - not valid here.```

[6.4.1.1.group_with_connection](../models_1_0/invalid/6.4.1.1.group_with_connection.cellml): Error detected correctly.
* Expected: ```Unexpected element connection```
* Output: ```[Error] [14:6] Unexpected element connection found - not valid here.```

[6.4.1.1.group_with_group](../models_1_0/invalid/6.4.1.1.group_with_group.cellml): Error detected correctly.
* Expected: ```Unexpected element group```
* Output: ```[Error] [12:6] Unexpected element group found - not valid here.```

[6.4.1.1.group_with_map_components](../models_1_0/invalid/6.4.1.1.group_with_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected element map_components```
* Output: ```[Error] [10:6] Unexpected element map_components found - not valid here.```

[6.4.1.1.group_with_map_variables](../models_1_0/invalid/6.4.1.1.group_with_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected element map_variables```
* Output: ```[Error] [14:6] Unexpected element map_variables found - not valid here.```

[6.4.1.1.group_with_math](../models_1_0/invalid/6.4.1.1.group_with_math.cellml): Error detected correctly.
* Expected: ```Unexpected element math```
* Output: ```[Error] [12:6] Unexpected element math found - not valid here.```

[6.4.1.1.group_with_model](../models_1_0/invalid/6.4.1.1.group_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [10:6] Unexpected element model found - not valid here.```

[6.4.1.1.group_with_reaction](../models_1_0/invalid/6.4.1.1.group_with_reaction.cellml): Error detected correctly.
* Expected: ```Unexpected element reaction```
* Output: ```[Error] [12:6] Unexpected element reaction found - not valid here.```

[6.4.1.1.group_with_role](../models_1_0/invalid/6.4.1.1.group_with_role.cellml): Error detected correctly.
* Expected: ```Unexpected element role```
* Output: ```[Error] [10:6] Unexpected element role found - not valid here.```

[6.4.1.1.group_with_unit](../models_1_0/invalid/6.4.1.1.group_with_unit.cellml): Error detected correctly.
* Expected: ```Unexpected element unit```
* Output: ```[Error] [7:6] Unexpected element unit found - not valid here.```

[6.4.1.1.group_with_units](../models_1_0/invalid/6.4.1.1.group_with_units.cellml): Error detected correctly.
* Expected: ```Unexpected element units```
* Output: ```[Error] [10:6] Unexpected element units found - not valid here.```

[6.4.1.1.group_with_variable](../models_1_0/invalid/6.4.1.1.group_with_variable.cellml): Error detected correctly.
* Expected: ```Unexpected element variable```
* Output: ```[Error] [10:6] Unexpected element variable found - not valid here.```

[6.4.1.1.group_with_variable_ref](../models_1_0/invalid/6.4.1.1.group_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element variable_ref```
* Output: ```[Error] [12:6] Unexpected element variable_ref found - not valid here.```


---

#### 6.4.1

[6.4.1.group_child_order_1](../models_1_0/valid/6.4.1.group_child_order_1.cellml): Valid file passed validation.

[6.4.1.group_child_order_2](../models_1_0/valid/6.4.1.group_child_order_2.cellml): Valid file passed validation.


---

##### 6.4.2.1

[6.4.2.1.relationship_ref_name](../models_1_0/valid/6.4.2.1.relationship_ref_name.cellml): Valid file passed validation.

[6.4.2.1.relationship_ref_relationship_1](../models_1_0/valid/6.4.2.1.relationship_ref_relationship_1.cellml): Valid file passed validation.

[6.4.2.1.relationship_ref_relationship_2](../models_1_0/valid/6.4.2.1.relationship_ref_relationship_2.cellml): Valid file passed validation.

[6.4.2.1.relationship_ref_relationship_missing](../models_1_0/invalid/6.4.2.1.relationship_ref_relationship_missing.cellml): Error detected correctly.
* Expected: ```Relationship attribute is mandatory```
* Output: ```[Error] [7:6] Relationship attribute is mandatory on relationship_ref (section 6.4.1.1).```

[6.4.2.1.relationship_ref_with_component](../models_1_0/invalid/6.4.2.1.relationship_ref_with_component.cellml): Error detected correctly.
* Expected: ```Unexpected element component```
* Output: ```[Error] [7:8] Unexpected element component found - not valid here.```

[6.4.2.1.relationship_ref_with_component_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element component_ref```
* Output: ```[Error] [9:8] Unexpected element component_ref found - not valid here.```

[6.4.2.1.relationship_ref_with_connection](../models_1_0/invalid/6.4.2.1.relationship_ref_with_connection.cellml): Error detected correctly.
* Expected: ```Unexpected element connection```
* Output: ```[Error] [11:8] Unexpected element connection found - not valid here.```

[6.4.2.1.relationship_ref_with_group](../models_1_0/invalid/6.4.2.1.relationship_ref_with_group.cellml): Error detected correctly.
* Expected: ```Unexpected element group```
* Output: ```[Error] [9:8] Unexpected element group found - not valid here.```

[6.4.2.1.relationship_ref_with_map_components](../models_1_0/invalid/6.4.2.1.relationship_ref_with_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected element map_components```
* Output: ```[Error] [7:8] Unexpected element map_components found - not valid here.```

[6.4.2.1.relationship_ref_with_map_variables](../models_1_0/invalid/6.4.2.1.relationship_ref_with_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected element map_variables```
* Output: ```[Error] [11:8] Unexpected element map_variables found - not valid here.```

[6.4.2.1.relationship_ref_with_math](../models_1_0/invalid/6.4.2.1.relationship_ref_with_math.cellml): Error detected correctly.
* Expected: ```Unexpected element math```
* Output: ```[Error] [9:8] Unexpected element math found - not valid here.```

[6.4.2.1.relationship_ref_with_model](../models_1_0/invalid/6.4.2.1.relationship_ref_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [7:8] Unexpected element model found - not valid here.```

[6.4.2.1.relationship_ref_with_reaction](../models_1_0/invalid/6.4.2.1.relationship_ref_with_reaction.cellml): Error detected correctly.
* Expected: ```Unexpected element reaction```
* Output: ```[Error] [9:8] Unexpected element reaction found - not valid here.```

[6.4.2.1.relationship_ref_with_relationship_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element relationship_ref```
* Output: ```[Error] [7:8] Unexpected element relationship_ref found - not valid here.```

[6.4.2.1.relationship_ref_with_role](../models_1_0/invalid/6.4.2.1.relationship_ref_with_role.cellml): Error detected correctly.
* Expected: ```Unexpected element role```
* Output: ```[Error] [7:8] Unexpected element role found - not valid here.```

[6.4.2.1.relationship_ref_with_unit](../models_1_0/invalid/6.4.2.1.relationship_ref_with_unit.cellml): Error detected correctly.
* Expected: ```Unexpected element unit```
* Output: ```[Error] [7:8] Unexpected element unit found - not valid here.```

[6.4.2.1.relationship_ref_with_units](../models_1_0/invalid/6.4.2.1.relationship_ref_with_units.cellml): Error detected correctly.
* Expected: ```Unexpected element units```
* Output: ```[Error] [7:8] Unexpected element units found - not valid here.```

[6.4.2.1.relationship_ref_with_variable](../models_1_0/invalid/6.4.2.1.relationship_ref_with_variable.cellml): Error detected correctly.
* Expected: ```Unexpected element variable```
* Output: ```[Error] [7:8] Unexpected element variable found - not valid here.```

[6.4.2.1.relationship_ref_with_variable_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element variable_ref```
* Output: ```[Error] [9:8] Unexpected element variable_ref found - not valid here.```


---

##### 6.4.2.2

[6.4.2.2.relationship_ref_relationship_invalid](../models_1_0/invalid/6.4.2.2.relationship_ref_relationship_invalid.cellml): Error detected correctly.
* Expected: ```The value of a relationship attribute in the CellML namespace```
* Output: ```[Error] [6:19] The value of a relationship attribute in the CellML namespace must be "containment" or "encapsulation" (section 6.4.2.2).```


---

##### 6.4.2.3

[6.4.2.3.relationship_ref_name_invalid](../models_1_0/invalid/6.4.2.3.relationship_ref_name_invalid.cellml): Error detected correctly.
* Expected: ```A valid CellML identifier must contain at least one letter```
* Output:
  * ```[Error] [6:11] A valid CellML identifier must contain at least one letter (section 2.4.1).```
  * ```[Error] [6:11] A valid CellML identifier must contain at least one letter (section 2.4.1).```

[6.4.2.3.relationship_ref_name_not_unique_model_wide](../models_1_0/valid/6.4.2.3.relationship_ref_name_not_unique_model_wide.cellml): Valid file passed validation.


---

##### 6.4.2.4

[6.4.2.4.relationship_ref_encapsulation_duplicate](../models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_duplicate.cellml): Error detected correctly.
* Expected: ```A name attribute must not be defined```
* Output:
  * ```[Error] [9:6] A name attribute must not be defined on a  element with a relationship attribute value of "encapsulation" (section 6.4.2.4).```
  * ```[Error] [10:6] A name attribute must not be defined on a  element with a relationship attribute value of "encapsulation" (section 6.4.2.4).```

[6.4.2.4.relationship_ref_encapsulation_named](../models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_named.cellml): Error detected correctly.
* Expected: ```A name attribute must not be defined```
* Output: ```[Error] [6:6] A name attribute must not be defined on a  element with a relationship attribute value of "encapsulation" (section 6.4.2.4).```


---

##### 6.4.2.5

[6.4.2.5.relationship_ref_duplicate_named](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_named.cellml): Error detected correctly.
* Expected: ```Duplicate relationship_ref within group```
* Output: ```[Error] [10:6] Duplicate relationship_ref within group.```

[6.4.2.5.relationship_ref_duplicate_unnamed_1](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_unnamed_1.cellml): Error detected correctly.
* Expected: ```Duplicate relationship_ref within group```
* Output: ```[Error] [10:6] Duplicate relationship_ref within group.```

[6.4.2.5.relationship_ref_duplicate_unnamed_2](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_unnamed_2.cellml): Error detected correctly.
* Expected: ```Duplicate relationship_ref within group```
* Output: ```[Error] [10:6] Duplicate relationship_ref within group.```

[6.4.2.5.relationship_ref_multiple_1](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_1.cellml): Valid file passed validation.

[6.4.2.5.relationship_ref_multiple_2](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_2.cellml): Valid file passed validation.

[6.4.2.5.relationship_ref_multiple_3](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_3.cellml): Valid file passed validation.


---

##### 6.4.3.1

[6.4.3.1.component_ref_component_missing](../models_1_0/invalid/6.4.3.1.component_ref_component_missing.cellml): Error detected correctly.
* Expected: ```must define a component attribute```
* Output:
  * ```[Error] [8:8] A  element must define a component attribute (section 6.4.3.1).```
  * ```[Error] [8:8] Component_ref element references component which does not exist.```

[6.4.3.1.component_ref_nesting](../models_1_0/valid/6.4.3.1.component_ref_nesting.cellml): Valid file passed validation.

[6.4.3.1.component_ref_with_component](../models_1_0/invalid/6.4.3.1.component_ref_with_component.cellml): Error detected correctly.
* Expected: ```Unexpected element component```
* Output: ```[Error] [9:8] Unexpected element component found - not valid here.```

[6.4.3.1.component_ref_with_connection](../models_1_0/invalid/6.4.3.1.component_ref_with_connection.cellml): Error detected correctly.
* Expected: ```Unexpected element connection```
* Output: ```[Error] [13:8] Unexpected element connection found - not valid here.```

[6.4.3.1.component_ref_with_group](../models_1_0/invalid/6.4.3.1.component_ref_with_group.cellml): Error detected correctly.
* Expected: ```Unexpected element group```
* Output: ```[Error] [11:8] Unexpected element group found - not valid here.```

[6.4.3.1.component_ref_with_map_components](../models_1_0/invalid/6.4.3.1.component_ref_with_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected element map_components```
* Output: ```[Error] [9:8] Unexpected element map_components found - not valid here.```

[6.4.3.1.component_ref_with_map_variables](../models_1_0/invalid/6.4.3.1.component_ref_with_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected element map_variables```
* Output: ```[Error] [13:8] Unexpected element map_variables found - not valid here.```

[6.4.3.1.component_ref_with_math](../models_1_0/invalid/6.4.3.1.component_ref_with_math.cellml): Error detected correctly.
* Expected: ```Unexpected element math```
* Output: ```[Error] [11:8] Unexpected element math found - not valid here.```

[6.4.3.1.component_ref_with_model](../models_1_0/invalid/6.4.3.1.component_ref_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [9:8] Unexpected element model found - not valid here.```

[6.4.3.1.component_ref_with_reaction](../models_1_0/invalid/6.4.3.1.component_ref_with_reaction.cellml): Error detected correctly.
* Expected: ```Unexpected element reaction```
* Output: ```[Error] [11:8] Unexpected element reaction found - not valid here.```

[6.4.3.1.component_ref_with_relationship_ref](../models_1_0/invalid/6.4.3.1.component_ref_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element relationship_ref```
* Output: ```[Error] [9:8] Unexpected element relationship_ref found - not valid here.```

[6.4.3.1.component_ref_with_role](../models_1_0/invalid/6.4.3.1.component_ref_with_role.cellml): Error detected correctly.
* Expected: ```Unexpected element role```
* Output: ```[Error] [9:8] Unexpected element role found - not valid here.```

[6.4.3.1.component_ref_with_unit](../models_1_0/invalid/6.4.3.1.component_ref_with_unit.cellml): Error detected correctly.
* Expected: ```Unexpected element unit```
* Output: ```[Error] [9:8] Unexpected element unit found - not valid here.```

[6.4.3.1.component_ref_with_units](../models_1_0/invalid/6.4.3.1.component_ref_with_units.cellml): Error detected correctly.
* Expected: ```Unexpected element units```
* Output: ```[Error] [9:8] Unexpected element units found - not valid here.```

[6.4.3.1.component_ref_with_variable](../models_1_0/invalid/6.4.3.1.component_ref_with_variable.cellml): Error detected correctly.
* Expected: ```Unexpected element variable```
* Output: ```[Error] [9:8] Unexpected element variable found - not valid here.```

[6.4.3.1.component_ref_with_variable_ref](../models_1_0/invalid/6.4.3.1.component_ref_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element variable_ref```
* Output: ```[Error] [11:8] Unexpected element variable_ref found - not valid here.```


---

##### 6.4.3.2

[6.4.3.2.component_ref_children_declared_twice_1](../models_1_0/invalid/6.4.3.2.component_ref_children_declared_twice_1.cellml): Error detected correctly.
* Expected: ```elements that reference a given component may contain further```
* Output: ```[Error] [12:6] In a given hierarchy, only one of the  elements that reference a given component may contain further  elements, but the containment hierarchy has more than one non-terminal component_ref to A.```

[6.4.3.2.component_ref_children_declared_twice_2](../models_1_0/invalid/6.4.3.2.component_ref_children_declared_twice_2.cellml): Error detected correctly.
* Expected: ```elements that reference a given component may contain further```
* Output: ```[Error] [15:6] In a given hierarchy, only one of the  elements that reference a given component may contain further  elements, but the containment hierarchy has more than one non-terminal component_ref to A.```

[6.4.3.2.component_ref_children_declared_twice_3](../models_1_0/invalid/6.4.3.2.component_ref_children_declared_twice_3.cellml): Error detected correctly.
* Expected: ```elements that reference a given component may contain further```
* Output: ```[Error] [15:6] In a given hierarchy, only one of the  elements that reference a given component may contain further  elements, but the containment hierarchy with name A has more than one non-terminal component_ref to A.```

🔵 [6.4.3.2.component_ref_cycle_1](../models_1_0/invalid/6.4.3.2.component_ref_cycle_1.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_cycle_2](../models_1_0/invalid/6.4.3.2.component_ref_cycle_2.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_cycle_3](../models_1_0/invalid/6.4.3.2.component_ref_cycle_3.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_cycle_4](../models_1_0/invalid/6.4.3.2.component_ref_cycle_4.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_cycle_5](../models_1_0/invalid/6.4.3.2.component_ref_cycle_5.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_cycle_6](../models_1_0/invalid/6.4.3.2.component_ref_cycle_6.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_cycle_7](../models_1_0/invalid/6.4.3.2.component_ref_cycle_7.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_cycle_8](../models_1_0/invalid/6.4.3.2.component_ref_cycle_8.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_duplicate_child_1](../models_1_0/invalid/6.4.3.2.component_ref_duplicate_child_1.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_duplicate_child_2](../models_1_0/invalid/6.4.3.2.component_ref_duplicate_child_2.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_duplicate_child_3](../models_1_0/invalid/6.4.3.2.component_ref_duplicate_child_3.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_duplicate_child_4](../models_1_0/invalid/6.4.3.2.component_ref_duplicate_child_4.cellml): **Error not detected.**

[6.4.3.2.component_ref_no_children_containment](../models_1_0/invalid/6.4.3.2.component_ref_no_children_containment.cellml): Error detected correctly.
* Expected: ```does not have any child component_ref elements```
* Output: ```[Error] [7:6] Component_ref element appears as child of a group element but does not have any child component_ref elements.```

[6.4.3.2.component_ref_no_children_encapsulation](../models_1_0/invalid/6.4.3.2.component_ref_no_children_encapsulation.cellml): Error detected correctly.
* Expected: ```does not have any child component_ref elements```
* Output: ```[Error] [7:6] Component_ref element appears as child of a group element but does not have any child component_ref elements.```

🔴 [6.4.3.2.component_ref_no_children_extension](../models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml): **Valid file failed validation.**
* Output: ```[Error] [9:6] Component_ref element appears as child of a group element but does not have any child component_ref elements.```

[6.4.3.2.component_ref_overlapping_containment](../models_1_0/valid/6.4.3.2.component_ref_overlapping_containment.cellml): Valid file passed validation.

🔵 [6.4.3.2.component_ref_overlapping_encapsulation](../models_1_0/invalid/6.4.3.2.component_ref_overlapping_encapsulation.cellml): **Error not detected.**

[6.4.3.2.component_ref_split_named](../models_1_0/valid/6.4.3.2.component_ref_split_named.cellml): Valid file passed validation.

[6.4.3.2.component_ref_split_unnamed_1](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_1.cellml): Valid file passed validation.

[6.4.3.2.component_ref_split_unnamed_2](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_2.cellml): Valid file passed validation.


---

##### 6.4.3.3

[6.4.3.3.component_ref_component_invalid](../models_1_0/invalid/6.4.3.3.component_ref_component_invalid.cellml): Error detected correctly.
* Expected: ```A valid CellML identifier must contain at least```
* Output:
  * ```[Error] [8:8] Component_ref element references component which does not exist.```
  * ```[Error] [8:18] A valid CellML identifier must contain at least one letter (section 2.4.1).```
  * ```[Error] [8:18] A valid CellML identifier must only contain alphanumeric characters from the US-ASCII character set and the underscore character (section 2.4.1).```

[6.4.3.3.component_ref_component_nonexistent_1](../models_1_0/invalid/6.4.3.3.component_ref_component_nonexistent_1.cellml): Error detected correctly.
* Expected: ```Component_ref element references component which does not exist```
* Output: ```[Error] [7:6] Component_ref element references component which does not exist.```

[6.4.3.3.component_ref_component_nonexistent_2](../models_1_0/invalid/6.4.3.3.component_ref_component_nonexistent_2.cellml): Error detected correctly.
* Expected: ```Component_ref element references component which does not exist```
* Output: ```[Error] [8:8] Component_ref element references component which does not exist.```


---

## 7. Reactions

##### 7.4.1.1

[7.4.1.1.reaction_variable_ref_missing](../models_1_0/invalid/7.4.1.1.reaction_variable_ref_missing.cellml): Error detected correctly.
* Expected: ```must contain at least one```
* Output: ```[Error] [5:6] Each  element must contain at least one  element (section 7.4.1.1).```

[7.4.1.1.reaction_with_component](../models_1_0/invalid/7.4.1.1.reaction_with_component.cellml): Error detected correctly.
* Expected: ```Unexpected element component```
* Output: ```[Error] [9:8] Unexpected element component found - not valid here.```

[7.4.1.1.reaction_with_component_ref](../models_1_0/invalid/7.4.1.1.reaction_with_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element component_ref```
* Output: ```[Error] [9:8] Unexpected element component_ref found - not valid here.```

[7.4.1.1.reaction_with_connection](../models_1_0/invalid/7.4.1.1.reaction_with_connection.cellml): Error detected correctly.
* Expected: ```Unexpected element connection```
* Output: ```[Error] [9:8] Unexpected element connection found - not valid here.```

[7.4.1.1.reaction_with_group](../models_1_0/invalid/7.4.1.1.reaction_with_group.cellml): Error detected correctly.
* Expected: ```Unexpected element group```
* Output: ```[Error] [9:8] Unexpected element group found - not valid here.```

[7.4.1.1.reaction_with_map_components](../models_1_0/invalid/7.4.1.1.reaction_with_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected element map_components```
* Output: ```[Error] [9:8] Unexpected element map_components found - not valid here.```

[7.4.1.1.reaction_with_map_variables](../models_1_0/invalid/7.4.1.1.reaction_with_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected element map_variables```
* Output: ```[Error] [9:8] Unexpected element map_variables found - not valid here.```

[7.4.1.1.reaction_with_math](../models_1_0/invalid/7.4.1.1.reaction_with_math.cellml): Error detected correctly.
* Expected: ```Unexpected element math```
* Output: ```[Error] [9:8] Unexpected element math found - not valid here.```

[7.4.1.1.reaction_with_model](../models_1_0/invalid/7.4.1.1.reaction_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [9:8] Unexpected element model found - not valid here.```

[7.4.1.1.reaction_with_reaction](../models_1_0/invalid/7.4.1.1.reaction_with_reaction.cellml): Error detected correctly.
* Expected: ```Unexpected element reaction```
* Output: ```[Error] [10:8] Unexpected element reaction found - not valid here.```

[7.4.1.1.reaction_with_relationship_ref](../models_1_0/invalid/7.4.1.1.reaction_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element relationship_ref```
* Output: ```[Error] [9:8] Unexpected element relationship_ref found - not valid here.```

[7.4.1.1.reaction_with_role](../models_1_0/invalid/7.4.1.1.reaction_with_role.cellml): Error detected correctly.
* Expected: ```Unexpected element role```
* Output: ```[Error] [9:8] Unexpected element role found - not valid here.```

[7.4.1.1.reaction_with_unit](../models_1_0/invalid/7.4.1.1.reaction_with_unit.cellml): Error detected correctly.
* Expected: ```Unexpected element unit```
* Output: ```[Error] [9:8] Unexpected element unit found - not valid here.```

[7.4.1.1.reaction_with_units](../models_1_0/invalid/7.4.1.1.reaction_with_units.cellml): Error detected correctly.
* Expected: ```Unexpected element units```
* Output: ```[Error] [9:8] Unexpected element units found - not valid here.```

[7.4.1.1.reaction_with_variable](../models_1_0/invalid/7.4.1.1.reaction_with_variable.cellml): Error detected correctly.
* Expected: ```Unexpected element variable```
* Output: ```[Error] [9:8] Unexpected element variable found - not valid here.```


---

##### 7.4.1.2

[7.4.1.2.reaction_reversible_invalid](../models_1_0/invalid/7.4.1.2.reaction_reversible_invalid.cellml): Error detected correctly.
* Expected: ```the reversible attribute must have a value of "yes" or "no"```
* Output: ```[Error] [5:17] If present, the reversible attribute must have a value of "yes" or "no" (section 7.4.1.2).```

[7.4.1.2.reaction_reversible_no](../models_1_0/valid/7.4.1.2.reaction_reversible_no.cellml): Valid file passed validation.

[7.4.1.2.reaction_reversible_yes](../models_1_0/valid/7.4.1.2.reaction_reversible_yes.cellml): Valid file passed validation.


---

##### 7.4.1.3

🔵 [7.4.1.3.reaction_encapsulating_delta_variable](../models_1_0/invalid/7.4.1.3.reaction_encapsulating_delta_variable.cellml): **Error not detected.**


---

##### 7.4.2.1

[7.4.2.1.variable_ref_role_missing](../models_1_0/invalid/7.4.2.1.variable_ref_role_missing.cellml): Error detected correctly.
* Expected: ```must contain at least one```
* Output: ```[Error] [6:8] Each  element must contain at least one  element (section 7.4.2.1).```

[7.4.2.1.variable_ref_variable_missing](../models_1_0/invalid/7.4.2.1.variable_ref_variable_missing.cellml): Error detected correctly.
* Expected: ```must define a variable attribute```
* Output: ```[Error] [6:8] Each  element must define a variable attribute (section 7.4.2.1).```

[7.4.2.1.variable_ref_with_component](../models_1_0/invalid/7.4.2.1.variable_ref_with_component.cellml): Error detected correctly.
* Expected: ```Unexpected element component```
* Output: ```[Error] [8:10] Unexpected element component found - not valid here.```

[7.4.2.1.variable_ref_with_component_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element component_ref```
* Output: ```[Error] [8:10] Unexpected element component_ref found - not valid here.```

[7.4.2.1.variable_ref_with_connection](../models_1_0/invalid/7.4.2.1.variable_ref_with_connection.cellml): Error detected correctly.
* Expected: ```Unexpected element connection```
* Output: ```[Error] [8:10] Unexpected element connection found - not valid here.```

[7.4.2.1.variable_ref_with_group](../models_1_0/invalid/7.4.2.1.variable_ref_with_group.cellml): Error detected correctly.
* Expected: ```Unexpected element group```
* Output: ```[Error] [8:10] Unexpected element group found - not valid here.```

[7.4.2.1.variable_ref_with_map_components](../models_1_0/invalid/7.4.2.1.variable_ref_with_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected element map_components```
* Output: ```[Error] [8:10] Unexpected element map_components found - not valid here.```

[7.4.2.1.variable_ref_with_map_variables](../models_1_0/invalid/7.4.2.1.variable_ref_with_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected element map_variables```
* Output: ```[Error] [8:10] Unexpected element map_variables found - not valid here.```

[7.4.2.1.variable_ref_with_math](../models_1_0/invalid/7.4.2.1.variable_ref_with_math.cellml): Error detected correctly.
* Expected: ```Unexpected element math```
* Output: ```[Error] [8:10] Unexpected element math found - not valid here.```

[7.4.2.1.variable_ref_with_model](../models_1_0/invalid/7.4.2.1.variable_ref_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [8:10] Unexpected element model found - not valid here.```

[7.4.2.1.variable_ref_with_reaction](../models_1_0/invalid/7.4.2.1.variable_ref_with_reaction.cellml): Error detected correctly.
* Expected: ```Unexpected element reaction```
* Output: ```[Error] [9:10] Unexpected element reaction found - not valid here.```

[7.4.2.1.variable_ref_with_relationship_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element relationship_ref```
* Output: ```[Error] [8:10] Unexpected element relationship_ref found - not valid here.```

[7.4.2.1.variable_ref_with_unit](../models_1_0/invalid/7.4.2.1.variable_ref_with_unit.cellml): Error detected correctly.
* Expected: ```Unexpected element unit```
* Output: ```[Error] [8:10] Unexpected element unit found - not valid here.```

[7.4.2.1.variable_ref_with_units](../models_1_0/invalid/7.4.2.1.variable_ref_with_units.cellml): Error detected correctly.
* Expected: ```Unexpected element units```
* Output: ```[Error] [8:10] Unexpected element units found - not valid here.```

[7.4.2.1.variable_ref_with_variable](../models_1_0/invalid/7.4.2.1.variable_ref_with_variable.cellml): Error detected correctly.
* Expected: ```Unexpected element variable```
* Output: ```[Error] [8:10] Unexpected element variable found - not valid here.```

[7.4.2.1.variable_ref_with_variable_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element variable_ref```
* Output: ```[Error] [9:10] Unexpected element variable_ref found - not valid here.```


---

##### 7.4.2.2

🔵 [7.4.2.2.variable_ref_variable_duplicate](../models_1_0/invalid/7.4.2.2.variable_ref_variable_duplicate.cellml): **Error not detected.**

🔵 [7.4.2.2.variable_ref_variable_hidden](../models_1_0/invalid/7.4.2.2.variable_ref_variable_hidden.cellml): **Error not detected.**

🔵 [7.4.2.2.variable_ref_variable_nonexistent](../models_1_0/invalid/7.4.2.2.variable_ref_variable_nonexistent.cellml): **Error not detected.**


---

##### 7.4.3.1

[7.4.3.1.role_role_missing](../models_1_0/invalid/7.4.3.1.role_role_missing.cellml): Error detected correctly.
* Expected: ```must define a role attribute```
* Output: ```[Error] [7:10] Each  element must define a role attribute (section 7.4.3.1).```

[7.4.3.1.role_with_component](../models_1_0/invalid/7.4.3.1.role_with_component.cellml): Error detected correctly.
* Expected: ```Unexpected element component```
* Output: ```[Error] [8:12] Unexpected element component found - not valid here.```

[7.4.3.1.role_with_component_ref](../models_1_0/invalid/7.4.3.1.role_with_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element component_ref```
* Output: ```[Error] [8:12] Unexpected element component_ref found - not valid here.```

[7.4.3.1.role_with_connection](../models_1_0/invalid/7.4.3.1.role_with_connection.cellml): Error detected correctly.
* Expected: ```Unexpected element connection```
* Output: ```[Error] [8:12] Unexpected element connection found - not valid here.```

[7.4.3.1.role_with_group](../models_1_0/invalid/7.4.3.1.role_with_group.cellml): Error detected correctly.
* Expected: ```Unexpected element group```
* Output: ```[Error] [8:12] Unexpected element group found - not valid here.```

[7.4.3.1.role_with_map_components](../models_1_0/invalid/7.4.3.1.role_with_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected element map_components```
* Output: ```[Error] [8:12] Unexpected element map_components found - not valid here.```

[7.4.3.1.role_with_map_variables](../models_1_0/invalid/7.4.3.1.role_with_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected element map_variables```
* Output: ```[Error] [8:12] Unexpected element map_variables found - not valid here.```

[7.4.3.1.role_with_model](../models_1_0/invalid/7.4.3.1.role_with_model.cellml): Error detected correctly.
* Expected: ```Unexpected element model```
* Output: ```[Error] [8:12] Unexpected element model found - not valid here.```

[7.4.3.1.role_with_reaction](../models_1_0/invalid/7.4.3.1.role_with_reaction.cellml): Error detected correctly.
* Expected: ```Unexpected element reaction```
* Output: ```[Error] [9:12] Unexpected element reaction found - not valid here.```

[7.4.3.1.role_with_relationship_ref](../models_1_0/invalid/7.4.3.1.role_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element relationship_ref```
* Output: ```[Error] [8:12] Unexpected element relationship_ref found - not valid here.```

[7.4.3.1.role_with_role](../models_1_0/invalid/7.4.3.1.role_with_role.cellml): Error detected correctly.
* Expected: ```Unexpected element role```
* Output: ```[Error] [8:12] Unexpected element role found - not valid here.```

[7.4.3.1.role_with_unit](../models_1_0/invalid/7.4.3.1.role_with_unit.cellml): Error detected correctly.
* Expected: ```Unexpected element unit```
* Output: ```[Error] [8:12] Unexpected element unit found - not valid here.```

[7.4.3.1.role_with_units](../models_1_0/invalid/7.4.3.1.role_with_units.cellml): Error detected correctly.
* Expected: ```Unexpected element units```
* Output: ```[Error] [8:12] Unexpected element units found - not valid here.```

[7.4.3.1.role_with_variable](../models_1_0/invalid/7.4.3.1.role_with_variable.cellml): Error detected correctly.
* Expected: ```Unexpected element variable```
* Output: ```[Error] [8:12] Unexpected element variable found - not valid here.```

[7.4.3.1.role_with_variable_ref](../models_1_0/invalid/7.4.3.1.role_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Unexpected element variable_ref```
* Output: ```[Error] [9:12] Unexpected element variable_ref found - not valid here.```


---

##### 7.4.3.2

[7.4.3.2.role_role_invalid](../models_1_0/invalid/7.4.3.2.role_role_invalid.cellml): Error detected correctly.
* Expected: ```must take one of the following seven values```
* Output: ```[Error] [7:15] The role attribute must take one of the following seven values: reactant, product, catalyst, activator, inhibitor, modifier, rate (section 7.4.3.2).```


---

##### 7.4.3.3

🔵 [7.4.3.3.reaction_multiple_rates](../models_1_0/invalid/7.4.3.3.reaction_multiple_rates.cellml): **Error not detected.**

🔵 [7.4.3.3.role_rate_with_delta_variable](../models_1_0/invalid/7.4.3.3.role_rate_with_delta_variable.cellml): **Error not detected.**

🔵 [7.4.3.3.role_rate_with_multiple_roles](../models_1_0/invalid/7.4.3.3.role_rate_with_multiple_roles.cellml): **Error not detected.**

🔵 [7.4.3.3.role_rate_with_stoichiometry](../models_1_0/invalid/7.4.3.3.role_rate_with_stoichiometry.cellml): **Error not detected.**


---

##### 7.4.3.4

[7.4.3.4.role_direction_invalid](../models_1_0/invalid/7.4.3.4.role_direction_invalid.cellml): Error detected correctly.
* Expected: ```the direction attribute must take one of the following```
* Output: ```[Error] [20:20] If present, the direction attribute must take one of the following three values: forward, reverse, both (section 7.4.3.4).```


---

##### 7.4.3.5

🔵 [7.4.3.5.role_direction_both_irreversible](../models_1_0/invalid/7.4.3.5.role_direction_both_irreversible.cellml): **Error not detected.**

🔵 [7.4.3.5.role_direction_both_product](../models_1_0/invalid/7.4.3.5.role_direction_both_product.cellml): **Error not detected.**

🔵 [7.4.3.5.role_direction_both_rate](../models_1_0/invalid/7.4.3.5.role_direction_both_rate.cellml): **Error not detected.**

🔵 [7.4.3.5.role_direction_both_reactant](../models_1_0/invalid/7.4.3.5.role_direction_both_reactant.cellml): **Error not detected.**

🔵 [7.4.3.5.role_direction_reverse_irreversible](../models_1_0/invalid/7.4.3.5.role_direction_reverse_irreversible.cellml): **Error not detected.**

🔵 [7.4.3.5.role_direction_reverse_product](../models_1_0/invalid/7.4.3.5.role_direction_reverse_product.cellml): **Error not detected.**

🔵 [7.4.3.5.role_direction_reverse_rate](../models_1_0/invalid/7.4.3.5.role_direction_reverse_rate.cellml): **Error not detected.**

🔵 [7.4.3.5.role_direction_reverse_reactant](../models_1_0/invalid/7.4.3.5.role_direction_reverse_reactant.cellml): **Error not detected.**

🔵 [7.4.3.5.role_direction_role_duplicate](../models_1_0/invalid/7.4.3.5.role_direction_role_duplicate.cellml): **Error not detected.**


---

##### 7.4.3.6

[7.4.3.6.role_stoichiometry_invalid](../models_1_0/invalid/7.4.3.6.role_stoichiometry_invalid.cellml): Error detected correctly.
* Expected: ```Expected a real number```
* Output: ```[Error] [11:60] Expected a real number, but didn't get one in a valid format.```


---

##### 7.4.3.7

🔵 [7.4.3.7.role_delta_variable_duplicate_1](../models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_1.cellml): **Error not detected.**

🔵 [7.4.3.7.role_delta_variable_duplicate_2](../models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_2.cellml): **Error not detected.**

🔵 [7.4.3.7.role_delta_variable_nonexistent_1](../models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_1.cellml): **Error not detected.**

🔵 [7.4.3.7.role_delta_variable_nonexistent_2](../models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_2.cellml): **Error not detected.**


---

##### 7.4.3.8

🔵 [7.4.3.8.role_delta_variable_activator](../models_1_0/invalid/7.4.3.8.role_delta_variable_activator.cellml): **Error not detected.**

🔵 [7.4.3.8.role_delta_variable_catalyst](../models_1_0/invalid/7.4.3.8.role_delta_variable_catalyst.cellml): **Error not detected.**

🔵 [7.4.3.8.role_delta_variable_inhibitor](../models_1_0/invalid/7.4.3.8.role_delta_variable_inhibitor.cellml): **Error not detected.**

🔵 [7.4.3.8.role_delta_variable_modifier](../models_1_0/invalid/7.4.3.8.role_delta_variable_modifier.cellml): **Error not detected.**

🔵 [7.4.3.8.role_delta_variable_with_rate_and_math](../models_1_0/invalid/7.4.3.8.role_delta_variable_with_rate_and_math.cellml): **Error not detected.**

🔵 [7.4.3.8.role_delta_variable_with_stoichiometry_no_rate](../models_1_0/invalid/7.4.3.8.role_delta_variable_with_stoichiometry_no_rate.cellml): **Error not detected.**

🔵 [7.4.3.8.role_delta_variable_without_rate_or_math](../models_1_0/invalid/7.4.3.8.role_delta_variable_without_rate_or_math.cellml): **Error not detected.**


---

##### 7.4.3.9

🔵 [7.4.3.9.role_math_not_relevant](../models_1_0/invalid/7.4.3.9.role_math_not_relevant.cellml): **Error not detected.**


---

#### 7.4.3

[7.4.3.reaction_all_roles_and_attributes](../models_1_0/valid/7.4.3.reaction_all_roles_and_attributes.cellml): Valid file passed validation.

[7.4.3.reaction_reversible_no](../models_1_0/valid/7.4.3.reaction_reversible_no.cellml): Valid file passed validation.

[7.4.3.reaction_simple](../models_1_0/valid/7.4.3.reaction_simple.cellml): Valid file passed validation.


---

## 8. Metadata framework

#### 8.4.1

🔵 [8.4.1.cmeta_id_duplicate](../models_1_0/invalid/8.4.1.cmeta_id_duplicate.cellml): **Error not detected.**

[8.4.1.cmeta_id_in_component](../models_1_0/valid/8.4.1.cmeta_id_in_component.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_component_ref](../models_1_0/valid/8.4.1.cmeta_id_in_component_ref.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_connection](../models_1_0/valid/8.4.1.cmeta_id_in_connection.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_group](../models_1_0/valid/8.4.1.cmeta_id_in_group.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_map_components](../models_1_0/valid/8.4.1.cmeta_id_in_map_components.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_map_variables](../models_1_0/valid/8.4.1.cmeta_id_in_map_variables.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_model](../models_1_0/valid/8.4.1.cmeta_id_in_model.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_reaction](../models_1_0/valid/8.4.1.cmeta_id_in_reaction.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_relationship_ref](../models_1_0/valid/8.4.1.cmeta_id_in_relationship_ref.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_role](../models_1_0/valid/8.4.1.cmeta_id_in_role.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_unit](../models_1_0/valid/8.4.1.cmeta_id_in_unit.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_units_1](../models_1_0/valid/8.4.1.cmeta_id_in_units_1.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_units_2](../models_1_0/valid/8.4.1.cmeta_id_in_units_2.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_variable](../models_1_0/valid/8.4.1.cmeta_id_in_variable.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_variable_ref](../models_1_0/valid/8.4.1.cmeta_id_in_variable_ref.cellml): Valid file passed validation.


---

#### 8.4.2

[8.4.2.rdf_in_component](../models_1_0/valid/8.4.2.rdf_in_component.cellml): Valid file passed validation.

[8.4.2.rdf_in_component_ref](../models_1_0/valid/8.4.2.rdf_in_component_ref.cellml): Valid file passed validation.

[8.4.2.rdf_in_connection](../models_1_0/valid/8.4.2.rdf_in_connection.cellml): Valid file passed validation.

[8.4.2.rdf_in_group](../models_1_0/valid/8.4.2.rdf_in_group.cellml): Valid file passed validation.

[8.4.2.rdf_in_map_components](../models_1_0/valid/8.4.2.rdf_in_map_components.cellml): Valid file passed validation.

[8.4.2.rdf_in_map_variables](../models_1_0/valid/8.4.2.rdf_in_map_variables.cellml): Valid file passed validation.

[8.4.2.rdf_in_model](../models_1_0/valid/8.4.2.rdf_in_model.cellml): Valid file passed validation.

[8.4.2.rdf_in_reaction](../models_1_0/valid/8.4.2.rdf_in_reaction.cellml): Valid file passed validation.

[8.4.2.rdf_in_relationship_ref](../models_1_0/valid/8.4.2.rdf_in_relationship_ref.cellml): Valid file passed validation.

[8.4.2.rdf_in_role](../models_1_0/valid/8.4.2.rdf_in_role.cellml): Valid file passed validation.

[8.4.2.rdf_in_unit](../models_1_0/valid/8.4.2.rdf_in_unit.cellml): Valid file passed validation.

[8.4.2.rdf_in_units_1](../models_1_0/valid/8.4.2.rdf_in_units_1.cellml): Valid file passed validation.

[8.4.2.rdf_in_units_2](../models_1_0/valid/8.4.2.rdf_in_units_2.cellml): Valid file passed validation.

[8.4.2.rdf_in_variable](../models_1_0/valid/8.4.2.rdf_in_variable.cellml): Valid file passed validation.

[8.4.2.rdf_in_variable_ref](../models_1_0/valid/8.4.2.rdf_in_variable_ref.cellml): Valid file passed validation.


---

## C. Advanced units functionality

#### 103.3.3

[C.3.3.unit_checking_arithmetic_minus_operand_error_1](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_minus_operand_error_1.cellml): Valid file passed validation.

[C.3.3.unit_checking_arithmetic_minus_operand_error_2](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_minus_operand_error_2.cellml): Valid file passed validation.

[C.3.3.unit_checking_arithmetic_minus_operand_error_3](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_minus_operand_error_3.cellml): Valid file passed validation.

[C.3.3.unit_checking_arithmetic_plus_operand_error_1](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_plus_operand_error_1.cellml): Valid file passed validation.

[C.3.3.unit_checking_arithmetic_plus_operand_error_2](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_plus_operand_error_2.cellml): Valid file passed validation.

[C.3.3.unit_checking_arithmetic_plus_operand_error_3](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_plus_operand_error_3.cellml): Valid file passed validation.

[C.3.3.unit_checking_arithmetic_plus_operand_error_4](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_plus_operand_error_4.cellml): Valid file passed validation.

🔴 [C.3.3.unit_checking_arithmetic_power_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_power_operand_error.cellml): **Valid file failed validation.**
* Output: ```[Error] [13:12] Expected exponent to pow operator to be dimensionless.```

🔴 [C.3.3.unit_checking_arithmetic_root_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_root_operand_error.cellml): **Valid file failed validation.**
* Output: ```[Error] [11:12] Degree qualifier should be in dimensionless units.```

[C.3.3.unit_checking_compare_eq_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_eq_operand_mismatch.cellml): Valid file passed validation.

[C.3.3.unit_checking_compare_geq_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_geq_operand_mismatch.cellml): Valid file passed validation.

[C.3.3.unit_checking_compare_gt_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_gt_operand_mismatch.cellml): Valid file passed validation.

[C.3.3.unit_checking_compare_leq_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_leq_operand_mismatch.cellml): Valid file passed validation.

[C.3.3.unit_checking_compare_lt_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_lt_operand_mismatch.cellml): Valid file passed validation.

[C.3.3.unit_checking_compare_neq_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_neq_operand_mismatch.cellml): Valid file passed validation.

🔴 [C.3.3.unit_checking_derivative_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_derivative_operand_error.cellml): **Valid file failed validation.**
* Output: ```[Error] [14:12] Degree qualifier should be in dimensionless units.```

[C.3.3.unit_checking_function_exp_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_function_exp_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_function_factorial_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_function_factorial_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_function_ln_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_function_ln_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_function_log_operand_error_1](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_function_log_operand_error_1.cellml): Valid file passed validation.

[C.3.3.unit_checking_function_log_operand_error_2](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_function_log_operand_error_2.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_arccos_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arccos_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_arccosh_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arccosh_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_arccot_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arccot_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_arccoth_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arccoth_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_arccsc_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arccsc_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_arccsch_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arccsch_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_arcsec_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arcsec_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_arcsech_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arcsech_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_arcsin_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arcsin_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_arcsinh_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arcsinh_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_arctan_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arctan_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_arctanh_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_arctanh_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_cos_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_cos_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_cosh_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_cosh_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_cot_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_cot_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_coth_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_coth_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_csc_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_csc_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_csch_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_csch_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_sec_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_sec_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_sech_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_sech_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_sin_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_sin_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_sinh_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_sinh_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_tan_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_tan_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_trig_tanh_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_trig_tanh_operand_error.cellml): Valid file passed validation.

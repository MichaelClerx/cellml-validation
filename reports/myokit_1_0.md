# Myokit - CellML 1.0

Performance:
* 96% according to spec (155 out of 161)
* 1 out of 1 valid files passed
* 154 out of 160 invalid files detected

Issues:
* 0 valid files failed validation
* 1 invalid files passed validation
* 5 invalid files failed validation for the wrong reason

Test implementation issues
* **603 tests not run**

Results per category

(Valid passed, invalid failed, valid failed, invalid passed, invalid failed for wrong reason, percent classified correctly according to spec)

|Category|V Pass|I Fail|🔴 V Fail|🔵 I Pass|🔶 I Bad|Score|
|-|-|-|-|-|-|-|
|[0. Not mentioned in spec](#0-not-mentioned-in-spec)|1|10|0|0|0|100%|
|[2. Fundamentals](#2-fundamentals)|0|22|0|1|4|81%|
|[3. Model structure](#3-model-structure)|0|122|0|0|1|99%|
|[4. Mathematics](#4-mathematics)|0|0|0|0|0|0%|
|[5. Units](#5-units)|0|0|0|0|0|0%|
|[6. Grouping](#6-grouping)|0|0|0|0|0|0%|
|[7. Reactions](#7-reactions)|0|0|0|0|0|0%|
|[8. Metadata framework](#8-metadata-framework)|0|0|0|0|0|0%|
|[C. Advanced units functionality](#c-advanced-units-functionality)|0|0|0|0|0|0%|


---

## 0. Not mentioned in spec

### 0.0

[0.0.root_namespace_1](../models_1_0/valid/0.0.root_namespace_1.cellml): Valid file passed validation.

❗`0.0.root_namespace_2`: **Test not run**

[0.0.root_node_namespace_wrong](../models_1_0/invalid/0.0.root_node_namespace_wrong.cellml): Error detected correctly.
* Expected: ```Root node must be in CellML```
* Output: ```Error on line 5. Root node must be in CellML 1.0 or 1.1 namespace.```

[0.0.root_node_not_model](../models_1_0/invalid/0.0.root_node_not_model.cellml): Error detected correctly.
* Expected: ```Root node must be a CellML model```
* Output: ```Error on line 5. Root node must be a CellML model element.```

[0.0.root_node_two_elements](../models_1_0/invalid/0.0.root_node_two_elements.cellml): Error detected correctly.
* Expected: ```Extra content at the end of the document```
* Output: ```Unable to parse XML: Extra content at the end of the document, line 6, column 1 (0.0.root_node_two_elements.cellml, line 6)```

[0.0.root_node_two_models](../models_1_0/invalid/0.0.root_node_two_models.cellml): Error detected correctly.
* Expected: ```Extra content at the end of the document```
* Output: ```Unable to parse XML: Extra content at the end of the document, line 6, column 1 (0.0.root_node_two_models.cellml, line 6)```


---

### 0.1

[0.1.real_number_invalid_1](../models_1_0/invalid/0.1.real_number_invalid_1.cellml): Error detected correctly.
* Expected: ```must be a real number```
* Output: ```Error on line 7. If given, a variable initial_value must be a real number (3.4.3.7).```

[0.1.real_number_invalid_2](../models_1_0/invalid/0.1.real_number_invalid_2.cellml): Error detected correctly.
* Expected: ```must be a real number```
* Output: ```Error on line 7. If given, a variable initial_value must be a real number (3.4.3.7).```

[0.1.real_number_invalid_3](../models_1_0/invalid/0.1.real_number_invalid_3.cellml): Error detected correctly.
* Expected: ```must be a real number```
* Output: ```Error on line 7. If given, a variable initial_value must be a real number (3.4.3.7).```

[0.1.real_number_invalid_4](../models_1_0/invalid/0.1.real_number_invalid_4.cellml): Error detected correctly.
* Expected: ```must be a real number```
* Output: ```Error on line 7. If given, a variable initial_value must be a real number (3.4.3.7).```

[0.1.real_number_invalid_5](../models_1_0/invalid/0.1.real_number_invalid_5.cellml): Error detected correctly.
* Expected: ```must be a real number```
* Output: ```Error on line 7. If given, a variable initial_value must be a real number (3.4.3.7).```

[0.1.real_number_invalid_6](../models_1_0/invalid/0.1.real_number_invalid_6.cellml): Error detected correctly.
* Expected: ```must be a real number```
* Output: ```Error on line 7. If given, a variable initial_value must be a real number (3.4.3.7).```

❗`0.1.real_numbers`: **Test not run**

❗`0.1.real_numbers_extreme`: **Test not run**

❗`0.2.component_name_same_as_model`: **Test not run**

❗`0.2.variable_name_same_as_model`: **Test not run**


---

## 2. Fundamentals

#### 2.4.1

[2.4.1.identifier_empty](../models_1_0/invalid/2.4.1.identifier_empty.cellml): Error detected correctly.
* Expected: ```valid CellML identifier```
* Output: ```Error on line 6. Component name must be a valid CellML identifier (3.4.2.2).```

[2.4.1.identifier_only_underscore](../models_1_0/invalid/2.4.1.identifier_only_underscore.cellml): Error detected correctly.
* Expected: ```valid CellML identifier```
* Output: ```Error on line 6. Component name must be a valid CellML identifier (3.4.2.2).```

[2.4.1.identifier_unexpected_character_1](../models_1_0/invalid/2.4.1.identifier_unexpected_character_1.cellml): Error detected correctly.
* Expected: ```valid CellML identifier```
* Output: ```Error on line 6. Component name must be a valid CellML identifier (3.4.2.2).```

[2.4.1.identifier_unexpected_character_2](../models_1_0/invalid/2.4.1.identifier_unexpected_character_2.cellml): Error detected correctly.
* Expected: ```valid CellML identifier```
* Output: ```Error on line 6. Component name must be a valid CellML identifier (3.4.2.2).```

[2.4.1.identifier_unexpected_character_unicode](../models_1_0/invalid/2.4.1.identifier_unexpected_character_unicode.cellml): Error detected correctly.
* Expected: ```valid CellML identifier```
* Output: ```Error on line 6. Component name must be a valid CellML identifier (3.4.2.2).```

❗`2.4.1.valid_identifiers`: **Test not run**


---

#### 2.4.2

[2.4.2.imaginary_attributes_1](../models_1_0/invalid/2.4.2.imaginary_attributes_1.cellml): Error detected correctly.
* Expected: ```Unexpected attribute fruit```
* Output: ```Error on line 7. Unexpected attribute fruit found in cellml:model[@name="imaginary_attributes_1"].```

🔶 [2.4.2.imaginary_attributes_2](../models_1_0/invalid/2.4.2.imaginary_attributes_2.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Unexpected attribute cellml:fruit found in cellml:model[@name="imaginary_attributes_2"].```

[2.4.2.imaginary_elements](../models_1_0/invalid/2.4.2.imaginary_elements.cellml): Error detected correctly.
* Expected: ```found element of type cellml:fruit```
* Output: ```Error on line 6. Unexpected content type in cellml:model[@name="imaginary_elements"], found element of type cellml:fruit.```


---

#### 2.4.3

🔵 [2.4.3.cellml_attributes_inside_extensions](../models_1_0/invalid/2.4.3.cellml_attributes_inside_extensions.cellml): **Error not detected.**
* Output: ```OK```

[2.4.3.cellml_elements_inside_extensions](../models_1_0/invalid/2.4.3.cellml_elements_inside_extensions.cellml): Error detected correctly.
* Expected: ```CellML element cellml:component found inside extension element```
* Output: ```Error on line 9. CellML element cellml:component found inside extension element {http://fruit.org}banana (2.4.3).```

❗`2.4.3.component_ref_with_extensions`: **Test not run**

❗`2.4.3.component_with_extensions`: **Test not run**

❗`2.4.3.connection_with_extensions`: **Test not run**

❗`2.4.3.group_with_extensions`: **Test not run**

❗`2.4.3.map_components_with_extensions`: **Test not run**

❗`2.4.3.map_variables_with_extensions`: **Test not run**

❗`2.4.3.model_with_extensions`: **Test not run**

❗`2.4.3.reaction_with_extensions`: **Test not run**

❗`2.4.3.relationship_ref_with_extensions`: **Test not run**

❗`2.4.3.role_with_extensions`: **Test not run**

❗`2.4.3.unit_with_extensions`: **Test not run**

❗`2.4.3.units_with_extensions`: **Test not run**

❗`2.4.3.variable_ref_with_extensions`: **Test not run**

❗`2.4.3.variable_with_extensions`: **Test not run**

❗`2.4.4.model_linux_line_breaks`: **Test not run**

❗`2.4.4.model_windows_line_breaks`: **Test not run**

❗`2.4.4.model_with_spaces`: **Test not run**

❗`2.4.4.model_with_tabs`: **Test not run**


---

#### 2.4.4

[2.4.4.text_in_component](../models_1_0/invalid/2.4.4.text_in_component.cellml): Error detected correctly.
* Expected: ```Text found in cellml:component```
* Output: ```Error on line 6. Text found in cellml:component[@name="c1"].```

[2.4.4.text_in_component_ref](../models_1_0/invalid/2.4.4.text_in_component_ref.cellml): Error detected correctly.
* Expected: ```Text found in cellml:component_ref```
* Output: ```Error on line 11. Text found in cellml:component_ref.```

[2.4.4.text_in_connection](../models_1_0/invalid/2.4.4.text_in_connection.cellml): Error detected correctly.
* Expected: ```Text found in cellml:connection```
* Output: ```Error on line 14. Text found in cellml:connection (after cellml:map_variables element).```

[2.4.4.text_in_group](../models_1_0/invalid/2.4.4.text_in_group.cellml): Error detected correctly.
* Expected: ```Text found in cellml:group```
* Output: ```Error on line 10. Text found in cellml:group (after cellml:component_ref element).```

[2.4.4.text_in_map_components](../models_1_0/invalid/2.4.4.text_in_map_components.cellml): Error detected correctly.
* Expected: ```Text found in cellml:map_components```
* Output: ```Error on line 7. Text found in cellml:map_components.```

[2.4.4.text_in_map_variables](../models_1_0/invalid/2.4.4.text_in_map_variables.cellml): Error detected correctly.
* Expected: ```Text found in cellml:map_variables```
* Output: ```Error on line 14. Text found in cellml:map_variables.```

[2.4.4.text_in_model](../models_1_0/invalid/2.4.4.text_in_model.cellml): Error detected correctly.
* Expected: ```Text found in cellml:model```
* Output: ```Error on line 5. Text found in cellml:model[@name="text_in_model"].```

🔶 [2.4.4.text_in_reaction](../models_1_0/invalid/2.4.4.text_in_reaction.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

[2.4.4.text_in_relationship_ref](../models_1_0/invalid/2.4.4.text_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```Text found in cellml:relationship_ref```
* Output: ```Error on line 9. Text found in cellml:relationship_ref.```

🔶 [2.4.4.text_in_role](../models_1_0/invalid/2.4.4.text_in_role.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

[2.4.4.text_in_unit](../models_1_0/invalid/2.4.4.text_in_unit.cellml): Error detected correctly.
* Expected: ```Text found in cellml:unit```
* Output: ```Error on line 7. Text found in cellml:unit.```

[2.4.4.text_in_units_1](../models_1_0/invalid/2.4.4.text_in_units_1.cellml): Error detected correctly.
* Expected: ```Text found in cellml:units```
* Output: ```Error on line 7. Text found in cellml:units[@name="orange"] (after cellml:unit element).```

[2.4.4.text_in_units_2](../models_1_0/invalid/2.4.4.text_in_units_2.cellml): Error detected correctly.
* Expected: ```Text found in cellml:units```
* Output: ```Error on line 8. Text found in cellml:units[@name="apple"] (after cellml:unit element).```

[2.4.4.text_in_variable](../models_1_0/invalid/2.4.4.text_in_variable.cellml): Error detected correctly.
* Expected: ```Text found in cellml:variable```
* Output: ```Error on line 7. Text found in cellml:variable[@name="a"].```

🔶 [2.4.4.text_in_variable_ref](../models_1_0/invalid/2.4.4.text_in_variable_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```


---

#### 2.5.1

[2.5.1.identifiers_are_case_sensitive](../models_1_0/invalid/2.5.1.identifiers_are_case_sensitive.cellml): Error detected correctly.
* Expected: ```must refer to a component in the current model```
* Output: ```Error on line 13. A map_components component_1 attribute must refer to a component in the current model, got "a" (3.4.5.2).```


---

#### 2.5.2

[2.5.2.attribute_in_cellml_namespace](../models_1_0/invalid/2.5.2.attribute_in_cellml_namespace.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cellml:private_interface```
* Output: ```Error on line 8. Unexpected attribute cellml:private_interface found in cellml:variable[@name="v"].```

❗`3.4.1.1.model_child_order_1`: **Test not run**

❗`3.4.1.1.model_child_order_2`: **Test not run**

❗`3.4.1.1.model_empty`: **Test not run**


---

## 3. Model structure

##### 3.4.1.1

[3.4.1.1.model_name_missing](../models_1_0/invalid/3.4.1.1.model_name_missing.cellml): Error detected correctly.
* Expected: ```must have a name attribute```
* Output: ```Error on line 4. Model element must have a name attribute (3.4.1.1).```

[3.4.1.1.model_with_component_ref](../models_1_0/invalid/3.4.1.1.model_with_component_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component_ref```
* Output: ```Error on line 6. Unexpected content type in cellml:model[@name="model_with_component_ref"], found element of type cellml:component_ref.```

❗`3.4.1.1.model_with_components`: **Test not run**

❗`3.4.1.1.model_with_connections`: **Test not run**

❗`3.4.1.1.model_with_groups`: **Test not run**

[3.4.1.1.model_with_map_components](../models_1_0/invalid/3.4.1.1.model_with_map_components.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_components```
* Output: ```Error on line 8. Unexpected content type in cellml:model[@name="model_with_map_components"], found element of type cellml:map_components.```

[3.4.1.1.model_with_map_variables](../models_1_0/invalid/3.4.1.1.model_with_map_variables.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_variables```
* Output: ```Error on line 12. Unexpected content type in cellml:model[@name="model_with_map_variables"], found element of type cellml:map_variables.```

[3.4.1.1.model_with_math](../models_1_0/invalid/3.4.1.1.model_with_math.cellml): Error detected correctly.
* Expected: ```found element of type mathml:math```
* Output: ```Error on line 10. Unexpected content type in cellml:model[@name="model_with_math"], found element of type mathml:math.```

[3.4.1.1.model_with_model](../models_1_0/invalid/3.4.1.1.model_with_model.cellml): Error detected correctly.
* Expected: ```found element of type cellml:model```
* Output: ```Error on line 6. Unexpected content type in cellml:model[@name="model_with_model"], found element of type cellml:model.```

❗`3.4.1.1.model_with_one_component`: **Test not run**

❗`3.4.1.1.model_with_one_connection`: **Test not run**

❗`3.4.1.1.model_with_one_group`: **Test not run**

❗`3.4.1.1.model_with_one_units`: **Test not run**

[3.4.1.1.model_with_reaction](../models_1_0/invalid/3.4.1.1.model_with_reaction.cellml): Error detected correctly.
* Expected: ```found element of type cellml:reaction```
* Output: ```Error on line 9. Unexpected content type in cellml:model[@name="model_with_reaction"], found element of type cellml:reaction.```

[3.4.1.1.model_with_relationship_ref](../models_1_0/invalid/3.4.1.1.model_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:relationship_ref```
* Output: ```Error on line 6. Unexpected content type in cellml:model[@name="model_with_relationship_ref"], found element of type cellml:relationship_ref.```

[3.4.1.1.model_with_role](../models_1_0/invalid/3.4.1.1.model_with_role.cellml): Error detected correctly.
* Expected: ```found element of type cellml:role```
* Output: ```Error on line 6. Unexpected content type in cellml:model[@name="model_with_role"], found element of type cellml:role.```

[3.4.1.1.model_with_unit](../models_1_0/invalid/3.4.1.1.model_with_unit.cellml): Error detected correctly.
* Expected: ```found element of type cellml:unit```
* Output: ```Error on line 6. Unexpected content type in cellml:model[@name="model_with_unit"], found element of type cellml:unit.```

❗`3.4.1.1.model_with_units`: **Test not run**

[3.4.1.1.model_with_variable](../models_1_0/invalid/3.4.1.1.model_with_variable.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable```
* Output: ```Error on line 6. Unexpected content type in cellml:model[@name="model_with_variable"], found element of type cellml:variable.```

[3.4.1.1.model_with_variable_ref](../models_1_0/invalid/3.4.1.1.model_with_variable_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable_ref```
* Output: ```Error on line 6. Unexpected content type in cellml:model[@name="model_with_variable_ref"], found element of type cellml:variable_ref.```


---

##### 3.4.1.2

[3.4.1.2.model_name_invalid](../models_1_0/invalid/3.4.1.2.model_name_invalid.cellml): Error detected correctly.
* Expected: ```Model name must be a valid CellML identifier```
* Output: ```Error on line 4. Model name must be a valid CellML identifier (3.4.1.2).```

❗`3.4.2.1.component_child_order_1`: **Test not run**

❗`3.4.2.1.component_child_order_2`: **Test not run**

❗`3.4.2.1.component_empty`: **Test not run**


---

##### 3.4.2.1

[3.4.2.1.component_name_missing](../models_1_0/invalid/3.4.2.1.component_name_missing.cellml): Error detected correctly.
* Expected: ```Component element must have a name attribute```
* Output: ```Error on line 6. Component element must have a name attribute (3.4.2.1).```

[3.4.2.1.component_with_component](../models_1_0/invalid/3.4.2.1.component_with_component.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="c1"], found element of type cellml:component.```

[3.4.2.1.component_with_component_ref](../models_1_0/invalid/3.4.2.1.component_with_component_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component_ref```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="component"], found element of type cellml:component_ref.```

[3.4.2.1.component_with_connection](../models_1_0/invalid/3.4.2.1.component_with_connection.cellml): Error detected correctly.
* Expected: ```found element of type cellml:connection```
* Output: ```Error on line 13. Unexpected content type in cellml:component[@name="C"], found element of type cellml:connection.```

[3.4.2.1.component_with_group](../models_1_0/invalid/3.4.2.1.component_with_group.cellml): Error detected correctly.
* Expected: ```found element of type cellml:group```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="A"], found element of type cellml:group.```

[3.4.2.1.component_with_map_components](../models_1_0/invalid/3.4.2.1.component_with_map_components.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_components```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="c1"], found element of type cellml:map_components.```

[3.4.2.1.component_with_map_variables](../models_1_0/invalid/3.4.2.1.component_with_map_variables.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_variables```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="c1"], found element of type cellml:map_variables.```

❗`3.4.2.1.component_with_maths`: **Test not run**

[3.4.2.1.component_with_model](../models_1_0/invalid/3.4.2.1.component_with_model.cellml): Error detected correctly.
* Expected: ```found element of type cellml:model```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="c1"], found element of type cellml:model.```

❗`3.4.2.1.component_with_one_math`: **Test not run**

❗`3.4.2.1.component_with_one_reaction`: **Test not run**

❗`3.4.2.1.component_with_one_units`: **Test not run**

❗`3.4.2.1.component_with_one_variable`: **Test not run**

❗`3.4.2.1.component_with_reactions`: **Test not run**

[3.4.2.1.component_with_relationship_ref](../models_1_0/invalid/3.4.2.1.component_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:relationship_ref```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="component"], found element of type cellml:relationship_ref.```

[3.4.2.1.component_with_role](../models_1_0/invalid/3.4.2.1.component_with_role.cellml): Error detected correctly.
* Expected: ```found element of type cellml:role```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="component"], found element of type cellml:role.```

[3.4.2.1.component_with_unit](../models_1_0/invalid/3.4.2.1.component_with_unit.cellml): Error detected correctly.
* Expected: ```found element of type cellml:unit```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="component"], found element of type cellml:unit.```

❗`3.4.2.1.component_with_units`: **Test not run**

[3.4.2.1.component_with_variable_ref](../models_1_0/invalid/3.4.2.1.component_with_variable_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable_ref```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="component"], found element of type cellml:variable_ref.```

❗`3.4.2.1.component_with_variables`: **Test not run**


---

##### 3.4.2.2

[3.4.2.2.component_name_duplicate](../models_1_0/invalid/3.4.2.2.component_name_duplicate.cellml): Error detected correctly.
* Expected: ```Component name must be unique```
* Output: ```Error on line 7. Component name must be unique within model (3.4.2.2).```

[3.4.2.2.component_name_invalid](../models_1_0/invalid/3.4.2.2.component_name_invalid.cellml): Error detected correctly.
* Expected: ```Component name must be a valid CellML identifier```
* Output: ```Error on line 6. Component name must be a valid CellML identifier (3.4.2.2).```


---

##### 3.4.3.1

[3.4.3.1.variable_name_missing](../models_1_0/invalid/3.4.3.1.variable_name_missing.cellml): Error detected correctly.
* Expected: ```Variable element must have a name attribute```
* Output: ```Error on line 7. Variable element must have a name attribute (3.4.3.1).```

[3.4.3.1.variable_units_missing](../models_1_0/invalid/3.4.3.1.variable_units_missing.cellml): Error detected correctly.
* Expected: ```Variable element must have a units attribute```
* Output: ```Error on line 7. Variable element must have a units attribute (3.4.3.1).```

[3.4.3.1.variable_with_component](../models_1_0/invalid/3.4.3.1.variable_with_component.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component```
* Output: ```Error on line 8. Unexpected content type in cellml:variable[@name="x"], found element of type cellml:component.```

[3.4.3.1.variable_with_component_ref](../models_1_0/invalid/3.4.3.1.variable_with_component_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component_ref```
* Output: ```Error on line 8. Unexpected content type in cellml:variable[@name="x"], found element of type cellml:component_ref.```

[3.4.3.1.variable_with_connection](../models_1_0/invalid/3.4.3.1.variable_with_connection.cellml): Error detected correctly.
* Expected: ```found element of type cellml:connection```
* Output: ```Error on line 14. Unexpected content type in cellml:variable[@name="b"], found element of type cellml:connection.```

[3.4.3.1.variable_with_group](../models_1_0/invalid/3.4.3.1.variable_with_group.cellml): Error detected correctly.
* Expected: ```found element of type cellml:group```
* Output: ```Error on line 8. Unexpected content type in cellml:variable[@name="x"], found element of type cellml:group.```

❗`3.4.3.1.variable_with_initial_value`: **Test not run**

❗`3.4.3.1.variable_with_interfaces`: **Test not run**

[3.4.3.1.variable_with_map_components](../models_1_0/invalid/3.4.3.1.variable_with_map_components.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_components```
* Output: ```Error on line 8. Unexpected content type in cellml:variable[@name="x"], found element of type cellml:map_components.```

[3.4.3.1.variable_with_map_variables](../models_1_0/invalid/3.4.3.1.variable_with_map_variables.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_variables```
* Output: ```Error on line 8. Unexpected content type in cellml:variable[@name="x"], found element of type cellml:map_variables.```

[3.4.3.1.variable_with_math](../models_1_0/invalid/3.4.3.1.variable_with_math.cellml): Error detected correctly.
* Expected: ```found element of type mathml:math```
* Output: ```Error on line 9. Unexpected content type in cellml:variable[@name="a"], found element of type mathml:math.```

[3.4.3.1.variable_with_model](../models_1_0/invalid/3.4.3.1.variable_with_model.cellml): Error detected correctly.
* Expected: ```found element of type cellml:model```
* Output: ```Error on line 8. Unexpected content type in cellml:variable[@name="x"], found element of type cellml:model.```

[3.4.3.1.variable_with_reaction](../models_1_0/invalid/3.4.3.1.variable_with_reaction.cellml): Error detected correctly.
* Expected: ```found element of type cellml:reaction```
* Output: ```Error on line 8. Unexpected content type in cellml:variable[@name="x"], found element of type cellml:reaction.```

[3.4.3.1.variable_with_relationship_ref](../models_1_0/invalid/3.4.3.1.variable_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:relationship_ref```
* Output: ```Error on line 8. Unexpected content type in cellml:variable[@name="x"], found element of type cellml:relationship_ref.```

[3.4.3.1.variable_with_role](../models_1_0/invalid/3.4.3.1.variable_with_role.cellml): Error detected correctly.
* Expected: ```found element of type cellml:role```
* Output: ```Error on line 8. Unexpected content type in cellml:variable[@name="x"], found element of type cellml:role.```

[3.4.3.1.variable_with_unit](../models_1_0/invalid/3.4.3.1.variable_with_unit.cellml): Error detected correctly.
* Expected: ```found element of type cellml:unit```
* Output: ```Error on line 8. Unexpected content type in cellml:variable[@name="x"], found element of type cellml:unit.```

[3.4.3.1.variable_with_units](../models_1_0/invalid/3.4.3.1.variable_with_units.cellml): Error detected correctly.
* Expected: ```found element of type cellml:units```
* Output: ```Error on line 8. Unexpected content type in cellml:variable[@name="x"], found element of type cellml:units.```

[3.4.3.1.variable_with_variable](../models_1_0/invalid/3.4.3.1.variable_with_variable.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable```
* Output: ```Error on line 8. Unexpected content type in cellml:variable[@name="x"], found element of type cellml:variable.```

[3.4.3.1.variable_with_variable_ref](../models_1_0/invalid/3.4.3.1.variable_with_variable_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable_ref```
* Output: ```Error on line 8. Unexpected content type in cellml:variable[@name="x"], found element of type cellml:variable_ref.```

❗`3.4.3.1.variable_without_initial_value`: **Test not run**


---

##### 3.4.3.2

[3.4.3.2.variable_name_duplicate](../models_1_0/invalid/3.4.3.2.variable_name_duplicate.cellml): Error detected correctly.
* Expected: ```Variable name must be unique```
* Output: ```Error on line 8. Variable name must be unique within Component (3.4.3.2).```

[3.4.3.2.variable_name_invalid](../models_1_0/invalid/3.4.3.2.variable_name_invalid.cellml): Error detected correctly.
* Expected: ```Variable name must be a valid CellML identifier```
* Output: ```Error on line 7. Variable name must be a valid CellML identifier (3.4.3.2).```

❗`3.4.3.2.variable_name_same_as_cousin`: **Test not run**

❗`3.4.3.2.variable_name_same_as_parent`: **Test not run**

❗`3.4.3.3.variable_units_component`: **Test not run**

❗`3.4.3.3.variable_units_model`: **Test not run**


---

##### 3.4.3.3

[3.4.3.3.variable_units_other_component](../models_1_0/invalid/3.4.3.3.variable_units_other_component.cellml): Error detected correctly.
* Expected: ```must reference a units element```
* Output: ```Error on line 7. Variable units attribute must reference a units element in the current component or model, or one of the predefined units (3.4.3.3).```

❗`3.4.3.3.variable_units_predefined`: **Test not run**

[3.4.3.3.variable_units_unknown](../models_1_0/invalid/3.4.3.3.variable_units_unknown.cellml): Error detected correctly.
* Expected: ```must reference a units element```
* Output: ```Error on line 7. Variable units attribute must reference a units element in the current component or model, or one of the predefined units (3.4.3.3).```


---

##### 3.4.3.4

[3.4.3.4.variable_interface_public_invalid](../models_1_0/invalid/3.4.3.4.variable_interface_public_invalid.cellml): Error detected correctly.
* Expected: ```Public interface must be```
* Output: ```Error on line 7. Public interface must be "in", "out", or "none" (3.4.3.4).```


---

##### 3.4.3.5

[3.4.3.5.variable_interface_private_invalid](../models_1_0/invalid/3.4.3.5.variable_interface_private_invalid.cellml): Error detected correctly.
* Expected: ```Private interface must be```
* Output: ```Error on line 7. Private interface must be "in", "out", or "none" (3.4.3.5).```


---

##### 3.4.3.6

[3.4.3.6.variable_interfaces_both_in](../models_1_0/invalid/3.4.3.6.variable_interfaces_both_in.cellml): Error detected correctly.
* Expected: ```can not both be "in"```
* Output: ```Error on line 10. Public and private interface can not both be "in" (3.4.3.6).```


---

##### 3.4.3.7

[3.4.3.7.variable_initial_value_empty](../models_1_0/invalid/3.4.3.7.variable_initial_value_empty.cellml): Error detected correctly.
* Expected: ```initial_value must be a real number```
* Output: ```Error on line 7. If given, a variable initial_value must be a real number (3.4.3.7).```

[3.4.3.7.variable_initial_value_invalid](../models_1_0/invalid/3.4.3.7.variable_initial_value_invalid.cellml): Error detected correctly.
* Expected: ```initial_value must be a real number```
* Output: ```Error on line 7. If given, a variable initial_value must be a real number (3.4.3.7).```


---

##### 3.4.3.8

[3.4.3.8.variable_interfaces_private_in_and_initial](../models_1_0/invalid/3.4.3.8.variable_interfaces_private_in_and_initial.cellml): Error detected correctly.
* Expected: ```initial value cannot be set```
* Output: ```Error on line 11. An initial value cannot be set for Variable[@name="a"] in Component[@name="A"], which has private_interface="in" (3.4.3.8).```

[3.4.3.8.variable_interfaces_public_in_and_initial](../models_1_0/invalid/3.4.3.8.variable_interfaces_public_in_and_initial.cellml): Error detected correctly.
* Expected: ```initial value cannot be set```
* Output: ```Error on line 11. An initial value cannot be set for Variable[@name="a"] in Component[@name="A"], which has public_interface="in" (3.4.3.8).```


---

##### 3.4.4.1

[3.4.4.1.connection_empty](../models_1_0/invalid/3.4.4.1.connection_empty.cellml): Error detected correctly.
* Expected: ```exactly one map_component```
* Output: ```Error on line 6. A connection must contain exactly one map_components element, found 0 (3.4.4.1).```

[3.4.4.1.connection_map_components_missing](../models_1_0/invalid/3.4.4.1.connection_map_components_missing.cellml): Error detected correctly.
* Expected: ```exactly one map_components```
* Output: ```Error on line 14. A connection must contain exactly one map_components element, found 0 (3.4.4.1).```

[3.4.4.1.connection_map_components_multiple](../models_1_0/invalid/3.4.4.1.connection_map_components_multiple.cellml): Error detected correctly.
* Expected: ```exactly one map_components```
* Output: ```Error on line 17. A connection must contain exactly one map_components element, found 2 (3.4.4.1).```

[3.4.4.1.connection_map_variables_missing_1](../models_1_0/invalid/3.4.4.1.connection_map_variables_missing_1.cellml): Error detected correctly.
* Expected: ```at least one map_variables```
* Output: ```Error on line 12. A connection must contain at least one map_variables element (3.4.4.1).```

[3.4.4.1.connection_map_variables_missing_2](../models_1_0/invalid/3.4.4.1.connection_map_variables_missing_2.cellml): Error detected correctly.
* Expected: ```at least one map_variables```
* Output: ```Error on line 13. A connection must contain at least one map_variables element (3.4.4.1).```

[3.4.4.1.connection_only_extensions](../models_1_0/invalid/3.4.4.1.connection_only_extensions.cellml): Error detected correctly.
* Expected: ```exactly one map_components```
* Output: ```Error on line 7. A connection must contain exactly one map_components element, found 0 (3.4.4.1).```

[3.4.4.1.connection_with_component](../models_1_0/invalid/3.4.4.1.connection_with_component.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type cellml:component.```

[3.4.4.1.connection_with_component_ref](../models_1_0/invalid/3.4.4.1.connection_with_component_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component_ref```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type cellml:component_ref.```

[3.4.4.1.connection_with_connection](../models_1_0/invalid/3.4.4.1.connection_with_connection.cellml): Error detected correctly.
* Expected: ```found element of type cellml:connection```
* Output: ```Error on line 19. Unexpected content type in cellml:connection, found element of type cellml:connection.```

[3.4.4.1.connection_with_group](../models_1_0/invalid/3.4.4.1.connection_with_group.cellml): Error detected correctly.
* Expected: ```found element of type cellml:group```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type cellml:group.```

❗`3.4.4.1.connection_with_map_variables`: **Test not run**

[3.4.4.1.connection_with_math](../models_1_0/invalid/3.4.4.1.connection_with_math.cellml): Error detected correctly.
* Expected: ```found element of type mathml:math```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type mathml:math.```

[3.4.4.1.connection_with_model](../models_1_0/invalid/3.4.4.1.connection_with_model.cellml): Error detected correctly.
* Expected: ```found element of type cellml:model```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type cellml:model.```

[3.4.4.1.connection_with_name_attribute](../models_1_0/invalid/3.4.4.1.connection_with_name_attribute.cellml): Error detected correctly.
* Expected: ```Unexpected attribute name```
* Output: ```Error on line 12. Unexpected attribute name found in cellml:connection.```

❗`3.4.4.1.connection_with_one_map_variables`: **Test not run**

[3.4.4.1.connection_with_reaction](../models_1_0/invalid/3.4.4.1.connection_with_reaction.cellml): Error detected correctly.
* Expected: ```found element of type cellml:reaction```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type cellml:reaction.```

[3.4.4.1.connection_with_relationship_ref](../models_1_0/invalid/3.4.4.1.connection_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:relationship_ref```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type cellml:relationship_ref.```

[3.4.4.1.connection_with_role](../models_1_0/invalid/3.4.4.1.connection_with_role.cellml): Error detected correctly.
* Expected: ```found element of type cellml:role```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type cellml:role.```

[3.4.4.1.connection_with_unit](../models_1_0/invalid/3.4.4.1.connection_with_unit.cellml): Error detected correctly.
* Expected: ```found element of type cellml:unit```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type cellml:unit.```

[3.4.4.1.connection_with_units](../models_1_0/invalid/3.4.4.1.connection_with_units.cellml): Error detected correctly.
* Expected: ```found element of type cellml:units```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type cellml:units.```

[3.4.4.1.connection_with_variable](../models_1_0/invalid/3.4.4.1.connection_with_variable.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type cellml:variable.```

[3.4.4.1.connection_with_variable_ref](../models_1_0/invalid/3.4.4.1.connection_with_variable_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable_ref```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type cellml:variable_ref.```

❗`3.4.5.1.connection_any_order_1`: **Test not run**

❗`3.4.5.1.connection_any_order_2`: **Test not run**


---

##### 3.4.5.1

[3.4.5.1.map_components_component_1_missing](../models_1_0/invalid/3.4.5.1.map_components_component_1_missing.cellml): Error detected correctly.
* Expected: ```must define a component_1 attribute```
* Output: ```Error on line 7. A map_components element must define a component_1 attribute (3.4.5.1).```

[3.4.5.1.map_components_component_2_missing](../models_1_0/invalid/3.4.5.1.map_components_component_2_missing.cellml): Error detected correctly.
* Expected: ```must define a component_2 attribute```
* Output: ```Error on line 7. A map_components element must define a component_2 attribute (3.4.5.1).```

[3.4.5.1.map_components_with_component](../models_1_0/invalid/3.4.5.1.map_components_with_component.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:component.```

[3.4.5.1.map_components_with_component_ref](../models_1_0/invalid/3.4.5.1.map_components_with_component_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component_ref```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:component_ref.```

[3.4.5.1.map_components_with_connection](../models_1_0/invalid/3.4.5.1.map_components_with_connection.cellml): Error detected correctly.
* Expected: ```found element of type cellml:connection```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:connection.```

[3.4.5.1.map_components_with_group](../models_1_0/invalid/3.4.5.1.map_components_with_group.cellml): Error detected correctly.
* Expected: ```found element of type cellml:group```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:group.```

[3.4.5.1.map_components_with_map_components](../models_1_0/invalid/3.4.5.1.map_components_with_map_components.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_components```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:map_components.```

[3.4.5.1.map_components_with_map_variables](../models_1_0/invalid/3.4.5.1.map_components_with_map_variables.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_variables```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:map_variables.```

[3.4.5.1.map_components_with_math](../models_1_0/invalid/3.4.5.1.map_components_with_math.cellml): Error detected correctly.
* Expected: ```found element of type mathml:math```
* Output: ```Error on line 9. Unexpected content type in cellml:map_components, found element of type mathml:math.```

[3.4.5.1.map_components_with_model](../models_1_0/invalid/3.4.5.1.map_components_with_model.cellml): Error detected correctly.
* Expected: ```found element of type cellml:model```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:model.```

[3.4.5.1.map_components_with_reaction](../models_1_0/invalid/3.4.5.1.map_components_with_reaction.cellml): Error detected correctly.
* Expected: ```found element of type cellml:reaction```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:reaction.```

[3.4.5.1.map_components_with_relationship_ref](../models_1_0/invalid/3.4.5.1.map_components_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:relationship_ref```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:relationship_ref.```

[3.4.5.1.map_components_with_role](../models_1_0/invalid/3.4.5.1.map_components_with_role.cellml): Error detected correctly.
* Expected: ```found element of type cellml:role```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:role.```

[3.4.5.1.map_components_with_unit](../models_1_0/invalid/3.4.5.1.map_components_with_unit.cellml): Error detected correctly.
* Expected: ```found element of type cellml:unit```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:unit.```

[3.4.5.1.map_components_with_units](../models_1_0/invalid/3.4.5.1.map_components_with_units.cellml): Error detected correctly.
* Expected: ```found element of type cellml:units```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:units.```

[3.4.5.1.map_components_with_variable](../models_1_0/invalid/3.4.5.1.map_components_with_variable.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:variable.```

[3.4.5.1.map_components_with_variable_ref](../models_1_0/invalid/3.4.5.1.map_components_with_variable_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable_ref```
* Output: ```Error on line 8. Unexpected content type in cellml:map_components, found element of type cellml:variable_ref.```


---

##### 3.4.5.2

[3.4.5.2.map_components_component_1_nonexistent](../models_1_0/invalid/3.4.5.2.map_components_component_1_nonexistent.cellml): Error detected correctly.
* Expected: ```component_1 attribute must refer to a component in the current model```
* Output: ```Error on line 8. A map_components component_1 attribute must refer to a component in the current model, got "c" (3.4.5.2).```


---

##### 3.4.5.3

[3.4.5.3.map_components_component_2_nonexistent](../models_1_0/invalid/3.4.5.3.map_components_component_2_nonexistent.cellml): Error detected correctly.
* Expected: ```component_2 attribute must refer to a component in the current model```
* Output: ```Error on line 8. A map_components component_2 attribute must refer to a component in the current model, got "c" (3.4.5.3).```


---

##### 3.4.5.4

[3.4.5.4.map_components_component_1_equals_2](../models_1_0/invalid/3.4.5.4.map_components_component_1_equals_2.cellml): Error detected correctly.
* Expected: ```must be different```
* Output: ```Error on line 7. The component_1 and component_2 attributes in a map_components element must be different, got "A" twice (3.4.5.4).```

[3.4.5.4.map_components_duplicate](../models_1_0/invalid/3.4.5.4.map_components_duplicate.cellml): Error detected correctly.
* Expected: ```Each connection in a model must connect a unique pair```
* Output: ```Error on line 11. Each connection in a model must connect a unique pair of components, found multiple for "a" and "b" (3.4.5.4).```

[3.4.5.4.map_components_duplicate_mirrored](../models_1_0/invalid/3.4.5.4.map_components_duplicate_mirrored.cellml): Error detected correctly.
* Expected: ```Each connection in a model must connect a unique pair```
* Output: ```Error on line 11. Each connection in a model must connect a unique pair of components, found multiple for "b" and "a" (3.4.5.4).```


---

##### 3.4.6.1

[3.4.6.1.map_variables_variable_1_missing](../models_1_0/invalid/3.4.6.1.map_variables_variable_1_missing.cellml): Error detected correctly.
* Expected: ```must define a variable_1 attribute```
* Output: ```Error on line 14. A map_variables element must define a variable_1 attribute (3.4.6.1).```

[3.4.6.1.map_variables_variable_2_missing](../models_1_0/invalid/3.4.6.1.map_variables_variable_2_missing.cellml): Error detected correctly.
* Expected: ```must define a variable_2 attribute```
* Output: ```Error on line 14. A map_variables element must define a variable_2 attribute (3.4.6.1).```

[3.4.6.1.map_variables_with_component](../models_1_0/invalid/3.4.6.1.map_variables_with_component.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:component.```

[3.4.6.1.map_variables_with_component_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_component_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component_ref```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:component_ref.```

[3.4.6.1.map_variables_with_connection](../models_1_0/invalid/3.4.6.1.map_variables_with_connection.cellml): Error detected correctly.
* Expected: ```found element of type cellml:connection```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:connection.```

[3.4.6.1.map_variables_with_group](../models_1_0/invalid/3.4.6.1.map_variables_with_group.cellml): Error detected correctly.
* Expected: ```found element of type cellml:group```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:group.```

[3.4.6.1.map_variables_with_map_components](../models_1_0/invalid/3.4.6.1.map_variables_with_map_components.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_components```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:map_components.```

[3.4.6.1.map_variables_with_map_variables](../models_1_0/invalid/3.4.6.1.map_variables_with_map_variables.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_variables```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:map_variables.```

[3.4.6.1.map_variables_with_math](../models_1_0/invalid/3.4.6.1.map_variables_with_math.cellml): Error detected correctly.
* Expected: ```found element of type mathml:math```
* Output: ```Error on line 10. Unexpected content type in cellml:map_variables, found element of type mathml:math.```

[3.4.6.1.map_variables_with_model](../models_1_0/invalid/3.4.6.1.map_variables_with_model.cellml): Error detected correctly.
* Expected: ```found element of type cellml:model```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:model.```

[3.4.6.1.map_variables_with_reaction](../models_1_0/invalid/3.4.6.1.map_variables_with_reaction.cellml): Error detected correctly.
* Expected: ```found element of type cellml:reaction```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:reaction.```

[3.4.6.1.map_variables_with_relationship_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:relationship_ref```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:relationship_ref.```

[3.4.6.1.map_variables_with_role](../models_1_0/invalid/3.4.6.1.map_variables_with_role.cellml): Error detected correctly.
* Expected: ```found element of type cellml:role```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:role.```

[3.4.6.1.map_variables_with_unit](../models_1_0/invalid/3.4.6.1.map_variables_with_unit.cellml): Error detected correctly.
* Expected: ```found element of type cellml:unit```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:unit.```

[3.4.6.1.map_variables_with_units](../models_1_0/invalid/3.4.6.1.map_variables_with_units.cellml): Error detected correctly.
* Expected: ```found element of type cellml:units```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:units.```

[3.4.6.1.map_variables_with_variable](../models_1_0/invalid/3.4.6.1.map_variables_with_variable.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:variable.```

[3.4.6.1.map_variables_with_variable_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_variable_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable_ref```
* Output: ```Error on line 9. Unexpected content type in cellml:map_variables, found element of type cellml:variable_ref.```


---

##### 3.4.6.2

[3.4.6.2.map_variables_variable_1_nonexistent](../models_1_0/invalid/3.4.6.2.map_variables_variable_1_nonexistent.cellml): Error detected correctly.
* Expected: ```variable_1 attribute must refer to a variable```
* Output: ```Error on line 12. A map_variables variable_1 attribute must refer to a variable in component_1, got "a" (3.4.6.2).```


---

##### 3.4.6.3

[3.4.6.3.map_variables_variable_2_nonexistent](../models_1_0/invalid/3.4.6.3.map_variables_variable_2_nonexistent.cellml): Error detected correctly.
* Expected: ```variable_2 attribute must refer to a variable```
* Output: ```Error on line 12. A map_variables variable_2 attribute must refer to a variable in component_2, got "Variable[@name="a"] in Component[@name="c1"]" (3.4.6.3).```

❗`3.4.6.4.map_variables_chain_down`: **Test not run**

❗`3.4.6.4.map_variables_chain_up`: **Test not run**


---

##### 3.4.6.4

[3.4.6.4.map_variables_child_multiple_out_1](../models_1_0/invalid/3.4.6.4.map_variables_child_multiple_out_1.cellml): Error detected correctly.
* Expected: ```already connected```
* Output: ```Error on line 24. Invalid connection: Variable[@name="x"] in Component[@name="A"] has a public_interface of "in" and is already connected to a variable with an interface of "out".```

[3.4.6.4.map_variables_child_multiple_out_2](../models_1_0/invalid/3.4.6.4.map_variables_child_multiple_out_2.cellml): Error detected correctly.
* Expected: ```already connected```
* Output: ```Error on line 30. Invalid connection: Variable[@name="x"] in Component[@name="A"] has a public_interface of "in" and is already connected to a variable with an interface of "out".```

[3.4.6.4.map_variables_child_out_to_out_1](../models_1_0/invalid/3.4.6.4.map_variables_child_out_to_out_1.cellml): Error detected correctly.
* Expected: ```private_interface of "out", while```
* Output: ```Error on line 23. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a private_interface of "out", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "out" (3.4.6.4).```

[3.4.6.4.map_variables_child_out_to_out_2](../models_1_0/invalid/3.4.6.4.map_variables_child_out_to_out_2.cellml): Error detected correctly.
* Expected: ```private_interface of "out", while```
* Output: ```Error on line 23. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a private_interface of "out", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "out" (3.4.6.4).```

[3.4.6.4.map_variables_child_private_in](../models_1_0/invalid/3.4.6.4.map_variables_child_private_in.cellml): Error detected correctly.
* Expected: ```public_interface of "none"```
* Output: ```Error on line 23. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a private_interface of "out", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "none" (3.4.6.4).```

[3.4.6.4.map_variables_child_private_out](../models_1_0/invalid/3.4.6.4.map_variables_child_private_out.cellml): Error detected correctly.
* Expected: ```public_interface of "none"```
* Output: ```Error on line 23. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a private_interface of "in", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "none" (3.4.6.4).```

🔶 [3.4.6.4.map_variables_hidden_aunt_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_aunt_1.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 29. Connections can only be made between components that are siblings or have a parent-child (encapsulation) relationship (3.4.6.4).```

❗`3.4.6.4.map_variables_hidden_aunt_2`: **Test not run**

❗`3.4.6.4.map_variables_hidden_cousins_1`: **Test not run**

❗`3.4.6.4.map_variables_hidden_cousins_2`: **Test not run**

❗`3.4.6.4.map_variables_hidden_cousins_3`: **Test not run**

❗`3.4.6.4.map_variables_hidden_cousins_4`: **Test not run**

❗`3.4.6.4.map_variables_hidden_grandchild_1`: **Test not run**

❗`3.4.6.4.map_variables_hidden_grandchild_2`: **Test not run**

❗`3.4.6.4.map_variables_hidden_grandparent_1`: **Test not run**

❗`3.4.6.4.map_variables_hidden_grandparent_2`: **Test not run**

❗`3.4.6.4.map_variables_hidden_niece_1`: **Test not run**

❗`3.4.6.4.map_variables_hidden_niece_2`: **Test not run**

❗`3.4.6.4.map_variables_nested_sibling_connection`: **Test not run**

❗`3.4.6.4.map_variables_nested_sibling_private_in`: **Test not run**

❗`3.4.6.4.map_variables_nested_sibling_private_in_and_out`: **Test not run**

❗`3.4.6.4.map_variables_nested_sibling_private_out`: **Test not run**

❗`3.4.6.4.map_variables_parent_connection_1`: **Test not run**

❗`3.4.6.4.map_variables_parent_connection_2`: **Test not run**

❗`3.4.6.4.map_variables_parent_in_to_in_1`: **Test not run**

❗`3.4.6.4.map_variables_parent_in_to_in_2`: **Test not run**

❗`3.4.6.4.map_variables_parent_multiple_1`: **Test not run**

❗`3.4.6.4.map_variables_parent_multiple_2`: **Test not run**

❗`3.4.6.4.map_variables_parent_multiple_out`: **Test not run**

❗`3.4.6.4.map_variables_parent_out_to_out_1`: **Test not run**

❗`3.4.6.4.map_variables_parent_out_to_out_2`: **Test not run**

❗`3.4.6.4.map_variables_parent_public_in`: **Test not run**

❗`3.4.6.4.map_variables_parent_public_out`: **Test not run**

❗`3.4.6.4.map_variables_sibling_connection_1`: **Test not run**

❗`3.4.6.4.map_variables_sibling_connection_2`: **Test not run**

❗`3.4.6.4.map_variables_sibling_connection_3`: **Test not run**

❗`3.4.6.4.map_variables_sibling_in_to_in`: **Test not run**

❗`3.4.6.4.map_variables_sibling_multiple_1`: **Test not run**

❗`3.4.6.4.map_variables_sibling_multiple_2`: **Test not run**

❗`3.4.6.4.map_variables_sibling_multiple_out_1`: **Test not run**

❗`3.4.6.4.map_variables_sibling_multiple_out_2`: **Test not run**

❗`3.4.6.4.map_variables_sibling_mutual`: **Test not run**

❗`3.4.6.4.map_variables_sibling_out_to_out`: **Test not run**

❗`3.4.6.4.map_variables_sibling_private_in_1`: **Test not run**

❗`3.4.6.4.map_variables_sibling_private_in_2`: **Test not run**

❗`3.4.6.4.map_variables_sibling_private_in_and_out`: **Test not run**

❗`3.4.6.4.map_variables_sibling_private_out_1`: **Test not run**

❗`3.4.6.4.map_variables_sibling_private_out_2`: **Test not run**

❗`3.4.6.4.map_variables_talking_aunt`: **Test not run**

❗`3.4.6.4.map_variables_talking_cousins`: **Test not run**

❗`3.4.6.4.map_variables_talking_niece`: **Test not run**

❗`4.2.3_1.mathml_basics`: **Test not run**

❗`4.2.3_2.1.mathml_numbers_real`: **Test not run**

❗`4.2.3_2.2.mathml_numbers_integer`: **Test not run**

❗`4.2.3_2.3.mathml_numbers_real_base`: **Test not run**

❗`4.2.3_2.4.mathml_numbers_integer_base`: **Test not run**

❗`4.2.3_2.5.mathml_numbers_e_notation`: **Test not run**

❗`4.2.3_2.6.mathml_numbers_rational`: **Test not run**

❗`4.2.3_3.1_mathml_arithmetic_binary`: **Test not run**

❗`4.2.3_3.2_mathml_arithmetic_n_ary`: **Test not run**

❗`4.2.3_3.2_mathml_arithmetic_unary`: **Test not run**

❗`4.2.3_4.1_mathml_functions_basic`: **Test not run**

❗`4.2.3_4.2_mathml_functions_non_smooth`: **Test not run**

❗`4.2.3_4.3_mathml_functions_factorial`: **Test not run**

❗`4.2.3_4.4_mathml_functions_trig`: **Test not run**

❗`4.2.3_4.5_mathml_functions_trig_hyperbolic`: **Test not run**

❗`4.2.3_4.6_mathml_functions_trig_redundant`: **Test not run**

❗`4.2.3_4.7_mathml_functions_trig_redundant_hyperbolic`: **Test not run**

❗`4.2.3_5.1_mathml_derivatives`: **Test not run**

❗`4.2.3_5.2_mathml_derivatives_degree`: **Test not run**

❗`4.2.3_5.3_mathml_derivatives_with_units`: **Test not run**

❗`4.2.3_5.4_mathml_derivatives_with_units_degree`: **Test not run**

❗`4.2.3_6.1_mathml_logic_one_piece`: **Test not run**

❗`4.2.3_6.2_mathml_logic_two_pieces`: **Test not run**

❗`4.2.3_6.3_mathml_logic_no_otherwise`: **Test not run**

❗`4.2.3_6.4_mathml_logic_comparisons`: **Test not run**

❗`4.2.3_6.5_mathml_logic_unary_operators`: **Test not run**

❗`4.2.3_6.6_mathml_logic_binary_operators`: **Test not run**

❗`4.2.3_6.7_mathml_logic_constants`: **Test not run**

❗`4.2.3_7.1_mathml_pi`: **Test not run**

❗`4.2.3_7.2_mathml_e`: **Test not run**

❗`4.2.3_7.3_mathml_nan_inf`: **Test not run**

❗`4.2.3_8.1_annotation`: **Test not run**

❗`4.2.3_8.2_annotation_xml`: **Test not run**

❗`4.4.1.math_not_math_component`: **Test not run**

❗`4.4.1.math_not_math_reaction`: **Test not run**

❗`4.4.2.ci_no_whitespace`: **Test not run**

❗`4.4.2.ci_non_local_aunt`: **Test not run**

❗`4.4.2.ci_non_local_child`: **Test not run**

❗`4.4.2.ci_non_local_cousin`: **Test not run**

❗`4.4.2.ci_non_local_nested_sibling`: **Test not run**

❗`4.4.2.ci_non_local_niece`: **Test not run**

❗`4.4.2.ci_non_local_parent`: **Test not run**

❗`4.4.2.ci_non_local_sibling`: **Test not run**

❗`4.4.2.ci_nonexistent`: **Test not run**

❗`4.4.2.ci_whitespace_1`: **Test not run**

❗`4.4.2.ci_whitespace_2`: **Test not run**

❗`4.4.2.ci_whitespace_3`: **Test not run**

❗`4.4.3.1.cn_component_units`: **Test not run**

❗`4.4.3.1.cn_model_units`: **Test not run**

❗`4.4.3.1.cn_predefined_units`: **Test not run**

❗`4.4.3.1.cn_units_missing`: **Test not run**

❗`4.4.3.2.cn_units_nonexistent_1`: **Test not run**

❗`4.4.3.2.cn_units_nonexistent_2`: **Test not run**

❗`4.4.3.2.cn_units_parent_component`: **Test not run**

❗`4.4.4.modify_nonexistent`: **Test not run**

❗`4.4.4.modify_private_in`: **Test not run**

❗`4.4.4.modify_private_out`: **Test not run**

❗`4.4.4.modify_public_in`: **Test not run**

❗`4.4.4.modify_public_out`: **Test not run**

❗`4.5.1.ordering_not_significant`: **Test not run**

❗`4.algebraic_model`: **Test not run**

❗`4.algebraic_ode_model`: **Test not run**

❗`4.math_and_initial_value`: **Test not run**

❗`4.math_overdefined`: **Test not run**

❗`5.2.2.unit_deca`: **Test not run**

❗`5.2.7.unit_checking_arithmetic`: **Test not run**

❗`5.2.7.unit_checking_comparisons`: **Test not run**

❗`5.2.7.unit_checking_derivatives`: **Test not run**

❗`5.2.7.unit_checking_derivatives_degree`: **Test not run**

❗`5.2.7.unit_checking_dimensionless`: **Test not run**

❗`5.2.7.unit_checking_functions_factorial`: **Test not run**

❗`5.2.7.unit_checking_functions_non_smooth`: **Test not run**

❗`5.2.7.unit_checking_functions_power_and_root`: **Test not run**

❗`5.2.7.unit_checking_internal_mismatch_1`: **Test not run**

❗`5.2.7.unit_checking_internal_mismatch_2`: **Test not run**

❗`5.2.7.unit_checking_internal_mismatch_3`: **Test not run**

❗`5.2.7.unit_checking_internal_mismatch_4`: **Test not run**

❗`5.2.7.unit_checking_name_differs`: **Test not run**

❗`5.2.7.unit_checking_piecewise`: **Test not run**

❗`5.2.7.unit_checking_piecewise_multi_unit`: **Test not run**

❗`5.2.7.unit_checking_repeated_unit`: **Test not run**

❗`5.2.7.unit_conversion_different_names_same_unit`: **Test not run**

❗`5.2.7.unit_conversion_dimensionless_exponent`: **Test not run**

❗`5.2.7.unit_conversion_dimensionless_multiplier_1`: **Test not run**

❗`5.2.7.unit_conversion_dimensionless_multiplier_2`: **Test not run**

❗`5.2.7.unit_conversion_dimensionless_offset`: **Test not run**

❗`5.2.7.unit_conversion_inconvertible_1`: **Test not run**

❗`5.2.7.unit_conversion_less_obvious`: **Test not run**

❗`5.2.7.unit_conversion_multiplier`: **Test not run**

❗`5.2.7.unit_conversion_new_base_units`: **Test not run**

❗`5.2.7.unit_conversion_offset`: **Test not run**

❗`5.2.7.unit_conversion_prefix`: **Test not run**

❗`5.4.1.1.units_base_units`: **Test not run**

❗`5.4.1.1.units_base_units_with_children`: **Test not run**

❗`5.4.1.1.units_empty_1`: **Test not run**

❗`5.4.1.1.units_empty_2`: **Test not run**

❗`5.4.1.1.units_name_missing`: **Test not run**

❗`5.4.1.1.units_with_component`: **Test not run**

❗`5.4.1.1.units_with_component_ref`: **Test not run**

❗`5.4.1.1.units_with_connection`: **Test not run**

❗`5.4.1.1.units_with_group`: **Test not run**

❗`5.4.1.1.units_with_map_components`: **Test not run**

❗`5.4.1.1.units_with_map_variables`: **Test not run**

❗`5.4.1.1.units_with_math`: **Test not run**

❗`5.4.1.1.units_with_model`: **Test not run**

❗`5.4.1.1.units_with_reaction`: **Test not run**

❗`5.4.1.1.units_with_relationship_ref`: **Test not run**

❗`5.4.1.1.units_with_role`: **Test not run**

❗`5.4.1.1.units_with_unit_children`: **Test not run**

❗`5.4.1.1.units_with_units`: **Test not run**

❗`5.4.1.1.units_with_variable`: **Test not run**

❗`5.4.1.1.units_with_variable_ref`: **Test not run**

❗`5.4.1.2.units_name_duplicate_1`: **Test not run**

❗`5.4.1.2.units_name_duplicate_2`: **Test not run**

❗`5.4.1.2.units_name_invalid`: **Test not run**

❗`5.4.1.2.units_name_predefined_ampere`: **Test not run**

❗`5.4.1.2.units_name_predefined_becquerel`: **Test not run**

❗`5.4.1.2.units_name_predefined_candela`: **Test not run**

❗`5.4.1.2.units_name_predefined_celsius`: **Test not run**

❗`5.4.1.2.units_name_predefined_component_ampere`: **Test not run**

❗`5.4.1.2.units_name_predefined_coulomb`: **Test not run**

❗`5.4.1.2.units_name_predefined_dimensionless`: **Test not run**

❗`5.4.1.2.units_name_predefined_farad`: **Test not run**

❗`5.4.1.2.units_name_predefined_gram`: **Test not run**

❗`5.4.1.2.units_name_predefined_gray`: **Test not run**

❗`5.4.1.2.units_name_predefined_henry`: **Test not run**

❗`5.4.1.2.units_name_predefined_hertz`: **Test not run**

❗`5.4.1.2.units_name_predefined_joule`: **Test not run**

❗`5.4.1.2.units_name_predefined_katal`: **Test not run**

❗`5.4.1.2.units_name_predefined_kelvin`: **Test not run**

❗`5.4.1.2.units_name_predefined_kilogram`: **Test not run**

❗`5.4.1.2.units_name_predefined_liter`: **Test not run**

❗`5.4.1.2.units_name_predefined_litre`: **Test not run**

❗`5.4.1.2.units_name_predefined_lumen`: **Test not run**

❗`5.4.1.2.units_name_predefined_lux`: **Test not run**

❗`5.4.1.2.units_name_predefined_meter`: **Test not run**

❗`5.4.1.2.units_name_predefined_metre`: **Test not run**

❗`5.4.1.2.units_name_predefined_mole`: **Test not run**

❗`5.4.1.2.units_name_predefined_newton`: **Test not run**

❗`5.4.1.2.units_name_predefined_ohm`: **Test not run**

❗`5.4.1.2.units_name_predefined_pascal`: **Test not run**

❗`5.4.1.2.units_name_predefined_radian`: **Test not run**

❗`5.4.1.2.units_name_predefined_second`: **Test not run**

❗`5.4.1.2.units_name_predefined_siemens`: **Test not run**

❗`5.4.1.2.units_name_predefined_sievert`: **Test not run**

❗`5.4.1.2.units_name_predefined_steradian`: **Test not run**

❗`5.4.1.2.units_name_predefined_tesla`: **Test not run**

❗`5.4.1.2.units_name_predefined_volt`: **Test not run**

❗`5.4.1.2.units_name_predefined_watt`: **Test not run**

❗`5.4.1.2.units_name_predefined_weber`: **Test not run**

❗`5.4.1.2.units_names_and_other_names`: **Test not run**

❗`5.4.1.2.units_shadowing_1`: **Test not run**

❗`5.4.1.2.units_shadowing_2`: **Test not run**

❗`5.4.1.3.units_base_units_invalid`: **Test not run**

❗`5.4.2.1.unit_offset_non_zero`: **Test not run**

❗`5.4.2.1.unit_offset_zero`: **Test not run**

❗`5.4.2.1.unit_prefix_exponent_multiplier`: **Test not run**

❗`5.4.2.1.unit_prefix_exponent_multiplier_huge`: **Test not run**

❗`5.4.2.1.unit_units_missing`: **Test not run**

❗`5.4.2.1.unit_with_component`: **Test not run**

❗`5.4.2.1.unit_with_component_ref`: **Test not run**

❗`5.4.2.1.unit_with_connection`: **Test not run**

❗`5.4.2.1.unit_with_group`: **Test not run**

❗`5.4.2.1.unit_with_map_components`: **Test not run**

❗`5.4.2.1.unit_with_map_variables`: **Test not run**

❗`5.4.2.1.unit_with_math`: **Test not run**

❗`5.4.2.1.unit_with_model`: **Test not run**

❗`5.4.2.1.unit_with_reaction`: **Test not run**

❗`5.4.2.1.unit_with_relationship_ref`: **Test not run**

❗`5.4.2.1.unit_with_role`: **Test not run**

❗`5.4.2.1.unit_with_unit`: **Test not run**

❗`5.4.2.1.unit_with_units`: **Test not run**

❗`5.4.2.1.unit_with_variable`: **Test not run**

❗`5.4.2.1.unit_with_variable_ref`: **Test not run**

❗`5.4.2.2.unit_cycle_1`: **Test not run**

❗`5.4.2.2.unit_cycle_2`: **Test not run**

❗`5.4.2.2.unit_cycle_3`: **Test not run**

❗`5.4.2.2.unit_units_invalid`: **Test not run**

❗`5.4.2.2.unit_units_local_1`: **Test not run**

❗`5.4.2.2.unit_units_local_2`: **Test not run**

❗`5.4.2.3.unit_prefix_integer`: **Test not run**

❗`5.4.2.3.unit_prefix_named`: **Test not run**

❗`5.4.2.3.unit_prefix_real`: **Test not run**

❗`5.4.2.3.unit_prefix_real_int`: **Test not run**

❗`5.4.2.3.unit_prefix_spaces`: **Test not run**

❗`5.4.2.3.unit_prefix_unknown`: **Test not run**

❗`5.4.2.4.unit_exponent_invalid`: **Test not run**

❗`5.4.2.5.unit_multiplier_invalid`: **Test not run**

❗`5.4.2.6.unit_offset_invalid`: **Test not run**

❗`5.4.2.7.unit_offset_and_exponent`: **Test not run**

❗`5.4.2.7.unit_offset_and_siblings_1`: **Test not run**

❗`5.4.2.7.unit_offset_and_siblings_2`: **Test not run**

❗`5.4.2.7.unit_offset_non_zero_and_exponent_one`: **Test not run**

❗`5.4.2.7.unit_offset_zero_and_exponent`: **Test not run**

❗`5.4.2.7.unit_offset_zero_and_siblings`: **Test not run**

❗`5.5.2.boolean_arithmetic_divide`: **Test not run**

❗`5.5.2.boolean_arithmetic_minus`: **Test not run**

❗`5.5.2.boolean_arithmetic_plus`: **Test not run**

❗`5.5.2.boolean_arithmetic_power_1`: **Test not run**

❗`5.5.2.boolean_arithmetic_power_2`: **Test not run**

❗`5.5.2.boolean_arithmetic_root_1`: **Test not run**

❗`5.5.2.boolean_arithmetic_root_2`: **Test not run**

❗`5.5.2.boolean_arithmetic_times`: **Test not run**

❗`5.5.2.boolean_compare_eq_operand_error`: **Test not run**

❗`5.5.2.boolean_compare_geq_operand_error`: **Test not run**

❗`5.5.2.boolean_compare_gt_operand_error`: **Test not run**

❗`5.5.2.boolean_compare_leq_operand_error`: **Test not run**

❗`5.5.2.boolean_compare_lt_operand_error`: **Test not run**

❗`5.5.2.boolean_compare_neq_operand_error`: **Test not run**

❗`5.5.2.boolean_derivatives_1`: **Test not run**

❗`5.5.2.boolean_derivatives_2`: **Test not run**

❗`5.5.2.boolean_function_abs`: **Test not run**

❗`5.5.2.boolean_function_ceiling`: **Test not run**

❗`5.5.2.boolean_function_exp`: **Test not run**

❗`5.5.2.boolean_function_factorial`: **Test not run**

❗`5.5.2.boolean_function_floor`: **Test not run**

❗`5.5.2.boolean_function_ln`: **Test not run**

❗`5.5.2.boolean_function_log_1`: **Test not run**

❗`5.5.2.boolean_function_log_2`: **Test not run**

❗`5.5.2.boolean_logic_and_operand_error`: **Test not run**

❗`5.5.2.boolean_logic_not_operand_error`: **Test not run**

❗`5.5.2.boolean_logic_or_operand_error`: **Test not run**

❗`5.5.2.boolean_logic_xor_operand_error`: **Test not run**

❗`5.5.2.boolean_trig_arccos`: **Test not run**

❗`5.5.2.boolean_trig_arccosh`: **Test not run**

❗`5.5.2.boolean_trig_arccot`: **Test not run**

❗`5.5.2.boolean_trig_arccoth`: **Test not run**

❗`5.5.2.boolean_trig_arccsc`: **Test not run**

❗`5.5.2.boolean_trig_arccsch`: **Test not run**

❗`5.5.2.boolean_trig_arcsec`: **Test not run**

❗`5.5.2.boolean_trig_arcsech`: **Test not run**

❗`5.5.2.boolean_trig_arcsin`: **Test not run**

❗`5.5.2.boolean_trig_arcsinh`: **Test not run**

❗`5.5.2.boolean_trig_arctan`: **Test not run**

❗`5.5.2.boolean_trig_arctanh`: **Test not run**

❗`5.5.2.boolean_trig_cos`: **Test not run**

❗`5.5.2.boolean_trig_cosh`: **Test not run**

❗`5.5.2.boolean_trig_cot`: **Test not run**

❗`5.5.2.boolean_trig_coth`: **Test not run**

❗`5.5.2.boolean_trig_csc`: **Test not run**

❗`5.5.2.boolean_trig_csch`: **Test not run**

❗`5.5.2.boolean_trig_sec`: **Test not run**

❗`5.5.2.boolean_trig_sech`: **Test not run**

❗`5.5.2.boolean_trig_sin`: **Test not run**

❗`5.5.2.boolean_trig_sinh`: **Test not run**

❗`5.5.2.boolean_trig_tan`: **Test not run**

❗`5.5.2.boolean_trig_tanh`: **Test not run**

❗`5.5.2.boolean_variable_1`: **Test not run**

❗`5.5.2.boolean_variable_2`: **Test not run**

❗`5.5.2.boolean_variable_3`: **Test not run**

❗`6.4.1.1.group_component_ref_missing_1`: **Test not run**

❗`6.4.1.1.group_component_ref_missing_2`: **Test not run**

❗`6.4.1.1.group_component_ref_multiple`: **Test not run**

❗`6.4.1.1.group_component_ref_single`: **Test not run**

❗`6.4.1.1.group_empty`: **Test not run**

❗`6.4.1.1.group_only_extensions`: **Test not run**

❗`6.4.1.1.group_relationship_ref_missing_1`: **Test not run**

❗`6.4.1.1.group_relationship_ref_missing_2`: **Test not run**

❗`6.4.1.1.group_with_component`: **Test not run**

❗`6.4.1.1.group_with_connection`: **Test not run**

❗`6.4.1.1.group_with_group`: **Test not run**

❗`6.4.1.1.group_with_map_components`: **Test not run**

❗`6.4.1.1.group_with_map_variables`: **Test not run**

❗`6.4.1.1.group_with_math`: **Test not run**

❗`6.4.1.1.group_with_model`: **Test not run**

❗`6.4.1.1.group_with_reaction`: **Test not run**

❗`6.4.1.1.group_with_role`: **Test not run**

❗`6.4.1.1.group_with_unit`: **Test not run**

❗`6.4.1.1.group_with_units`: **Test not run**

❗`6.4.1.1.group_with_variable`: **Test not run**

❗`6.4.1.1.group_with_variable_ref`: **Test not run**

❗`6.4.1.group_child_order_1`: **Test not run**

❗`6.4.1.group_child_order_2`: **Test not run**

❗`6.4.2.1.relationship_ref_name`: **Test not run**

❗`6.4.2.1.relationship_ref_relationship_1`: **Test not run**

❗`6.4.2.1.relationship_ref_relationship_2`: **Test not run**

❗`6.4.2.1.relationship_ref_relationship_missing`: **Test not run**

❗`6.4.2.1.relationship_ref_with_component`: **Test not run**

❗`6.4.2.1.relationship_ref_with_component_ref`: **Test not run**

❗`6.4.2.1.relationship_ref_with_connection`: **Test not run**

❗`6.4.2.1.relationship_ref_with_group`: **Test not run**

❗`6.4.2.1.relationship_ref_with_map_components`: **Test not run**

❗`6.4.2.1.relationship_ref_with_map_variables`: **Test not run**

❗`6.4.2.1.relationship_ref_with_math`: **Test not run**

❗`6.4.2.1.relationship_ref_with_model`: **Test not run**

❗`6.4.2.1.relationship_ref_with_reaction`: **Test not run**

❗`6.4.2.1.relationship_ref_with_relationship_ref`: **Test not run**

❗`6.4.2.1.relationship_ref_with_role`: **Test not run**

❗`6.4.2.1.relationship_ref_with_unit`: **Test not run**

❗`6.4.2.1.relationship_ref_with_units`: **Test not run**

❗`6.4.2.1.relationship_ref_with_variable`: **Test not run**

❗`6.4.2.1.relationship_ref_with_variable_ref`: **Test not run**

❗`6.4.2.2.relationship_ref_relationship_invalid`: **Test not run**

❗`6.4.2.3.relationship_ref_name_invalid`: **Test not run**

❗`6.4.2.3.relationship_ref_name_not_unique_model_wide`: **Test not run**

❗`6.4.2.4.relationship_ref_encapsulation_duplicate`: **Test not run**

❗`6.4.2.4.relationship_ref_encapsulation_named`: **Test not run**

❗`6.4.2.5.relationship_ref_duplicate_named`: **Test not run**

❗`6.4.2.5.relationship_ref_duplicate_unnamed_1`: **Test not run**

❗`6.4.2.5.relationship_ref_duplicate_unnamed_2`: **Test not run**

❗`6.4.2.5.relationship_ref_multiple_1`: **Test not run**

❗`6.4.2.5.relationship_ref_multiple_2`: **Test not run**

❗`6.4.2.5.relationship_ref_multiple_3`: **Test not run**

❗`6.4.3.1.component_ref_component_missing`: **Test not run**

❗`6.4.3.1.component_ref_nesting`: **Test not run**

❗`6.4.3.1.component_ref_with_component`: **Test not run**

❗`6.4.3.1.component_ref_with_connection`: **Test not run**

❗`6.4.3.1.component_ref_with_group`: **Test not run**

❗`6.4.3.1.component_ref_with_map_components`: **Test not run**

❗`6.4.3.1.component_ref_with_map_variables`: **Test not run**

❗`6.4.3.1.component_ref_with_math`: **Test not run**

❗`6.4.3.1.component_ref_with_model`: **Test not run**

❗`6.4.3.1.component_ref_with_reaction`: **Test not run**

❗`6.4.3.1.component_ref_with_relationship_ref`: **Test not run**

❗`6.4.3.1.component_ref_with_role`: **Test not run**

❗`6.4.3.1.component_ref_with_unit`: **Test not run**

❗`6.4.3.1.component_ref_with_units`: **Test not run**

❗`6.4.3.1.component_ref_with_variable`: **Test not run**

❗`6.4.3.1.component_ref_with_variable_ref`: **Test not run**

❗`6.4.3.2.component_ref_children_declared_twice_1`: **Test not run**

❗`6.4.3.2.component_ref_children_declared_twice_2`: **Test not run**

❗`6.4.3.2.component_ref_children_declared_twice_3`: **Test not run**

❗`6.4.3.2.component_ref_cycle_1`: **Test not run**

❗`6.4.3.2.component_ref_cycle_2`: **Test not run**

❗`6.4.3.2.component_ref_cycle_3`: **Test not run**

❗`6.4.3.2.component_ref_cycle_4`: **Test not run**

❗`6.4.3.2.component_ref_duplicate_child_1`: **Test not run**

❗`6.4.3.2.component_ref_duplicate_child_2`: **Test not run**

❗`6.4.3.2.component_ref_no_children_containment`: **Test not run**

❗`6.4.3.2.component_ref_no_children_encapsulation`: **Test not run**

❗`6.4.3.2.component_ref_no_children_extension`: **Test not run**

❗`6.4.3.2.component_ref_overlapping_containment`: **Test not run**

❗`6.4.3.2.component_ref_overlapping_encapsulation`: **Test not run**

❗`6.4.3.2.component_ref_split_named`: **Test not run**

❗`6.4.3.2.component_ref_split_unnamed_1`: **Test not run**

❗`6.4.3.2.component_ref_split_unnamed_2`: **Test not run**

❗`6.4.3.3.component_ref_component_invalid`: **Test not run**

❗`6.4.3.3.component_ref_component_nonexistent_1`: **Test not run**

❗`6.4.3.3.component_ref_component_nonexistent_2`: **Test not run**

❗`7.4.1.1.reaction_variable_ref_missing`: **Test not run**

❗`7.4.1.1.reaction_with_component`: **Test not run**

❗`7.4.1.1.reaction_with_component_ref`: **Test not run**

❗`7.4.1.1.reaction_with_connection`: **Test not run**

❗`7.4.1.1.reaction_with_group`: **Test not run**

❗`7.4.1.1.reaction_with_map_components`: **Test not run**

❗`7.4.1.1.reaction_with_map_variables`: **Test not run**

❗`7.4.1.1.reaction_with_math`: **Test not run**

❗`7.4.1.1.reaction_with_model`: **Test not run**

❗`7.4.1.1.reaction_with_reaction`: **Test not run**

❗`7.4.1.1.reaction_with_relationship_ref`: **Test not run**

❗`7.4.1.1.reaction_with_role`: **Test not run**

❗`7.4.1.1.reaction_with_unit`: **Test not run**

❗`7.4.1.1.reaction_with_units`: **Test not run**

❗`7.4.1.1.reaction_with_variable`: **Test not run**

❗`7.4.1.2.reaction_reversible_invalid`: **Test not run**

❗`7.4.1.2.reaction_reversible_no`: **Test not run**

❗`7.4.1.2.reaction_reversible_yes`: **Test not run**

❗`7.4.1.3.reaction_encapsulating_delta_variable`: **Test not run**

❗`7.4.2.1.variable_ref_role_missing`: **Test not run**

❗`7.4.2.1.variable_ref_variable_missing`: **Test not run**

❗`7.4.2.1.variable_ref_with_component`: **Test not run**

❗`7.4.2.1.variable_ref_with_component_ref`: **Test not run**

❗`7.4.2.1.variable_ref_with_connection`: **Test not run**

❗`7.4.2.1.variable_ref_with_group`: **Test not run**

❗`7.4.2.1.variable_ref_with_map_components`: **Test not run**

❗`7.4.2.1.variable_ref_with_map_variables`: **Test not run**

❗`7.4.2.1.variable_ref_with_math`: **Test not run**

❗`7.4.2.1.variable_ref_with_model`: **Test not run**

❗`7.4.2.1.variable_ref_with_reaction`: **Test not run**

❗`7.4.2.1.variable_ref_with_relationship_ref`: **Test not run**

❗`7.4.2.1.variable_ref_with_unit`: **Test not run**

❗`7.4.2.1.variable_ref_with_units`: **Test not run**

❗`7.4.2.1.variable_ref_with_variable`: **Test not run**

❗`7.4.2.1.variable_ref_with_variable_ref`: **Test not run**

❗`7.4.2.2.variable_ref_variable_duplicate`: **Test not run**

❗`7.4.2.2.variable_ref_variable_hidden`: **Test not run**

❗`7.4.2.2.variable_ref_variable_nonexistent`: **Test not run**

❗`7.4.3.1.role_role_missing`: **Test not run**

❗`7.4.3.1.role_with_component`: **Test not run**

❗`7.4.3.1.role_with_component_ref`: **Test not run**

❗`7.4.3.1.role_with_connection`: **Test not run**

❗`7.4.3.1.role_with_group`: **Test not run**

❗`7.4.3.1.role_with_map_components`: **Test not run**

❗`7.4.3.1.role_with_map_variables`: **Test not run**

❗`7.4.3.1.role_with_model`: **Test not run**

❗`7.4.3.1.role_with_reaction`: **Test not run**

❗`7.4.3.1.role_with_relationship_ref`: **Test not run**

❗`7.4.3.1.role_with_role`: **Test not run**

❗`7.4.3.1.role_with_unit`: **Test not run**

❗`7.4.3.1.role_with_units`: **Test not run**

❗`7.4.3.1.role_with_variable`: **Test not run**

❗`7.4.3.1.role_with_variable_ref`: **Test not run**

❗`7.4.3.2.role_role_invalid`: **Test not run**

❗`7.4.3.3.reaction_multiple_rates`: **Test not run**

❗`7.4.3.3.role_rate_with_delta_variable`: **Test not run**

❗`7.4.3.3.role_rate_with_multiple_roles`: **Test not run**

❗`7.4.3.3.role_rate_with_stoichiometry`: **Test not run**

❗`7.4.3.4.role_direction_invalid`: **Test not run**

❗`7.4.3.5.role_direction_both_irreversible`: **Test not run**

❗`7.4.3.5.role_direction_both_product`: **Test not run**

❗`7.4.3.5.role_direction_both_rate`: **Test not run**

❗`7.4.3.5.role_direction_both_reactant`: **Test not run**

❗`7.4.3.5.role_direction_reverse_irreversible`: **Test not run**

❗`7.4.3.5.role_direction_reverse_product`: **Test not run**

❗`7.4.3.5.role_direction_reverse_rate`: **Test not run**

❗`7.4.3.5.role_direction_reverse_reactant`: **Test not run**

❗`7.4.3.5.role_direction_role_duplicate`: **Test not run**

❗`7.4.3.6.role_stoichiometry_invalid`: **Test not run**

❗`7.4.3.7.role_delta_variable_duplicate_1`: **Test not run**

❗`7.4.3.7.role_delta_variable_duplicate_2`: **Test not run**

❗`7.4.3.7.role_delta_variable_nonexistent_1`: **Test not run**

❗`7.4.3.7.role_delta_variable_nonexistent_2`: **Test not run**

❗`7.4.3.8.role_delta_variable_activator`: **Test not run**

❗`7.4.3.8.role_delta_variable_catalyst`: **Test not run**

❗`7.4.3.8.role_delta_variable_inhibitor`: **Test not run**

❗`7.4.3.8.role_delta_variable_modifier`: **Test not run**

❗`7.4.3.8.role_delta_variable_with_rate_and_math`: **Test not run**

❗`7.4.3.8.role_delta_variable_with_stoichiometry_no_rate`: **Test not run**

❗`7.4.3.8.role_delta_variable_without_rate_or_math`: **Test not run**

❗`7.4.3.9.role_math_not_relevant`: **Test not run**

❗`7.4.3.reaction_all_roles_and_attributes`: **Test not run**

❗`7.4.3.reaction_reversible_no`: **Test not run**

❗`7.4.3.reaction_simple`: **Test not run**

❗`8.4.1.cmeta_id_duplicate`: **Test not run**

❗`8.4.1.cmeta_id_in_component`: **Test not run**

❗`8.4.1.cmeta_id_in_component_ref`: **Test not run**

❗`8.4.1.cmeta_id_in_connection`: **Test not run**

❗`8.4.1.cmeta_id_in_group`: **Test not run**

❗`8.4.1.cmeta_id_in_map_components`: **Test not run**

❗`8.4.1.cmeta_id_in_map_variables`: **Test not run**

❗`8.4.1.cmeta_id_in_model`: **Test not run**

❗`8.4.1.cmeta_id_in_reaction`: **Test not run**

❗`8.4.1.cmeta_id_in_relationship_ref`: **Test not run**

❗`8.4.1.cmeta_id_in_role`: **Test not run**

❗`8.4.1.cmeta_id_in_unit`: **Test not run**

❗`8.4.1.cmeta_id_in_units_1`: **Test not run**

❗`8.4.1.cmeta_id_in_units_2`: **Test not run**

❗`8.4.1.cmeta_id_in_variable`: **Test not run**

❗`8.4.1.cmeta_id_in_variable_ref`: **Test not run**

❗`8.4.2.rdf_in_component`: **Test not run**

❗`8.4.2.rdf_in_component_ref`: **Test not run**

❗`8.4.2.rdf_in_connection`: **Test not run**

❗`8.4.2.rdf_in_group`: **Test not run**

❗`8.4.2.rdf_in_map_components`: **Test not run**

❗`8.4.2.rdf_in_map_variables`: **Test not run**

❗`8.4.2.rdf_in_model`: **Test not run**

❗`8.4.2.rdf_in_reaction`: **Test not run**

❗`8.4.2.rdf_in_relationship_ref`: **Test not run**

❗`8.4.2.rdf_in_role`: **Test not run**

❗`8.4.2.rdf_in_unit`: **Test not run**

❗`8.4.2.rdf_in_units_1`: **Test not run**

❗`8.4.2.rdf_in_units_2`: **Test not run**

❗`8.4.2.rdf_in_variable`: **Test not run**

❗`8.4.2.rdf_in_variable_ref`: **Test not run**

❗`C.3.3.unit_checking_arithmetic_minus_operand_error_1`: **Test not run**

❗`C.3.3.unit_checking_arithmetic_minus_operand_error_2`: **Test not run**

❗`C.3.3.unit_checking_arithmetic_minus_operand_error_3`: **Test not run**

❗`C.3.3.unit_checking_arithmetic_plus_operand_error_1`: **Test not run**

❗`C.3.3.unit_checking_arithmetic_plus_operand_error_2`: **Test not run**

❗`C.3.3.unit_checking_arithmetic_plus_operand_error_3`: **Test not run**

❗`C.3.3.unit_checking_arithmetic_plus_operand_error_4`: **Test not run**

❗`C.3.3.unit_checking_arithmetic_power_operand_error`: **Test not run**

❗`C.3.3.unit_checking_arithmetic_root_operand_error`: **Test not run**

❗`C.3.3.unit_checking_compare_eq_operand_mismatch`: **Test not run**

❗`C.3.3.unit_checking_compare_geq_operand_mismatch`: **Test not run**

❗`C.3.3.unit_checking_compare_gt_operand_mismatch`: **Test not run**

❗`C.3.3.unit_checking_compare_leq_operand_mismatch`: **Test not run**

❗`C.3.3.unit_checking_compare_lt_operand_mismatch`: **Test not run**

❗`C.3.3.unit_checking_compare_neq_operand_mismatch`: **Test not run**

❗`C.3.3.unit_checking_derivative_operand_error`: **Test not run**

❗`C.3.3.unit_checking_function_exp_operand_error`: **Test not run**

❗`C.3.3.unit_checking_function_factorial_operand_error`: **Test not run**

❗`C.3.3.unit_checking_function_ln_operand_error`: **Test not run**

❗`C.3.3.unit_checking_function_log_operand_error_1`: **Test not run**

❗`C.3.3.unit_checking_function_log_operand_error_2`: **Test not run**

❗`C.3.3.unit_checking_trig_arccos_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_arccosh_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_arccot_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_arccoth_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_arccsc_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_arccsch_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_arcsec_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_arcsech_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_arcsin_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_arcsinh_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_arctan_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_arctanh_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_cos_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_cosh_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_cot_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_coth_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_csc_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_csch_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_sec_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_sech_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_sin_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_sinh_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_tan_operand_error`: **Test not run**

❗`C.3.3.unit_checking_trig_tanh_operand_error`: **Test not run**

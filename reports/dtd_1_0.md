# DTD Validation - CellML 1.0

Performance:
* 86% according to spec (306 out of 354)
* 286 out of 317 valid files passed
* 20 out of 37 invalid files detected

Issues:
* 31 valid files failed validation
* 14 invalid files passed validation
* 3 invalid files failed validation for the wrong reason

Test implementation issues
* **410 tests not run**

Results per category

(Valid passed, invalid failed, valid failed, invalid passed, invalid failed for wrong reason, percent classified correctly according to spec)

|Category|V Pass|I Fail|🔴 V Fail|🔵 I Pass|🔶 I Bad|Score|
|-|-|-|-|-|-|-|
|[0. Not mentioned in spec](#0-not-mentioned-in-spec)|6|2|0|8|0|50%|
|[2. Fundamentals](#2-fundamentals)|5|18|14|6|3|50%|
|[3. Model structure](#3-model-structure)|50|0|0|0|0|100%|
|[4. Mathematics](#4-mathematics)|45|0|0|0|0|100%|
|[5. Units](#5-units)|100|0|0|0|0|100%|
|[6. Grouping](#6-grouping)|15|0|2|0|0|88%|
|[7. Reactions](#7-reactions)|5|0|0|0|0|100%|
|[8. Metadata framework](#8-metadata-framework)|15|0|15|0|0|50%|
|[C. Advanced units functionality](#c-advanced-units-functionality)|45|0|0|0|0|100%|


---

## 0. Not mentioned in spec

### 0.0

[0.0.root_namespace_1](../models_1_0/valid/0.0.root_namespace_1.cellml): Valid file passed validation.

[0.0.root_namespace_2](../models_1_0/valid/0.0.root_namespace_2.cellml): Valid file passed validation.

🔵 [0.0.root_node_namespace_wrong](../models_1_0/invalid/0.0.root_node_namespace_wrong.cellml): **Error not detected.**

🔵 [0.0.root_node_not_model](../models_1_0/invalid/0.0.root_node_not_model.cellml): **Error not detected.**

[0.0.root_node_two_elements](../models_1_0/invalid/0.0.root_node_two_elements.cellml): Error detected correctly.
* Expected: ```Extra content at the end of the document```
* Output: ```Extra content at the end of the document, line 6, column 1 (0.0.root_node_two_elements.cellml, line 6)```

[0.0.root_node_two_models](../models_1_0/invalid/0.0.root_node_two_models.cellml): Error detected correctly.
* Expected: ```Extra content at the end of the document```
* Output: ```Extra content at the end of the document, line 6, column 1 (0.0.root_node_two_models.cellml, line 6)```


---

### 0.1

🔵 [0.1.real_number_invalid_1](../models_1_0/invalid/0.1.real_number_invalid_1.cellml): **Error not detected.**

🔵 [0.1.real_number_invalid_2](../models_1_0/invalid/0.1.real_number_invalid_2.cellml): **Error not detected.**

🔵 [0.1.real_number_invalid_3](../models_1_0/invalid/0.1.real_number_invalid_3.cellml): **Error not detected.**

🔵 [0.1.real_number_invalid_4](../models_1_0/invalid/0.1.real_number_invalid_4.cellml): **Error not detected.**

🔵 [0.1.real_number_invalid_5](../models_1_0/invalid/0.1.real_number_invalid_5.cellml): **Error not detected.**

🔵 [0.1.real_number_invalid_6](../models_1_0/invalid/0.1.real_number_invalid_6.cellml): **Error not detected.**

[0.1.real_numbers](../models_1_0/valid/0.1.real_numbers.cellml): Valid file passed validation.

[0.1.real_numbers_extreme](../models_1_0/valid/0.1.real_numbers_extreme.cellml): Valid file passed validation.


---

### 0.2

[0.2.component_name_same_as_model](../models_1_0/valid/0.2.component_name_same_as_model.cellml): Valid file passed validation.

[0.2.variable_name_same_as_model](../models_1_0/valid/0.2.variable_name_same_as_model.cellml): Valid file passed validation.


---

## 2. Fundamentals

#### 2.4.1

🔵 [2.4.1.identifier_empty](../models_1_0/invalid/2.4.1.identifier_empty.cellml): **Error not detected.**

🔵 [2.4.1.identifier_only_underscore](../models_1_0/invalid/2.4.1.identifier_only_underscore.cellml): **Error not detected.**

🔵 [2.4.1.identifier_unexpected_character_1](../models_1_0/invalid/2.4.1.identifier_unexpected_character_1.cellml): **Error not detected.**

🔵 [2.4.1.identifier_unexpected_character_2](../models_1_0/invalid/2.4.1.identifier_unexpected_character_2.cellml): **Error not detected.**

🔵 [2.4.1.identifier_unexpected_character_unicode](../models_1_0/invalid/2.4.1.identifier_unexpected_character_unicode.cellml): **Error not detected.**

[2.4.1.valid_identifiers](../models_1_0/valid/2.4.1.valid_identifiers.cellml): Valid file passed validation.


---

#### 2.4.2

[2.4.2.imaginary_attributes_1](../models_1_0/invalid/2.4.2.imaginary_attributes_1.cellml): Error detected correctly.
* Expected: ```No declaration for attribute fruit```
* Output: ```Error on line 7: No declaration for attribute fruit of element model```

[2.4.2.imaginary_attributes_2](../models_1_0/invalid/2.4.2.imaginary_attributes_2.cellml): Error detected correctly.
* Expected: ```No declaration for attribute fruit```
* Output: ```Error on line 8: No declaration for attribute fruit of element model```

[2.4.2.imaginary_elements](../models_1_0/invalid/2.4.2.imaginary_elements.cellml): Error detected correctly.
* Expected: ```No declaration for element fruit```
* Output:
  * ```Error on line 5: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (fruit )```
  * ```Error on line 6: No declaration for element fruit```


---

#### 2.4.3

🔶 [2.4.3.cellml_attributes_inside_extensions](../models_1_0/invalid/2.4.3.cellml_attributes_inside_extensions.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```CellML attributes may not appears inside extension elements```
* Output:
  * ```Error on line 7: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (fruit:banana )```
  * ```Error on line 7: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 8: No declaration for element banana```
  * ```Error on line 8: No declaration for attribute name of element banana```

🔶 [2.4.3.cellml_elements_inside_extensions](../models_1_0/invalid/2.4.3.cellml_elements_inside_extensions.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```CellML attributes may not appears inside extension elements```
* Output:
  * ```Error on line 7: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (fruit:banana )```
  * ```Error on line 7: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 8: No declaration for element banana```

🔴 [2.4.3.component_ref_with_extensions](../models_1_0/valid/2.4.3.component_ref_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 12: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (fruit:orange fruit:pear )```
  * ```Error on line 12: No declaration for attribute banana of element component_ref```
  * ```Error on line 13: No declaration for element orange```
  * ```Error on line 13: No declaration for attribute peel of element orange```
  * ```Error on line 14: No declaration for element clementine```
  * ```Error on line 16: No declaration for element pear```

🔴 [2.4.3.component_with_extensions](../models_1_0/valid/2.4.3.component_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 7: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (fruit:orange fruit:pear )```
  * ```Error on line 7: No declaration for attribute banana of element component```
  * ```Error on line 8: No declaration for element orange```
  * ```Error on line 8: No declaration for attribute peel of element orange```
  * ```Error on line 9: No declaration for element clementine```
  * ```Error on line 11: No declaration for element pear```

🔴 [2.4.3.connection_with_extensions](../models_1_0/valid/2.4.3.connection_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 7: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (fruit:orange fruit:pear map_components map_variables )```
  * ```Error on line 7: No declaration for attribute x_a_day of element connection```
  * ```Error on line 8: No declaration for element orange```
  * ```Error on line 8: No declaration for attribute peel of element orange```
  * ```Error on line 9: No declaration for element clementine```
  * ```Error on line 11: No declaration for element pear```

🔴 [2.4.3.group_with_extensions](../models_1_0/valid/2.4.3.group_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 9: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (fruit:orange fruit:pear relationship_ref component_ref )```
  * ```Error on line 9: No declaration for attribute banana of element group```
  * ```Error on line 10: No declaration for element orange```
  * ```Error on line 10: No declaration for attribute peel of element orange```
  * ```Error on line 11: No declaration for element clementine```
  * ```Error on line 13: No declaration for element pear```

🔴 [2.4.3.map_components_with_extensions](../models_1_0/valid/2.4.3.map_components_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 8: Element map_components was declared EMPTY this one has content```
  * ```Error on line 8: No declaration for attribute x_a_day of element map_components```
  * ```Error on line 9: No declaration for element orange```
  * ```Error on line 9: No declaration for attribute peel of element orange```
  * ```Error on line 10: No declaration for element clementine```
  * ```Error on line 12: No declaration for element pear```

🔴 [2.4.3.map_variables_with_extensions](../models_1_0/valid/2.4.3.map_variables_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 9: Element map_variables was declared EMPTY this one has content```
  * ```Error on line 9: No declaration for attribute x_a_day of element map_variables```
  * ```Error on line 10: No declaration for element orange```
  * ```Error on line 10: No declaration for attribute peel of element orange```
  * ```Error on line 11: No declaration for element clementine```
  * ```Error on line 13: No declaration for element pear```

🔴 [2.4.3.model_with_extensions](../models_1_0/valid/2.4.3.model_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 7: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (fruit:orange fruit:pear )```
  * ```Error on line 7: No declaration for attribute x_a_day of element model```
  * ```Error on line 7: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 8: No declaration for element orange```
  * ```Error on line 8: No declaration for attribute peel of element orange```
  * ```Error on line 9: No declaration for element clementine```
  * ```Error on line 11: No declaration for element pear```

🔴 [2.4.3.reaction_with_extensions](../models_1_0/valid/2.4.3.reaction_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 9: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (fruit:orange fruit:pear variable_ref )```
  * ```Error on line 9: No declaration for attribute x_a_day of element reaction```
  * ```Error on line 10: No declaration for element orange```
  * ```Error on line 10: No declaration for attribute peel of element orange```
  * ```Error on line 11: No declaration for element clementine```
  * ```Error on line 13: No declaration for element pear```

🔴 [2.4.3.relationship_ref_with_extensions](../models_1_0/valid/2.4.3.relationship_ref_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 10: Element relationship_ref was declared EMPTY this one has content```
  * ```Error on line 10: No declaration for attribute banana of element relationship_ref```
  * ```Error on line 11: No declaration for element orange```
  * ```Error on line 11: No declaration for attribute peel of element orange```
  * ```Error on line 12: No declaration for element clementine```
  * ```Error on line 14: No declaration for element pear```

🔴 [2.4.3.role_with_extensions](../models_1_0/valid/2.4.3.role_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 11: Element role content does not follow the DTD, expecting (math)?, got (fruit:orange fruit:pear )```
  * ```Error on line 11: No declaration for attribute x_a_day of element role```
  * ```Error on line 12: No declaration for element orange```
  * ```Error on line 12: No declaration for attribute peel of element orange```
  * ```Error on line 13: No declaration for element clementine```
  * ```Error on line 15: No declaration for element pear```

🔴 [2.4.3.unit_with_extensions](../models_1_0/valid/2.4.3.unit_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 8: Element unit was declared EMPTY this one has content```
  * ```Error on line 8: No declaration for attribute x_a_day of element unit```
  * ```Error on line 9: No declaration for element orange```
  * ```Error on line 9: No declaration for attribute peel of element orange```
  * ```Error on line 10: No declaration for element clementine```
  * ```Error on line 12: No declaration for element pear```

🔴 [2.4.3.units_with_extensions](../models_1_0/valid/2.4.3.units_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 7: Element units content does not follow the DTD, expecting (unit)*, got (unit fruit:orange fruit:pear )```
  * ```Error on line 7: No declaration for attribute x_a_day of element units```
  * ```Error on line 9: No declaration for element orange```
  * ```Error on line 9: No declaration for attribute peel of element orange```
  * ```Error on line 10: No declaration for element clementine```
  * ```Error on line 12: No declaration for element pear```
  * ```Error on line 15: Element units content does not follow the DTD, expecting (unit)*, got (unit fruit:orange fruit:pear )```
  * ```Error on line 15: No declaration for attribute x_a_day of element units```
  * ```Error on line 17: No declaration for element orange```
  * ```Error on line 17: No declaration for attribute peel of element orange```
  * ```Error on line 18: No declaration for element clementine```
  * ```Error on line 20: No declaration for element pear```

🔴 [2.4.3.variable_ref_with_extensions](../models_1_0/valid/2.4.3.variable_ref_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 10: Element variable_ref content does not follow the DTD, expecting (role)+, got (fruit:orange fruit:pear role )```
  * ```Error on line 10: No declaration for attribute x_a_day of element variable_ref```
  * ```Error on line 11: No declaration for element orange```
  * ```Error on line 11: No declaration for attribute peel of element orange```
  * ```Error on line 12: No declaration for element clementine```
  * ```Error on line 14: No declaration for element pear```

🔴 [2.4.3.variable_with_extensions](../models_1_0/valid/2.4.3.variable_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 8: Element variable was declared EMPTY this one has content```
  * ```Error on line 8: No declaration for attribute x_a_day of element variable```
  * ```Error on line 9: No declaration for element orange```
  * ```Error on line 9: No declaration for attribute peel of element orange```
  * ```Error on line 10: No declaration for element clementine```
  * ```Error on line 12: No declaration for element pear```


---

#### 2.4.4

[2.4.4.model_linux_line_breaks](../models_1_0/valid/2.4.4.model_linux_line_breaks.cellml): Valid file passed validation.

[2.4.4.model_windows_line_breaks](../models_1_0/valid/2.4.4.model_windows_line_breaks.cellml): Valid file passed validation.

[2.4.4.model_with_spaces](../models_1_0/valid/2.4.4.model_with_spaces.cellml): Valid file passed validation.

[2.4.4.model_with_tabs](../models_1_0/valid/2.4.4.model_with_tabs.cellml): Valid file passed validation.

[2.4.4.text_in_component](../models_1_0/invalid/2.4.4.text_in_component.cellml): Error detected correctly.
* Expected: ```Element component content does not follow the DTD```
* Output: ```Error on line 6: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (CDATA)```

[2.4.4.text_in_component_ref](../models_1_0/invalid/2.4.4.text_in_component_ref.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 11: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (CDATA)```

[2.4.4.text_in_connection](../models_1_0/invalid/2.4.4.text_in_connection.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 12: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables CDATA)```

[2.4.4.text_in_group](../models_1_0/invalid/2.4.4.text_in_group.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 8: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref CDATA)```

[2.4.4.text_in_map_components](../models_1_0/invalid/2.4.4.text_in_map_components.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[2.4.4.text_in_map_variables](../models_1_0/invalid/2.4.4.text_in_map_variables.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 14: Element map_variables was declared EMPTY this one has content```

[2.4.4.text_in_model](../models_1_0/invalid/2.4.4.text_in_model.cellml): Error detected correctly.
* Expected: ```Element model content does not follow the DTD```
* Output: ```Error on line 5: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (CDATA)```

[2.4.4.text_in_reaction](../models_1_0/invalid/2.4.4.text_in_reaction.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref CDATA)```

[2.4.4.text_in_relationship_ref](../models_1_0/invalid/2.4.4.text_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 9: Element relationship_ref was declared EMPTY this one has content```

[2.4.4.text_in_role](../models_1_0/invalid/2.4.4.text_in_role.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (CDATA)```

[2.4.4.text_in_unit](../models_1_0/invalid/2.4.4.text_in_unit.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 7: Element unit was declared EMPTY this one has content```

[2.4.4.text_in_units_1](../models_1_0/invalid/2.4.4.text_in_units_1.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 6: Element units content does not follow the DTD, expecting (unit)*, got (unit CDATA)```

[2.4.4.text_in_units_2](../models_1_0/invalid/2.4.4.text_in_units_2.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 7: Element units content does not follow the DTD, expecting (unit)*, got (unit CDATA)```

[2.4.4.text_in_variable](../models_1_0/invalid/2.4.4.text_in_variable.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[2.4.4.text_in_variable_ref](../models_1_0/invalid/2.4.4.text_in_variable_ref.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (role CDATA)```


---

#### 2.5.1

🔵 [2.5.1.identifiers_are_case_sensitive](../models_1_0/invalid/2.5.1.identifiers_are_case_sensitive.cellml): **Error not detected.**


---

#### 2.5.2

🔶 [2.5.2.attribute_in_cellml_namespace](../models_1_0/invalid/2.5.2.attribute_in_cellml_namespace.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```No declaration for attribute name```
* Output: ```Error on line 8: No declaration for attribute private_interface of element variable```


---

## 3. Model structure

##### 3.4.1.1

[3.4.1.1.model_child_order_1](../models_1_0/valid/3.4.1.1.model_child_order_1.cellml): Valid file passed validation.

[3.4.1.1.model_child_order_2](../models_1_0/valid/3.4.1.1.model_child_order_2.cellml): Valid file passed validation.

[3.4.1.1.model_empty](../models_1_0/valid/3.4.1.1.model_empty.cellml): Valid file passed validation.

❗`3.4.1.1.model_name_missing`: **Test not run**

❗`3.4.1.1.model_with_component_ref`: **Test not run**

[3.4.1.1.model_with_components](../models_1_0/valid/3.4.1.1.model_with_components.cellml): Valid file passed validation.

[3.4.1.1.model_with_connections](../models_1_0/valid/3.4.1.1.model_with_connections.cellml): Valid file passed validation.

[3.4.1.1.model_with_groups](../models_1_0/valid/3.4.1.1.model_with_groups.cellml): Valid file passed validation.

❗`3.4.1.1.model_with_map_components`: **Test not run**

❗`3.4.1.1.model_with_map_variables`: **Test not run**

❗`3.4.1.1.model_with_math`: **Test not run**

❗`3.4.1.1.model_with_model`: **Test not run**

[3.4.1.1.model_with_one_component](../models_1_0/valid/3.4.1.1.model_with_one_component.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_connection](../models_1_0/valid/3.4.1.1.model_with_one_connection.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_group](../models_1_0/valid/3.4.1.1.model_with_one_group.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_units](../models_1_0/valid/3.4.1.1.model_with_one_units.cellml): Valid file passed validation.

❗`3.4.1.1.model_with_reaction`: **Test not run**

❗`3.4.1.1.model_with_relationship_ref`: **Test not run**

❗`3.4.1.1.model_with_role`: **Test not run**

❗`3.4.1.1.model_with_unit`: **Test not run**

[3.4.1.1.model_with_units](../models_1_0/valid/3.4.1.1.model_with_units.cellml): Valid file passed validation.

❗`3.4.1.1.model_with_variable`: **Test not run**

❗`3.4.1.1.model_with_variable_ref`: **Test not run**

❗`3.4.1.2.model_name_invalid`: **Test not run**


---

##### 3.4.2.1

[3.4.2.1.component_child_order_1](../models_1_0/valid/3.4.2.1.component_child_order_1.cellml): Valid file passed validation.

[3.4.2.1.component_child_order_2](../models_1_0/valid/3.4.2.1.component_child_order_2.cellml): Valid file passed validation.

[3.4.2.1.component_empty](../models_1_0/valid/3.4.2.1.component_empty.cellml): Valid file passed validation.

❗`3.4.2.1.component_name_missing`: **Test not run**

❗`3.4.2.1.component_with_component`: **Test not run**

❗`3.4.2.1.component_with_component_ref`: **Test not run**

❗`3.4.2.1.component_with_connection`: **Test not run**

❗`3.4.2.1.component_with_group`: **Test not run**

❗`3.4.2.1.component_with_map_components`: **Test not run**

❗`3.4.2.1.component_with_map_variables`: **Test not run**

[3.4.2.1.component_with_maths](../models_1_0/valid/3.4.2.1.component_with_maths.cellml): Valid file passed validation.

❗`3.4.2.1.component_with_model`: **Test not run**

[3.4.2.1.component_with_one_math](../models_1_0/valid/3.4.2.1.component_with_one_math.cellml): Valid file passed validation.

[3.4.2.1.component_with_one_reaction](../models_1_0/valid/3.4.2.1.component_with_one_reaction.cellml): Valid file passed validation.

[3.4.2.1.component_with_one_units](../models_1_0/valid/3.4.2.1.component_with_one_units.cellml): Valid file passed validation.

[3.4.2.1.component_with_one_variable](../models_1_0/valid/3.4.2.1.component_with_one_variable.cellml): Valid file passed validation.

[3.4.2.1.component_with_reactions](../models_1_0/valid/3.4.2.1.component_with_reactions.cellml): Valid file passed validation.

❗`3.4.2.1.component_with_relationship_ref`: **Test not run**

❗`3.4.2.1.component_with_role`: **Test not run**

❗`3.4.2.1.component_with_unit`: **Test not run**

[3.4.2.1.component_with_units](../models_1_0/valid/3.4.2.1.component_with_units.cellml): Valid file passed validation.

❗`3.4.2.1.component_with_variable_ref`: **Test not run**

[3.4.2.1.component_with_variables](../models_1_0/valid/3.4.2.1.component_with_variables.cellml): Valid file passed validation.

❗`3.4.2.2.component_name_duplicate`: **Test not run**

❗`3.4.2.2.component_name_invalid`: **Test not run**

❗`3.4.3.1.variable_name_missing`: **Test not run**

❗`3.4.3.1.variable_units_missing`: **Test not run**

❗`3.4.3.1.variable_with_component`: **Test not run**

❗`3.4.3.1.variable_with_component_ref`: **Test not run**

❗`3.4.3.1.variable_with_connection`: **Test not run**

❗`3.4.3.1.variable_with_group`: **Test not run**


---

##### 3.4.3.1

[3.4.3.1.variable_with_initial_value](../models_1_0/valid/3.4.3.1.variable_with_initial_value.cellml): Valid file passed validation.

[3.4.3.1.variable_with_interfaces](../models_1_0/valid/3.4.3.1.variable_with_interfaces.cellml): Valid file passed validation.

❗`3.4.3.1.variable_with_map_components`: **Test not run**

❗`3.4.3.1.variable_with_map_variables`: **Test not run**

❗`3.4.3.1.variable_with_math`: **Test not run**

❗`3.4.3.1.variable_with_model`: **Test not run**

❗`3.4.3.1.variable_with_reaction`: **Test not run**

❗`3.4.3.1.variable_with_relationship_ref`: **Test not run**

❗`3.4.3.1.variable_with_role`: **Test not run**

❗`3.4.3.1.variable_with_unit`: **Test not run**

❗`3.4.3.1.variable_with_units`: **Test not run**

❗`3.4.3.1.variable_with_variable`: **Test not run**

❗`3.4.3.1.variable_with_variable_ref`: **Test not run**

[3.4.3.1.variable_without_initial_value](../models_1_0/valid/3.4.3.1.variable_without_initial_value.cellml): Valid file passed validation.

❗`3.4.3.2.variable_name_duplicate`: **Test not run**

❗`3.4.3.2.variable_name_invalid`: **Test not run**


---

##### 3.4.3.2

[3.4.3.2.variable_name_same_as_cousin](../models_1_0/valid/3.4.3.2.variable_name_same_as_cousin.cellml): Valid file passed validation.

[3.4.3.2.variable_name_same_as_parent](../models_1_0/valid/3.4.3.2.variable_name_same_as_parent.cellml): Valid file passed validation.


---

##### 3.4.3.3

[3.4.3.3.variable_units_component](../models_1_0/valid/3.4.3.3.variable_units_component.cellml): Valid file passed validation.

[3.4.3.3.variable_units_model](../models_1_0/valid/3.4.3.3.variable_units_model.cellml): Valid file passed validation.

❗`3.4.3.3.variable_units_other_component`: **Test not run**

[3.4.3.3.variable_units_predefined](../models_1_0/valid/3.4.3.3.variable_units_predefined.cellml): Valid file passed validation.

❗`3.4.3.3.variable_units_unknown`: **Test not run**

❗`3.4.3.4.variable_interface_public_invalid`: **Test not run**

❗`3.4.3.5.variable_interface_private_invalid`: **Test not run**

❗`3.4.3.6.variable_interfaces_both_in`: **Test not run**

❗`3.4.3.7.variable_initial_value_empty`: **Test not run**

❗`3.4.3.7.variable_initial_value_invalid`: **Test not run**

❗`3.4.3.8.variable_interfaces_private_in_and_initial`: **Test not run**

❗`3.4.3.8.variable_interfaces_public_in_and_initial`: **Test not run**

❗`3.4.4.1.connection_empty`: **Test not run**

❗`3.4.4.1.connection_map_components_missing`: **Test not run**

❗`3.4.4.1.connection_map_components_multiple`: **Test not run**

❗`3.4.4.1.connection_map_variables_missing_1`: **Test not run**

❗`3.4.4.1.connection_map_variables_missing_2`: **Test not run**

❗`3.4.4.1.connection_only_extensions`: **Test not run**

❗`3.4.4.1.connection_with_component`: **Test not run**

❗`3.4.4.1.connection_with_component_ref`: **Test not run**

❗`3.4.4.1.connection_with_connection`: **Test not run**

❗`3.4.4.1.connection_with_group`: **Test not run**


---

##### 3.4.4.1

[3.4.4.1.connection_with_map_variables](../models_1_0/valid/3.4.4.1.connection_with_map_variables.cellml): Valid file passed validation.

❗`3.4.4.1.connection_with_math`: **Test not run**

❗`3.4.4.1.connection_with_model`: **Test not run**

❗`3.4.4.1.connection_with_name_attribute`: **Test not run**

[3.4.4.1.connection_with_one_map_variables](../models_1_0/valid/3.4.4.1.connection_with_one_map_variables.cellml): Valid file passed validation.

❗`3.4.4.1.connection_with_reaction`: **Test not run**

❗`3.4.4.1.connection_with_relationship_ref`: **Test not run**

❗`3.4.4.1.connection_with_role`: **Test not run**

❗`3.4.4.1.connection_with_unit`: **Test not run**

❗`3.4.4.1.connection_with_units`: **Test not run**

❗`3.4.4.1.connection_with_variable`: **Test not run**

❗`3.4.4.1.connection_with_variable_ref`: **Test not run**


---

##### 3.4.5.1

[3.4.5.1.connection_any_order_1](../models_1_0/valid/3.4.5.1.connection_any_order_1.cellml): Valid file passed validation.

[3.4.5.1.connection_any_order_2](../models_1_0/valid/3.4.5.1.connection_any_order_2.cellml): Valid file passed validation.

❗`3.4.5.1.map_components_component_1_missing`: **Test not run**

❗`3.4.5.1.map_components_component_2_missing`: **Test not run**

❗`3.4.5.1.map_components_with_component`: **Test not run**

❗`3.4.5.1.map_components_with_component_ref`: **Test not run**

❗`3.4.5.1.map_components_with_connection`: **Test not run**

❗`3.4.5.1.map_components_with_group`: **Test not run**

❗`3.4.5.1.map_components_with_map_components`: **Test not run**

❗`3.4.5.1.map_components_with_map_variables`: **Test not run**

❗`3.4.5.1.map_components_with_math`: **Test not run**

❗`3.4.5.1.map_components_with_model`: **Test not run**

❗`3.4.5.1.map_components_with_reaction`: **Test not run**

❗`3.4.5.1.map_components_with_relationship_ref`: **Test not run**

❗`3.4.5.1.map_components_with_role`: **Test not run**

❗`3.4.5.1.map_components_with_unit`: **Test not run**

❗`3.4.5.1.map_components_with_units`: **Test not run**

❗`3.4.5.1.map_components_with_variable`: **Test not run**

❗`3.4.5.1.map_components_with_variable_ref`: **Test not run**

❗`3.4.5.2.map_components_component_1_nonexistent`: **Test not run**

❗`3.4.5.3.map_components_component_2_nonexistent`: **Test not run**

❗`3.4.5.4.map_components_component_1_equals_2`: **Test not run**

❗`3.4.5.4.map_components_duplicate`: **Test not run**

❗`3.4.5.4.map_components_duplicate_mirrored`: **Test not run**

❗`3.4.6.1.map_variables_variable_1_missing`: **Test not run**

❗`3.4.6.1.map_variables_variable_2_missing`: **Test not run**

❗`3.4.6.1.map_variables_with_component`: **Test not run**

❗`3.4.6.1.map_variables_with_component_ref`: **Test not run**

❗`3.4.6.1.map_variables_with_connection`: **Test not run**

❗`3.4.6.1.map_variables_with_group`: **Test not run**

❗`3.4.6.1.map_variables_with_map_components`: **Test not run**

❗`3.4.6.1.map_variables_with_map_variables`: **Test not run**

❗`3.4.6.1.map_variables_with_math`: **Test not run**

❗`3.4.6.1.map_variables_with_model`: **Test not run**

❗`3.4.6.1.map_variables_with_reaction`: **Test not run**

❗`3.4.6.1.map_variables_with_relationship_ref`: **Test not run**

❗`3.4.6.1.map_variables_with_role`: **Test not run**

❗`3.4.6.1.map_variables_with_unit`: **Test not run**

❗`3.4.6.1.map_variables_with_units`: **Test not run**

❗`3.4.6.1.map_variables_with_variable`: **Test not run**

❗`3.4.6.1.map_variables_with_variable_ref`: **Test not run**

❗`3.4.6.2.map_variables_variable_1_nonexistent`: **Test not run**

❗`3.4.6.3.map_variables_variable_2_nonexistent`: **Test not run**


---

##### 3.4.6.4

[3.4.6.4.map_variables_chain_down](../models_1_0/valid/3.4.6.4.map_variables_chain_down.cellml): Valid file passed validation.

[3.4.6.4.map_variables_chain_up](../models_1_0/valid/3.4.6.4.map_variables_chain_up.cellml): Valid file passed validation.

❗`3.4.6.4.map_variables_child_multiple_out_1`: **Test not run**

❗`3.4.6.4.map_variables_child_multiple_out_2`: **Test not run**

❗`3.4.6.4.map_variables_child_out_to_out_1`: **Test not run**

❗`3.4.6.4.map_variables_child_out_to_out_2`: **Test not run**

❗`3.4.6.4.map_variables_child_private_in`: **Test not run**

❗`3.4.6.4.map_variables_child_private_out`: **Test not run**

❗`3.4.6.4.map_variables_hidden_aunt_1`: **Test not run**

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

[3.4.6.4.map_variables_nested_sibling_connection](../models_1_0/valid/3.4.6.4.map_variables_nested_sibling_connection.cellml): Valid file passed validation.

❗`3.4.6.4.map_variables_nested_sibling_private_in`: **Test not run**

❗`3.4.6.4.map_variables_nested_sibling_private_in_and_out`: **Test not run**

❗`3.4.6.4.map_variables_nested_sibling_private_out`: **Test not run**

[3.4.6.4.map_variables_parent_connection_1](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_connection_2](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_2.cellml): Valid file passed validation.

❗`3.4.6.4.map_variables_parent_in_to_in_1`: **Test not run**

❗`3.4.6.4.map_variables_parent_in_to_in_2`: **Test not run**

[3.4.6.4.map_variables_parent_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_2.cellml): Valid file passed validation.

❗`3.4.6.4.map_variables_parent_multiple_out`: **Test not run**

❗`3.4.6.4.map_variables_parent_out_to_out_1`: **Test not run**

❗`3.4.6.4.map_variables_parent_out_to_out_2`: **Test not run**

❗`3.4.6.4.map_variables_parent_public_in`: **Test not run**

❗`3.4.6.4.map_variables_parent_public_out`: **Test not run**

[3.4.6.4.map_variables_sibling_connection_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_connection_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_connection_3](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_3.cellml): Valid file passed validation.

❗`3.4.6.4.map_variables_sibling_in_to_in`: **Test not run**

[3.4.6.4.map_variables_sibling_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_2.cellml): Valid file passed validation.

❗`3.4.6.4.map_variables_sibling_multiple_out_1`: **Test not run**

❗`3.4.6.4.map_variables_sibling_multiple_out_2`: **Test not run**

[3.4.6.4.map_variables_sibling_mutual](../models_1_0/valid/3.4.6.4.map_variables_sibling_mutual.cellml): Valid file passed validation.

❗`3.4.6.4.map_variables_sibling_out_to_out`: **Test not run**

❗`3.4.6.4.map_variables_sibling_private_in_1`: **Test not run**

❗`3.4.6.4.map_variables_sibling_private_in_2`: **Test not run**

❗`3.4.6.4.map_variables_sibling_private_in_and_out`: **Test not run**

❗`3.4.6.4.map_variables_sibling_private_out_1`: **Test not run**

❗`3.4.6.4.map_variables_sibling_private_out_2`: **Test not run**

[3.4.6.4.map_variables_talking_aunt](../models_1_0/valid/3.4.6.4.map_variables_talking_aunt.cellml): Valid file passed validation.

[3.4.6.4.map_variables_talking_cousins](../models_1_0/valid/3.4.6.4.map_variables_talking_cousins.cellml): Valid file passed validation.

[3.4.6.4.map_variables_talking_niece](../models_1_0/valid/3.4.6.4.map_variables_talking_niece.cellml): Valid file passed validation.


---

## 4. Mathematics

### 4.2

[4.2.3_1.mathml_basics](../models_1_0/valid/4.2.3_1.mathml_basics.cellml): Valid file passed validation.

[4.2.3_2.1.mathml_numbers_real](../models_1_0/numbers/4.2.3_2.1.mathml_numbers_real.cellml): Valid file passed validation.

[4.2.3_2.2.mathml_numbers_integer](../models_1_0/numbers/4.2.3_2.2.mathml_numbers_integer.cellml): Valid file passed validation.

[4.2.3_2.3.mathml_numbers_real_base](../models_1_0/numbers/4.2.3_2.3.mathml_numbers_real_base.cellml): Valid file passed validation.

[4.2.3_2.4.mathml_numbers_integer_base](../models_1_0/numbers/4.2.3_2.4.mathml_numbers_integer_base.cellml): Valid file passed validation.

[4.2.3_2.5.mathml_numbers_e_notation](../models_1_0/numbers/4.2.3_2.5.mathml_numbers_e_notation.cellml): Valid file passed validation.

[4.2.3_2.6.mathml_numbers_rational](../models_1_0/numbers/4.2.3_2.6.mathml_numbers_rational.cellml): Valid file passed validation.

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

[4.2.3_8.1_annotation](../models_1_0/valid/4.2.3_8.1_annotation.cellml): Valid file passed validation.

[4.2.3_8.2_annotation_xml](../models_1_0/valid/4.2.3_8.2_annotation_xml.cellml): Valid file passed validation.

❗`4.4.1.math_not_math_component`: **Test not run**

❗`4.4.1.math_not_math_reaction`: **Test not run**


---

#### 4.4.2

[4.4.2.ci_no_whitespace](../models_1_0/valid/4.4.2.ci_no_whitespace.cellml): Valid file passed validation.

❗`4.4.2.ci_non_local_aunt`: **Test not run**

❗`4.4.2.ci_non_local_child`: **Test not run**

❗`4.4.2.ci_non_local_cousin`: **Test not run**

❗`4.4.2.ci_non_local_nested_sibling`: **Test not run**

❗`4.4.2.ci_non_local_niece`: **Test not run**

❗`4.4.2.ci_non_local_parent`: **Test not run**

❗`4.4.2.ci_non_local_sibling`: **Test not run**

❗`4.4.2.ci_nonexistent`: **Test not run**

[4.4.2.ci_whitespace_1](../models_1_0/valid/4.4.2.ci_whitespace_1.cellml): Valid file passed validation.

[4.4.2.ci_whitespace_2](../models_1_0/valid/4.4.2.ci_whitespace_2.cellml): Valid file passed validation.

[4.4.2.ci_whitespace_3](../models_1_0/valid/4.4.2.ci_whitespace_3.cellml): Valid file passed validation.


---

##### 4.4.3.1

[4.4.3.1.cn_component_units](../models_1_0/valid/4.4.3.1.cn_component_units.cellml): Valid file passed validation.

[4.4.3.1.cn_model_units](../models_1_0/valid/4.4.3.1.cn_model_units.cellml): Valid file passed validation.

[4.4.3.1.cn_predefined_units](../models_1_0/valid/4.4.3.1.cn_predefined_units.cellml): Valid file passed validation.

❗`4.4.3.1.cn_units_missing`: **Test not run**

❗`4.4.3.2.cn_units_nonexistent_1`: **Test not run**

❗`4.4.3.2.cn_units_nonexistent_2`: **Test not run**

❗`4.4.3.2.cn_units_parent_component`: **Test not run**

❗`4.4.4.modify_nonexistent`: **Test not run**

❗`4.4.4.modify_private_in`: **Test not run**


---

#### 4.4.4

[4.4.4.modify_private_out](../models_1_0/valid/4.4.4.modify_private_out.cellml): Valid file passed validation.

❗`4.4.4.modify_public_in`: **Test not run**

[4.4.4.modify_public_out](../models_1_0/valid/4.4.4.modify_public_out.cellml): Valid file passed validation.


---

#### 4.5.1

[4.5.1.ordering_not_significant](../models_1_0/valid/4.5.1.ordering_not_significant.cellml): Valid file passed validation.


---

[4.algebraic_model](../models_1_0/valid/4.algebraic_model.cellml): Valid file passed validation.

[4.algebraic_ode_model](../models_1_0/valid/4.algebraic_ode_model.cellml): Valid file passed validation.

❗`4.math_and_initial_value`: **Test not run**

❗`4.math_overdefined`: **Test not run**

❗`5.2.2.unit_deca`: **Test not run**


---

## 5. Units

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

[5.2.7.unit_conversion_dimensionless_multiplier_2](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_dimensionless_multiplier_2.cellml): Valid file passed validation.

[5.2.7.unit_conversion_dimensionless_offset](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_dimensionless_offset.cellml): Valid file passed validation.

[5.2.7.unit_conversion_inconvertible_1](../models_1_0/unit_conversion_inconvertible/5.2.7.unit_conversion_inconvertible_1.cellml): Valid file passed validation.

[5.2.7.unit_conversion_less_obvious](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_less_obvious.cellml): Valid file passed validation.

[5.2.7.unit_conversion_multiplier](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_multiplier.cellml): Valid file passed validation.

[5.2.7.unit_conversion_new_base_units](../models_1_0/unit_conversion_inconvertible/5.2.7.unit_conversion_new_base_units.cellml): Valid file passed validation.

[5.2.7.unit_conversion_offset](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_offset.cellml): Valid file passed validation.

[5.2.7.unit_conversion_prefix](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_prefix.cellml): Valid file passed validation.


---

##### 5.4.1.1

[5.4.1.1.units_base_units](../models_1_0/valid/5.4.1.1.units_base_units.cellml): Valid file passed validation.

❗`5.4.1.1.units_base_units_with_children`: **Test not run**

[5.4.1.1.units_empty_1](../models_1_0/valid/5.4.1.1.units_empty_1.cellml): Valid file passed validation.

[5.4.1.1.units_empty_2](../models_1_0/valid/5.4.1.1.units_empty_2.cellml): Valid file passed validation.

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

[5.4.1.1.units_with_unit_children](../models_1_0/valid/5.4.1.1.units_with_unit_children.cellml): Valid file passed validation.

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


---

##### 5.4.1.2

[5.4.1.2.units_names_and_other_names](../models_1_0/valid/5.4.1.2.units_names_and_other_names.cellml): Valid file passed validation.

[5.4.1.2.units_shadowing_1](../models_1_0/valid/5.4.1.2.units_shadowing_1.cellml): Valid file passed validation.

[5.4.1.2.units_shadowing_2](../models_1_0/valid/5.4.1.2.units_shadowing_2.cellml): Valid file passed validation.

❗`5.4.1.3.units_base_units_invalid`: **Test not run**


---

##### 5.4.2.1

[5.4.2.1.unit_offset_non_zero](../models_1_0/valid/5.4.2.1.unit_offset_non_zero.cellml): Valid file passed validation.

[5.4.2.1.unit_offset_zero](../models_1_0/valid/5.4.2.1.unit_offset_zero.cellml): Valid file passed validation.

[5.4.2.1.unit_prefix_exponent_multiplier](../models_1_0/valid/5.4.2.1.unit_prefix_exponent_multiplier.cellml): Valid file passed validation.

[5.4.2.1.unit_prefix_exponent_multiplier_huge](../models_1_0/valid/5.4.2.1.unit_prefix_exponent_multiplier_huge.cellml): Valid file passed validation.

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


---

##### 5.4.2.2

[5.4.2.2.unit_units_local_1](../models_1_0/valid/5.4.2.2.unit_units_local_1.cellml): Valid file passed validation.

[5.4.2.2.unit_units_local_2](../models_1_0/valid/5.4.2.2.unit_units_local_2.cellml): Valid file passed validation.


---

##### 5.4.2.3

[5.4.2.3.unit_prefix_integer](../models_1_0/valid/5.4.2.3.unit_prefix_integer.cellml): Valid file passed validation.

[5.4.2.3.unit_prefix_named](../models_1_0/valid/5.4.2.3.unit_prefix_named.cellml): Valid file passed validation.

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


---

##### 5.4.2.7

[5.4.2.7.unit_offset_non_zero_and_exponent_one](../models_1_0/valid/5.4.2.7.unit_offset_non_zero_and_exponent_one.cellml): Valid file passed validation.

[5.4.2.7.unit_offset_zero_and_exponent](../models_1_0/valid/5.4.2.7.unit_offset_zero_and_exponent.cellml): Valid file passed validation.

[5.4.2.7.unit_offset_zero_and_siblings](../models_1_0/valid/5.4.2.7.unit_offset_zero_and_siblings.cellml): Valid file passed validation.


---

#### 5.5.2

[5.5.2.boolean_arithmetic_divide](../models_1_0/booleans/5.5.2.boolean_arithmetic_divide.cellml): Valid file passed validation.

[5.5.2.boolean_arithmetic_minus](../models_1_0/booleans/5.5.2.boolean_arithmetic_minus.cellml): Valid file passed validation.

[5.5.2.boolean_arithmetic_plus](../models_1_0/booleans/5.5.2.boolean_arithmetic_plus.cellml): Valid file passed validation.

[5.5.2.boolean_arithmetic_power_1](../models_1_0/booleans/5.5.2.boolean_arithmetic_power_1.cellml): Valid file passed validation.

[5.5.2.boolean_arithmetic_power_2](../models_1_0/booleans/5.5.2.boolean_arithmetic_power_2.cellml): Valid file passed validation.

[5.5.2.boolean_arithmetic_root_1](../models_1_0/booleans/5.5.2.boolean_arithmetic_root_1.cellml): Valid file passed validation.

[5.5.2.boolean_arithmetic_root_2](../models_1_0/booleans/5.5.2.boolean_arithmetic_root_2.cellml): Valid file passed validation.

[5.5.2.boolean_arithmetic_times](../models_1_0/booleans/5.5.2.boolean_arithmetic_times.cellml): Valid file passed validation.

[5.5.2.boolean_compare_eq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_eq_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_geq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_geq_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_gt_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_gt_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_leq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_leq_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_lt_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_lt_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_neq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_neq_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_derivatives_1](../models_1_0/booleans/5.5.2.boolean_derivatives_1.cellml): Valid file passed validation.

[5.5.2.boolean_derivatives_2](../models_1_0/booleans/5.5.2.boolean_derivatives_2.cellml): Valid file passed validation.

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

❗`6.4.1.1.group_component_ref_missing_1`: **Test not run**

❗`6.4.1.1.group_component_ref_missing_2`: **Test not run**


---

## 6. Grouping

##### 6.4.1.1

[6.4.1.1.group_component_ref_multiple](../models_1_0/valid/6.4.1.1.group_component_ref_multiple.cellml): Valid file passed validation.

[6.4.1.1.group_component_ref_single](../models_1_0/valid/6.4.1.1.group_component_ref_single.cellml): Valid file passed validation.

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


---

#### 6.4.1

[6.4.1.group_child_order_1](../models_1_0/valid/6.4.1.group_child_order_1.cellml): Valid file passed validation.

[6.4.1.group_child_order_2](../models_1_0/valid/6.4.1.group_child_order_2.cellml): Valid file passed validation.


---

##### 6.4.2.1

[6.4.2.1.relationship_ref_name](../models_1_0/valid/6.4.2.1.relationship_ref_name.cellml): Valid file passed validation.

[6.4.2.1.relationship_ref_relationship_1](../models_1_0/valid/6.4.2.1.relationship_ref_relationship_1.cellml): Valid file passed validation.

🔴 [6.4.2.1.relationship_ref_relationship_2](../models_1_0/valid/6.4.2.1.relationship_ref_relationship_2.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 7: No declaration for attribute xmlns:family of element model```
  * ```Error on line 11: No declaration for attribute relationship of element relationship_ref```

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


---

##### 6.4.2.3

[6.4.2.3.relationship_ref_name_not_unique_model_wide](../models_1_0/valid/6.4.2.3.relationship_ref_name_not_unique_model_wide.cellml): Valid file passed validation.

❗`6.4.2.4.relationship_ref_encapsulation_duplicate`: **Test not run**

❗`6.4.2.4.relationship_ref_encapsulation_named`: **Test not run**

❗`6.4.2.5.relationship_ref_duplicate_named`: **Test not run**

❗`6.4.2.5.relationship_ref_duplicate_unnamed_1`: **Test not run**

❗`6.4.2.5.relationship_ref_duplicate_unnamed_2`: **Test not run**


---

##### 6.4.2.5

[6.4.2.5.relationship_ref_multiple_1](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_1.cellml): Valid file passed validation.

[6.4.2.5.relationship_ref_multiple_2](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_2.cellml): Valid file passed validation.

[6.4.2.5.relationship_ref_multiple_3](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_3.cellml): Valid file passed validation.

❗`6.4.3.1.component_ref_component_missing`: **Test not run**


---

##### 6.4.3.1

[6.4.3.1.component_ref_nesting](../models_1_0/valid/6.4.3.1.component_ref_nesting.cellml): Valid file passed validation.

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


---

##### 6.4.3.2

🔴 [6.4.3.2.component_ref_no_children_extension](../models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 12: No declaration for attribute relationship of element relationship_ref```

[6.4.3.2.component_ref_overlapping_containment](../models_1_0/valid/6.4.3.2.component_ref_overlapping_containment.cellml): Valid file passed validation.

❗`6.4.3.2.component_ref_overlapping_encapsulation`: **Test not run**

[6.4.3.2.component_ref_split_named](../models_1_0/valid/6.4.3.2.component_ref_split_named.cellml): Valid file passed validation.

[6.4.3.2.component_ref_split_unnamed_1](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_1.cellml): Valid file passed validation.

[6.4.3.2.component_ref_split_unnamed_2](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_2.cellml): Valid file passed validation.

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


---

## 7. Reactions

##### 7.4.1.2

[7.4.1.2.reaction_reversible_no](../models_1_0/valid/7.4.1.2.reaction_reversible_no.cellml): Valid file passed validation.

[7.4.1.2.reaction_reversible_yes](../models_1_0/valid/7.4.1.2.reaction_reversible_yes.cellml): Valid file passed validation.

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


---

#### 7.4.3

[7.4.3.reaction_all_roles_and_attributes](../models_1_0/valid/7.4.3.reaction_all_roles_and_attributes.cellml): Valid file passed validation.

[7.4.3.reaction_reversible_no](../models_1_0/valid/7.4.3.reaction_reversible_no.cellml): Valid file passed validation.

[7.4.3.reaction_simple](../models_1_0/valid/7.4.3.reaction_simple.cellml): Valid file passed validation.

❗`8.4.1.cmeta_id_duplicate`: **Test not run**


---

## 8. Metadata framework

#### 8.4.1

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

🔴 [8.4.2.rdf_in_component](../models_1_0/valid/8.4.2.rdf_in_component.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 9: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (rdf:RDF )```
  * ```Error on line 10: No declaration for element RDF```
  * ```Error on line 10: No declaration for attribute about of element RDF```
  * ```Error on line 11: No declaration for element description```

🔴 [8.4.2.rdf_in_component_ref](../models_1_0/valid/8.4.2.rdf_in_component_ref.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 14: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (rdf:RDF )```
  * ```Error on line 15: No declaration for element RDF```
  * ```Error on line 15: No declaration for attribute about of element RDF```
  * ```Error on line 16: No declaration for element description```

🔴 [8.4.2.rdf_in_connection](../models_1_0/valid/8.4.2.rdf_in_connection.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 15: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables rdf:RDF )```
  * ```Error on line 18: No declaration for element RDF```
  * ```Error on line 18: No declaration for attribute about of element RDF```
  * ```Error on line 19: No declaration for element description```

🔴 [8.4.2.rdf_in_group](../models_1_0/valid/8.4.2.rdf_in_group.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 11: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref rdf:RDF )```
  * ```Error on line 16: No declaration for element RDF```
  * ```Error on line 16: No declaration for attribute about of element RDF```
  * ```Error on line 17: No declaration for element description```

🔴 [8.4.2.rdf_in_map_components](../models_1_0/valid/8.4.2.rdf_in_map_components.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 10: Element map_components was declared EMPTY this one has content```
  * ```Error on line 11: No declaration for element RDF```
  * ```Error on line 11: No declaration for attribute about of element RDF```
  * ```Error on line 12: No declaration for element description```

🔴 [8.4.2.rdf_in_map_variables](../models_1_0/valid/8.4.2.rdf_in_map_variables.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 17: Element map_variables was declared EMPTY this one has content```
  * ```Error on line 18: No declaration for element RDF```
  * ```Error on line 18: No declaration for attribute about of element RDF```
  * ```Error on line 19: No declaration for element description```

🔴 [8.4.2.rdf_in_model](../models_1_0/valid/8.4.2.rdf_in_model.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 9: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (rdf:RDF )```
  * ```Error on line 9: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 9: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 10: No declaration for element RDF```
  * ```Error on line 10: No declaration for attribute about of element RDF```
  * ```Error on line 11: No declaration for element description```

🔴 [8.4.2.rdf_in_reaction](../models_1_0/valid/8.4.2.rdf_in_reaction.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 11: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref rdf:RDF )```
  * ```Error on line 15: No declaration for element RDF```
  * ```Error on line 15: No declaration for attribute about of element RDF```
  * ```Error on line 16: No declaration for element description```

🔴 [8.4.2.rdf_in_relationship_ref](../models_1_0/valid/8.4.2.rdf_in_relationship_ref.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 12: Element relationship_ref was declared EMPTY this one has content```
  * ```Error on line 13: No declaration for element RDF```
  * ```Error on line 13: No declaration for attribute about of element RDF```
  * ```Error on line 14: No declaration for element description```

🔴 [8.4.2.rdf_in_role](../models_1_0/valid/8.4.2.rdf_in_role.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 13: Element role content does not follow the DTD, expecting (math)?, got (rdf:RDF )```
  * ```Error on line 14: No declaration for element RDF```
  * ```Error on line 14: No declaration for attribute about of element RDF```
  * ```Error on line 15: No declaration for element description```

🔴 [8.4.2.rdf_in_unit](../models_1_0/valid/8.4.2.rdf_in_unit.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 10: Element unit was declared EMPTY this one has content```
  * ```Error on line 11: No declaration for element RDF```
  * ```Error on line 11: No declaration for attribute about of element RDF```
  * ```Error on line 12: No declaration for element description```

🔴 [8.4.2.rdf_in_units_1](../models_1_0/valid/8.4.2.rdf_in_units_1.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 9: Element units content does not follow the DTD, expecting (unit)*, got (unit rdf:RDF )```
  * ```Error on line 11: No declaration for element RDF```
  * ```Error on line 11: No declaration for attribute about of element RDF```
  * ```Error on line 12: No declaration for element description```

🔴 [8.4.2.rdf_in_units_2](../models_1_0/valid/8.4.2.rdf_in_units_2.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 10: Element units content does not follow the DTD, expecting (unit)*, got (unit rdf:RDF )```
  * ```Error on line 12: No declaration for element RDF```
  * ```Error on line 12: No declaration for attribute about of element RDF```
  * ```Error on line 13: No declaration for element description```

🔴 [8.4.2.rdf_in_variable](../models_1_0/valid/8.4.2.rdf_in_variable.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 10: Element variable was declared EMPTY this one has content```
  * ```Error on line 11: No declaration for element RDF```
  * ```Error on line 11: No declaration for attribute about of element RDF```
  * ```Error on line 12: No declaration for element description```

🔴 [8.4.2.rdf_in_variable_ref](../models_1_0/valid/8.4.2.rdf_in_variable_ref.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute xmlns:dc of element model```
  * ```Error on line 12: Element variable_ref content does not follow the DTD, expecting (role)+, got (rdf:RDF role )```
  * ```Error on line 13: No declaration for element RDF```
  * ```Error on line 13: No declaration for attribute about of element RDF```
  * ```Error on line 14: No declaration for element description```


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

[C.3.3.unit_checking_arithmetic_power_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_power_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_arithmetic_root_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_arithmetic_root_operand_error.cellml): Valid file passed validation.

[C.3.3.unit_checking_compare_eq_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_eq_operand_mismatch.cellml): Valid file passed validation.

[C.3.3.unit_checking_compare_geq_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_geq_operand_mismatch.cellml): Valid file passed validation.

[C.3.3.unit_checking_compare_gt_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_gt_operand_mismatch.cellml): Valid file passed validation.

[C.3.3.unit_checking_compare_leq_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_leq_operand_mismatch.cellml): Valid file passed validation.

[C.3.3.unit_checking_compare_lt_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_lt_operand_mismatch.cellml): Valid file passed validation.

[C.3.3.unit_checking_compare_neq_operand_mismatch](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_compare_neq_operand_mismatch.cellml): Valid file passed validation.

[C.3.3.unit_checking_derivative_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_derivative_operand_error.cellml): Valid file passed validation.

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

# DTD Validation - CellML 1.0

Performance:
* 72% according to spec (670 out of 927)
* 329 out of 375 valid files passed
* 341 out of 552 invalid files detected

Issues:
* 46 valid files failed validation
* 209 invalid files passed validation
* 2 invalid files failed validation for the wrong reason

Results per category

(Valid passed, invalid failed, valid failed, invalid passed, invalid failed for wrong reason, percent classified correctly according to spec)

|Category|V Pass|I Fail|🔴 V Fail|🔵 I Pass|🔶 I Bad|Score|
|-|-|-|-|-|-|-|
|[0. Not mentioned in spec](#0-not-mentioned-in-spec)|6|2|0|11|0|42%|
|[2. Fundamentals](#2-fundamentals)|5|95|29|6|2|72%|
|[3. Model structure](#3-model-structure)|50|97|0|58|0|71%|
|[4. Mathematics](#4-mathematics)|50|3|0|17|0|75%|
|[5. Units](#5-units)|136|32|0|57|0|74%|
|[6. Grouping](#6-grouping)|15|48|2|30|0|66%|
|[7. Reactions](#7-reactions)|5|49|0|30|0|64%|
|[8. Metadata framework](#8-metadata-framework)|15|15|15|0|0|66%|
|[C. Advanced units functionality](#c-advanced-units-functionality)|47|0|0|0|0|100%|


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

🔵 [0.1.real_number_invalid_7](../models_1_0/invalid/0.1.real_number_invalid_7.cellml): **Error not detected.**

🔵 [0.1.real_number_invalid_8](../models_1_0/invalid/0.1.real_number_invalid_8.cellml): **Error not detected.**

🔵 [0.1.real_number_invalid_9](../models_1_0/invalid/0.1.real_number_invalid_9.cellml): **Error not detected.**

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

[2.4.2.imaginary_elements_1](../models_1_0/invalid/2.4.2.imaginary_elements_1.cellml): Error detected correctly.
* Expected: ```No declaration for element fruit```
* Output:
  * ```Error on line 5: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (fruit )```
  * ```Error on line 6: No declaration for element fruit```

[2.4.2.imaginary_elements_2](../models_1_0/invalid/2.4.2.imaginary_elements_2.cellml): Error detected correctly.
* Expected: ```No declaration for element import```
* Output:
  * ```Error on line 7: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (import )```
  * ```Error on line 7: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 8: No declaration for element import```
  * ```Error on line 8: No declaration for attribute href of element import```
  * ```Error on line 9: No declaration for attribute units_ref of element units```


---

#### 2.4.3

[2.4.3.bad_cmeta_attribute_in_component](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_component.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 8: No declaration for attribute bob of element component```

[2.4.3.bad_cmeta_attribute_in_component_ref](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_component_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 13: No declaration for attribute bob of element component_ref```

[2.4.3.bad_cmeta_attribute_in_connection](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_connection.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 14: No declaration for attribute bob of element connection```

[2.4.3.bad_cmeta_attribute_in_group](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_group.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 10: No declaration for attribute bob of element group```

[2.4.3.bad_cmeta_attribute_in_map_components](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_map_components.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 9: No declaration for attribute bob of element map_components```

[2.4.3.bad_cmeta_attribute_in_map_variables](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_map_variables.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 16: No declaration for attribute bob of element map_variables```

[2.4.3.bad_cmeta_attribute_in_model](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_model.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 8: No declaration for attribute bob of element model```

[2.4.3.bad_cmeta_attribute_in_reaction](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_reaction.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 10: No declaration for attribute bob of element reaction```

[2.4.3.bad_cmeta_attribute_in_relationship_ref](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 11: No declaration for attribute bob of element relationship_ref```

[2.4.3.bad_cmeta_attribute_in_role](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_role.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 12: No declaration for attribute bob of element role```

[2.4.3.bad_cmeta_attribute_in_unit](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_unit.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 9: No declaration for attribute bob of element unit```

[2.4.3.bad_cmeta_attribute_in_units_1](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_units_1.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 8: No declaration for attribute bob of element units```

[2.4.3.bad_cmeta_attribute_in_units_2](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_units_2.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 9: No declaration for attribute bob of element units```

[2.4.3.bad_cmeta_attribute_in_variable](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_variable.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 9: No declaration for attribute bob of element variable```

[2.4.3.bad_cmeta_attribute_in_variable_ref](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_variable_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output: ```Error on line 11: No declaration for attribute bob of element variable_ref```

[2.4.3.bad_rdf_element_in_component](../models_1_0/invalid/2.4.3.bad_rdf_element_in_component.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 7: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (rdf:Description )```
  * ```Error on line 8: No declaration for element Description```
  * ```Error on line 8: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_component_ref](../models_1_0/invalid/2.4.3.bad_rdf_element_in_component_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 12: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (rdf:Description )```
  * ```Error on line 13: No declaration for element Description```
  * ```Error on line 13: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_connection](../models_1_0/invalid/2.4.3.bad_rdf_element_in_connection.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables rdf:Description )```
  * ```Error on line 16: No declaration for element Description```
  * ```Error on line 16: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_group](../models_1_0/invalid/2.4.3.bad_rdf_element_in_group.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 9: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref rdf:Description )```
  * ```Error on line 14: No declaration for element Description```
  * ```Error on line 14: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_map_components](../models_1_0/invalid/2.4.3.bad_rdf_element_in_map_components.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: Element map_components was declared EMPTY this one has content```
  * ```Error on line 9: No declaration for element Description```
  * ```Error on line 9: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_map_variables](../models_1_0/invalid/2.4.3.bad_rdf_element_in_map_variables.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 15: Element map_variables was declared EMPTY this one has content```
  * ```Error on line 16: No declaration for element Description```
  * ```Error on line 16: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_model](../models_1_0/invalid/2.4.3.bad_rdf_element_in_model.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (rdf:Description )```
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 7: No declaration for element Description```
  * ```Error on line 7: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_reaction](../models_1_0/invalid/2.4.3.bad_rdf_element_in_reaction.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 9: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref rdf:Description )```
  * ```Error on line 13: No declaration for element Description```
  * ```Error on line 13: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_relationship_ref](../models_1_0/invalid/2.4.3.bad_rdf_element_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 10: Element relationship_ref was declared EMPTY this one has content```
  * ```Error on line 11: No declaration for element Description```
  * ```Error on line 11: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_role](../models_1_0/invalid/2.4.3.bad_rdf_element_in_role.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 11: Element role content does not follow the DTD, expecting (math)?, got (rdf:Description )```
  * ```Error on line 12: No declaration for element Description```
  * ```Error on line 12: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_unit](../models_1_0/invalid/2.4.3.bad_rdf_element_in_unit.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: Element unit was declared EMPTY this one has content```
  * ```Error on line 9: No declaration for element Description```
  * ```Error on line 9: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_units_1](../models_1_0/invalid/2.4.3.bad_rdf_element_in_units_1.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 7: Element units content does not follow the DTD, expecting (unit)*, got (unit rdf:Description )```
  * ```Error on line 9: No declaration for element Description```
  * ```Error on line 9: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_units_2](../models_1_0/invalid/2.4.3.bad_rdf_element_in_units_2.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: Element units content does not follow the DTD, expecting (unit)*, got (unit rdf:Description )```
  * ```Error on line 10: No declaration for element Description```
  * ```Error on line 10: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_variable](../models_1_0/invalid/2.4.3.bad_rdf_element_in_variable.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: Element variable was declared EMPTY this one has content```
  * ```Error on line 9: No declaration for element Description```
  * ```Error on line 9: No declaration for attribute about of element Description```

[2.4.3.bad_rdf_element_in_variable_ref](../models_1_0/invalid/2.4.3.bad_rdf_element_in_variable_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 10: Element variable_ref content does not follow the DTD, expecting (role)+, got (rdf:Description role )```
  * ```Error on line 11: No declaration for element Description```
  * ```Error on line 11: No declaration for attribute about of element Description```

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

[2.4.3.cmeta_element_in_component](../models_1_0/invalid/2.4.3.cmeta_element_in_component.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 7: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (cmeta:species )```
  * ```Error on line 8: No declaration for element species```

[2.4.3.cmeta_element_in_component_ref](../models_1_0/invalid/2.4.3.cmeta_element_in_component_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 12: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (cmeta:species )```
  * ```Error on line 13: No declaration for element species```

[2.4.3.cmeta_element_in_connection](../models_1_0/invalid/2.4.3.cmeta_element_in_connection.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables cmeta:species )```
  * ```Error on line 16: No declaration for element species```

[2.4.3.cmeta_element_in_group](../models_1_0/invalid/2.4.3.cmeta_element_in_group.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 9: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref cmeta:species )```
  * ```Error on line 14: No declaration for element species```

[2.4.3.cmeta_element_in_map_components](../models_1_0/invalid/2.4.3.cmeta_element_in_map_components.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 8: Element map_components was declared EMPTY this one has content```
  * ```Error on line 9: No declaration for element species```

[2.4.3.cmeta_element_in_map_variables](../models_1_0/invalid/2.4.3.cmeta_element_in_map_variables.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 15: Element map_variables was declared EMPTY this one has content```
  * ```Error on line 16: No declaration for element species```

[2.4.3.cmeta_element_in_model](../models_1_0/invalid/2.4.3.cmeta_element_in_model.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (cmeta:species )```
  * ```Error on line 7: No declaration for element species```

[2.4.3.cmeta_element_in_reaction](../models_1_0/invalid/2.4.3.cmeta_element_in_reaction.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 9: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref cmeta:species )```
  * ```Error on line 13: No declaration for element species```

[2.4.3.cmeta_element_in_relationship_ref](../models_1_0/invalid/2.4.3.cmeta_element_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 10: Element relationship_ref was declared EMPTY this one has content```
  * ```Error on line 11: No declaration for element species```

[2.4.3.cmeta_element_in_role](../models_1_0/invalid/2.4.3.cmeta_element_in_role.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 11: Element role content does not follow the DTD, expecting (math)?, got (cmeta:species )```
  * ```Error on line 12: No declaration for element species```

[2.4.3.cmeta_element_in_unit](../models_1_0/invalid/2.4.3.cmeta_element_in_unit.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 8: Element unit was declared EMPTY this one has content```
  * ```Error on line 9: No declaration for element species```

[2.4.3.cmeta_element_in_units_1](../models_1_0/invalid/2.4.3.cmeta_element_in_units_1.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 7: Element units content does not follow the DTD, expecting (unit)*, got (unit cmeta:species )```
  * ```Error on line 9: No declaration for element species```

[2.4.3.cmeta_element_in_units_2](../models_1_0/invalid/2.4.3.cmeta_element_in_units_2.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 8: Element units content does not follow the DTD, expecting (unit)*, got (unit cmeta:species )```
  * ```Error on line 10: No declaration for element species```

[2.4.3.cmeta_element_in_variable](../models_1_0/invalid/2.4.3.cmeta_element_in_variable.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 8: Element variable was declared EMPTY this one has content```
  * ```Error on line 9: No declaration for element species```

[2.4.3.cmeta_element_in_variable_ref](../models_1_0/invalid/2.4.3.cmeta_element_in_variable_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 10: Element variable_ref content does not follow the DTD, expecting (role)+, got (cmeta:species role )```
  * ```Error on line 11: No declaration for element species```

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

[2.4.3.mathml_attribute_in_component](../models_1_0/invalid/2.4.3.mathml_attribute_in_component.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 7: No declaration for attribute sum of element component```

[2.4.3.mathml_attribute_in_component_ref](../models_1_0/invalid/2.4.3.mathml_attribute_in_component_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 12: No declaration for attribute sum of element component_ref```

[2.4.3.mathml_attribute_in_connection](../models_1_0/invalid/2.4.3.mathml_attribute_in_connection.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 13: No declaration for attribute sum of element connection```

[2.4.3.mathml_attribute_in_group](../models_1_0/invalid/2.4.3.mathml_attribute_in_group.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 9: No declaration for attribute sum of element group```

[2.4.3.mathml_attribute_in_map_components](../models_1_0/invalid/2.4.3.mathml_attribute_in_map_components.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 8: No declaration for attribute sum of element map_components```

[2.4.3.mathml_attribute_in_map_variables](../models_1_0/invalid/2.4.3.mathml_attribute_in_map_variables.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 15: No declaration for attribute sum of element map_variables```

[2.4.3.mathml_attribute_in_model](../models_1_0/invalid/2.4.3.mathml_attribute_in_model.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 7: No declaration for attribute sum of element model```
  * ```Error on line 7: No declaration for attribute xmlns:mathml of element model```

[2.4.3.mathml_attribute_in_reaction](../models_1_0/invalid/2.4.3.mathml_attribute_in_reaction.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 9: No declaration for attribute sum of element reaction```

[2.4.3.mathml_attribute_in_relationship_ref](../models_1_0/invalid/2.4.3.mathml_attribute_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 10: No declaration for attribute sum of element relationship_ref```

[2.4.3.mathml_attribute_in_role](../models_1_0/invalid/2.4.3.mathml_attribute_in_role.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 11: No declaration for attribute sum of element role```

[2.4.3.mathml_attribute_in_unit](../models_1_0/invalid/2.4.3.mathml_attribute_in_unit.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 8: No declaration for attribute sum of element unit```

[2.4.3.mathml_attribute_in_units_1](../models_1_0/invalid/2.4.3.mathml_attribute_in_units_1.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 7: No declaration for attribute sum of element units```

[2.4.3.mathml_attribute_in_units_2](../models_1_0/invalid/2.4.3.mathml_attribute_in_units_2.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 8: No declaration for attribute sum of element units```

[2.4.3.mathml_attribute_in_variable](../models_1_0/invalid/2.4.3.mathml_attribute_in_variable.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 8: No declaration for attribute sum of element variable```

[2.4.3.mathml_attribute_in_variable_ref](../models_1_0/invalid/2.4.3.mathml_attribute_in_variable_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:mathml of element model```
  * ```Error on line 10: No declaration for attribute sum of element variable_ref```

🔴 [2.4.3.model_with_extensions](../models_1_0/valid/2.4.3.model_with_extensions.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 7: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (fruit:orange fruit:pear )```
  * ```Error on line 7: No declaration for attribute x_a_day of element model```
  * ```Error on line 7: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 8: No declaration for element orange```
  * ```Error on line 8: No declaration for attribute peel of element orange```
  * ```Error on line 9: No declaration for element clementine```
  * ```Error on line 11: No declaration for element pear```

[2.4.3.rdf_attribute_in_component](../models_1_0/invalid/2.4.3.rdf_attribute_in_component.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 7: No declaration for attribute parseType of element component```

[2.4.3.rdf_attribute_in_component_ref](../models_1_0/invalid/2.4.3.rdf_attribute_in_component_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 12: No declaration for attribute parseType of element component_ref```

[2.4.3.rdf_attribute_in_connection](../models_1_0/invalid/2.4.3.rdf_attribute_in_connection.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 13: No declaration for attribute parseType of element connection```

[2.4.3.rdf_attribute_in_group](../models_1_0/invalid/2.4.3.rdf_attribute_in_group.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 9: No declaration for attribute parseType of element group```

[2.4.3.rdf_attribute_in_map_components](../models_1_0/invalid/2.4.3.rdf_attribute_in_map_components.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute parseType of element map_components```

[2.4.3.rdf_attribute_in_map_variables](../models_1_0/invalid/2.4.3.rdf_attribute_in_map_variables.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 15: No declaration for attribute parseType of element map_variables```

[2.4.3.rdf_attribute_in_model](../models_1_0/invalid/2.4.3.rdf_attribute_in_model.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 7: No declaration for attribute parseType of element model```
  * ```Error on line 7: No declaration for attribute xmlns:rdf of element model```

[2.4.3.rdf_attribute_in_reaction](../models_1_0/invalid/2.4.3.rdf_attribute_in_reaction.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 9: No declaration for attribute parseType of element reaction```

[2.4.3.rdf_attribute_in_relationship_ref](../models_1_0/invalid/2.4.3.rdf_attribute_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 10: No declaration for attribute parseType of element relationship_ref```

[2.4.3.rdf_attribute_in_role](../models_1_0/invalid/2.4.3.rdf_attribute_in_role.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 11: No declaration for attribute parseType of element role```

[2.4.3.rdf_attribute_in_unit](../models_1_0/invalid/2.4.3.rdf_attribute_in_unit.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute parseType of element unit```

[2.4.3.rdf_attribute_in_units_1](../models_1_0/invalid/2.4.3.rdf_attribute_in_units_1.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 7: No declaration for attribute parseType of element units```

[2.4.3.rdf_attribute_in_units_2](../models_1_0/invalid/2.4.3.rdf_attribute_in_units_2.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute parseType of element units```

[2.4.3.rdf_attribute_in_variable](../models_1_0/invalid/2.4.3.rdf_attribute_in_variable.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 8: No declaration for attribute parseType of element variable```

[2.4.3.rdf_attribute_in_variable_ref](../models_1_0/invalid/2.4.3.rdf_attribute_in_variable_ref.cellml): Error detected correctly.
* Expected: ```No declaration```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:rdf of element model```
  * ```Error on line 10: No declaration for attribute parseType of element variable_ref```

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

🔴 [2.4.3.xlink_href_in_component](../models_1_0/valid/2.4.3.xlink_href_in_component.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 7: No declaration for attribute href of element component```

🔴 [2.4.3.xlink_href_in_component_ref](../models_1_0/valid/2.4.3.xlink_href_in_component_ref.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 12: No declaration for attribute href of element component_ref```

🔴 [2.4.3.xlink_href_in_connection](../models_1_0/valid/2.4.3.xlink_href_in_connection.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 13: No declaration for attribute href of element connection```

🔴 [2.4.3.xlink_href_in_group](../models_1_0/valid/2.4.3.xlink_href_in_group.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 9: No declaration for attribute href of element group```

🔴 [2.4.3.xlink_href_in_map_components](../models_1_0/valid/2.4.3.xlink_href_in_map_components.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 10: Element map_components was declared EMPTY this one has content```
  * ```Error on line 10: No declaration for attribute href of element map_components```

🔴 [2.4.3.xlink_href_in_map_variables](../models_1_0/valid/2.4.3.xlink_href_in_map_variables.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 17: No declaration for attribute href of element map_variables```

🔴 [2.4.3.xlink_href_in_model](../models_1_0/valid/2.4.3.xlink_href_in_model.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 7: No declaration for attribute href of element model```
  * ```Error on line 7: No declaration for attribute xmlns:xlink of element model```

🔴 [2.4.3.xlink_href_in_reaction](../models_1_0/valid/2.4.3.xlink_href_in_reaction.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 9: No declaration for attribute href of element reaction```

🔴 [2.4.3.xlink_href_in_relationship_ref](../models_1_0/valid/2.4.3.xlink_href_in_relationship_ref.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 11: No declaration for attribute href of element relationship_ref```

🔴 [2.4.3.xlink_href_in_role](../models_1_0/valid/2.4.3.xlink_href_in_role.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 11: No declaration for attribute href of element role```

🔴 [2.4.3.xlink_href_in_unit](../models_1_0/valid/2.4.3.xlink_href_in_unit.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 8: No declaration for attribute href of element unit```

🔴 [2.4.3.xlink_href_in_units_1](../models_1_0/valid/2.4.3.xlink_href_in_units_1.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 8: No declaration for attribute href of element unit```

🔴 [2.4.3.xlink_href_in_units_2](../models_1_0/valid/2.4.3.xlink_href_in_units_2.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 8: No declaration for attribute href of element units```

🔴 [2.4.3.xlink_href_in_variable](../models_1_0/valid/2.4.3.xlink_href_in_variable.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 8: No declaration for attribute href of element variable```

🔴 [2.4.3.xlink_href_in_variable_ref](../models_1_0/valid/2.4.3.xlink_href_in_variable_ref.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:xlink of element model```
  * ```Error on line 10: No declaration for attribute href of element variable_ref```


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

[2.5.2.attribute_in_cellml_namespace](../models_1_0/invalid/2.5.2.attribute_in_cellml_namespace.cellml): Error detected correctly.
* Expected: ```No declaration for attribute private_interface```
* Output: ```Error on line 8: No declaration for attribute private_interface of element variable```


---

## 3. Model structure

##### 3.4.1.1

[3.4.1.1.model_child_order_1](../models_1_0/valid/3.4.1.1.model_child_order_1.cellml): Valid file passed validation.

[3.4.1.1.model_child_order_2](../models_1_0/valid/3.4.1.1.model_child_order_2.cellml): Valid file passed validation.

[3.4.1.1.model_empty](../models_1_0/valid/3.4.1.1.model_empty.cellml): Valid file passed validation.

[3.4.1.1.model_name_missing](../models_1_0/invalid/3.4.1.1.model_name_missing.cellml): Error detected correctly.
* Expected: ```Element model does not carry attribute name```
* Output: ```Error on line 4: Element model does not carry attribute name```

[3.4.1.1.model_with_component_ref](../models_1_0/invalid/3.4.1.1.model_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element model content does not follow the DTD```
* Output: ```Error on line 5: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (component_ref )```

[3.4.1.1.model_with_components](../models_1_0/valid/3.4.1.1.model_with_components.cellml): Valid file passed validation.

[3.4.1.1.model_with_connections](../models_1_0/valid/3.4.1.1.model_with_connections.cellml): Valid file passed validation.

[3.4.1.1.model_with_groups](../models_1_0/valid/3.4.1.1.model_with_groups.cellml): Valid file passed validation.

[3.4.1.1.model_with_map_components](../models_1_0/invalid/3.4.1.1.model_with_map_components.cellml): Error detected correctly.
* Expected: ```Element model content does not follow the DTD```
* Output: ```Error on line 5: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (component component map_components )```

[3.4.1.1.model_with_map_variables](../models_1_0/invalid/3.4.1.1.model_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element model content does not follow the DTD```
* Output: ```Error on line 5: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (component component map_variables )```

[3.4.1.1.model_with_math](../models_1_0/invalid/3.4.1.1.model_with_math.cellml): Error detected correctly.
* Expected: ```Element model content does not follow the DTD```
* Output: ```Error on line 6: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (component math )```

[3.4.1.1.model_with_model](../models_1_0/invalid/3.4.1.1.model_with_model.cellml): Error detected correctly.
* Expected: ```Element model content does not follow the DTD```
* Output: ```Error on line 5: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (model )```

[3.4.1.1.model_with_one_component](../models_1_0/valid/3.4.1.1.model_with_one_component.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_connection](../models_1_0/valid/3.4.1.1.model_with_one_connection.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_group](../models_1_0/valid/3.4.1.1.model_with_one_group.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_units](../models_1_0/valid/3.4.1.1.model_with_one_units.cellml): Valid file passed validation.

[3.4.1.1.model_with_reaction](../models_1_0/invalid/3.4.1.1.model_with_reaction.cellml): Error detected correctly.
* Expected: ```Element model content does not follow the DTD```
* Output: ```Error on line 5: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (component reaction )```

[3.4.1.1.model_with_relationship_ref](../models_1_0/invalid/3.4.1.1.model_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element model content does not follow the DTD```
* Output: ```Error on line 5: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (relationship_ref )```

[3.4.1.1.model_with_role](../models_1_0/invalid/3.4.1.1.model_with_role.cellml): Error detected correctly.
* Expected: ```Element model content does not follow the DTD```
* Output: ```Error on line 5: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (role )```

[3.4.1.1.model_with_unit](../models_1_0/invalid/3.4.1.1.model_with_unit.cellml): Error detected correctly.
* Expected: ```Element model content does not follow the DTD```
* Output: ```Error on line 5: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (unit )```

[3.4.1.1.model_with_units](../models_1_0/valid/3.4.1.1.model_with_units.cellml): Valid file passed validation.

[3.4.1.1.model_with_variable](../models_1_0/invalid/3.4.1.1.model_with_variable.cellml): Error detected correctly.
* Expected: ```Element model content does not follow the DTD```
* Output: ```Error on line 5: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (variable )```

[3.4.1.1.model_with_variable_ref](../models_1_0/invalid/3.4.1.1.model_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element model content does not follow the DTD```
* Output: ```Error on line 5: Element model content does not follow the DTD, expecting (units | component | group | connection)*, got (variable_ref )```


---

##### 3.4.1.2

🔵 [3.4.1.2.model_name_invalid](../models_1_0/invalid/3.4.1.2.model_name_invalid.cellml): **Error not detected.**


---

##### 3.4.2.1

[3.4.2.1.component_child_order_1](../models_1_0/valid/3.4.2.1.component_child_order_1.cellml): Valid file passed validation.

[3.4.2.1.component_child_order_2](../models_1_0/valid/3.4.2.1.component_child_order_2.cellml): Valid file passed validation.

[3.4.2.1.component_empty](../models_1_0/valid/3.4.2.1.component_empty.cellml): Valid file passed validation.

[3.4.2.1.component_name_missing](../models_1_0/invalid/3.4.2.1.component_name_missing.cellml): Error detected correctly.
* Expected: ```Element component does not carry attribute name```
* Output: ```Error on line 6: Element component does not carry attribute name```

[3.4.2.1.component_with_component](../models_1_0/invalid/3.4.2.1.component_with_component.cellml): Error detected correctly.
* Expected: ```Element component content does not follow the DTD```
* Output: ```Error on line 6: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (component )```

[3.4.2.1.component_with_component_ref](../models_1_0/invalid/3.4.2.1.component_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element component content does not follow the DTD```
* Output: ```Error on line 6: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (component_ref )```

[3.4.2.1.component_with_connection](../models_1_0/invalid/3.4.2.1.component_with_connection.cellml): Error detected correctly.
* Expected: ```Element component content does not follow the DTD```
* Output: ```Error on line 12: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (connection )```

[3.4.2.1.component_with_group](../models_1_0/invalid/3.4.2.1.component_with_group.cellml): Error detected correctly.
* Expected: ```Element component content does not follow the DTD```
* Output: ```Error on line 6: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (group )```

[3.4.2.1.component_with_map_components](../models_1_0/invalid/3.4.2.1.component_with_map_components.cellml): Error detected correctly.
* Expected: ```Element component content does not follow the DTD```
* Output: ```Error on line 6: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (map_components )```

[3.4.2.1.component_with_map_variables](../models_1_0/invalid/3.4.2.1.component_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element component content does not follow the DTD```
* Output: ```Error on line 6: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (map_variables variable )```

[3.4.2.1.component_with_maths](../models_1_0/valid/3.4.2.1.component_with_maths.cellml): Valid file passed validation.

[3.4.2.1.component_with_model](../models_1_0/invalid/3.4.2.1.component_with_model.cellml): Error detected correctly.
* Expected: ```Element component content does not follow the DTD```
* Output: ```Error on line 6: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (model )```

[3.4.2.1.component_with_one_math](../models_1_0/valid/3.4.2.1.component_with_one_math.cellml): Valid file passed validation.

[3.4.2.1.component_with_one_reaction](../models_1_0/valid/3.4.2.1.component_with_one_reaction.cellml): Valid file passed validation.

[3.4.2.1.component_with_one_units](../models_1_0/valid/3.4.2.1.component_with_one_units.cellml): Valid file passed validation.

[3.4.2.1.component_with_one_variable](../models_1_0/valid/3.4.2.1.component_with_one_variable.cellml): Valid file passed validation.

[3.4.2.1.component_with_reactions](../models_1_0/valid/3.4.2.1.component_with_reactions.cellml): Valid file passed validation.

[3.4.2.1.component_with_relationship_ref](../models_1_0/invalid/3.4.2.1.component_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element component content does not follow the DTD```
* Output: ```Error on line 6: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (relationship_ref )```

[3.4.2.1.component_with_role](../models_1_0/invalid/3.4.2.1.component_with_role.cellml): Error detected correctly.
* Expected: ```Element component content does not follow the DTD```
* Output: ```Error on line 6: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (role )```

[3.4.2.1.component_with_unit](../models_1_0/invalid/3.4.2.1.component_with_unit.cellml): Error detected correctly.
* Expected: ```Element component content does not follow the DTD```
* Output: ```Error on line 6: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (unit )```

[3.4.2.1.component_with_units](../models_1_0/valid/3.4.2.1.component_with_units.cellml): Valid file passed validation.

[3.4.2.1.component_with_variable_ref](../models_1_0/invalid/3.4.2.1.component_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element component content does not follow the DTD```
* Output: ```Error on line 6: Element component content does not follow the DTD, expecting (units | variable | reaction | math)*, got (variable_ref )```

[3.4.2.1.component_with_variables](../models_1_0/valid/3.4.2.1.component_with_variables.cellml): Valid file passed validation.


---

##### 3.4.2.2

🔵 [3.4.2.2.component_name_duplicate](../models_1_0/invalid/3.4.2.2.component_name_duplicate.cellml): **Error not detected.**

🔵 [3.4.2.2.component_name_invalid](../models_1_0/invalid/3.4.2.2.component_name_invalid.cellml): **Error not detected.**


---

##### 3.4.3.1

[3.4.3.1.variable_name_missing](../models_1_0/invalid/3.4.3.1.variable_name_missing.cellml): Error detected correctly.
* Expected: ```Element variable does not carry attribute name```
* Output: ```Error on line 7: Element variable does not carry attribute name```

[3.4.3.1.variable_units_missing](../models_1_0/invalid/3.4.3.1.variable_units_missing.cellml): Error detected correctly.
* Expected: ```Element variable does not carry attribute units```
* Output: ```Error on line 7: Element variable does not carry attribute units```

[3.4.3.1.variable_with_component](../models_1_0/invalid/3.4.3.1.variable_with_component.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_component_ref](../models_1_0/invalid/3.4.3.1.variable_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_connection](../models_1_0/invalid/3.4.3.1.variable_with_connection.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 13: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_group](../models_1_0/invalid/3.4.3.1.variable_with_group.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_initial_value](../models_1_0/valid/3.4.3.1.variable_with_initial_value.cellml): Valid file passed validation.

[3.4.3.1.variable_with_interfaces](../models_1_0/valid/3.4.3.1.variable_with_interfaces.cellml): Valid file passed validation.

[3.4.3.1.variable_with_map_components](../models_1_0/invalid/3.4.3.1.variable_with_map_components.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_map_variables](../models_1_0/invalid/3.4.3.1.variable_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_math](../models_1_0/invalid/3.4.3.1.variable_with_math.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 8: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_model](../models_1_0/invalid/3.4.3.1.variable_with_model.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_reaction](../models_1_0/invalid/3.4.3.1.variable_with_reaction.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_relationship_ref](../models_1_0/invalid/3.4.3.1.variable_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_role](../models_1_0/invalid/3.4.3.1.variable_with_role.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_unit](../models_1_0/invalid/3.4.3.1.variable_with_unit.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_units](../models_1_0/invalid/3.4.3.1.variable_with_units.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_variable](../models_1_0/invalid/3.4.3.1.variable_with_variable.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_with_variable_ref](../models_1_0/invalid/3.4.3.1.variable_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element variable was declared EMPTY this one has content```
* Output: ```Error on line 7: Element variable was declared EMPTY this one has content```

[3.4.3.1.variable_without_initial_value](../models_1_0/valid/3.4.3.1.variable_without_initial_value.cellml): Valid file passed validation.


---

##### 3.4.3.2

🔵 [3.4.3.2.variable_name_duplicate](../models_1_0/invalid/3.4.3.2.variable_name_duplicate.cellml): **Error not detected.**

🔵 [3.4.3.2.variable_name_invalid](../models_1_0/invalid/3.4.3.2.variable_name_invalid.cellml): **Error not detected.**

[3.4.3.2.variable_name_same_as_cousin](../models_1_0/valid/3.4.3.2.variable_name_same_as_cousin.cellml): Valid file passed validation.

[3.4.3.2.variable_name_same_as_parent](../models_1_0/valid/3.4.3.2.variable_name_same_as_parent.cellml): Valid file passed validation.


---

##### 3.4.3.3

[3.4.3.3.variable_units_component](../models_1_0/valid/3.4.3.3.variable_units_component.cellml): Valid file passed validation.

[3.4.3.3.variable_units_model](../models_1_0/valid/3.4.3.3.variable_units_model.cellml): Valid file passed validation.

🔵 [3.4.3.3.variable_units_other_component](../models_1_0/invalid/3.4.3.3.variable_units_other_component.cellml): **Error not detected.**

[3.4.3.3.variable_units_predefined](../models_1_0/valid/3.4.3.3.variable_units_predefined.cellml): Valid file passed validation.

🔵 [3.4.3.3.variable_units_unknown](../models_1_0/invalid/3.4.3.3.variable_units_unknown.cellml): **Error not detected.**


---

##### 3.4.3.4

[3.4.3.4.variable_interface_public_invalid](../models_1_0/invalid/3.4.3.4.variable_interface_public_invalid.cellml): Error detected correctly.
* Expected: ```attribute public_interface of variable is not among the enumerated```
* Output: ```Error on line 7: Value "apple" for attribute public_interface of variable is not among the enumerated set```


---

##### 3.4.3.5

[3.4.3.5.variable_interface_private_invalid](../models_1_0/invalid/3.4.3.5.variable_interface_private_invalid.cellml): Error detected correctly.
* Expected: ```attribute private_interface of variable is not among the enumerated```
* Output: ```Error on line 7: Value "apple" for attribute private_interface of variable is not among the enumerated set```


---

##### 3.4.3.6

🔵 [3.4.3.6.variable_interfaces_both_in](../models_1_0/invalid/3.4.3.6.variable_interfaces_both_in.cellml): **Error not detected.**


---

##### 3.4.3.7

🔵 [3.4.3.7.variable_initial_value_empty](../models_1_0/invalid/3.4.3.7.variable_initial_value_empty.cellml): **Error not detected.**

🔵 [3.4.3.7.variable_initial_value_invalid](../models_1_0/invalid/3.4.3.7.variable_initial_value_invalid.cellml): **Error not detected.**


---

##### 3.4.3.8

🔵 [3.4.3.8.variable_interfaces_private_in_and_initial](../models_1_0/invalid/3.4.3.8.variable_interfaces_private_in_and_initial.cellml): **Error not detected.**

🔵 [3.4.3.8.variable_interfaces_public_in_and_initial](../models_1_0/invalid/3.4.3.8.variable_interfaces_public_in_and_initial.cellml): **Error not detected.**


---

##### 3.4.4.1

[3.4.4.1.connection_empty](../models_1_0/invalid/3.4.4.1.connection_empty.cellml): Error detected correctly.
* Expected: ```expecting (map_components , map_variables+)```
* Output: ```Error on line 6: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got ```

[3.4.4.1.connection_map_components_missing](../models_1_0/invalid/3.4.4.1.connection_map_components_missing.cellml): Error detected correctly.
* Expected: ```expecting (map_components , map_variables+)```
* Output: ```Error on line 14: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_variables map_variables )```

[3.4.4.1.connection_map_components_multiple](../models_1_0/invalid/3.4.4.1.connection_map_components_multiple.cellml): Error detected correctly.
* Expected: ```expecting (map_components , map_variables+)```
* Output: ```Error on line 17: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_components map_variables map_variables )```

[3.4.4.1.connection_map_variables_missing_1](../models_1_0/invalid/3.4.4.1.connection_map_variables_missing_1.cellml): Error detected correctly.
* Expected: ```got (map_components )```
* Output: ```Error on line 12: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components )```

[3.4.4.1.connection_map_variables_missing_2](../models_1_0/invalid/3.4.4.1.connection_map_variables_missing_2.cellml): Error detected correctly.
* Expected: ```got (map_components fruit```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components fruit:apple fruit:banana )```
  * ```Error on line 15: No declaration for element apple```
  * ```Error on line 16: No declaration for element banana```

[3.4.4.1.connection_only_extensions](../models_1_0/invalid/3.4.4.1.connection_only_extensions.cellml): Error detected correctly.
* Expected: ```got (fruit```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 7: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (fruit:apple fruit:banana fruit:cherry )```
  * ```Error on line 8: No declaration for element apple```
  * ```Error on line 9: No declaration for element banana```
  * ```Error on line 10: No declaration for element cherry```

[3.4.4.1.connection_with_component](../models_1_0/invalid/3.4.4.1.connection_with_component.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables component )```

[3.4.4.1.connection_with_component_ref](../models_1_0/invalid/3.4.4.1.connection_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables component_ref )```

[3.4.4.1.connection_with_connection](../models_1_0/invalid/3.4.4.1.connection_with_connection.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 16: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables connection )```

[3.4.4.1.connection_with_group](../models_1_0/invalid/3.4.4.1.connection_with_group.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables group )```

[3.4.4.1.connection_with_map_variables](../models_1_0/valid/3.4.4.1.connection_with_map_variables.cellml): Valid file passed validation.

[3.4.4.1.connection_with_math](../models_1_0/invalid/3.4.4.1.connection_with_math.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables math )```

[3.4.4.1.connection_with_model](../models_1_0/invalid/3.4.4.1.connection_with_model.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables model )```

[3.4.4.1.connection_with_name_attribute](../models_1_0/invalid/3.4.4.1.connection_with_name_attribute.cellml): Error detected correctly.
* Expected: ```No declaration for attribute name of element connection```
* Output: ```Error on line 12: No declaration for attribute name of element connection```

[3.4.4.1.connection_with_one_map_variables](../models_1_0/valid/3.4.4.1.connection_with_one_map_variables.cellml): Valid file passed validation.

[3.4.4.1.connection_with_reaction](../models_1_0/invalid/3.4.4.1.connection_with_reaction.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables reaction )```

[3.4.4.1.connection_with_relationship_ref](../models_1_0/invalid/3.4.4.1.connection_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables relationship_ref )```

[3.4.4.1.connection_with_role](../models_1_0/invalid/3.4.4.1.connection_with_role.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables role )```

[3.4.4.1.connection_with_unit](../models_1_0/invalid/3.4.4.1.connection_with_unit.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables unit )```

[3.4.4.1.connection_with_units](../models_1_0/invalid/3.4.4.1.connection_with_units.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables units )```

[3.4.4.1.connection_with_variable](../models_1_0/invalid/3.4.4.1.connection_with_variable.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables variable )```

[3.4.4.1.connection_with_variable_ref](../models_1_0/invalid/3.4.4.1.connection_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element connection content does not follow the DTD```
* Output: ```Error on line 13: Element connection content does not follow the DTD, expecting (map_components , map_variables+), got (map_components map_variables variable_ref )```


---

##### 3.4.5.1

[3.4.5.1.connection_any_order_1](../models_1_0/valid/3.4.5.1.connection_any_order_1.cellml): Valid file passed validation.

[3.4.5.1.connection_any_order_2](../models_1_0/valid/3.4.5.1.connection_any_order_2.cellml): Valid file passed validation.

[3.4.5.1.map_components_component_1_missing](../models_1_0/invalid/3.4.5.1.map_components_component_1_missing.cellml): Error detected correctly.
* Expected: ```Element map_components does not carry attribute component_1```
* Output: ```Error on line 7: Element map_components does not carry attribute component_1```

[3.4.5.1.map_components_component_2_missing](../models_1_0/invalid/3.4.5.1.map_components_component_2_missing.cellml): Error detected correctly.
* Expected: ```Element map_components does not carry attribute component_2```
* Output: ```Error on line 7: Element map_components does not carry attribute component_2```

[3.4.5.1.map_components_with_component](../models_1_0/invalid/3.4.5.1.map_components_with_component.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_component_ref](../models_1_0/invalid/3.4.5.1.map_components_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_connection](../models_1_0/invalid/3.4.5.1.map_components_with_connection.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_group](../models_1_0/invalid/3.4.5.1.map_components_with_group.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_map_components](../models_1_0/invalid/3.4.5.1.map_components_with_map_components.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_map_variables](../models_1_0/invalid/3.4.5.1.map_components_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_math](../models_1_0/invalid/3.4.5.1.map_components_with_math.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_model](../models_1_0/invalid/3.4.5.1.map_components_with_model.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_reaction](../models_1_0/invalid/3.4.5.1.map_components_with_reaction.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_relationship_ref](../models_1_0/invalid/3.4.5.1.map_components_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_role](../models_1_0/invalid/3.4.5.1.map_components_with_role.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_unit](../models_1_0/invalid/3.4.5.1.map_components_with_unit.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_units](../models_1_0/invalid/3.4.5.1.map_components_with_units.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_variable](../models_1_0/invalid/3.4.5.1.map_components_with_variable.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```

[3.4.5.1.map_components_with_variable_ref](../models_1_0/invalid/3.4.5.1.map_components_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element map_components was declared EMPTY this one has content```
* Output: ```Error on line 7: Element map_components was declared EMPTY this one has content```


---

##### 3.4.5.2

🔵 [3.4.5.2.map_components_component_1_nonexistent](../models_1_0/invalid/3.4.5.2.map_components_component_1_nonexistent.cellml): **Error not detected.**


---

##### 3.4.5.3

🔵 [3.4.5.3.map_components_component_2_nonexistent](../models_1_0/invalid/3.4.5.3.map_components_component_2_nonexistent.cellml): **Error not detected.**


---

##### 3.4.5.4

🔵 [3.4.5.4.map_components_component_1_equals_2](../models_1_0/invalid/3.4.5.4.map_components_component_1_equals_2.cellml): **Error not detected.**

🔵 [3.4.5.4.map_components_duplicate](../models_1_0/invalid/3.4.5.4.map_components_duplicate.cellml): **Error not detected.**

🔵 [3.4.5.4.map_components_duplicate_mirrored](../models_1_0/invalid/3.4.5.4.map_components_duplicate_mirrored.cellml): **Error not detected.**


---

##### 3.4.6.1

🔵 [3.4.6.1.map_variables_duplicate_1](../models_1_0/duplicate_connections/3.4.6.1.map_variables_duplicate_1.cellml): **Error not detected.**

🔵 [3.4.6.1.map_variables_duplicate_2](../models_1_0/duplicate_connections/3.4.6.1.map_variables_duplicate_2.cellml): **Error not detected.**

[3.4.6.1.map_variables_variable_1_missing](../models_1_0/invalid/3.4.6.1.map_variables_variable_1_missing.cellml): Error detected correctly.
* Expected: ```Element map_variables does not carry attribute variable_1```
* Output: ```Error on line 14: Element map_variables does not carry attribute variable_1```

[3.4.6.1.map_variables_variable_2_missing](../models_1_0/invalid/3.4.6.1.map_variables_variable_2_missing.cellml): Error detected correctly.
* Expected: ```Element map_variables does not carry attribute variable_2```
* Output: ```Error on line 14: Element map_variables does not carry attribute variable_2```

[3.4.6.1.map_variables_with_component](../models_1_0/invalid/3.4.6.1.map_variables_with_component.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_component_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_connection](../models_1_0/invalid/3.4.6.1.map_variables_with_connection.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_group](../models_1_0/invalid/3.4.6.1.map_variables_with_group.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_map_components](../models_1_0/invalid/3.4.6.1.map_variables_with_map_components.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_map_variables](../models_1_0/invalid/3.4.6.1.map_variables_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_math](../models_1_0/invalid/3.4.6.1.map_variables_with_math.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 9: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_model](../models_1_0/invalid/3.4.6.1.map_variables_with_model.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_reaction](../models_1_0/invalid/3.4.6.1.map_variables_with_reaction.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_relationship_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_role](../models_1_0/invalid/3.4.6.1.map_variables_with_role.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_unit](../models_1_0/invalid/3.4.6.1.map_variables_with_unit.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_units](../models_1_0/invalid/3.4.6.1.map_variables_with_units.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_variable](../models_1_0/invalid/3.4.6.1.map_variables_with_variable.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```

[3.4.6.1.map_variables_with_variable_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element map_variables was declared EMPTY this one has content```
* Output: ```Error on line 8: Element map_variables was declared EMPTY this one has content```


---

##### 3.4.6.2

🔵 [3.4.6.2.map_variables_variable_1_nonexistent](../models_1_0/invalid/3.4.6.2.map_variables_variable_1_nonexistent.cellml): **Error not detected.**


---

##### 3.4.6.3

🔵 [3.4.6.3.map_variables_variable_2_nonexistent](../models_1_0/invalid/3.4.6.3.map_variables_variable_2_nonexistent.cellml): **Error not detected.**


---

##### 3.4.6.4

[3.4.6.4.map_variables_chain_down](../models_1_0/valid/3.4.6.4.map_variables_chain_down.cellml): Valid file passed validation.

[3.4.6.4.map_variables_chain_up](../models_1_0/valid/3.4.6.4.map_variables_chain_up.cellml): Valid file passed validation.

🔵 [3.4.6.4.map_variables_child_multiple_out_1](../models_1_0/invalid/3.4.6.4.map_variables_child_multiple_out_1.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_child_multiple_out_2](../models_1_0/invalid/3.4.6.4.map_variables_child_multiple_out_2.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_child_out_to_out_1](../models_1_0/invalid/3.4.6.4.map_variables_child_out_to_out_1.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_child_out_to_out_2](../models_1_0/invalid/3.4.6.4.map_variables_child_out_to_out_2.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_child_private_in](../models_1_0/invalid/3.4.6.4.map_variables_child_private_in.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_child_private_out](../models_1_0/invalid/3.4.6.4.map_variables_child_private_out.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_hidden_aunt_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_aunt_1.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_hidden_aunt_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_aunt_2.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_hidden_cousins_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_1.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_hidden_cousins_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_2.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_hidden_cousins_3](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_3.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_hidden_cousins_4](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_4.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_hidden_grandchild_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandchild_1.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_hidden_grandchild_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandchild_2.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_hidden_grandparent_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandparent_1.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_hidden_grandparent_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandparent_2.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_hidden_niece_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_niece_1.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_hidden_niece_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_niece_2.cellml): **Error not detected.**

[3.4.6.4.map_variables_nested_sibling_connection](../models_1_0/valid/3.4.6.4.map_variables_nested_sibling_connection.cellml): Valid file passed validation.

🔵 [3.4.6.4.map_variables_nested_sibling_private_in](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_in.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_nested_sibling_private_in_and_out](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_in_and_out.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_nested_sibling_private_out](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_out.cellml): **Error not detected.**

[3.4.6.4.map_variables_parent_connection_1](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_connection_2](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_2.cellml): Valid file passed validation.

🔵 [3.4.6.4.map_variables_parent_in_to_in_1](../models_1_0/invalid/3.4.6.4.map_variables_parent_in_to_in_1.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_parent_in_to_in_2](../models_1_0/invalid/3.4.6.4.map_variables_parent_in_to_in_2.cellml): **Error not detected.**

[3.4.6.4.map_variables_parent_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_2.cellml): Valid file passed validation.

🔵 [3.4.6.4.map_variables_parent_multiple_out](../models_1_0/invalid/3.4.6.4.map_variables_parent_multiple_out.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_parent_out_to_out_1](../models_1_0/invalid/3.4.6.4.map_variables_parent_out_to_out_1.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_parent_out_to_out_2](../models_1_0/invalid/3.4.6.4.map_variables_parent_out_to_out_2.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_parent_public_in](../models_1_0/invalid/3.4.6.4.map_variables_parent_public_in.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_parent_public_out](../models_1_0/invalid/3.4.6.4.map_variables_parent_public_out.cellml): **Error not detected.**

[3.4.6.4.map_variables_sibling_connection_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_connection_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_connection_3](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_3.cellml): Valid file passed validation.

🔵 [3.4.6.4.map_variables_sibling_in_to_in](../models_1_0/invalid/3.4.6.4.map_variables_sibling_in_to_in.cellml): **Error not detected.**

[3.4.6.4.map_variables_sibling_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_2.cellml): Valid file passed validation.

🔵 [3.4.6.4.map_variables_sibling_multiple_out_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_multiple_out_1.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_sibling_multiple_out_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_multiple_out_2.cellml): **Error not detected.**

[3.4.6.4.map_variables_sibling_mutual](../models_1_0/valid/3.4.6.4.map_variables_sibling_mutual.cellml): Valid file passed validation.

🔵 [3.4.6.4.map_variables_sibling_out_to_out](../models_1_0/invalid/3.4.6.4.map_variables_sibling_out_to_out.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_sibling_private_in_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_1.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_sibling_private_in_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_2.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_sibling_private_in_and_out](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_and_out.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_sibling_private_out_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_out_1.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_sibling_private_out_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_out_2.cellml): **Error not detected.**

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

[4.2.3_6.8_mathml_logic_embedded](../models_1_0/valid/4.2.3_6.8_mathml_logic_embedded.cellml): Valid file passed validation.

[4.2.3_7.1_mathml_pi](../models_1_0/valid/4.2.3_7.1_mathml_pi.cellml): Valid file passed validation.

[4.2.3_7.2_mathml_e](../models_1_0/valid/4.2.3_7.2_mathml_e.cellml): Valid file passed validation.

[4.2.3_7.3_mathml_nan_inf](../models_1_0/valid/4.2.3_7.3_mathml_nan_inf.cellml): Valid file passed validation.

[4.2.3_8.1_annotation](../models_1_0/valid/4.2.3_8.1_annotation.cellml): Valid file passed validation.

[4.2.3_8.2_annotation_xml](../models_1_0/valid/4.2.3_8.2_annotation_xml.cellml): Valid file passed validation.


---

#### 4.4.1

[4.4.1.math_not_math_component](../models_1_0/invalid/4.4.1.math_not_math_component.cellml): Error detected correctly.
* Expected: ```Element apply content does not follow the DTD```
* Output:
  * ```Error on line 10: Element apply content does not follow the DTD, expecting (csymbol | ci | cn | apply | reln | lambda | condition | declare | sep | semantics | annotation | annotation-xml | integers | reals | rationals | naturalnumbers | complexes | primes | exponentiale | imaginaryi | notanumber | true | false | emptyset | pi | eulergamma | infinity | interval | list | matrix | matrixrow | set | vector | piecewise | lowlimit | uplimit | bvar | degree | logbase | momentabout | domainofapplication | inverse | ident | domain | codomain | image | abs | conjugate | exp | factorial | arg | real | imaginary | floor | ceiling | not | ln | sin | cos | tan | sec | csc | cot | sinh | cosh | tanh | sech | csch | coth | arcsin | arccos | arctan | arccosh | arccot | arccoth | arccsc | arccsch | arcsec | arcsech | arcsinh | arctanh | determinant | transpose | card | quotient | divide | power | rem | implies | vectorproduct | scalarproduct | outerproduct | setdiff | fn | compose | plus | times | max | min | gcd | lcm | and | or | xor | union | intersect | cartesianproduct | mean | sdev | variance | median | mode | selector | root | minus | log | int | diff | partialdiff | divergence | grad | curl | laplacian | sum | product | limit | moment | exists | forall | neq | factorof | in | notin | notsubset | notprsubset | tendsto | eq | leq | lt | geq | gt | equivalent | approx | subset | prsubset | mi | mn | mo | mtext | ms | mspace | mrow | mfrac | msqrt | mroot | menclose | mstyle | merror | mpadded | mphantom | mfenced | msub | msup | msubsup | munder | mover | munderover | mmultiscripts | mtable | mtr | mlabeledtr | mtd | maligngroup | malignmark | maction)*, got (eq ci cake )```
  * ```Error on line 13: No declaration for element cake```
  * ```Error on line 14: No declaration for element fruit```
  * ```Error on line 15: No declaration for element cream```
  * ```Error on line 15: No declaration for attribute type of element cream```

[4.4.1.math_not_math_reaction](../models_1_0/invalid/4.4.1.math_not_math_reaction.cellml): Error detected correctly.
* Expected: ```Element apply content does not follow the DTD```
* Output:
  * ```Error on line 13: Element apply content does not follow the DTD, expecting (csymbol | ci | cn | apply | reln | lambda | condition | declare | sep | semantics | annotation | annotation-xml | integers | reals | rationals | naturalnumbers | complexes | primes | exponentiale | imaginaryi | notanumber | true | false | emptyset | pi | eulergamma | infinity | interval | list | matrix | matrixrow | set | vector | piecewise | lowlimit | uplimit | bvar | degree | logbase | momentabout | domainofapplication | inverse | ident | domain | codomain | image | abs | conjugate | exp | factorial | arg | real | imaginary | floor | ceiling | not | ln | sin | cos | tan | sec | csc | cot | sinh | cosh | tanh | sech | csch | coth | arcsin | arccos | arctan | arccosh | arccot | arccoth | arccsc | arccsch | arcsec | arcsech | arcsinh | arctanh | determinant | transpose | card | quotient | divide | power | rem | implies | vectorproduct | scalarproduct | outerproduct | setdiff | fn | compose | plus | times | max | min | gcd | lcm | and | or | xor | union | intersect | cartesianproduct | mean | sdev | variance | median | mode | selector | root | minus | log | int | diff | partialdiff | divergence | grad | curl | laplacian | sum | product | limit | moment | exists | forall | neq | factorof | in | notin | notsubset | notprsubset | tendsto | eq | leq | lt | geq | gt | equivalent | approx | subset | prsubset | mi | mn | mo | mtext | ms | mspace | mrow | mfrac | msqrt | mroot | menclose | mstyle | merror | mpadded | mphantom | mfenced | msub | msup | msubsup | munder | mover | munderover | mmultiscripts | mtable | mtr | mlabeledtr | mtd | maligngroup | malignmark | maction)*, got (eq ci cake )```
  * ```Error on line 16: No declaration for element cake```
  * ```Error on line 17: No declaration for element fruit```
  * ```Error on line 18: No declaration for element cream```
  * ```Error on line 18: No declaration for attribute type of element cream```


---

#### 4.4.2

[4.4.2.ci_no_whitespace](../models_1_0/valid/4.4.2.ci_no_whitespace.cellml): Valid file passed validation.

🔵 [4.4.2.ci_non_local_aunt](../models_1_0/invalid/4.4.2.ci_non_local_aunt.cellml): **Error not detected.**

🔵 [4.4.2.ci_non_local_child](../models_1_0/invalid/4.4.2.ci_non_local_child.cellml): **Error not detected.**

🔵 [4.4.2.ci_non_local_cousin](../models_1_0/invalid/4.4.2.ci_non_local_cousin.cellml): **Error not detected.**

🔵 [4.4.2.ci_non_local_nested_sibling](../models_1_0/invalid/4.4.2.ci_non_local_nested_sibling.cellml): **Error not detected.**

🔵 [4.4.2.ci_non_local_niece](../models_1_0/invalid/4.4.2.ci_non_local_niece.cellml): **Error not detected.**

🔵 [4.4.2.ci_non_local_parent](../models_1_0/invalid/4.4.2.ci_non_local_parent.cellml): **Error not detected.**

🔵 [4.4.2.ci_non_local_sibling](../models_1_0/invalid/4.4.2.ci_non_local_sibling.cellml): **Error not detected.**

🔵 [4.4.2.ci_nonexistent](../models_1_0/invalid/4.4.2.ci_nonexistent.cellml): **Error not detected.**

[4.4.2.ci_whitespace_1](../models_1_0/valid/4.4.2.ci_whitespace_1.cellml): Valid file passed validation.

[4.4.2.ci_whitespace_2](../models_1_0/valid/4.4.2.ci_whitespace_2.cellml): Valid file passed validation.

[4.4.2.ci_whitespace_3](../models_1_0/valid/4.4.2.ci_whitespace_3.cellml): Valid file passed validation.


---

##### 4.4.3.1

[4.4.3.1.cn_component_units](../models_1_0/valid/4.4.3.1.cn_component_units.cellml): Valid file passed validation.

[4.4.3.1.cn_model_units](../models_1_0/valid/4.4.3.1.cn_model_units.cellml): Valid file passed validation.

[4.4.3.1.cn_predefined_units](../models_1_0/valid/4.4.3.1.cn_predefined_units.cellml): Valid file passed validation.

[4.4.3.1.cn_units_missing](../models_1_0/invalid/4.4.3.1.cn_units_missing.cellml): Error detected correctly.
* Expected: ```Element cn does not carry attribute cellml:units```
* Output: ```Error on line 13: Element cn does not carry attribute cellml:units```


---

##### 4.4.3.2

🔵 [4.4.3.2.cn_units_nonexistent_1](../models_1_0/invalid/4.4.3.2.cn_units_nonexistent_1.cellml): **Error not detected.**

🔵 [4.4.3.2.cn_units_nonexistent_2](../models_1_0/invalid/4.4.3.2.cn_units_nonexistent_2.cellml): **Error not detected.**

🔵 [4.4.3.2.cn_units_parent_component](../models_1_0/invalid/4.4.3.2.cn_units_parent_component.cellml): **Error not detected.**


---

#### 4.4.4

🔵 [4.4.4.dae_public_in](../models_1_0/invalid/4.4.4.dae_public_in.cellml): **Error not detected.**

🔵 [4.4.4.modify_nonexistent](../models_1_0/invalid/4.4.4.modify_nonexistent.cellml): **Error not detected.**

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

[4.overdefined_direct_and_direct](../models_1_0/overdefined/4.overdefined_direct_and_direct.cellml): Valid file passed validation.

[4.overdefined_direct_and_initial](../models_1_0/overdefined/4.overdefined_direct_and_initial.cellml): Valid file passed validation.

[4.overdefined_direct_and_ode](../models_1_0/overdefined/4.overdefined_direct_and_ode.cellml): Valid file passed validation.

[4.overdefined_ode_and_ode](../models_1_0/overdefined/4.overdefined_ode_and_ode.cellml): Valid file passed validation.


---

## 5. Units

#### 5.2.1

[5.2.1.units_ampere](../models_1_0/valid/5.2.1.units_ampere.cellml): Valid file passed validation.

[5.2.1.units_becquerel](../models_1_0/valid/5.2.1.units_becquerel.cellml): Valid file passed validation.

[5.2.1.units_candela](../models_1_0/valid/5.2.1.units_candela.cellml): Valid file passed validation.

[5.2.1.units_celsius](../models_1_0/valid/5.2.1.units_celsius.cellml): Valid file passed validation.

[5.2.1.units_coulomb](../models_1_0/valid/5.2.1.units_coulomb.cellml): Valid file passed validation.

[5.2.1.units_dimensionless](../models_1_0/valid/5.2.1.units_dimensionless.cellml): Valid file passed validation.

[5.2.1.units_farad](../models_1_0/valid/5.2.1.units_farad.cellml): Valid file passed validation.

[5.2.1.units_gram](../models_1_0/valid/5.2.1.units_gram.cellml): Valid file passed validation.

[5.2.1.units_gray](../models_1_0/valid/5.2.1.units_gray.cellml): Valid file passed validation.

[5.2.1.units_henry](../models_1_0/valid/5.2.1.units_henry.cellml): Valid file passed validation.

[5.2.1.units_hertz](../models_1_0/valid/5.2.1.units_hertz.cellml): Valid file passed validation.

[5.2.1.units_joule](../models_1_0/valid/5.2.1.units_joule.cellml): Valid file passed validation.

[5.2.1.units_katal](../models_1_0/valid/5.2.1.units_katal.cellml): Valid file passed validation.

[5.2.1.units_kelvin](../models_1_0/valid/5.2.1.units_kelvin.cellml): Valid file passed validation.

[5.2.1.units_kilogram](../models_1_0/valid/5.2.1.units_kilogram.cellml): Valid file passed validation.

[5.2.1.units_liter](../models_1_0/valid/5.2.1.units_liter.cellml): Valid file passed validation.

[5.2.1.units_litre](../models_1_0/valid/5.2.1.units_litre.cellml): Valid file passed validation.

[5.2.1.units_lumen](../models_1_0/valid/5.2.1.units_lumen.cellml): Valid file passed validation.

[5.2.1.units_lux](../models_1_0/valid/5.2.1.units_lux.cellml): Valid file passed validation.

[5.2.1.units_meter](../models_1_0/valid/5.2.1.units_meter.cellml): Valid file passed validation.

[5.2.1.units_metre](../models_1_0/valid/5.2.1.units_metre.cellml): Valid file passed validation.

[5.2.1.units_mole](../models_1_0/valid/5.2.1.units_mole.cellml): Valid file passed validation.

[5.2.1.units_newton](../models_1_0/valid/5.2.1.units_newton.cellml): Valid file passed validation.

[5.2.1.units_ohm](../models_1_0/valid/5.2.1.units_ohm.cellml): Valid file passed validation.

[5.2.1.units_pascal](../models_1_0/valid/5.2.1.units_pascal.cellml): Valid file passed validation.

[5.2.1.units_radian](../models_1_0/valid/5.2.1.units_radian.cellml): Valid file passed validation.

[5.2.1.units_second](../models_1_0/valid/5.2.1.units_second.cellml): Valid file passed validation.

[5.2.1.units_siemens](../models_1_0/valid/5.2.1.units_siemens.cellml): Valid file passed validation.

[5.2.1.units_sievert](../models_1_0/valid/5.2.1.units_sievert.cellml): Valid file passed validation.

[5.2.1.units_steradian](../models_1_0/valid/5.2.1.units_steradian.cellml): Valid file passed validation.

[5.2.1.units_tesla](../models_1_0/valid/5.2.1.units_tesla.cellml): Valid file passed validation.

[5.2.1.units_volt](../models_1_0/valid/5.2.1.units_volt.cellml): Valid file passed validation.

[5.2.1.units_watt](../models_1_0/valid/5.2.1.units_watt.cellml): Valid file passed validation.

[5.2.1.units_weber](../models_1_0/valid/5.2.1.units_weber.cellml): Valid file passed validation.


---

#### 5.2.2

🔵 [5.2.2.unit_deca](../models_1_0/unit_deca/5.2.2.unit_deca.cellml): **Error not detected.**


---

#### 5.2.7

[5.2.7.unit_checking_aliases](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_aliases.cellml): Valid file passed validation.

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

[5.2.7.unit_checking_piecewise_1](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_piecewise_1.cellml): Valid file passed validation.

[5.2.7.unit_checking_piecewise_2](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_piecewise_2.cellml): Valid file passed validation.

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

🔵 [5.4.1.1.units_base_units_with_children](../models_1_0/invalid/5.4.1.1.units_base_units_with_children.cellml): **Error not detected.**

🔵 [5.4.1.1.units_empty_1](../models_1_0/units_empty/5.4.1.1.units_empty_1.cellml): **Error not detected.**

🔵 [5.4.1.1.units_empty_2](../models_1_0/units_empty/5.4.1.1.units_empty_2.cellml): **Error not detected.**

[5.4.1.1.units_name_missing](../models_1_0/invalid/5.4.1.1.units_name_missing.cellml): Error detected correctly.
* Expected: ```Element units does not carry attribute name```
* Output: ```Error on line 6: Element units does not carry attribute name```

[5.4.1.1.units_with_component](../models_1_0/invalid/5.4.1.1.units_with_component.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 6: Element units content does not follow the DTD, expecting (unit)*, got (unit component )```

[5.4.1.1.units_with_component_ref](../models_1_0/invalid/5.4.1.1.units_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 6: Element units content does not follow the DTD, expecting (unit)*, got (unit component_ref )```

[5.4.1.1.units_with_connection](../models_1_0/invalid/5.4.1.1.units_with_connection.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 12: Element units content does not follow the DTD, expecting (unit)*, got (unit connection )```

[5.4.1.1.units_with_group](../models_1_0/invalid/5.4.1.1.units_with_group.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 6: Element units content does not follow the DTD, expecting (unit)*, got (unit group )```

[5.4.1.1.units_with_map_components](../models_1_0/invalid/5.4.1.1.units_with_map_components.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 6: Element units content does not follow the DTD, expecting (unit)*, got (unit map_components )```

[5.4.1.1.units_with_map_variables](../models_1_0/invalid/5.4.1.1.units_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 6: Element units content does not follow the DTD, expecting (unit)*, got (unit map_variables )```

[5.4.1.1.units_with_math](../models_1_0/invalid/5.4.1.1.units_with_math.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 9: Element units content does not follow the DTD, expecting (unit)*, got (unit math )```

[5.4.1.1.units_with_model](../models_1_0/invalid/5.4.1.1.units_with_model.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 6: Element units content does not follow the DTD, expecting (unit)*, got (unit model )```

[5.4.1.1.units_with_reaction](../models_1_0/invalid/5.4.1.1.units_with_reaction.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 7: Element units content does not follow the DTD, expecting (unit)*, got (unit reaction )```

[5.4.1.1.units_with_relationship_ref](../models_1_0/invalid/5.4.1.1.units_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 6: Element units content does not follow the DTD, expecting (unit)*, got (unit relationship_ref )```

[5.4.1.1.units_with_role](../models_1_0/invalid/5.4.1.1.units_with_role.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 6: Element units content does not follow the DTD, expecting (unit)*, got (unit role )```

[5.4.1.1.units_with_unit_children](../models_1_0/valid/5.4.1.1.units_with_unit_children.cellml): Valid file passed validation.

[5.4.1.1.units_with_units](../models_1_0/invalid/5.4.1.1.units_with_units.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 6: Element units content does not follow the DTD, expecting (unit)*, got (unit units )```

[5.4.1.1.units_with_variable](../models_1_0/invalid/5.4.1.1.units_with_variable.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 7: Element units content does not follow the DTD, expecting (unit)*, got (unit variable )```

[5.4.1.1.units_with_variable_ref](../models_1_0/invalid/5.4.1.1.units_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element units content does not follow the DTD```
* Output: ```Error on line 8: Element units content does not follow the DTD, expecting (unit)*, got (unit variable_ref )```


---

##### 5.4.1.2

🔵 [5.4.1.2.units_name_duplicate_1](../models_1_0/invalid/5.4.1.2.units_name_duplicate_1.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_duplicate_2](../models_1_0/invalid/5.4.1.2.units_name_duplicate_2.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_invalid](../models_1_0/invalid/5.4.1.2.units_name_invalid.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_ampere](../models_1_0/invalid/5.4.1.2.units_name_predefined_ampere.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_becquerel](../models_1_0/invalid/5.4.1.2.units_name_predefined_becquerel.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_candela](../models_1_0/invalid/5.4.1.2.units_name_predefined_candela.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_celsius](../models_1_0/invalid/5.4.1.2.units_name_predefined_celsius.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_component_ampere](../models_1_0/invalid/5.4.1.2.units_name_predefined_component_ampere.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_coulomb](../models_1_0/invalid/5.4.1.2.units_name_predefined_coulomb.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_dimensionless](../models_1_0/invalid/5.4.1.2.units_name_predefined_dimensionless.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_farad](../models_1_0/invalid/5.4.1.2.units_name_predefined_farad.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_gram](../models_1_0/invalid/5.4.1.2.units_name_predefined_gram.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_gray](../models_1_0/invalid/5.4.1.2.units_name_predefined_gray.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_henry](../models_1_0/invalid/5.4.1.2.units_name_predefined_henry.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_hertz](../models_1_0/invalid/5.4.1.2.units_name_predefined_hertz.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_joule](../models_1_0/invalid/5.4.1.2.units_name_predefined_joule.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_katal](../models_1_0/invalid/5.4.1.2.units_name_predefined_katal.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_kelvin](../models_1_0/invalid/5.4.1.2.units_name_predefined_kelvin.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_kilogram](../models_1_0/invalid/5.4.1.2.units_name_predefined_kilogram.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_liter](../models_1_0/invalid/5.4.1.2.units_name_predefined_liter.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_litre](../models_1_0/invalid/5.4.1.2.units_name_predefined_litre.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_lumen](../models_1_0/invalid/5.4.1.2.units_name_predefined_lumen.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_lux](../models_1_0/invalid/5.4.1.2.units_name_predefined_lux.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_meter](../models_1_0/invalid/5.4.1.2.units_name_predefined_meter.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_metre](../models_1_0/invalid/5.4.1.2.units_name_predefined_metre.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_mole](../models_1_0/invalid/5.4.1.2.units_name_predefined_mole.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_newton](../models_1_0/invalid/5.4.1.2.units_name_predefined_newton.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_ohm](../models_1_0/invalid/5.4.1.2.units_name_predefined_ohm.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_pascal](../models_1_0/invalid/5.4.1.2.units_name_predefined_pascal.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_radian](../models_1_0/invalid/5.4.1.2.units_name_predefined_radian.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_second](../models_1_0/invalid/5.4.1.2.units_name_predefined_second.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_siemens](../models_1_0/invalid/5.4.1.2.units_name_predefined_siemens.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_sievert](../models_1_0/invalid/5.4.1.2.units_name_predefined_sievert.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_steradian](../models_1_0/invalid/5.4.1.2.units_name_predefined_steradian.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_tesla](../models_1_0/invalid/5.4.1.2.units_name_predefined_tesla.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_volt](../models_1_0/invalid/5.4.1.2.units_name_predefined_volt.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_watt](../models_1_0/invalid/5.4.1.2.units_name_predefined_watt.cellml): **Error not detected.**

🔵 [5.4.1.2.units_name_predefined_weber](../models_1_0/invalid/5.4.1.2.units_name_predefined_weber.cellml): **Error not detected.**

[5.4.1.2.units_names_and_other_names](../models_1_0/valid/5.4.1.2.units_names_and_other_names.cellml): Valid file passed validation.

[5.4.1.2.units_shadowing_1](../models_1_0/valid/5.4.1.2.units_shadowing_1.cellml): Valid file passed validation.

[5.4.1.2.units_shadowing_2](../models_1_0/valid/5.4.1.2.units_shadowing_2.cellml): Valid file passed validation.


---

##### 5.4.1.3

[5.4.1.3.units_base_units_invalid](../models_1_0/invalid/5.4.1.3.units_base_units_invalid.cellml): Error detected correctly.
* Expected: ```for attribute base_units of units is not among the enumerated set```
* Output: ```Error on line 6: Value "certainly" for attribute base_units of units is not among the enumerated set```


---

##### 5.4.2.1

[5.4.2.1.unit_offset_non_zero](../models_1_0/valid/5.4.2.1.unit_offset_non_zero.cellml): Valid file passed validation.

[5.4.2.1.unit_offset_zero](../models_1_0/valid/5.4.2.1.unit_offset_zero.cellml): Valid file passed validation.

[5.4.2.1.unit_prefix_exponent_multiplier](../models_1_0/valid/5.4.2.1.unit_prefix_exponent_multiplier.cellml): Valid file passed validation.

[5.4.2.1.unit_prefix_exponent_multiplier_huge](../models_1_0/valid/5.4.2.1.unit_prefix_exponent_multiplier_huge.cellml): Valid file passed validation.

[5.4.2.1.unit_units_missing](../models_1_0/invalid/5.4.2.1.unit_units_missing.cellml): Error detected correctly.
* Expected: ```Element unit does not carry attribute units```
* Output: ```Error on line 7: Element unit does not carry attribute units```

[5.4.2.1.unit_with_component](../models_1_0/invalid/5.4.2.1.unit_with_component.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 7: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_component_ref](../models_1_0/invalid/5.4.2.1.unit_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 7: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_connection](../models_1_0/invalid/5.4.2.1.unit_with_connection.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 7: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_group](../models_1_0/invalid/5.4.2.1.unit_with_group.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 7: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_map_components](../models_1_0/invalid/5.4.2.1.unit_with_map_components.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 7: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_map_variables](../models_1_0/invalid/5.4.2.1.unit_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 7: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_math](../models_1_0/invalid/5.4.2.1.unit_with_math.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 8: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_model](../models_1_0/invalid/5.4.2.1.unit_with_model.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 7: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_reaction](../models_1_0/invalid/5.4.2.1.unit_with_reaction.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 9: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_relationship_ref](../models_1_0/invalid/5.4.2.1.unit_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 7: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_role](../models_1_0/invalid/5.4.2.1.unit_with_role.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 7: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_unit](../models_1_0/invalid/5.4.2.1.unit_with_unit.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 7: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_units](../models_1_0/invalid/5.4.2.1.unit_with_units.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 7: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_variable](../models_1_0/invalid/5.4.2.1.unit_with_variable.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 8: Element unit was declared EMPTY this one has content```

[5.4.2.1.unit_with_variable_ref](../models_1_0/invalid/5.4.2.1.unit_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element unit was declared EMPTY this one has content```
* Output: ```Error on line 9: Element unit was declared EMPTY this one has content```


---

##### 5.4.2.2

🔵 [5.4.2.2.unit_cycle_1](../models_1_0/invalid/5.4.2.2.unit_cycle_1.cellml): **Error not detected.**

🔵 [5.4.2.2.unit_cycle_2](../models_1_0/invalid/5.4.2.2.unit_cycle_2.cellml): **Error not detected.**

🔵 [5.4.2.2.unit_cycle_3](../models_1_0/invalid/5.4.2.2.unit_cycle_3.cellml): **Error not detected.**

🔵 [5.4.2.2.unit_units_invalid](../models_1_0/invalid/5.4.2.2.unit_units_invalid.cellml): **Error not detected.**

[5.4.2.2.unit_units_local_1](../models_1_0/valid/5.4.2.2.unit_units_local_1.cellml): Valid file passed validation.

[5.4.2.2.unit_units_local_2](../models_1_0/valid/5.4.2.2.unit_units_local_2.cellml): Valid file passed validation.

[5.4.2.2.unit_units_local_3](../models_1_0/valid/5.4.2.2.unit_units_local_3.cellml): Valid file passed validation.

[5.4.2.2.unit_units_local_4](../models_1_0/valid/5.4.2.2.unit_units_local_4.cellml): Valid file passed validation.


---

##### 5.4.2.3

🔵 [5.4.2.3.unit_prefix_e_notation_int](../models_1_0/invalid/5.4.2.3.unit_prefix_e_notation_int.cellml): **Error not detected.**

[5.4.2.3.unit_prefix_integer](../models_1_0/valid/5.4.2.3.unit_prefix_integer.cellml): Valid file passed validation.

[5.4.2.3.unit_prefix_named](../models_1_0/valid/5.4.2.3.unit_prefix_named.cellml): Valid file passed validation.

🔵 [5.4.2.3.unit_prefix_real](../models_1_0/invalid/5.4.2.3.unit_prefix_real.cellml): **Error not detected.**

🔵 [5.4.2.3.unit_prefix_real_int](../models_1_0/invalid/5.4.2.3.unit_prefix_real_int.cellml): **Error not detected.**

🔵 [5.4.2.3.unit_prefix_spaces](../models_1_0/invalid/5.4.2.3.unit_prefix_spaces.cellml): **Error not detected.**

🔵 [5.4.2.3.unit_prefix_unknown](../models_1_0/invalid/5.4.2.3.unit_prefix_unknown.cellml): **Error not detected.**


---

##### 5.4.2.4

🔵 [5.4.2.4.unit_exponent_invalid](../models_1_0/invalid/5.4.2.4.unit_exponent_invalid.cellml): **Error not detected.**


---

##### 5.4.2.5

🔵 [5.4.2.5.unit_multiplier_invalid](../models_1_0/invalid/5.4.2.5.unit_multiplier_invalid.cellml): **Error not detected.**


---

##### 5.4.2.6

🔵 [5.4.2.6.unit_offset_invalid](../models_1_0/invalid/5.4.2.6.unit_offset_invalid.cellml): **Error not detected.**


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


---

## 6. Grouping

##### 6.4.1.1

🔵 [6.4.1.1.group_component_ref_missing_1](../models_1_0/invalid/6.4.1.1.group_component_ref_missing_1.cellml): **Error not detected.**
* Expected: ```Element group content does not follow the DTD```

[6.4.1.1.group_component_ref_missing_2](../models_1_0/invalid/6.4.1.1.group_component_ref_missing_2.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 9: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref fruit:apple )```
  * ```Error on line 11: No declaration for element apple```

[6.4.1.1.group_component_ref_multiple](../models_1_0/valid/6.4.1.1.group_component_ref_multiple.cellml): Valid file passed validation.

[6.4.1.1.group_component_ref_single](../models_1_0/valid/6.4.1.1.group_component_ref_single.cellml): Valid file passed validation.

[6.4.1.1.group_empty](../models_1_0/invalid/6.4.1.1.group_empty.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 6: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got ```

[6.4.1.1.group_only_extensions](../models_1_0/invalid/6.4.1.1.group_only_extensions.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:hi of element model```
  * ```Error on line 7: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (hi:hello hi:bonjour hi:hola hi:hallo )```
  * ```Error on line 8: No declaration for element hello```
  * ```Error on line 9: No declaration for element howareyou```
  * ```Error on line 11: No declaration for element bonjour```
  * ```Error on line 11: No declaration for attribute name of element bonjour```
  * ```Error on line 12: No declaration for element hola```
  * ```Error on line 13: No declaration for element hallo```

🔵 [6.4.1.1.group_relationship_ref_missing_1](../models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_1.cellml): **Error not detected.**
* Expected: ```Element group failed to validate content```

[6.4.1.1.group_relationship_ref_missing_2](../models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_2.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output:
  * ```Error on line 6: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 9: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (component_ref fruit:apple )```
  * ```Error on line 13: No declaration for element apple```

[6.4.1.1.group_with_component](../models_1_0/invalid/6.4.1.1.group_with_component.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 8: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref component )```

[6.4.1.1.group_with_connection](../models_1_0/invalid/6.4.1.1.group_with_connection.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 12: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref connection )```

[6.4.1.1.group_with_group](../models_1_0/invalid/6.4.1.1.group_with_group.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 10: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref group )```

[6.4.1.1.group_with_map_components](../models_1_0/invalid/6.4.1.1.group_with_map_components.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 8: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref map_components )```

[6.4.1.1.group_with_map_variables](../models_1_0/invalid/6.4.1.1.group_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 12: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref map_variables )```

[6.4.1.1.group_with_math](../models_1_0/invalid/6.4.1.1.group_with_math.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 11: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref math )```

[6.4.1.1.group_with_model](../models_1_0/invalid/6.4.1.1.group_with_model.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 8: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref model )```

[6.4.1.1.group_with_reaction](../models_1_0/invalid/6.4.1.1.group_with_reaction.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 10: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref reaction )```

[6.4.1.1.group_with_role](../models_1_0/invalid/6.4.1.1.group_with_role.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 8: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref role )```

[6.4.1.1.group_with_unit](../models_1_0/invalid/6.4.1.1.group_with_unit.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 8: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref unit component_ref )```

[6.4.1.1.group_with_units](../models_1_0/invalid/6.4.1.1.group_with_units.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 8: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref units )```

[6.4.1.1.group_with_variable](../models_1_0/invalid/6.4.1.1.group_with_variable.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 8: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref variable )```

[6.4.1.1.group_with_variable_ref](../models_1_0/invalid/6.4.1.1.group_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element group content does not follow the DTD```
* Output: ```Error on line 10: Element group content does not follow the DTD, expecting (relationship_ref | component_ref)+, got (relationship_ref component_ref variable_ref )```


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

[6.4.2.1.relationship_ref_relationship_missing](../models_1_0/invalid/6.4.2.1.relationship_ref_relationship_missing.cellml): Error detected correctly.
* Expected: ```relationship_ref does not carry attribute relationship```
* Output: ```Error on line 10: Element relationship_ref does not carry attribute relationship```

[6.4.2.1.relationship_ref_with_component](../models_1_0/invalid/6.4.2.1.relationship_ref_with_component.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 9: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_component_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 12: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_connection](../models_1_0/invalid/6.4.2.1.relationship_ref_with_connection.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 13: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_group](../models_1_0/invalid/6.4.2.1.relationship_ref_with_group.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 11: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_map_components](../models_1_0/invalid/6.4.2.1.relationship_ref_with_map_components.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 9: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_map_variables](../models_1_0/invalid/6.4.2.1.relationship_ref_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 13: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_math](../models_1_0/invalid/6.4.2.1.relationship_ref_with_math.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 12: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_model](../models_1_0/invalid/6.4.2.1.relationship_ref_with_model.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 9: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_reaction](../models_1_0/invalid/6.4.2.1.relationship_ref_with_reaction.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 11: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_relationship_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 9: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_role](../models_1_0/invalid/6.4.2.1.relationship_ref_with_role.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 9: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_unit](../models_1_0/invalid/6.4.2.1.relationship_ref_with_unit.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 9: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_units](../models_1_0/invalid/6.4.2.1.relationship_ref_with_units.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 9: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_variable](../models_1_0/invalid/6.4.2.1.relationship_ref_with_variable.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 9: Element relationship_ref was declared EMPTY this one has content```

[6.4.2.1.relationship_ref_with_variable_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element relationship_ref was declared EMPTY this one has content```
* Output: ```Error on line 11: Element relationship_ref was declared EMPTY this one has content```


---

##### 6.4.2.2

🔵 [6.4.2.2.relationship_ref_relationship_invalid](../models_1_0/invalid/6.4.2.2.relationship_ref_relationship_invalid.cellml): **Error not detected.**


---

##### 6.4.2.3

🔵 [6.4.2.3.relationship_ref_name_invalid](../models_1_0/invalid/6.4.2.3.relationship_ref_name_invalid.cellml): **Error not detected.**

[6.4.2.3.relationship_ref_name_not_unique_model_wide](../models_1_0/valid/6.4.2.3.relationship_ref_name_not_unique_model_wide.cellml): Valid file passed validation.


---

##### 6.4.2.4

🔵 [6.4.2.4.relationship_ref_encapsulation_duplicate](../models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_duplicate.cellml): **Error not detected.**

🔵 [6.4.2.4.relationship_ref_encapsulation_named](../models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_named.cellml): **Error not detected.**


---

##### 6.4.2.5

🔵 [6.4.2.5.relationship_ref_duplicate_named](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_named.cellml): **Error not detected.**

🔵 [6.4.2.5.relationship_ref_duplicate_unnamed_1](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_unnamed_1.cellml): **Error not detected.**

🔵 [6.4.2.5.relationship_ref_duplicate_unnamed_2](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_unnamed_2.cellml): **Error not detected.**

[6.4.2.5.relationship_ref_multiple_1](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_1.cellml): Valid file passed validation.

[6.4.2.5.relationship_ref_multiple_2](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_2.cellml): Valid file passed validation.

[6.4.2.5.relationship_ref_multiple_3](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_3.cellml): Valid file passed validation.


---

##### 6.4.3.1

[6.4.3.1.component_ref_component_missing](../models_1_0/invalid/6.4.3.1.component_ref_component_missing.cellml): Error detected correctly.
* Expected: ```Element component_ref does not carry attribute component```
* Output: ```Error on line 11: Element component_ref does not carry attribute component```

[6.4.3.1.component_ref_nesting](../models_1_0/valid/6.4.3.1.component_ref_nesting.cellml): Valid file passed validation.

[6.4.3.1.component_ref_with_component](../models_1_0/invalid/6.4.3.1.component_ref_with_component.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 10: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref component )```

[6.4.3.1.component_ref_with_connection](../models_1_0/invalid/6.4.3.1.component_ref_with_connection.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 14: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref connection )```

[6.4.3.1.component_ref_with_group](../models_1_0/invalid/6.4.3.1.component_ref_with_group.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 12: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref group )```

[6.4.3.1.component_ref_with_map_components](../models_1_0/invalid/6.4.3.1.component_ref_with_map_components.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 10: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref map_components )```

[6.4.3.1.component_ref_with_map_variables](../models_1_0/invalid/6.4.3.1.component_ref_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 14: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref map_variables )```

[6.4.3.1.component_ref_with_math](../models_1_0/invalid/6.4.3.1.component_ref_with_math.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 13: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref math )```

[6.4.3.1.component_ref_with_model](../models_1_0/invalid/6.4.3.1.component_ref_with_model.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 10: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref model )```

[6.4.3.1.component_ref_with_reaction](../models_1_0/invalid/6.4.3.1.component_ref_with_reaction.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 12: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref reaction )```

[6.4.3.1.component_ref_with_relationship_ref](../models_1_0/invalid/6.4.3.1.component_ref_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 10: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref relationship_ref )```

[6.4.3.1.component_ref_with_role](../models_1_0/invalid/6.4.3.1.component_ref_with_role.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 10: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref role )```

[6.4.3.1.component_ref_with_unit](../models_1_0/invalid/6.4.3.1.component_ref_with_unit.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 10: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref unit )```

[6.4.3.1.component_ref_with_units](../models_1_0/invalid/6.4.3.1.component_ref_with_units.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 10: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref units )```

[6.4.3.1.component_ref_with_variable](../models_1_0/invalid/6.4.3.1.component_ref_with_variable.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 10: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref variable )```

[6.4.3.1.component_ref_with_variable_ref](../models_1_0/invalid/6.4.3.1.component_ref_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element component_ref content does not follow the DTD```
* Output: ```Error on line 12: Element component_ref content does not follow the DTD, expecting (component_ref)*, got (component_ref variable_ref )```


---

##### 6.4.3.2

🔵 [6.4.3.2.component_ref_children_declared_twice_1](../models_1_0/invalid/6.4.3.2.component_ref_children_declared_twice_1.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_children_declared_twice_2](../models_1_0/invalid/6.4.3.2.component_ref_children_declared_twice_2.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_children_declared_twice_3](../models_1_0/invalid/6.4.3.2.component_ref_children_declared_twice_3.cellml): **Error not detected.**

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

🔵 [6.4.3.2.component_ref_no_children_containment](../models_1_0/invalid/6.4.3.2.component_ref_no_children_containment.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_no_children_encapsulation](../models_1_0/invalid/6.4.3.2.component_ref_no_children_encapsulation.cellml): **Error not detected.**

🔴 [6.4.3.2.component_ref_no_children_extension](../models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml): **Valid file failed validation.**
* Output:
  * ```Error on line 8: No declaration for attribute xmlns:fruit of element model```
  * ```Error on line 12: No declaration for attribute relationship of element relationship_ref```

[6.4.3.2.component_ref_overlapping_containment](../models_1_0/valid/6.4.3.2.component_ref_overlapping_containment.cellml): Valid file passed validation.

🔵 [6.4.3.2.component_ref_overlapping_encapsulation](../models_1_0/invalid/6.4.3.2.component_ref_overlapping_encapsulation.cellml): **Error not detected.**

[6.4.3.2.component_ref_split_named](../models_1_0/valid/6.4.3.2.component_ref_split_named.cellml): Valid file passed validation.

[6.4.3.2.component_ref_split_unnamed_1](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_1.cellml): Valid file passed validation.

[6.4.3.2.component_ref_split_unnamed_2](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_2.cellml): Valid file passed validation.


---

##### 6.4.3.3

🔵 [6.4.3.3.component_ref_component_invalid](../models_1_0/invalid/6.4.3.3.component_ref_component_invalid.cellml): **Error not detected.**

🔵 [6.4.3.3.component_ref_component_nonexistent_1](../models_1_0/invalid/6.4.3.3.component_ref_component_nonexistent_1.cellml): **Error not detected.**

🔵 [6.4.3.3.component_ref_component_nonexistent_2](../models_1_0/invalid/6.4.3.3.component_ref_component_nonexistent_2.cellml): **Error not detected.**


---

## 7. Reactions

##### 7.4.1.1

[7.4.1.1.reaction_variable_ref_missing](../models_1_0/invalid/7.4.1.1.reaction_variable_ref_missing.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got ```

[7.4.1.1.reaction_with_component](../models_1_0/invalid/7.4.1.1.reaction_with_component.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref component )```

[7.4.1.1.reaction_with_component_ref](../models_1_0/invalid/7.4.1.1.reaction_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref component_ref )```

[7.4.1.1.reaction_with_connection](../models_1_0/invalid/7.4.1.1.reaction_with_connection.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref connection )```

[7.4.1.1.reaction_with_group](../models_1_0/invalid/7.4.1.1.reaction_with_group.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref group )```

[7.4.1.1.reaction_with_map_components](../models_1_0/invalid/7.4.1.1.reaction_with_map_components.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref map_components )```

[7.4.1.1.reaction_with_map_variables](../models_1_0/invalid/7.4.1.1.reaction_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref map_variables )```

[7.4.1.1.reaction_with_math](../models_1_0/invalid/7.4.1.1.reaction_with_math.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 9: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref math )```

[7.4.1.1.reaction_with_model](../models_1_0/invalid/7.4.1.1.reaction_with_model.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref model )```

[7.4.1.1.reaction_with_reaction](../models_1_0/invalid/7.4.1.1.reaction_with_reaction.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 9: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref reaction )```

[7.4.1.1.reaction_with_relationship_ref](../models_1_0/invalid/7.4.1.1.reaction_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref relationship_ref )```

[7.4.1.1.reaction_with_role](../models_1_0/invalid/7.4.1.1.reaction_with_role.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref role )```

[7.4.1.1.reaction_with_unit](../models_1_0/invalid/7.4.1.1.reaction_with_unit.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref unit )```

[7.4.1.1.reaction_with_units](../models_1_0/invalid/7.4.1.1.reaction_with_units.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref units )```

[7.4.1.1.reaction_with_variable](../models_1_0/invalid/7.4.1.1.reaction_with_variable.cellml): Error detected correctly.
* Expected: ```Element reaction content does not follow the DTD```
* Output: ```Error on line 8: Element reaction content does not follow the DTD, expecting (variable_ref)+, got (variable_ref variable )```


---

##### 7.4.1.2

[7.4.1.2.reaction_reversible_invalid](../models_1_0/invalid/7.4.1.2.reaction_reversible_invalid.cellml): Error detected correctly.
* Expected: ```attribute reversible of reaction is not among the enumerated set```
* Output: ```Error on line 8: Value "definitely" for attribute reversible of reaction is not among the enumerated set```

[7.4.1.2.reaction_reversible_no](../models_1_0/valid/7.4.1.2.reaction_reversible_no.cellml): Valid file passed validation.

[7.4.1.2.reaction_reversible_yes](../models_1_0/valid/7.4.1.2.reaction_reversible_yes.cellml): Valid file passed validation.


---

##### 7.4.1.3

🔵 [7.4.1.3.reaction_encapsulating_delta_variable](../models_1_0/invalid/7.4.1.3.reaction_encapsulating_delta_variable.cellml): **Error not detected.**


---

##### 7.4.2.1

[7.4.2.1.variable_ref_role_missing](../models_1_0/invalid/7.4.2.1.variable_ref_role_missing.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got ```

[7.4.2.1.variable_ref_variable_missing](../models_1_0/invalid/7.4.2.1.variable_ref_variable_missing.cellml): Error detected correctly.
* Expected: ```variable_ref does not carry attribute variable```
* Output: ```Error on line 9: Element variable_ref does not carry attribute variable```

[7.4.2.1.variable_ref_with_component](../models_1_0/invalid/7.4.2.1.variable_ref_with_component.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (role component )```

[7.4.2.1.variable_ref_with_component_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (role component_ref )```

[7.4.2.1.variable_ref_with_connection](../models_1_0/invalid/7.4.2.1.variable_ref_with_connection.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (role connection )```

[7.4.2.1.variable_ref_with_group](../models_1_0/invalid/7.4.2.1.variable_ref_with_group.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (role group )```

[7.4.2.1.variable_ref_with_map_components](../models_1_0/invalid/7.4.2.1.variable_ref_with_map_components.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (role map_components )```

[7.4.2.1.variable_ref_with_map_variables](../models_1_0/invalid/7.4.2.1.variable_ref_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (role map_variables )```

[7.4.2.1.variable_ref_with_math](../models_1_0/invalid/7.4.2.1.variable_ref_with_math.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 10: Element variable_ref content does not follow the DTD, expecting (role)+, got (role math )```

[7.4.2.1.variable_ref_with_model](../models_1_0/invalid/7.4.2.1.variable_ref_with_model.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (role model )```

[7.4.2.1.variable_ref_with_reaction](../models_1_0/invalid/7.4.2.1.variable_ref_with_reaction.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 10: Element variable_ref content does not follow the DTD, expecting (role)+, got (role reaction )```

[7.4.2.1.variable_ref_with_relationship_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (role relationship_ref )```

[7.4.2.1.variable_ref_with_unit](../models_1_0/invalid/7.4.2.1.variable_ref_with_unit.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (role unit )```

[7.4.2.1.variable_ref_with_units](../models_1_0/invalid/7.4.2.1.variable_ref_with_units.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (role units )```

[7.4.2.1.variable_ref_with_variable](../models_1_0/invalid/7.4.2.1.variable_ref_with_variable.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 9: Element variable_ref content does not follow the DTD, expecting (role)+, got (role variable )```

[7.4.2.1.variable_ref_with_variable_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element variable_ref content does not follow the DTD```
* Output: ```Error on line 10: Element variable_ref content does not follow the DTD, expecting (role)+, got (role variable_ref )```


---

##### 7.4.2.2

🔵 [7.4.2.2.variable_ref_variable_duplicate](../models_1_0/invalid/7.4.2.2.variable_ref_variable_duplicate.cellml): **Error not detected.**

🔵 [7.4.2.2.variable_ref_variable_hidden](../models_1_0/invalid/7.4.2.2.variable_ref_variable_hidden.cellml): **Error not detected.**

🔵 [7.4.2.2.variable_ref_variable_nonexistent](../models_1_0/invalid/7.4.2.2.variable_ref_variable_nonexistent.cellml): **Error not detected.**


---

##### 7.4.3.1

[7.4.3.1.role_role_missing](../models_1_0/invalid/7.4.3.1.role_role_missing.cellml): Error detected correctly.
* Expected: ```Element role does not carry attribute role```
* Output: ```Error on line 10: Element role does not carry attribute role```

[7.4.3.1.role_with_component](../models_1_0/invalid/7.4.3.1.role_with_component.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (component )```

[7.4.3.1.role_with_component_ref](../models_1_0/invalid/7.4.3.1.role_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (component_ref )```

[7.4.3.1.role_with_connection](../models_1_0/invalid/7.4.3.1.role_with_connection.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (connection )```

[7.4.3.1.role_with_group](../models_1_0/invalid/7.4.3.1.role_with_group.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (group )```

[7.4.3.1.role_with_map_components](../models_1_0/invalid/7.4.3.1.role_with_map_components.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (map_components )```

[7.4.3.1.role_with_map_variables](../models_1_0/invalid/7.4.3.1.role_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (map_variables )```

[7.4.3.1.role_with_model](../models_1_0/invalid/7.4.3.1.role_with_model.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (model )```

[7.4.3.1.role_with_reaction](../models_1_0/invalid/7.4.3.1.role_with_reaction.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 11: Element role content does not follow the DTD, expecting (math)?, got (reaction )```

[7.4.3.1.role_with_relationship_ref](../models_1_0/invalid/7.4.3.1.role_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (relationship_ref )```

[7.4.3.1.role_with_role](../models_1_0/invalid/7.4.3.1.role_with_role.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 11: Element role content does not follow the DTD, expecting (math)?, got (role )```

[7.4.3.1.role_with_unit](../models_1_0/invalid/7.4.3.1.role_with_unit.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (unit )```

[7.4.3.1.role_with_units](../models_1_0/invalid/7.4.3.1.role_with_units.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (units )```

[7.4.3.1.role_with_variable](../models_1_0/invalid/7.4.3.1.role_with_variable.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 10: Element role content does not follow the DTD, expecting (math)?, got (variable )```

[7.4.3.1.role_with_variable_ref](../models_1_0/invalid/7.4.3.1.role_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element role content does not follow the DTD```
* Output: ```Error on line 11: Element role content does not follow the DTD, expecting (math)?, got (variable_ref )```


---

##### 7.4.3.2

[7.4.3.2.role_role_invalid](../models_1_0/invalid/7.4.3.2.role_role_invalid.cellml): Error detected correctly.
* Expected: ```attribute role of role is not among the enumerated set```
* Output: ```Error on line 10: Value "mole" for attribute role of role is not among the enumerated set```


---

##### 7.4.3.3

🔵 [7.4.3.3.reaction_multiple_rates](../models_1_0/invalid/7.4.3.3.reaction_multiple_rates.cellml): **Error not detected.**

🔵 [7.4.3.3.role_rate_with_delta_variable](../models_1_0/invalid/7.4.3.3.role_rate_with_delta_variable.cellml): **Error not detected.**

🔵 [7.4.3.3.role_rate_with_multiple_roles](../models_1_0/invalid/7.4.3.3.role_rate_with_multiple_roles.cellml): **Error not detected.**

🔵 [7.4.3.3.role_rate_with_stoichiometry](../models_1_0/invalid/7.4.3.3.role_rate_with_stoichiometry.cellml): **Error not detected.**


---

##### 7.4.3.4

[7.4.3.4.role_direction_invalid](../models_1_0/invalid/7.4.3.4.role_direction_invalid.cellml): Error detected correctly.
* Expected: ```attribute direction of role is not among the enumerated set```
* Output: ```Error on line 24: Value "backward" for attribute direction of role is not among the enumerated set```


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

🔵 [7.4.3.6.role_stoichiometry_invalid](../models_1_0/invalid/7.4.3.6.role_stoichiometry_invalid.cellml): **Error not detected.**


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

[8.4.1.duplicate_cmeta_id_in_component](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_component.cellml): Error detected correctly.
* Expected: ```ID a already defined```
* Output: ```Error on line 8: ID a already defined```

[8.4.1.duplicate_cmeta_id_in_component_ref](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_component_ref.cellml): Error detected correctly.
* Expected: ```ID y already defined```
* Output: ```Error on line 14: ID y already defined```

[8.4.1.duplicate_cmeta_id_in_connection](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_connection.cellml): Error detected correctly.
* Expected: ```ID hello already defined```
* Output: ```Error on line 13: ID hello already defined```

[8.4.1.duplicate_cmeta_id_in_group](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_group.cellml): Error detected correctly.
* Expected: ```ID x already defined```
* Output: ```Error on line 11: ID x already defined```

[8.4.1.duplicate_cmeta_id_in_map_components](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_components.cellml): Error detected correctly.
* Expected: ```ID x already defined```
* Output: ```Error on line 12: ID x already defined```

[8.4.1.duplicate_cmeta_id_in_map_variables](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_variables.cellml): Error detected correctly.
* Expected: ```ID x already defined```
* Output: ```Error on line 15: ID x already defined```

[8.4.1.duplicate_cmeta_id_in_model](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_model.cellml): Error detected correctly.
* Expected: ```ID x already defined```
* Output: ```Error on line 9: ID x already defined```

[8.4.1.duplicate_cmeta_id_in_reaction](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_reaction.cellml): Error detected correctly.
* Expected: ```ID x already defined```
* Output: ```Error on line 9: ID x already defined```

[8.4.1.duplicate_cmeta_id_in_relationship_ref](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```ID x already defined```
* Output: ```Error on line 12: ID x already defined```

[8.4.1.duplicate_cmeta_id_in_role](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_role.cellml): Error detected correctly.
* Expected: ```ID a already defined```
* Output: ```Error on line 11: ID a already defined```

[8.4.1.duplicate_cmeta_id_in_unit](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_unit.cellml): Error detected correctly.
* Expected: ```ID apple already defined```
* Output: ```Error on line 11: ID apple already defined```

[8.4.1.duplicate_cmeta_id_in_units_1](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_units_1.cellml): Error detected correctly.
* Expected: ```ID orange already defined```
* Output: ```Error on line 10: ID orange already defined```

[8.4.1.duplicate_cmeta_id_in_units_2](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_units_2.cellml): Error detected correctly.
* Expected: ```ID apple already defined```
* Output: ```Error on line 9: ID apple already defined```

[8.4.1.duplicate_cmeta_id_in_variable](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable.cellml): Error detected correctly.
* Expected: ```ID a already defined```
* Output: ```Error on line 9: ID a already defined```

[8.4.1.duplicate_cmeta_id_in_variable_ref](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable_ref.cellml): Error detected correctly.
* Expected: ```ID a already defined```
* Output: ```Error on line 10: ID a already defined```


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

[C.3.3.unit_checking_power_fraction](../models_1_0/unit_checking_consistent/C.3.3.unit_checking_power_fraction.cellml): Valid file passed validation.

[C.3.3.unit_checking_power_half](../models_1_0/unit_checking_consistent/C.3.3.unit_checking_power_half.cellml): Valid file passed validation.

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

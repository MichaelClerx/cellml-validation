# Cellmlmanip Validation - CellML 1.0

Performance:
* 76% according to spec (703 out of 923)
* 267 out of 375 valid files passed
* 436 out of 548 invalid files detected

Issues:
* 108 valid files failed validation
* 67 invalid files passed validation
* 45 invalid files failed validation for the wrong reason

Results per category

(Valid passed, invalid failed, valid failed, invalid passed, invalid failed for wrong reason, percent classified correctly according to spec)

|Category|V Pass|I Fail|🔴 V Fail|🔵 I Pass|🔶 I Bad|Score|
|-|-|-|-|-|-|-|
|[0. Not mentioned in spec](#0-not-mentioned-in-spec)|6|10|0|0|0|100%|
|[2. Fundamentals](#2-fundamentals)|24|42|10|40|21|48%|
|[3. Model structure](#3-model-structure)|43|147|7|8|0|92%|
|[4. Mathematics](#4-mathematics)|32|16|18|2|2|68%|
|[5. Units](#5-units)|84|80|52|0|8|73%|
|[6. Grouping](#6-grouping)|12|58|5|17|3|73%|
|[7. Reactions](#7-reactions)|0|68|5|0|11|80%|
|[8. Metadata framework](#8-metadata-framework)|21|15|9|0|0|80%|
|[C. Advanced units functionality](#c-advanced-units-functionality)|45|0|2|0|0|95%|


---

## 0. Not mentioned in spec

### 0.0

[0.0.root_namespace_1](../models_1_0/valid/0.0.root_namespace_1.cellml): Valid file passed validation.

[0.0.root_namespace_2](../models_1_0/valid/0.0.root_namespace_2.cellml): Valid file passed validation.

[0.0.root_node_namespace_wrong](../models_1_0/invalid/0.0.root_node_namespace_wrong.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/0.0.root_node_namespace_wrong.cellml:5:0:ERROR:RELAXNGV:RELAXNG_ERR_ELEMWRONGNS: Element model has wrong namespace: expecting http://www.cellml.org/cellml/1.0#```

[0.0.root_node_not_model](../models_1_0/invalid/0.0.root_node_not_model.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/0.0.root_node_not_model.cellml:5:0:ERROR:RELAXNGV:RELAXNG_ERR_ELEMNAME: Expecting element model, got component```

[0.0.root_node_two_elements](../models_1_0/invalid/0.0.root_node_two_elements.cellml): Error detected correctly.
* Expected: ```Extra content at the end of the document```
* Output: ```Extra content at the end of the document, line 6, column 1 (0.0.root_node_two_elements.cellml, line 6)```

[0.0.root_node_two_models](../models_1_0/invalid/0.0.root_node_two_models.cellml): Error detected correctly.
* Expected: ```Extra content at the end of the document```
* Output: ```Extra content at the end of the document, line 6, column 1 (0.0.root_node_two_models.cellml, line 6)```


---

### 0.1

[0.1.real_number_invalid_1](../models_1_0/invalid/0.1.real_number_invalid_1.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_1.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute initial_value for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_1.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[0.1.real_number_invalid_2](../models_1_0/invalid/0.1.real_number_invalid_2.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_2.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute initial_value for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_2.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_2.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[0.1.real_number_invalid_3](../models_1_0/invalid/0.1.real_number_invalid_3.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_3.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute initial_value for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_3.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_3.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[0.1.real_number_invalid_4](../models_1_0/invalid/0.1.real_number_invalid_4.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_4.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute initial_value for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_4.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_4.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[0.1.real_number_invalid_5](../models_1_0/invalid/0.1.real_number_invalid_5.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_5.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute initial_value for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_5.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_5.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[0.1.real_number_invalid_6](../models_1_0/invalid/0.1.real_number_invalid_6.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_6.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute initial_value for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_6.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/0.1.real_number_invalid_6.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

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
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_empty.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_empty.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_empty.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.1.identifier_only_underscore](../models_1_0/invalid/2.4.1.identifier_only_underscore.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_only_underscore.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_only_underscore.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_only_underscore.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.1.identifier_unexpected_character_1](../models_1_0/invalid/2.4.1.identifier_unexpected_character_1.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_unexpected_character_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_unexpected_character_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_unexpected_character_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.1.identifier_unexpected_character_2](../models_1_0/invalid/2.4.1.identifier_unexpected_character_2.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_unexpected_character_2.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_unexpected_character_2.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_unexpected_character_2.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.1.identifier_unexpected_character_unicode](../models_1_0/invalid/2.4.1.identifier_unexpected_character_unicode.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_unexpected_character_unicode.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_unexpected_character_unicode.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.1.identifier_unexpected_character_unicode.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.1.valid_identifiers](../models_1_0/valid/2.4.1.valid_identifiers.cellml): Valid file passed validation.


---

#### 2.4.2

[2.4.2.imaginary_attributes_1](../models_1_0/invalid/2.4.2.imaginary_attributes_1.cellml): Error detected correctly.
* Expected: ```Invalid attribute fruit for element model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.2.imaginary_attributes_1.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute fruit for element model```

[2.4.2.imaginary_attributes_2](../models_1_0/invalid/2.4.2.imaginary_attributes_2.cellml): Error detected correctly.
* Expected: ```Invalid attribute fruit for element model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.2.imaginary_attributes_2.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute fruit for element model```

[2.4.2.imaginary_elements_1](../models_1_0/invalid/2.4.2.imaginary_elements_1.cellml): Error detected correctly.
* Expected: ```Element model has extra content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.2.imaginary_elements_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: fruit```

[2.4.2.imaginary_elements_2](../models_1_0/invalid/2.4.2.imaginary_elements_2.cellml): Error detected correctly.
* Expected: ```Element model has extra content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.2.imaginary_elements_2.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: import```


---

#### 2.4.3

🔵 [2.4.3.bad_cmeta_attribute_in_component](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_component.cellml): **Error not detected.**

🔵 [2.4.3.bad_cmeta_attribute_in_component_ref](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_component_ref.cellml): **Error not detected.**

🔵 [2.4.3.bad_cmeta_attribute_in_connection](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_connection.cellml): **Error not detected.**

🔵 [2.4.3.bad_cmeta_attribute_in_group](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_group.cellml): **Error not detected.**

🔵 [2.4.3.bad_cmeta_attribute_in_map_components](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_map_components.cellml): **Error not detected.**

🔵 [2.4.3.bad_cmeta_attribute_in_map_variables](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_map_variables.cellml): **Error not detected.**

🔵 [2.4.3.bad_cmeta_attribute_in_model](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_model.cellml): **Error not detected.**

🔶 [2.4.3.bad_cmeta_attribute_in_reaction](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_reaction.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

🔵 [2.4.3.bad_cmeta_attribute_in_relationship_ref](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_relationship_ref.cellml): **Error not detected.**

🔶 [2.4.3.bad_cmeta_attribute_in_role](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_role.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

🔵 [2.4.3.bad_cmeta_attribute_in_unit](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_unit.cellml): **Error not detected.**

🔵 [2.4.3.bad_cmeta_attribute_in_units_1](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_units_1.cellml): **Error not detected.**

🔶 [2.4.3.bad_cmeta_attribute_in_units_2](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_units_2.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Defining units inside components is not supported (found in component A).```

🔶 [2.4.3.bad_cmeta_attribute_in_variable](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_variable.cellml): **Invalid file failed for unexpected reason.**
* Output: ```add_variable() got an unexpected keyword argument '{http://www.cellml.org/metadata/1.0#}bob'```

🔶 [2.4.3.bad_cmeta_attribute_in_variable_ref](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_variable_ref.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

[2.4.3.bad_rdf_element_in_component](../models_1_0/invalid/2.4.3.bad_rdf_element_in_component.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component has extra content: Description. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_component.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.bad_rdf_element_in_component_ref](../models_1_0/invalid/2.4.3.bad_rdf_element_in_component_ref.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_component_ref.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: Description. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component_ref in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_component_ref.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_component_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_component_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_component_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.bad_rdf_element_in_connection](../models_1_0/invalid/2.4.3.bad_rdf_element_in_connection.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_connection.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: Description. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_connection.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.bad_rdf_element_in_group](../models_1_0/invalid/2.4.3.bad_rdf_element_in_group.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_group.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: Description. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_group.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.bad_rdf_element_in_map_components](../models_1_0/invalid/2.4.3.bad_rdf_element_in_map_components.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_map_components.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: Description. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_map_components.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_map_components.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_map_components.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.bad_rdf_element_in_map_variables](../models_1_0/invalid/2.4.3.bad_rdf_element_in_map_variables.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_map_variables.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: Description. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_map_variables.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_map_variables.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_map_variables.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.bad_rdf_element_in_model](../models_1_0/invalid/2.4.3.bad_rdf_element_in_model.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_model.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: Description```

[2.4.3.bad_rdf_element_in_reaction](../models_1_0/invalid/2.4.3.bad_rdf_element_in_reaction.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_reaction.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: Description. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_reaction.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_reaction.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.bad_rdf_element_in_relationship_ref](../models_1_0/invalid/2.4.3.bad_rdf_element_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_relationship_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: Description. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_relationship_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_relationship_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_relationship_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.bad_rdf_element_in_role](../models_1_0/invalid/2.4.3.bad_rdf_element_in_role.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_role.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: Description. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_role.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_role.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_role.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_role.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_role.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.bad_rdf_element_in_unit](../models_1_0/invalid/2.4.3.bad_rdf_element_in_unit.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_unit.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: Description. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_unit.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_unit.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_unit.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.bad_rdf_element_in_units_1](../models_1_0/invalid/2.4.3.bad_rdf_element_in_units_1.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_units_1.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: Description. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_units_1.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.bad_rdf_element_in_units_2](../models_1_0/invalid/2.4.3.bad_rdf_element_in_units_2.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_units_2.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: Description. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_units_2.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_units_2.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.bad_rdf_element_in_variable](../models_1_0/invalid/2.4.3.bad_rdf_element_in_variable.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_variable.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: Description. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_variable.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.bad_rdf_element_in_variable_ref](../models_1_0/invalid/2.4.3.bad_rdf_element_in_variable_ref.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_variable_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element role, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_variable_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_variable_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_variable_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_variable_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.bad_rdf_element_in_variable_ref.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.cellml_attributes_inside_extensions](../models_1_0/invalid/2.4.3.cellml_attributes_inside_extensions.cellml): Error detected correctly.
* Expected: ```Element model failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.cellml_attributes_inside_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element units, got nothing. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element banana in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.cellml_attributes_inside_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.cellml_attributes_inside_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.3.cellml_elements_inside_extensions](../models_1_0/invalid/2.4.3.cellml_elements_inside_extensions.cellml): Error detected correctly.
* Expected: ```Element model failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.cellml_elements_inside_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element units, got nothing. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element banana in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.cellml_elements_inside_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.3.cellml_elements_inside_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

🔵 [2.4.3.cmeta_element_in_component](../models_1_0/invalid/2.4.3.cmeta_element_in_component.cellml): **Error not detected.**

🔵 [2.4.3.cmeta_element_in_component_ref](../models_1_0/invalid/2.4.3.cmeta_element_in_component_ref.cellml): **Error not detected.**

🔵 [2.4.3.cmeta_element_in_connection](../models_1_0/invalid/2.4.3.cmeta_element_in_connection.cellml): **Error not detected.**

🔵 [2.4.3.cmeta_element_in_group](../models_1_0/invalid/2.4.3.cmeta_element_in_group.cellml): **Error not detected.**

🔵 [2.4.3.cmeta_element_in_map_components](../models_1_0/invalid/2.4.3.cmeta_element_in_map_components.cellml): **Error not detected.**

🔵 [2.4.3.cmeta_element_in_map_variables](../models_1_0/invalid/2.4.3.cmeta_element_in_map_variables.cellml): **Error not detected.**

🔵 [2.4.3.cmeta_element_in_model](../models_1_0/invalid/2.4.3.cmeta_element_in_model.cellml): **Error not detected.**

🔶 [2.4.3.cmeta_element_in_reaction](../models_1_0/invalid/2.4.3.cmeta_element_in_reaction.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

🔵 [2.4.3.cmeta_element_in_relationship_ref](../models_1_0/invalid/2.4.3.cmeta_element_in_relationship_ref.cellml): **Error not detected.**

🔶 [2.4.3.cmeta_element_in_role](../models_1_0/invalid/2.4.3.cmeta_element_in_role.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

🔵 [2.4.3.cmeta_element_in_unit](../models_1_0/invalid/2.4.3.cmeta_element_in_unit.cellml): **Error not detected.**

🔶 [2.4.3.cmeta_element_in_units_1](../models_1_0/invalid/2.4.3.cmeta_element_in_units_1.cellml): **Invalid file failed for unexpected reason.**
* Output: ```'units'```

🔶 [2.4.3.cmeta_element_in_units_2](../models_1_0/invalid/2.4.3.cmeta_element_in_units_2.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Defining units inside components is not supported (found in component A).```

🔵 [2.4.3.cmeta_element_in_variable](../models_1_0/invalid/2.4.3.cmeta_element_in_variable.cellml): **Error not detected.**

🔶 [2.4.3.cmeta_element_in_variable_ref](../models_1_0/invalid/2.4.3.cmeta_element_in_variable_ref.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

[2.4.3.component_ref_with_extensions](../models_1_0/valid/2.4.3.component_ref_with_extensions.cellml): Valid file passed validation.

[2.4.3.component_with_extensions](../models_1_0/valid/2.4.3.component_with_extensions.cellml): Valid file passed validation.

[2.4.3.connection_with_extensions](../models_1_0/valid/2.4.3.connection_with_extensions.cellml): Valid file passed validation.

[2.4.3.group_with_extensions](../models_1_0/valid/2.4.3.group_with_extensions.cellml): Valid file passed validation.

[2.4.3.map_components_with_extensions](../models_1_0/valid/2.4.3.map_components_with_extensions.cellml): Valid file passed validation.

[2.4.3.map_variables_with_extensions](../models_1_0/valid/2.4.3.map_variables_with_extensions.cellml): Valid file passed validation.

🔵 [2.4.3.mathml_attribute_in_component](../models_1_0/invalid/2.4.3.mathml_attribute_in_component.cellml): **Error not detected.**

🔵 [2.4.3.mathml_attribute_in_component_ref](../models_1_0/invalid/2.4.3.mathml_attribute_in_component_ref.cellml): **Error not detected.**

🔵 [2.4.3.mathml_attribute_in_connection](../models_1_0/invalid/2.4.3.mathml_attribute_in_connection.cellml): **Error not detected.**

🔵 [2.4.3.mathml_attribute_in_group](../models_1_0/invalid/2.4.3.mathml_attribute_in_group.cellml): **Error not detected.**

🔵 [2.4.3.mathml_attribute_in_map_components](../models_1_0/invalid/2.4.3.mathml_attribute_in_map_components.cellml): **Error not detected.**

🔵 [2.4.3.mathml_attribute_in_map_variables](../models_1_0/invalid/2.4.3.mathml_attribute_in_map_variables.cellml): **Error not detected.**

🔵 [2.4.3.mathml_attribute_in_model](../models_1_0/invalid/2.4.3.mathml_attribute_in_model.cellml): **Error not detected.**

🔶 [2.4.3.mathml_attribute_in_reaction](../models_1_0/invalid/2.4.3.mathml_attribute_in_reaction.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

🔵 [2.4.3.mathml_attribute_in_relationship_ref](../models_1_0/invalid/2.4.3.mathml_attribute_in_relationship_ref.cellml): **Error not detected.**

🔶 [2.4.3.mathml_attribute_in_role](../models_1_0/invalid/2.4.3.mathml_attribute_in_role.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

🔵 [2.4.3.mathml_attribute_in_unit](../models_1_0/invalid/2.4.3.mathml_attribute_in_unit.cellml): **Error not detected.**

🔵 [2.4.3.mathml_attribute_in_units_1](../models_1_0/invalid/2.4.3.mathml_attribute_in_units_1.cellml): **Error not detected.**

🔶 [2.4.3.mathml_attribute_in_units_2](../models_1_0/invalid/2.4.3.mathml_attribute_in_units_2.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Defining units inside components is not supported (found in component A).```

🔶 [2.4.3.mathml_attribute_in_variable](../models_1_0/invalid/2.4.3.mathml_attribute_in_variable.cellml): **Invalid file failed for unexpected reason.**
* Output: ```add_variable() got an unexpected keyword argument '{http://www.w3.org/1998/Math/MathML}sum'```

🔶 [2.4.3.mathml_attribute_in_variable_ref](../models_1_0/invalid/2.4.3.mathml_attribute_in_variable_ref.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

[2.4.3.model_with_extensions](../models_1_0/valid/2.4.3.model_with_extensions.cellml): Valid file passed validation.

🔵 [2.4.3.rdf_attribute_in_component](../models_1_0/invalid/2.4.3.rdf_attribute_in_component.cellml): **Error not detected.**

🔵 [2.4.3.rdf_attribute_in_component_ref](../models_1_0/invalid/2.4.3.rdf_attribute_in_component_ref.cellml): **Error not detected.**

🔵 [2.4.3.rdf_attribute_in_connection](../models_1_0/invalid/2.4.3.rdf_attribute_in_connection.cellml): **Error not detected.**

🔵 [2.4.3.rdf_attribute_in_group](../models_1_0/invalid/2.4.3.rdf_attribute_in_group.cellml): **Error not detected.**

🔵 [2.4.3.rdf_attribute_in_map_components](../models_1_0/invalid/2.4.3.rdf_attribute_in_map_components.cellml): **Error not detected.**

🔵 [2.4.3.rdf_attribute_in_map_variables](../models_1_0/invalid/2.4.3.rdf_attribute_in_map_variables.cellml): **Error not detected.**

🔵 [2.4.3.rdf_attribute_in_model](../models_1_0/invalid/2.4.3.rdf_attribute_in_model.cellml): **Error not detected.**

🔶 [2.4.3.rdf_attribute_in_reaction](../models_1_0/invalid/2.4.3.rdf_attribute_in_reaction.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

🔵 [2.4.3.rdf_attribute_in_relationship_ref](../models_1_0/invalid/2.4.3.rdf_attribute_in_relationship_ref.cellml): **Error not detected.**

🔶 [2.4.3.rdf_attribute_in_role](../models_1_0/invalid/2.4.3.rdf_attribute_in_role.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

🔵 [2.4.3.rdf_attribute_in_unit](../models_1_0/invalid/2.4.3.rdf_attribute_in_unit.cellml): **Error not detected.**

🔵 [2.4.3.rdf_attribute_in_units_1](../models_1_0/invalid/2.4.3.rdf_attribute_in_units_1.cellml): **Error not detected.**

🔶 [2.4.3.rdf_attribute_in_units_2](../models_1_0/invalid/2.4.3.rdf_attribute_in_units_2.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Defining units inside components is not supported (found in component A).```

🔶 [2.4.3.rdf_attribute_in_variable](../models_1_0/invalid/2.4.3.rdf_attribute_in_variable.cellml): **Invalid file failed for unexpected reason.**
* Output: ```add_variable() got an unexpected keyword argument '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}parseType'```

🔶 [2.4.3.rdf_attribute_in_variable_ref](../models_1_0/invalid/2.4.3.rdf_attribute_in_variable_ref.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

🔴 [2.4.3.reaction_with_extensions](../models_1_0/valid/2.4.3.reaction_with_extensions.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

[2.4.3.relationship_ref_with_extensions](../models_1_0/valid/2.4.3.relationship_ref_with_extensions.cellml): Valid file passed validation.

🔴 [2.4.3.role_with_extensions](../models_1_0/valid/2.4.3.role_with_extensions.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

[2.4.3.unit_with_extensions](../models_1_0/valid/2.4.3.unit_with_extensions.cellml): Valid file passed validation.

🔴 [2.4.3.units_with_extensions](../models_1_0/valid/2.4.3.units_with_extensions.cellml): **Valid file failed validation.**
* Output: ```'units'```

🔴 [2.4.3.variable_ref_with_extensions](../models_1_0/valid/2.4.3.variable_ref_with_extensions.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

🔴 [2.4.3.variable_with_extensions](../models_1_0/valid/2.4.3.variable_with_extensions.cellml): **Valid file failed validation.**
* Output: ```add_variable() got an unexpected keyword argument '{http://fruit.org}x_a_day'```

[2.4.3.xlink_href_in_component](../models_1_0/valid/2.4.3.xlink_href_in_component.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_component_ref](../models_1_0/valid/2.4.3.xlink_href_in_component_ref.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_connection](../models_1_0/valid/2.4.3.xlink_href_in_connection.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_group](../models_1_0/valid/2.4.3.xlink_href_in_group.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_map_components](../models_1_0/valid/2.4.3.xlink_href_in_map_components.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_map_variables](../models_1_0/valid/2.4.3.xlink_href_in_map_variables.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_model](../models_1_0/valid/2.4.3.xlink_href_in_model.cellml): Valid file passed validation.

🔴 [2.4.3.xlink_href_in_reaction](../models_1_0/valid/2.4.3.xlink_href_in_reaction.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

[2.4.3.xlink_href_in_relationship_ref](../models_1_0/valid/2.4.3.xlink_href_in_relationship_ref.cellml): Valid file passed validation.

🔴 [2.4.3.xlink_href_in_role](../models_1_0/valid/2.4.3.xlink_href_in_role.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

[2.4.3.xlink_href_in_unit](../models_1_0/valid/2.4.3.xlink_href_in_unit.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_units_1](../models_1_0/valid/2.4.3.xlink_href_in_units_1.cellml): Valid file passed validation.

🔴 [2.4.3.xlink_href_in_units_2](../models_1_0/valid/2.4.3.xlink_href_in_units_2.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

🔴 [2.4.3.xlink_href_in_variable](../models_1_0/valid/2.4.3.xlink_href_in_variable.cellml): **Valid file failed validation.**
* Output: ```add_variable() got an unexpected keyword argument '{http://www.w3.org/1999/xlink}href'```

🔴 [2.4.3.xlink_href_in_variable_ref](../models_1_0/valid/2.4.3.xlink_href_in_variable_ref.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```


---

#### 2.4.4

[2.4.4.model_linux_line_breaks](../models_1_0/valid/2.4.4.model_linux_line_breaks.cellml): Valid file passed validation.

[2.4.4.model_windows_line_breaks](../models_1_0/valid/2.4.4.model_windows_line_breaks.cellml): Valid file passed validation.

[2.4.4.model_with_spaces](../models_1_0/valid/2.4.4.model_with_spaces.cellml): Valid file passed validation.

[2.4.4.model_with_tabs](../models_1_0/valid/2.4.4.model_with_tabs.cellml): Valid file passed validation.

[2.4.4.text_in_component](../models_1_0/invalid/2.4.4.text_in_component.cellml): Error detected correctly.
* Expected: ```Element component has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component has extra content: text. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.4.text_in_component_ref](../models_1_0/invalid/2.4.4.text_in_component_ref.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_component_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: text. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component_ref in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_component_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_component_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_component_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_component_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.4.text_in_connection](../models_1_0/invalid/2.4.4.text_in_connection.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_connection.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: text. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_connection.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.4.text_in_group](../models_1_0/invalid/2.4.4.text_in_group.cellml): Error detected correctly.
* Expected: ```Element group has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_group.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: text. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_group.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.4.text_in_map_components](../models_1_0/invalid/2.4.4.text_in_map_components.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_map_components.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: text. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.4.text_in_map_variables](../models_1_0/invalid/2.4.4.text_in_map_variables.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_map_variables.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: text. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_map_variables.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_map_variables.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_map_variables.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.4.text_in_model](../models_1_0/invalid/2.4.4.text_in_model.cellml): Error detected correctly.
* Expected: ```Element model has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_model.cellml:5:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: text```

[2.4.4.text_in_reaction](../models_1_0/invalid/2.4.4.text_in_reaction.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_reaction.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: text. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_reaction.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_reaction.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.4.text_in_relationship_ref](../models_1_0/invalid/2.4.4.text_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_relationship_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: text. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.4.text_in_role](../models_1_0/invalid/2.4.4.text_in_role.cellml): Error detected correctly.
* Expected: ```Element role has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_role.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: text. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_role.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_role.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_role.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_role.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.4.text_in_unit](../models_1_0/invalid/2.4.4.text_in_unit.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_unit.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: text. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.4.text_in_units_1](../models_1_0/invalid/2.4.4.text_in_units_1.cellml): Error detected correctly.
* Expected: ```Element units has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_units_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: text. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_units_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.4.text_in_units_2](../models_1_0/invalid/2.4.4.text_in_units_2.cellml): Error detected correctly.
* Expected: ```Element units has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_units_2.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: text. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_units_2.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_units_2.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.4.text_in_variable](../models_1_0/invalid/2.4.4.text_in_variable.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_variable.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: text. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_variable.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[2.4.4.text_in_variable_ref](../models_1_0/invalid/2.4.4.text_in_variable_ref.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: text```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_variable_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: text. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_variable_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_variable_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_variable_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.4.4.text_in_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

#### 2.5.1

🔶 [2.5.1.identifiers_are_case_sensitive](../models_1_0/invalid/2.5.1.identifiers_are_case_sensitive.cellml): **Invalid file failed for unexpected reason.**
* Output: ```'a$x'```


---

#### 2.5.2

[2.5.2.attribute_in_cellml_namespace](../models_1_0/invalid/2.5.2.attribute_in_cellml_namespace.cellml): Error detected correctly.
* Expected: ```Element model failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/2.5.2.attribute_in_cellml_namespace.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute private_interface for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.5.2.attribute_in_cellml_namespace.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/2.5.2.attribute_in_cellml_namespace.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

## 3. Model structure

##### 3.4.1.1

[3.4.1.1.model_child_order_1](../models_1_0/valid/3.4.1.1.model_child_order_1.cellml): Valid file passed validation.

[3.4.1.1.model_child_order_2](../models_1_0/valid/3.4.1.1.model_child_order_2.cellml): Valid file passed validation.

[3.4.1.1.model_empty](../models_1_0/valid/3.4.1.1.model_empty.cellml): Valid file passed validation.

[3.4.1.1.model_name_missing](../models_1_0/invalid/3.4.1.1.model_name_missing.cellml): Error detected correctly.
* Expected: ```Element model failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.1.model_name_missing.cellml:4:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.1.model_name_missing.cellml:4:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.1.1.model_with_component_ref](../models_1_0/invalid/3.4.1.1.model_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element model has extra content: component_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.1.model_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: component_ref```

[3.4.1.1.model_with_components](../models_1_0/valid/3.4.1.1.model_with_components.cellml): Valid file passed validation.

[3.4.1.1.model_with_connections](../models_1_0/valid/3.4.1.1.model_with_connections.cellml): Valid file passed validation.

[3.4.1.1.model_with_groups](../models_1_0/valid/3.4.1.1.model_with_groups.cellml): Valid file passed validation.

[3.4.1.1.model_with_map_components](../models_1_0/invalid/3.4.1.1.model_with_map_components.cellml): Error detected correctly.
* Expected: ```Element model has extra content: map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.1.model_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: map_components```

[3.4.1.1.model_with_map_variables](../models_1_0/invalid/3.4.1.1.model_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element model has extra content: map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.1.model_with_map_variables.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: map_variables```

[3.4.1.1.model_with_math](../models_1_0/invalid/3.4.1.1.model_with_math.cellml): Error detected correctly.
* Expected: ```Element model has extra content: math```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.1.model_with_math.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: math```

[3.4.1.1.model_with_model](../models_1_0/invalid/3.4.1.1.model_with_model.cellml): Error detected correctly.
* Expected: ```Element model has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.1.model_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: model```

[3.4.1.1.model_with_one_component](../models_1_0/valid/3.4.1.1.model_with_one_component.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_connection](../models_1_0/valid/3.4.1.1.model_with_one_connection.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_group](../models_1_0/valid/3.4.1.1.model_with_one_group.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_units](../models_1_0/valid/3.4.1.1.model_with_one_units.cellml): Valid file passed validation.

[3.4.1.1.model_with_reaction](../models_1_0/invalid/3.4.1.1.model_with_reaction.cellml): Error detected correctly.
* Expected: ```Element model has extra content: reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.1.model_with_reaction.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: reaction```

[3.4.1.1.model_with_relationship_ref](../models_1_0/invalid/3.4.1.1.model_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element model has extra content: relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.1.model_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: relationship_ref```

[3.4.1.1.model_with_role](../models_1_0/invalid/3.4.1.1.model_with_role.cellml): Error detected correctly.
* Expected: ```Element model has extra content: role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.1.model_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: role```

[3.4.1.1.model_with_unit](../models_1_0/invalid/3.4.1.1.model_with_unit.cellml): Error detected correctly.
* Expected: ```Element model has extra content: unit```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.1.model_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: unit```

[3.4.1.1.model_with_units](../models_1_0/valid/3.4.1.1.model_with_units.cellml): Valid file passed validation.

[3.4.1.1.model_with_variable](../models_1_0/invalid/3.4.1.1.model_with_variable.cellml): Error detected correctly.
* Expected: ```Element model has extra content: variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.1.model_with_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: variable```

[3.4.1.1.model_with_variable_ref](../models_1_0/invalid/3.4.1.1.model_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element model has extra content: variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.1.model_with_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element model has extra content: variable_ref```


---

##### 3.4.1.2

[3.4.1.2.model_name_invalid](../models_1_0/invalid/3.4.1.2.model_name_invalid.cellml): Error detected correctly.
* Expected: ```Element model failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.2.model_name_invalid.cellml:4:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.1.2.model_name_invalid.cellml:4:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 3.4.2.1

🔴 [3.4.2.1.component_child_order_1](../models_1_0/valid/3.4.2.1.component_child_order_1.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

🔴 [3.4.2.1.component_child_order_2](../models_1_0/valid/3.4.2.1.component_child_order_2.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

[3.4.2.1.component_empty](../models_1_0/valid/3.4.2.1.component_empty.cellml): Valid file passed validation.

[3.4.2.1.component_name_missing](../models_1_0/invalid/3.4.2.1.component_name_missing.cellml): Error detected correctly.
* Expected: ```Element component failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_name_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_name_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_name_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.2.1.component_with_component](../models_1_0/invalid/3.4.2.1.component_with_component.cellml): Error detected correctly.
* Expected: ```Element component has extra content: component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_component.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component has extra content: component. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.2.1.component_with_component_ref](../models_1_0/invalid/3.4.2.1.component_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element component has extra content: component_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_component_ref.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component has extra content: component_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.2.1.component_with_connection](../models_1_0/invalid/3.4.2.1.component_with_connection.cellml): Error detected correctly.
* Expected: ```Element component has extra content: connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_connection.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component has extra content: connection. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_connection.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.2.1.component_with_group](../models_1_0/invalid/3.4.2.1.component_with_group.cellml): Error detected correctly.
* Expected: ```Element component has extra content: group```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_group.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component has extra content: group. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.2.1.component_with_map_components](../models_1_0/invalid/3.4.2.1.component_with_map_components.cellml): Error detected correctly.
* Expected: ```Element component has extra content: map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_map_components.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component has extra content: map_components. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.2.1.component_with_map_variables](../models_1_0/invalid/3.4.2.1.component_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element component has extra content: map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_map_variables.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component has extra content: map_variables. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.2.1.component_with_maths](../models_1_0/valid/3.4.2.1.component_with_maths.cellml): Valid file passed validation.

[3.4.2.1.component_with_model](../models_1_0/invalid/3.4.2.1.component_with_model.cellml): Error detected correctly.
* Expected: ```Element component has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_model.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component has extra content: model. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.2.1.component_with_one_math](../models_1_0/valid/3.4.2.1.component_with_one_math.cellml): Valid file passed validation.

🔴 [3.4.2.1.component_with_one_reaction](../models_1_0/valid/3.4.2.1.component_with_one_reaction.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

🔴 [3.4.2.1.component_with_one_units](../models_1_0/valid/3.4.2.1.component_with_one_units.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

[3.4.2.1.component_with_one_variable](../models_1_0/valid/3.4.2.1.component_with_one_variable.cellml): Valid file passed validation.

🔴 [3.4.2.1.component_with_reactions](../models_1_0/valid/3.4.2.1.component_with_reactions.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

[3.4.2.1.component_with_relationship_ref](../models_1_0/invalid/3.4.2.1.component_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element component has extra content: relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_relationship_ref.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component has extra content: relationship_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.2.1.component_with_role](../models_1_0/invalid/3.4.2.1.component_with_role.cellml): Error detected correctly.
* Expected: ```Element component has extra content: role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_role.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component has extra content: role. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.2.1.component_with_unit](../models_1_0/invalid/3.4.2.1.component_with_unit.cellml): Error detected correctly.
* Expected: ```Element component has extra content: unit```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_unit.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component has extra content: unit. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

🔴 [3.4.2.1.component_with_units](../models_1_0/valid/3.4.2.1.component_with_units.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

[3.4.2.1.component_with_variable_ref](../models_1_0/invalid/3.4.2.1.component_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element component has extra content: variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_variable_ref.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component has extra content: variable_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.1.component_with_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.2.1.component_with_variables](../models_1_0/valid/3.4.2.1.component_with_variables.cellml): Valid file passed validation.


---

##### 3.4.2.2

🔵 [3.4.2.2.component_name_duplicate](../models_1_0/invalid/3.4.2.2.component_name_duplicate.cellml): **Error not detected.**

[3.4.2.2.component_name_invalid](../models_1_0/invalid/3.4.2.2.component_name_invalid.cellml): Error detected correctly.
* Expected: ```Element component failed to validate```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.2.component_name_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.2.component_name_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.2.2.component_name_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 3.4.3.1

[3.4.3.1.variable_name_missing](../models_1_0/invalid/3.4.3.1.variable_name_missing.cellml): Error detected correctly.
* Expected: ```Element variable failed to validate attributes```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_name_missing.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element variable failed to validate attributes. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_name_missing.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_name_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_units_missing](../models_1_0/invalid/3.4.3.1.variable_units_missing.cellml): Error detected correctly.
* Expected: ```Element variable failed to validate attributes```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_units_missing.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element variable failed to validate attributes. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_units_missing.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_units_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_component](../models_1_0/invalid/3.4.3.1.variable_with_component.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: component. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_component.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_component_ref](../models_1_0/invalid/3.4.3.1.variable_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: component_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_component_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: component_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_component_ref.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_connection](../models_1_0/invalid/3.4.3.1.variable_with_connection.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_connection.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: connection. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_connection.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_connection.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_group](../models_1_0/invalid/3.4.3.1.variable_with_group.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: group```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_group.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: group. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_group.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_initial_value](../models_1_0/valid/3.4.3.1.variable_with_initial_value.cellml): Valid file passed validation.

[3.4.3.1.variable_with_interfaces](../models_1_0/valid/3.4.3.1.variable_with_interfaces.cellml): Valid file passed validation.

[3.4.3.1.variable_with_map_components](../models_1_0/invalid/3.4.3.1.variable_with_map_components.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: map_component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: map_components. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_map_components.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_map_variables](../models_1_0/invalid/3.4.3.1.variable_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_map_variables.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: map_variables. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_map_variables.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_math](../models_1_0/invalid/3.4.3.1.variable_with_math.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: math```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_math.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: math. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_math.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_model](../models_1_0/invalid/3.4.3.1.variable_with_model.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: model. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_model.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_reaction](../models_1_0/invalid/3.4.3.1.variable_with_reaction.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_reaction.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: reaction. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_reaction.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_reaction.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_relationship_ref](../models_1_0/invalid/3.4.3.1.variable_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: relationship_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_relationship_ref.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_role](../models_1_0/invalid/3.4.3.1.variable_with_role.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_role.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: role. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_role.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_unit](../models_1_0/invalid/3.4.3.1.variable_with_unit.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: unit```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: unit. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_unit.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_units](../models_1_0/invalid/3.4.3.1.variable_with_units.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: units. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_units.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_variable](../models_1_0/invalid/3.4.3.1.variable_with_variable.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_variable.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_with_variable_ref](../models_1_0/invalid/3.4.3.1.variable_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element variable has extra content: variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_variable_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable has extra content: variable_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_variable_ref.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.1.variable_with_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.1.variable_without_initial_value](../models_1_0/valid/3.4.3.1.variable_without_initial_value.cellml): Valid file passed validation.


---

##### 3.4.3.2

[3.4.3.2.variable_name_duplicate](../models_1_0/invalid/3.4.3.2.variable_name_duplicate.cellml): Error detected correctly.
* Expected: ```already exists```
* Output: ```Variable c$x already exists.```

[3.4.3.2.variable_name_invalid](../models_1_0/invalid/3.4.3.2.variable_name_invalid.cellml): Error detected correctly.
* Expected: ```Element variable failed to validate attributes```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.2.variable_name_invalid.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element variable failed to validate attributes. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.2.variable_name_invalid.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.2.variable_name_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.2.variable_name_same_as_cousin](../models_1_0/valid/3.4.3.2.variable_name_same_as_cousin.cellml): Valid file passed validation.

[3.4.3.2.variable_name_same_as_parent](../models_1_0/valid/3.4.3.2.variable_name_same_as_parent.cellml): Valid file passed validation.


---

##### 3.4.3.3

🔴 [3.4.3.3.variable_units_component](../models_1_0/valid/3.4.3.3.variable_units_component.cellml): **Valid file failed validation.**
* Output: ```'Unknown unit oranges.'```

[3.4.3.3.variable_units_model](../models_1_0/valid/3.4.3.3.variable_units_model.cellml): Valid file passed validation.

[3.4.3.3.variable_units_other_component](../models_1_0/invalid/3.4.3.3.variable_units_other_component.cellml): Error detected correctly.
* Expected: ```Unknown unit oranges```
* Output: ```'Unknown unit oranges.'```

[3.4.3.3.variable_units_predefined](../models_1_0/valid/3.4.3.3.variable_units_predefined.cellml): Valid file passed validation.

[3.4.3.3.variable_units_unknown](../models_1_0/invalid/3.4.3.3.variable_units_unknown.cellml): Error detected correctly.
* Expected: ```Unknown unit oranges```
* Output: ```'Unknown unit oranges.'```


---

##### 3.4.3.4

[3.4.3.4.variable_interface_public_invalid](../models_1_0/invalid/3.4.3.4.variable_interface_public_invalid.cellml): Error detected correctly.
* Expected: ```Invalid attribute public_interface for element variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.4.variable_interface_public_invalid.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute public_interface for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.4.variable_interface_public_invalid.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.4.variable_interface_public_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 3.4.3.5

[3.4.3.5.variable_interface_private_invalid](../models_1_0/invalid/3.4.3.5.variable_interface_private_invalid.cellml): Error detected correctly.
* Expected: ```Invalid attribute private_interface for element variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.5.variable_interface_private_invalid.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute private_interface for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.5.variable_interface_private_invalid.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.5.variable_interface_private_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 3.4.3.6

[3.4.3.6.variable_interfaces_both_in](../models_1_0/invalid/3.4.3.6.variable_interfaces_both_in.cellml): Error detected correctly.
* Expected: ```Invalid attribute public_interface for element variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.6.variable_interfaces_both_in.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute public_interface for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.6.variable_interfaces_both_in.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.6.variable_interfaces_both_in.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 3.4.3.7

[3.4.3.7.variable_initial_value_empty](../models_1_0/invalid/3.4.3.7.variable_initial_value_empty.cellml): Error detected correctly.
* Expected: ```Invalid attribute initial_value for element variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.7.variable_initial_value_empty.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute initial_value for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.7.variable_initial_value_empty.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.7.variable_initial_value_empty.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.7.variable_initial_value_invalid](../models_1_0/invalid/3.4.3.7.variable_initial_value_invalid.cellml): Error detected correctly.
* Expected: ```Invalid attribute initial_value for element variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.7.variable_initial_value_invalid.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute initial_value for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.7.variable_initial_value_invalid.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.7.variable_initial_value_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 3.4.3.8

[3.4.3.8.variable_interfaces_private_in_and_initial](../models_1_0/invalid/3.4.3.8.variable_interfaces_private_in_and_initial.cellml): Error detected correctly.
* Expected: ```Invalid attribute initial_value for element variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.8.variable_interfaces_private_in_and_initial.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute initial_value for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.8.variable_interfaces_private_in_and_initial.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.8.variable_interfaces_private_in_and_initial.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.3.8.variable_interfaces_public_in_and_initial](../models_1_0/invalid/3.4.3.8.variable_interfaces_public_in_and_initial.cellml): Error detected correctly.
* Expected: ```Invalid attribute initial_value for element variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.8.variable_interfaces_public_in_and_initial.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute initial_value for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.8.variable_interfaces_public_in_and_initial.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.3.8.variable_interfaces_public_in_and_initial.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 3.4.4.1

[3.4.4.1.connection_empty](../models_1_0/invalid/3.4.4.1.connection_empty.cellml): Error detected correctly.
* Expected: ```Expecting an element map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_empty.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element map_components, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_empty.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_empty.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_empty.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_map_components_missing](../models_1_0/invalid/3.4.4.1.connection_map_components_missing.cellml): Error detected correctly.
* Expected: ```Expecting an element map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_components_missing.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element map_components, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_components_missing.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_components_missing.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_components_missing.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_map_components_multiple](../models_1_0/invalid/3.4.4.1.connection_map_components_multiple.cellml): Error detected correctly.
* Expected: ```Extra element map_components```
* Output: ```Invalid or unsupported CellML file. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element map_components in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_components_multiple.cellml:19:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_components_multiple.cellml:17:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_map_variables_missing_1](../models_1_0/invalid/3.4.4.1.connection_map_variables_missing_1.cellml): Error detected correctly.
* Expected: ```Expecting an element map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_variables_missing_1.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element map_variables, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_variables_missing_1.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_variables_missing_1.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_variables_missing_1.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_map_variables_missing_2](../models_1_0/invalid/3.4.4.1.connection_map_variables_missing_2.cellml): Error detected correctly.
* Expected: ```Expecting an element map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_variables_missing_2.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element map_variables, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_variables_missing_2.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_variables_missing_2.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_map_variables_missing_2.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_only_extensions](../models_1_0/invalid/3.4.4.1.connection_only_extensions.cellml): Error detected correctly.
* Expected: ```Element connection failed to validate```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_only_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element map_components, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_only_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_only_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_only_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_component](../models_1_0/invalid/3.4.4.1.connection_with_component.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_component.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: component. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_component.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_component_ref](../models_1_0/invalid/3.4.4.1.connection_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: component_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_component_ref.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: component_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_component_ref.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_connection](../models_1_0/invalid/3.4.4.1.connection_with_connection.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_connection.cellml:19:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: connection. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_connection.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_group](../models_1_0/invalid/3.4.4.1.connection_with_group.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: group```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_group.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: group. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_group.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_map_variables](../models_1_0/valid/3.4.4.1.connection_with_map_variables.cellml): Valid file passed validation.

[3.4.4.1.connection_with_math](../models_1_0/invalid/3.4.4.1.connection_with_math.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: math```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_math.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: math. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_math.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_model](../models_1_0/invalid/3.4.4.1.connection_with_model.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_model.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: model. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_model.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_name_attribute](../models_1_0/invalid/3.4.4.1.connection_with_name_attribute.cellml): Error detected correctly.
* Expected: ```Invalid attribute name for element connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_name_attribute.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute name for element connection. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_name_attribute.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_one_map_variables](../models_1_0/valid/3.4.4.1.connection_with_one_map_variables.cellml): Valid file passed validation.

[3.4.4.1.connection_with_reaction](../models_1_0/invalid/3.4.4.1.connection_with_reaction.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_reaction.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: reaction. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_reaction.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_relationship_ref](../models_1_0/invalid/3.4.4.1.connection_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_relationship_ref.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: relationship_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_relationship_ref.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_role](../models_1_0/invalid/3.4.4.1.connection_with_role.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_role.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: role. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_role.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_unit](../models_1_0/invalid/3.4.4.1.connection_with_unit.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: unit```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_unit.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: unit. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_unit.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_units](../models_1_0/invalid/3.4.4.1.connection_with_units.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_units.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: units. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_units.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_variable](../models_1_0/invalid/3.4.4.1.connection_with_variable.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_variable.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_variable.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.4.1.connection_with_variable_ref](../models_1_0/invalid/3.4.4.1.connection_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element connection has extra content: variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_variable_ref.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element connection has extra content: variable_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.4.1.connection_with_variable_ref.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 3.4.5.1

[3.4.5.1.connection_any_order_1](../models_1_0/valid/3.4.5.1.connection_any_order_1.cellml): Valid file passed validation.

[3.4.5.1.connection_any_order_2](../models_1_0/valid/3.4.5.1.connection_any_order_2.cellml): Valid file passed validation.

[3.4.5.1.map_components_component_1_missing](../models_1_0/invalid/3.4.5.1.map_components_component_1_missing.cellml): Error detected correctly.
* Expected: ```Element map_components failed to validate attributes```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_component_1_missing.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element map_components failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_component_1_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_component_1_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_component_1_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_component_2_missing](../models_1_0/invalid/3.4.5.1.map_components_component_2_missing.cellml): Error detected correctly.
* Expected: ```Element map_components failed to validate attributes```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_component_2_missing.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element map_components failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_component_2_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_component_2_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_component_2_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_component](../models_1_0/invalid/3.4.5.1.map_components_with_component.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: component. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_component_ref](../models_1_0/invalid/3.4.5.1.map_components_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: component_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_component_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: component_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_connection](../models_1_0/invalid/3.4.5.1.map_components_with_connection.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_connection.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: connection. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_connection.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_connection.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_connection.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_group](../models_1_0/invalid/3.4.5.1.map_components_with_group.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: group```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_group.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: group. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_map_components](../models_1_0/invalid/3.4.5.1.map_components_with_map_components.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: map_components. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_map_variables](../models_1_0/invalid/3.4.5.1.map_components_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_map_variables.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: map_variables. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_math](../models_1_0/invalid/3.4.5.1.map_components_with_math.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: math```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_math.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: math. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_model](../models_1_0/invalid/3.4.5.1.map_components_with_model.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: model. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_reaction](../models_1_0/invalid/3.4.5.1.map_components_with_reaction.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_reaction.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: reaction. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_reaction.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_reaction.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_reaction.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_relationship_ref](../models_1_0/invalid/3.4.5.1.map_components_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: relationship_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_role](../models_1_0/invalid/3.4.5.1.map_components_with_role.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_role.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: role. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_unit](../models_1_0/invalid/3.4.5.1.map_components_with_unit.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: unit```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: unit. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_units](../models_1_0/invalid/3.4.5.1.map_components_with_units.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: units. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_variable](../models_1_0/invalid/3.4.5.1.map_components_with_variable.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: variable. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.5.1.map_components_with_variable_ref](../models_1_0/invalid/3.4.5.1.map_components_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element map_components has extra content: variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_variable_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_components has extra content: variable_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.5.1.map_components_with_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 3.4.5.2

[3.4.5.2.map_components_component_1_nonexistent](../models_1_0/invalid/3.4.5.2.map_components_component_1_nonexistent.cellml): Error detected correctly.
* Expected: ```c$x```
* Output: ```'c$x'```


---

##### 3.4.5.3

[3.4.5.3.map_components_component_2_nonexistent](../models_1_0/invalid/3.4.5.3.map_components_component_2_nonexistent.cellml): Error detected correctly.
* Expected: ```c$x```
* Output: ```'c$x'```


---

##### 3.4.5.4

[3.4.5.4.map_components_component_1_equals_2](../models_1_0/invalid/3.4.5.4.map_components_component_1_equals_2.cellml): Error detected correctly.
* Expected: ```Target already assigned to```
* Output: ```Target already assigned to A$a before assignment to A$a```

🔵 [3.4.5.4.map_components_duplicate](../models_1_0/invalid/3.4.5.4.map_components_duplicate.cellml): **Error not detected.**

🔵 [3.4.5.4.map_components_duplicate_mirrored](../models_1_0/invalid/3.4.5.4.map_components_duplicate_mirrored.cellml): **Error not detected.**


---

##### 3.4.6.1

[3.4.6.1.map_variables_duplicate_1](../models_1_0/duplicate_connections/3.4.6.1.map_variables_duplicate_1.cellml): Error detected correctly.
* Expected: ```Target already assigned```
* Output: ```Target already assigned to A$a before assignment to A$a```

[3.4.6.1.map_variables_duplicate_2](../models_1_0/duplicate_connections/3.4.6.1.map_variables_duplicate_2.cellml): Error detected correctly.
* Expected: ```Target already assigned```
* Output: ```Target already assigned to B$b before assignment to B$b```

[3.4.6.1.map_variables_variable_1_missing](../models_1_0/invalid/3.4.6.1.map_variables_variable_1_missing.cellml): Error detected correctly.
* Expected: ```Element map_variables failed to validate attributes```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_variable_1_missing.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element map_variables failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_variable_1_missing.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_variable_1_missing.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_variable_1_missing.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_variable_2_missing](../models_1_0/invalid/3.4.6.1.map_variables_variable_2_missing.cellml): Error detected correctly.
* Expected: ```Element map_variables failed to validate attributes```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_variable_2_missing.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element map_variables failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_variable_2_missing.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_variable_2_missing.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_variable_2_missing.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_component](../models_1_0/invalid/3.4.6.1.map_variables_with_component.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_component.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: component. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_component_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: component_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_component_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: component_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_connection](../models_1_0/invalid/3.4.6.1.map_variables_with_connection.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_connection.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: connection. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_connection.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_connection.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_connection.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_group](../models_1_0/invalid/3.4.6.1.map_variables_with_group.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: group```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_group.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: group. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_map_components](../models_1_0/invalid/3.4.6.1.map_variables_with_map_components.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_map_components.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: map_components. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_map_variables](../models_1_0/invalid/3.4.6.1.map_variables_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_map_variables.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: map_variables. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_math](../models_1_0/invalid/3.4.6.1.map_variables_with_math.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: math```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_math.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: math. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_model](../models_1_0/invalid/3.4.6.1.map_variables_with_model.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_model.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: model. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_reaction](../models_1_0/invalid/3.4.6.1.map_variables_with_reaction.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_reaction.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: reaction. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_reaction.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_reaction.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_reaction.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_relationship_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_relationship_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: relationship_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_role](../models_1_0/invalid/3.4.6.1.map_variables_with_role.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_role.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: role. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_unit](../models_1_0/invalid/3.4.6.1.map_variables_with_unit.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: unit```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_unit.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: unit. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_units](../models_1_0/invalid/3.4.6.1.map_variables_with_units.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_units.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: units. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_variable](../models_1_0/invalid/3.4.6.1.map_variables_with_variable.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_variable.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: variable. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[3.4.6.1.map_variables_with_variable_ref](../models_1_0/invalid/3.4.6.1.map_variables_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element map_variables has extra content: variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_variable_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element map_variables has extra content: variable_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/3.4.6.1.map_variables_with_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 3.4.6.2

[3.4.6.2.map_variables_variable_1_nonexistent](../models_1_0/invalid/3.4.6.2.map_variables_variable_1_nonexistent.cellml): Error detected correctly.
* Expected: ```c1$a```
* Output: ```'c1$a'```


---

##### 3.4.6.3

[3.4.6.3.map_variables_variable_2_nonexistent](../models_1_0/invalid/3.4.6.3.map_variables_variable_2_nonexistent.cellml): Error detected correctly.
* Expected: ```c2$b```
* Output: ```'c2$b'```


---

##### 3.4.6.4

[3.4.6.4.map_variables_chain_down](../models_1_0/valid/3.4.6.4.map_variables_chain_down.cellml): Valid file passed validation.

[3.4.6.4.map_variables_chain_up](../models_1_0/valid/3.4.6.4.map_variables_chain_up.cellml): Valid file passed validation.

[3.4.6.4.map_variables_child_multiple_out_1](../models_1_0/invalid/3.4.6.4.map_variables_child_multiple_out_1.cellml): Error detected correctly.
* Expected: ```Target already assigned to```
* Output: ```Target already assigned to B$a before assignment to B$b```

[3.4.6.4.map_variables_child_multiple_out_2](../models_1_0/invalid/3.4.6.4.map_variables_child_multiple_out_2.cellml): Error detected correctly.
* Expected: ```Target already assigned to```
* Output: ```Target already assigned to B$a before assignment to C$b```

[3.4.6.4.map_variables_child_out_to_out_1](../models_1_0/invalid/3.4.6.4.map_variables_child_out_to_out_1.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (B, a)```

[3.4.6.4.map_variables_child_out_to_out_2](../models_1_0/invalid/3.4.6.4.map_variables_child_out_to_out_2.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (B, a)```

[3.4.6.4.map_variables_child_private_in](../models_1_0/invalid/3.4.6.4.map_variables_child_private_in.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (B, a)```

[3.4.6.4.map_variables_child_private_out](../models_1_0/invalid/3.4.6.4.map_variables_child_private_out.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (B, a)```

[3.4.6.4.map_variables_hidden_aunt_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_aunt_1.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, q) - (BB, s)```

[3.4.6.4.map_variables_hidden_aunt_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_aunt_2.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, q) - (BB, s)```

[3.4.6.4.map_variables_hidden_cousins_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_1.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (AA, a) - (BB, a)```

[3.4.6.4.map_variables_hidden_cousins_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_2.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (AA, a) - (BB, a)```

🔵 [3.4.6.4.map_variables_hidden_cousins_3](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_3.cellml): **Error not detected.**

[3.4.6.4.map_variables_hidden_cousins_4](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_4.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (AA, a) - (BB, a)```

[3.4.6.4.map_variables_hidden_grandchild_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandchild_1.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (C, a)```

[3.4.6.4.map_variables_hidden_grandchild_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandchild_2.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (C, a)```

[3.4.6.4.map_variables_hidden_grandparent_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandparent_1.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (C, a)```

[3.4.6.4.map_variables_hidden_grandparent_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandparent_2.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (C, a)```

[3.4.6.4.map_variables_hidden_niece_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_niece_1.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, q) - (BB, s)```

[3.4.6.4.map_variables_hidden_niece_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_niece_2.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, q) - (BB, s)```

[3.4.6.4.map_variables_nested_sibling_connection](../models_1_0/valid/3.4.6.4.map_variables_nested_sibling_connection.cellml): Valid file passed validation.

🔵 [3.4.6.4.map_variables_nested_sibling_private_in](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_in.cellml): **Error not detected.**

[3.4.6.4.map_variables_nested_sibling_private_in_and_out](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_in_and_out.cellml): Error detected correctly.
* Expected: ```Target already assigned```
* Output: ```Target already assigned to B$a before assignment to None```

[3.4.6.4.map_variables_nested_sibling_private_out](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_out.cellml): Error detected correctly.
* Expected: ```Target already assigned```
* Output: ```Target already assigned to B$a before assignment to None```

[3.4.6.4.map_variables_parent_connection_1](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_connection_2](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_in_to_in_1](../models_1_0/invalid/3.4.6.4.map_variables_parent_in_to_in_1.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (B, a)```

[3.4.6.4.map_variables_parent_in_to_in_2](../models_1_0/invalid/3.4.6.4.map_variables_parent_in_to_in_2.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (B, a)```

[3.4.6.4.map_variables_parent_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_multiple_out](../models_1_0/invalid/3.4.6.4.map_variables_parent_multiple_out.cellml): Error detected correctly.
* Expected: ```Target already assigned```
* Output: ```Target already assigned to A$a before assignment to A$b```

[3.4.6.4.map_variables_parent_out_to_out_1](../models_1_0/invalid/3.4.6.4.map_variables_parent_out_to_out_1.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (B, a)```

[3.4.6.4.map_variables_parent_out_to_out_2](../models_1_0/invalid/3.4.6.4.map_variables_parent_out_to_out_2.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (B, a)```

[3.4.6.4.map_variables_parent_public_in](../models_1_0/invalid/3.4.6.4.map_variables_parent_public_in.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (B, a)```

[3.4.6.4.map_variables_parent_public_out](../models_1_0/invalid/3.4.6.4.map_variables_parent_public_out.cellml): Error detected correctly.
* Expected: ```Cannot determine the source & target for connection```
* Output: ```Cannot determine the source & target for connection (A, a) - (B, a)```

[3.4.6.4.map_variables_sibling_connection_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_connection_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_connection_3](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_3.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_in_to_in](../models_1_0/invalid/3.4.6.4.map_variables_sibling_in_to_in.cellml): Error detected correctly.
* Expected: ```Unable to add connections to the model```
* Output: ```Unable to add connections to the model```

[3.4.6.4.map_variables_sibling_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_multiple_out_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_multiple_out_1.cellml): Error detected correctly.
* Expected: ```Target already assigned```
* Output: ```Target already assigned to A$a before assignment to A$b```

[3.4.6.4.map_variables_sibling_multiple_out_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_multiple_out_2.cellml): Error detected correctly.
* Expected: ```Target already assigned```
* Output: ```Target already assigned to A$a before assignment to B$a```

[3.4.6.4.map_variables_sibling_mutual](../models_1_0/valid/3.4.6.4.map_variables_sibling_mutual.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_out_to_out](../models_1_0/invalid/3.4.6.4.map_variables_sibling_out_to_out.cellml): Error detected correctly.
* Expected: ```Target already assigned```
* Output: ```Target already assigned to B$a before assignment to A$a```

🔵 [3.4.6.4.map_variables_sibling_private_in_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_1.cellml): **Error not detected.**

[3.4.6.4.map_variables_sibling_private_in_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_2.cellml): Error detected correctly.
* Expected: ```Target already assigned```
* Output: ```Target already assigned to B$a before assignment to None```

🔵 [3.4.6.4.map_variables_sibling_private_in_and_out](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_and_out.cellml): **Error not detected.**

🔵 [3.4.6.4.map_variables_sibling_private_out_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_out_1.cellml): **Error not detected.**

[3.4.6.4.map_variables_sibling_private_out_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_out_2.cellml): Error detected correctly.
* Expected: ```Unable to add connections```
* Output: ```Unable to add connections to the model```

[3.4.6.4.map_variables_talking_aunt](../models_1_0/valid/3.4.6.4.map_variables_talking_aunt.cellml): Valid file passed validation.

[3.4.6.4.map_variables_talking_cousins](../models_1_0/valid/3.4.6.4.map_variables_talking_cousins.cellml): Valid file passed validation.

[3.4.6.4.map_variables_talking_niece](../models_1_0/valid/3.4.6.4.map_variables_talking_niece.cellml): Valid file passed validation.


---

## 4. Mathematics

### 4.2

[4.2.3_1.mathml_basics](../models_1_0/valid/4.2.3_1.mathml_basics.cellml): Valid file passed validation.

🔴 [4.2.3_2.1.mathml_numbers_real](../models_1_0/numbers/4.2.3_2.1.mathml_numbers_real.cellml): **Valid file failed validation.**
* Output: ```Unimplemented type attribute for <cn>: real```

🔴 [4.2.3_2.2.mathml_numbers_integer](../models_1_0/numbers/4.2.3_2.2.mathml_numbers_integer.cellml): **Valid file failed validation.**
* Output: ```Unimplemented type attribute for <cn>: integer```

🔴 [4.2.3_2.3.mathml_numbers_real_base](../models_1_0/numbers/4.2.3_2.3.mathml_numbers_real_base.cellml): **Valid file failed validation.**
* Output: ```Unimplemented type attribute for <cn>: real```

🔴 [4.2.3_2.4.mathml_numbers_integer_base](../models_1_0/numbers/4.2.3_2.4.mathml_numbers_integer_base.cellml): **Valid file failed validation.**
* Output: ```Unimplemented type attribute for <cn>: integer```

[4.2.3_2.5.mathml_numbers_e_notation](../models_1_0/numbers/4.2.3_2.5.mathml_numbers_e_notation.cellml): Valid file passed validation.

🔴 [4.2.3_2.6.mathml_numbers_rational](../models_1_0/numbers/4.2.3_2.6.mathml_numbers_rational.cellml): **Valid file failed validation.**
* Output: ```Unimplemented type attribute for <cn>: rational```

[4.2.3_3.1_mathml_arithmetic_binary](../models_1_0/valid/4.2.3_3.1_mathml_arithmetic_binary.cellml): Valid file passed validation.

[4.2.3_3.2_mathml_arithmetic_n_ary](../models_1_0/valid/4.2.3_3.2_mathml_arithmetic_n_ary.cellml): Valid file passed validation.

[4.2.3_3.2_mathml_arithmetic_unary](../models_1_0/valid/4.2.3_3.2_mathml_arithmetic_unary.cellml): Valid file passed validation.

[4.2.3_4.1_mathml_functions_basic](../models_1_0/valid/4.2.3_4.1_mathml_functions_basic.cellml): Valid file passed validation.

[4.2.3_4.2_mathml_functions_non_smooth](../models_1_0/valid/4.2.3_4.2_mathml_functions_non_smooth.cellml): Valid file passed validation.

🔴 [4.2.3_4.3_mathml_functions_factorial](../models_1_0/valid/4.2.3_4.3_mathml_functions_factorial.cellml): **Valid file failed validation.**
* Output: ```No handler for element <factorial>```

[4.2.3_4.4_mathml_functions_trig](../models_1_0/valid/4.2.3_4.4_mathml_functions_trig.cellml): Valid file passed validation.

[4.2.3_4.5_mathml_functions_trig_hyperbolic](../models_1_0/valid/4.2.3_4.5_mathml_functions_trig_hyperbolic.cellml): Valid file passed validation.

[4.2.3_4.6_mathml_functions_trig_redundant](../models_1_0/valid/4.2.3_4.6_mathml_functions_trig_redundant.cellml): Valid file passed validation.

[4.2.3_4.7_mathml_functions_trig_redundant_hyperbolic](../models_1_0/valid/4.2.3_4.7_mathml_functions_trig_redundant_hyperbolic.cellml): Valid file passed validation.

[4.2.3_5.1_mathml_derivatives](../models_1_0/valid/4.2.3_5.1_mathml_derivatives.cellml): Valid file passed validation.

🔴 [4.2.3_5.2_mathml_derivatives_degree](../models_1_0/valid/4.2.3_5.2_mathml_derivatives_degree.cellml): **Valid file failed validation.**
* Output: ```Equation LHS should be a derivative or variable, not 0```

[4.2.3_5.3_mathml_derivatives_with_units](../models_1_0/valid/4.2.3_5.3_mathml_derivatives_with_units.cellml): Valid file passed validation.

🔴 [4.2.3_5.4_mathml_derivatives_with_units_degree](../models_1_0/valid/4.2.3_5.4_mathml_derivatives_with_units_degree.cellml): **Valid file failed validation.**
* Output: ```Equation LHS should be a derivative or variable, not 0```

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

🔴 [4.2.3_7.3_mathml_nan_inf](../models_1_0/valid/4.2.3_7.3_mathml_nan_inf.cellml): **Valid file failed validation.**
* Output: ```The argument `equation` must be a sympy.Eq.```

🔴 [4.2.3_8.1_annotation](../models_1_0/valid/4.2.3_8.1_annotation.cellml): **Valid file failed validation.**
* Output: ```No handler for element <semantics>```

🔴 [4.2.3_8.2_annotation_xml](../models_1_0/valid/4.2.3_8.2_annotation_xml.cellml): **Valid file failed validation.**
* Output: ```'Unknown unit per_millisecond.'```


---

#### 4.4.1

[4.4.1.math_not_math_component](../models_1_0/invalid/4.4.1.math_not_math_component.cellml): Error detected correctly.
* Expected: ```Element component failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/4.4.1.math_not_math_component.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element math has extra content: apply. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element math in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/4.4.1.math_not_math_component.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/4.4.1.math_not_math_component.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[4.4.1.math_not_math_reaction](../models_1_0/invalid/4.4.1.math_not_math_reaction.cellml): Error detected correctly.
* Expected: ```Element role failed to validate content```
* Output: ```Invalid or unsupported CellML file. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element math in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/4.4.1.math_not_math_reaction.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element role failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/4.4.1.math_not_math_reaction.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/4.4.1.math_not_math_reaction.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element math has extra content: apply. /home/michael/dev/cellml/validation/models_1_0/invalid/4.4.1.math_not_math_reaction.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/4.4.1.math_not_math_reaction.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

#### 4.4.2

[4.4.2.ci_no_whitespace](../models_1_0/valid/4.4.2.ci_no_whitespace.cellml): Valid file passed validation.

[4.4.2.ci_non_local_aunt](../models_1_0/invalid/4.4.2.ci_non_local_aunt.cellml): Error detected correctly.
* Expected: ```not found in symbol dict```
* Output: ```AA$y not found in symbol dict```

[4.4.2.ci_non_local_child](../models_1_0/invalid/4.4.2.ci_non_local_child.cellml): Error detected correctly.
* Expected: ```not found in symbol dict```
* Output: ```A$y not found in symbol dict```

[4.4.2.ci_non_local_cousin](../models_1_0/invalid/4.4.2.ci_non_local_cousin.cellml): Error detected correctly.
* Expected: ```not found in symbol dict```
* Output: ```AA$y not found in symbol dict```

[4.4.2.ci_non_local_nested_sibling](../models_1_0/invalid/4.4.2.ci_non_local_nested_sibling.cellml): Error detected correctly.
* Expected: ```not found in symbol dict```
* Output: ```B$y not found in symbol dict```

[4.4.2.ci_non_local_niece](../models_1_0/invalid/4.4.2.ci_non_local_niece.cellml): Error detected correctly.
* Expected: ```not found in symbol dict```
* Output: ```B$y not found in symbol dict```

[4.4.2.ci_non_local_parent](../models_1_0/invalid/4.4.2.ci_non_local_parent.cellml): Error detected correctly.
* Expected: ```not found in symbol dict```
* Output: ```AA$y not found in symbol dict```

[4.4.2.ci_non_local_sibling](../models_1_0/invalid/4.4.2.ci_non_local_sibling.cellml): Error detected correctly.
* Expected: ```not found in symbol dict```
* Output: ```B$y not found in symbol dict```

[4.4.2.ci_nonexistent](../models_1_0/invalid/4.4.2.ci_nonexistent.cellml): Error detected correctly.
* Expected: ```not found in symbol dict```
* Output: ```A$y not found in symbol dict```

[4.4.2.ci_whitespace_1](../models_1_0/valid/4.4.2.ci_whitespace_1.cellml): Valid file passed validation.

[4.4.2.ci_whitespace_2](../models_1_0/valid/4.4.2.ci_whitespace_2.cellml): Valid file passed validation.

[4.4.2.ci_whitespace_3](../models_1_0/valid/4.4.2.ci_whitespace_3.cellml): Valid file passed validation.


---

##### 4.4.3.1

🔴 [4.4.3.1.cn_component_units](../models_1_0/valid/4.4.3.1.cn_component_units.cellml): **Valid file failed validation.**
* Output: ```'Unknown unit wooster.'```

[4.4.3.1.cn_model_units](../models_1_0/valid/4.4.3.1.cn_model_units.cellml): Valid file passed validation.

[4.4.3.1.cn_predefined_units](../models_1_0/valid/4.4.3.1.cn_predefined_units.cellml): Valid file passed validation.

[4.4.3.1.cn_units_missing](../models_1_0/invalid/4.4.3.1.cn_units_missing.cellml): Error detected correctly.
* Expected: ```Element component failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/4.4.3.1.cn_units_missing.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element math has extra content: apply. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element math in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/4.4.3.1.cn_units_missing.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/4.4.3.1.cn_units_missing.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 4.4.3.2

[4.4.3.2.cn_units_nonexistent_1](../models_1_0/invalid/4.4.3.2.cn_units_nonexistent_1.cellml): Error detected correctly.
* Expected: ```Unknown unit```
* Output: ```'Unknown unit wooster.'```

[4.4.3.2.cn_units_nonexistent_2](../models_1_0/invalid/4.4.3.2.cn_units_nonexistent_2.cellml): Error detected correctly.
* Expected: ```Defining units inside components is not supported```
* Output: ```Defining units inside components is not supported (found in component B).```

🔶 [4.4.3.2.cn_units_parent_component](../models_1_0/invalid/4.4.3.2.cn_units_parent_component.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Defining units inside components is not supported (found in component A).```


---

#### 4.4.4

🔶 [4.4.4.dae_public_in](../models_1_0/invalid/4.4.4.dae_public_in.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Equation LHS should be a derivative or variable, not _b$x + _b$y```

[4.4.4.modify_nonexistent](../models_1_0/invalid/4.4.4.modify_nonexistent.cellml): Error detected correctly.
* Expected: ```A$x not found```
* Output: ```A$x not found in symbol dict```

🔵 [4.4.4.modify_private_in](../models_1_0/invalid/4.4.4.modify_private_in.cellml): **Error not detected.**

[4.4.4.modify_private_out](../models_1_0/valid/4.4.4.modify_private_out.cellml): Valid file passed validation.

🔵 [4.4.4.modify_public_in](../models_1_0/invalid/4.4.4.modify_public_in.cellml): **Error not detected.**

[4.4.4.modify_public_out](../models_1_0/valid/4.4.4.modify_public_out.cellml): Valid file passed validation.


---

#### 4.5.1

[4.5.1.ordering_not_significant](../models_1_0/valid/4.5.1.ordering_not_significant.cellml): Valid file passed validation.


---

🔴 [4.algebraic_model](../models_1_0/valid/4.algebraic_model.cellml): **Valid file failed validation.**
* Output: ```Equation LHS should be a derivative or variable, not _A$x + _A$y```

🔴 [4.algebraic_ode_model](../models_1_0/valid/4.algebraic_ode_model.cellml): **Valid file failed validation.**
* Output: ```Equation LHS should be a derivative or variable, not 2.0```

[4.math_and_initial_value](../models_1_0/invalid/4.math_and_initial_value.cellml): Error detected correctly.
* Expected: ```defined twice```
* Output: ```The variable A$x is defined twice (Eq(_A$x, _1) and Eq(_A$x, _1))```

[4.math_overdefined](../models_1_0/invalid/4.math_overdefined.cellml): Error detected correctly.
* Expected: ```defined twice```
* Output: ```The variable A$x is defined twice (Eq(_A$x, _1) and Eq(_A$x, _1))```

🔴 [4.overdefined_direct_and_direct](../models_1_0/overdefined/4.overdefined_direct_and_direct.cellml): **Valid file failed validation.**
* Output: ```The variable A$x is defined twice (Eq(_A$x, _-1) and Eq(_A$x, _1))```

🔴 [4.overdefined_direct_and_initial](../models_1_0/overdefined/4.overdefined_direct_and_initial.cellml): **Valid file failed validation.**
* Output: ```The variable A$x is defined twice (Eq(_A$x, _3) and Eq(_A$x, _2000))```

🔴 [4.overdefined_direct_and_ode](../models_1_0/overdefined/4.overdefined_direct_and_ode.cellml): **Valid file failed validation.**
* Output: ```The variable A$x is defined twice (Eq(Derivative(_A$x, _A$t), _0.001) and Eq(_A$x, _1))```

🔴 [4.overdefined_ode_and_ode](../models_1_0/overdefined/4.overdefined_ode_and_ode.cellml): **Valid file failed validation.**
* Output: ```The variable A$x is defined twice (Eq(Derivative(_A$x, _A$t), _2) and Eq(Derivative(_A$x, _A$t), _0.001))```


---

## 5. Units

#### 5.2.1

[5.2.1.units_ampere](../models_1_0/valid/5.2.1.units_ampere.cellml): Valid file passed validation.

[5.2.1.units_becquerel](../models_1_0/valid/5.2.1.units_becquerel.cellml): Valid file passed validation.

[5.2.1.units_candela](../models_1_0/valid/5.2.1.units_candela.cellml): Valid file passed validation.

🔴 [5.2.1.units_celsius](../models_1_0/valid/5.2.1.units_celsius.cellml): **Valid file failed validation.**
* Output: ```'Unit celsiusis not currently supported by cellmlmanip.'```

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

[5.2.2.unit_deca](../models_1_0/unit_deca/5.2.2.unit_deca.cellml): Error detected correctly.
* Expected: ```Invalid attribute prefix for element unit```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/unit_deca/5.2.2.unit_deca.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute prefix for element unit. /home/michael/dev/cellml/validation/models_1_0/unit_deca/5.2.2.unit_deca.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/unit_deca/5.2.2.unit_deca.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/unit_deca/5.2.2.unit_deca.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

#### 5.2.7

[5.2.7.unit_checking_aliases](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_aliases.cellml): Valid file passed validation.

[5.2.7.unit_checking_arithmetic](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_arithmetic.cellml): Valid file passed validation.

[5.2.7.unit_checking_comparisons](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_comparisons.cellml): Valid file passed validation.

[5.2.7.unit_checking_derivatives](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_derivatives.cellml): Valid file passed validation.

🔴 [5.2.7.unit_checking_derivatives_degree](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_derivatives_degree.cellml): **Valid file failed validation.**
* Output: ```Equation LHS should be a derivative or variable, not 0```

[5.2.7.unit_checking_dimensionless](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_dimensionless.cellml): Valid file passed validation.

🔴 [5.2.7.unit_checking_functions_factorial](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_functions_factorial.cellml): **Valid file failed validation.**
* Output: ```No handler for element <factorial>```

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

🔴 [5.2.7.unit_conversion_inconvertible_1](../models_1_0/unit_conversion_inconvertible/5.2.7.unit_conversion_inconvertible_1.cellml): **Valid file failed validation.**
* Output: ```Cannot convert from 'volt' ([length] ** 2 * [mass] / [current] / [time] ** 3) to 'meter' ([length])```

[5.2.7.unit_conversion_less_obvious](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_less_obvious.cellml): Valid file passed validation.

[5.2.7.unit_conversion_multiplier](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_multiplier.cellml): Valid file passed validation.

🔴 [5.2.7.unit_conversion_new_base_units](../models_1_0/unit_conversion_inconvertible/5.2.7.unit_conversion_new_base_units.cellml): **Valid file failed validation.**
* Output: ```Cannot convert from 'store372_wooster' ([store372_wooster]) to 'dimensionless' (dimensionless)```

[5.2.7.unit_conversion_offset](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_offset.cellml): Valid file passed validation.

[5.2.7.unit_conversion_prefix](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_prefix.cellml): Valid file passed validation.


---

##### 5.4.1.1

[5.4.1.1.units_base_units](../models_1_0/valid/5.4.1.1.units_base_units.cellml): Valid file passed validation.

[5.4.1.1.units_base_units_with_children](../models_1_0/invalid/5.4.1.1.units_base_units_with_children.cellml): Error detected correctly.
* Expected: ```Invalid attribute base_units for element units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_base_units_with_children.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute base_units for element units. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_base_units_with_children.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_empty_1](../models_1_0/units_empty/5.4.1.1.units_empty_1.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported CellML file```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/units_empty/5.4.1.1.units_empty_1.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element unit, got nothing. /home/michael/dev/cellml/validation/models_1_0/units_empty/5.4.1.1.units_empty_1.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/units_empty/5.4.1.1.units_empty_1.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/units_empty/5.4.1.1.units_empty_1.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_empty_2](../models_1_0/units_empty/5.4.1.1.units_empty_2.cellml): Error detected correctly.
* Expected: ```Invalid or unsupported CellML file```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/units_empty/5.4.1.1.units_empty_2.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element unit, got nothing. /home/michael/dev/cellml/validation/models_1_0/units_empty/5.4.1.1.units_empty_2.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/units_empty/5.4.1.1.units_empty_2.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/units_empty/5.4.1.1.units_empty_2.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/units_empty/5.4.1.1.units_empty_2.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_name_missing](../models_1_0/invalid/5.4.1.1.units_name_missing.cellml): Error detected correctly.
* Expected: ```Element units failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_name_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_name_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_name_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_component](../models_1_0/invalid/5.4.1.1.units_with_component.cellml): Error detected correctly.
* Expected: ```Element units has extra content: component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: component. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_component_ref](../models_1_0/invalid/5.4.1.1.units_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element units has extra content: component_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_component_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: component_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_connection](../models_1_0/invalid/5.4.1.1.units_with_connection.cellml): Error detected correctly.
* Expected: ```Element units has extra content: connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_connection.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: connection. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_connection.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_group](../models_1_0/invalid/5.4.1.1.units_with_group.cellml): Error detected correctly.
* Expected: ```Element units has extra content: group```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_group.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: group. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_map_components](../models_1_0/invalid/5.4.1.1.units_with_map_components.cellml): Error detected correctly.
* Expected: ```Element units has extra content: map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: map_components. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_map_variables](../models_1_0/invalid/5.4.1.1.units_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element units has extra content: map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_map_variables.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: map_variables. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_math](../models_1_0/invalid/5.4.1.1.units_with_math.cellml): Error detected correctly.
* Expected: ```Element units has extra content: math```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_math.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: math. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_math.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_model](../models_1_0/invalid/5.4.1.1.units_with_model.cellml): Error detected correctly.
* Expected: ```Element units has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: model. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_reaction](../models_1_0/invalid/5.4.1.1.units_with_reaction.cellml): Error detected correctly.
* Expected: ```Element units has extra content: reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_reaction.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: reaction. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_reaction.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_reaction.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_relationship_ref](../models_1_0/invalid/5.4.1.1.units_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element units has extra content: relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: relationship_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_role](../models_1_0/invalid/5.4.1.1.units_with_role.cellml): Error detected correctly.
* Expected: ```Element units has extra content: role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_role.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: role. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_unit_children](../models_1_0/valid/5.4.1.1.units_with_unit_children.cellml): Valid file passed validation.

[5.4.1.1.units_with_units](../models_1_0/invalid/5.4.1.1.units_with_units.cellml): Error detected correctly.
* Expected: ```Element units has extra content: units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: units. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_variable](../models_1_0/invalid/5.4.1.1.units_with_variable.cellml): Error detected correctly.
* Expected: ```Element units has extra content: variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_variable.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_variable.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_variable_ref](../models_1_0/invalid/5.4.1.1.units_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element units has extra content: variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_variable_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element units has extra content: variable_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_variable_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.1.units_with_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 5.4.1.2

🔶 [5.4.1.2.units_name_duplicate_1](../models_1_0/invalid/5.4.1.2.units_name_duplicate_1.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Cannot redefine unit <wooster>.```

🔶 [5.4.1.2.units_name_duplicate_2](../models_1_0/invalid/5.4.1.2.units_name_duplicate_2.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Defining units inside components is not supported (found in component A).```

[5.4.1.2.units_name_invalid](../models_1_0/invalid/5.4.1.2.units_name_invalid.cellml): Error detected correctly.
* Expected: ```Element units failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.2.units_name_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.2.units_name_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.2.units_name_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.2.units_name_predefined_ampere](../models_1_0/invalid/5.4.1.2.units_name_predefined_ampere.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <ampere>.```

[5.4.1.2.units_name_predefined_becquerel](../models_1_0/invalid/5.4.1.2.units_name_predefined_becquerel.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <becquerel>.```

[5.4.1.2.units_name_predefined_candela](../models_1_0/invalid/5.4.1.2.units_name_predefined_candela.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <candela>.```

[5.4.1.2.units_name_predefined_celsius](../models_1_0/invalid/5.4.1.2.units_name_predefined_celsius.cellml): Error detected correctly.
* Expected: ```Unit <celsius> is not currently```
* Output: ```Unit <celsius> is not currently supported by cellmlmanip.```

🔶 [5.4.1.2.units_name_predefined_component_ampere](../models_1_0/invalid/5.4.1.2.units_name_predefined_component_ampere.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Defining units inside components is not supported (found in component A).```

[5.4.1.2.units_name_predefined_coulomb](../models_1_0/invalid/5.4.1.2.units_name_predefined_coulomb.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <coulomb>.```

[5.4.1.2.units_name_predefined_dimensionless](../models_1_0/invalid/5.4.1.2.units_name_predefined_dimensionless.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML```
* Output: ```Cannot redefine CellML unit <dimensionless>.```

[5.4.1.2.units_name_predefined_farad](../models_1_0/invalid/5.4.1.2.units_name_predefined_farad.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <farad>.```

[5.4.1.2.units_name_predefined_gram](../models_1_0/invalid/5.4.1.2.units_name_predefined_gram.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <gram>.```

[5.4.1.2.units_name_predefined_gray](../models_1_0/invalid/5.4.1.2.units_name_predefined_gray.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <gray>.```

[5.4.1.2.units_name_predefined_henry](../models_1_0/invalid/5.4.1.2.units_name_predefined_henry.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <henry>.```

[5.4.1.2.units_name_predefined_hertz](../models_1_0/invalid/5.4.1.2.units_name_predefined_hertz.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <hertz>.```

[5.4.1.2.units_name_predefined_joule](../models_1_0/invalid/5.4.1.2.units_name_predefined_joule.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <joule>.```

[5.4.1.2.units_name_predefined_katal](../models_1_0/invalid/5.4.1.2.units_name_predefined_katal.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <katal>.```

[5.4.1.2.units_name_predefined_kelvin](../models_1_0/invalid/5.4.1.2.units_name_predefined_kelvin.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <kelvin>.```

[5.4.1.2.units_name_predefined_kilogram](../models_1_0/invalid/5.4.1.2.units_name_predefined_kilogram.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <kilogram>.```

[5.4.1.2.units_name_predefined_liter](../models_1_0/invalid/5.4.1.2.units_name_predefined_liter.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <liter>.```

[5.4.1.2.units_name_predefined_litre](../models_1_0/invalid/5.4.1.2.units_name_predefined_litre.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <litre>.```

[5.4.1.2.units_name_predefined_lumen](../models_1_0/invalid/5.4.1.2.units_name_predefined_lumen.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <lumen>.```

[5.4.1.2.units_name_predefined_lux](../models_1_0/invalid/5.4.1.2.units_name_predefined_lux.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <lux>.```

[5.4.1.2.units_name_predefined_meter](../models_1_0/invalid/5.4.1.2.units_name_predefined_meter.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <meter>.```

[5.4.1.2.units_name_predefined_metre](../models_1_0/invalid/5.4.1.2.units_name_predefined_metre.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <metre>.```

[5.4.1.2.units_name_predefined_mole](../models_1_0/invalid/5.4.1.2.units_name_predefined_mole.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <mole>.```

[5.4.1.2.units_name_predefined_newton](../models_1_0/invalid/5.4.1.2.units_name_predefined_newton.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <newton>.```

[5.4.1.2.units_name_predefined_ohm](../models_1_0/invalid/5.4.1.2.units_name_predefined_ohm.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <ohm>.```

[5.4.1.2.units_name_predefined_pascal](../models_1_0/invalid/5.4.1.2.units_name_predefined_pascal.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <pascal>.```

[5.4.1.2.units_name_predefined_radian](../models_1_0/invalid/5.4.1.2.units_name_predefined_radian.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <radian>.```

[5.4.1.2.units_name_predefined_second](../models_1_0/invalid/5.4.1.2.units_name_predefined_second.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <second>.```

[5.4.1.2.units_name_predefined_siemens](../models_1_0/invalid/5.4.1.2.units_name_predefined_siemens.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <siemens>.```

[5.4.1.2.units_name_predefined_sievert](../models_1_0/invalid/5.4.1.2.units_name_predefined_sievert.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <sievert>.```

[5.4.1.2.units_name_predefined_steradian](../models_1_0/invalid/5.4.1.2.units_name_predefined_steradian.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <steradian>.```

[5.4.1.2.units_name_predefined_tesla](../models_1_0/invalid/5.4.1.2.units_name_predefined_tesla.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <tesla>.```

[5.4.1.2.units_name_predefined_volt](../models_1_0/invalid/5.4.1.2.units_name_predefined_volt.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <volt>.```

[5.4.1.2.units_name_predefined_watt](../models_1_0/invalid/5.4.1.2.units_name_predefined_watt.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <watt>.```

[5.4.1.2.units_name_predefined_weber](../models_1_0/invalid/5.4.1.2.units_name_predefined_weber.cellml): Error detected correctly.
* Expected: ```Cannot redefine CellML unit```
* Output: ```Cannot redefine CellML unit <weber>.```

🔴 [5.4.1.2.units_names_and_other_names](../models_1_0/valid/5.4.1.2.units_names_and_other_names.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component units_names_and_other_names).```

🔴 [5.4.1.2.units_shadowing_1](../models_1_0/valid/5.4.1.2.units_shadowing_1.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

🔴 [5.4.1.2.units_shadowing_2](../models_1_0/valid/5.4.1.2.units_shadowing_2.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```


---

##### 5.4.1.3

[5.4.1.3.units_base_units_invalid](../models_1_0/invalid/5.4.1.3.units_base_units_invalid.cellml): Error detected correctly.
* Expected: ```Invalid attribute base_units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.3.units_base_units_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute base_units for element units. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.1.3.units_base_units_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 5.4.2.1

[5.4.2.1.unit_offset_non_zero](../models_1_0/valid/5.4.2.1.unit_offset_non_zero.cellml): Valid file passed validation.

[5.4.2.1.unit_offset_zero](../models_1_0/valid/5.4.2.1.unit_offset_zero.cellml): Valid file passed validation.

[5.4.2.1.unit_prefix_exponent_multiplier](../models_1_0/valid/5.4.2.1.unit_prefix_exponent_multiplier.cellml): Valid file passed validation.

[5.4.2.1.unit_prefix_exponent_multiplier_huge](../models_1_0/valid/5.4.2.1.unit_prefix_exponent_multiplier_huge.cellml): Valid file passed validation.

[5.4.2.1.unit_units_missing](../models_1_0/invalid/5.4.2.1.unit_units_missing.cellml): Error detected correctly.
* Expected: ```Element unit failed to validate attributes```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_units_missing.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element unit failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_units_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_units_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_units_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_component](../models_1_0/invalid/5.4.2.1.unit_with_component.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: component. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_component_ref](../models_1_0/invalid/5.4.2.1.unit_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: component_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_component_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: component_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_connection](../models_1_0/invalid/5.4.2.1.unit_with_connection.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_connection.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: connection. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_connection.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_connection.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_connection.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_group](../models_1_0/invalid/5.4.2.1.unit_with_group.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: group```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_group.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: group. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_map_components](../models_1_0/invalid/5.4.2.1.unit_with_map_components.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: map_components. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_map_variables](../models_1_0/invalid/5.4.2.1.unit_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_map_variables.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: map_variables. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_math](../models_1_0/invalid/5.4.2.1.unit_with_math.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: math```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_math.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: math. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_model](../models_1_0/invalid/5.4.2.1.unit_with_model.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: model. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_reaction](../models_1_0/invalid/5.4.2.1.unit_with_reaction.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_reaction.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: reaction. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_reaction.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_reaction.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_reaction.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_reaction.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_relationship_ref](../models_1_0/invalid/5.4.2.1.unit_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: relationship_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_role](../models_1_0/invalid/5.4.2.1.unit_with_role.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_role.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: role. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_unit](../models_1_0/invalid/5.4.2.1.unit_with_unit.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: unit```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: unit. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_units](../models_1_0/invalid/5.4.2.1.unit_with_units.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: units. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_variable](../models_1_0/invalid/5.4.2.1.unit_with_variable.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_variable.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: variable. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_variable.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_variable.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_variable.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.1.unit_with_variable_ref](../models_1_0/invalid/5.4.2.1.unit_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element unit has extra content: variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_variable_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element unit has extra content: variable_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_variable_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_variable_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_variable_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.1.unit_with_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 5.4.2.2

🔶 [5.4.2.2.unit_cycle_1](../models_1_0/invalid/5.4.2.2.unit_cycle_1.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```unit cycle```
* Output: ```Running test causes infinite loop```

🔶 [5.4.2.2.unit_cycle_2](../models_1_0/invalid/5.4.2.2.unit_cycle_2.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```unit cycle```
* Output: ```Running test causes infinite loop```

🔶 [5.4.2.2.unit_cycle_3](../models_1_0/invalid/5.4.2.2.unit_cycle_3.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```unit cycle```
* Output: ```Running test causes infinite loop```

🔶 [5.4.2.2.unit_units_invalid](../models_1_0/invalid/5.4.2.2.unit_units_invalid.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```unit cycle```
* Output: ```Running test causes infinite loop```

🔴 [5.4.2.2.unit_units_local_1](../models_1_0/valid/5.4.2.2.unit_units_local_1.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

🔴 [5.4.2.2.unit_units_local_2](../models_1_0/valid/5.4.2.2.unit_units_local_2.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

[5.4.2.2.unit_units_local_3](../models_1_0/valid/5.4.2.2.unit_units_local_3.cellml): Valid file passed validation.

🔴 [5.4.2.2.unit_units_local_4](../models_1_0/valid/5.4.2.2.unit_units_local_4.cellml): **Valid file failed validation.**
* Output: ```'Unknown unit meter_per_second.'```


---

##### 5.4.2.3

[5.4.2.3.unit_prefix_integer](../models_1_0/valid/5.4.2.3.unit_prefix_integer.cellml): Valid file passed validation.

[5.4.2.3.unit_prefix_named](../models_1_0/valid/5.4.2.3.unit_prefix_named.cellml): Valid file passed validation.

[5.4.2.3.unit_prefix_real](../models_1_0/invalid/5.4.2.3.unit_prefix_real.cellml): Error detected correctly.
* Expected: ```Invalid attribute prefix```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.3.unit_prefix_real.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute prefix for element unit. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.3.unit_prefix_real.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.3.unit_prefix_real.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.3.unit_prefix_real.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.3.unit_prefix_real_int](../models_1_0/invalid/5.4.2.3.unit_prefix_real_int.cellml): Error detected correctly.
* Expected: ```Invalid attribute prefix```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.3.unit_prefix_real_int.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute prefix for element unit. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.3.unit_prefix_real_int.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.3.unit_prefix_real_int.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.3.unit_prefix_real_int.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

🔶 [5.4.2.3.unit_prefix_spaces](../models_1_0/invalid/5.4.2.3.unit_prefix_spaces.cellml): **Invalid file failed for unexpected reason.**
* Output: ```'e' is not defined in the unit registry```

[5.4.2.3.unit_prefix_unknown](../models_1_0/invalid/5.4.2.3.unit_prefix_unknown.cellml): Error detected correctly.
* Expected: ```Invalid attribute prefix```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.3.unit_prefix_unknown.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute prefix for element unit. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.3.unit_prefix_unknown.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.3.unit_prefix_unknown.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.3.unit_prefix_unknown.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 5.4.2.4

[5.4.2.4.unit_exponent_invalid](../models_1_0/invalid/5.4.2.4.unit_exponent_invalid.cellml): Error detected correctly.
* Expected: ```Invalid attribute exponent```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.4.unit_exponent_invalid.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute exponent for element unit. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.4.unit_exponent_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.4.unit_exponent_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.4.unit_exponent_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 5.4.2.5

[5.4.2.5.unit_multiplier_invalid](../models_1_0/invalid/5.4.2.5.unit_multiplier_invalid.cellml): Error detected correctly.
* Expected: ```Invalid attribute multiplier```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.5.unit_multiplier_invalid.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute multiplier for element unit. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.5.unit_multiplier_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.5.unit_multiplier_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.5.unit_multiplier_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 5.4.2.6

[5.4.2.6.unit_offset_invalid](../models_1_0/invalid/5.4.2.6.unit_offset_invalid.cellml): Error detected correctly.
* Expected: ```Invalid attribute offset```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.6.unit_offset_invalid.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute offset for element unit. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.6.unit_offset_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.6.unit_offset_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.6.unit_offset_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 5.4.2.7

[5.4.2.7.unit_offset_and_exponent](../models_1_0/invalid/5.4.2.7.unit_offset_and_exponent.cellml): Error detected correctly.
* Expected: ```Invalid attribute offset```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.7.unit_offset_and_exponent.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute offset for element unit. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.7.unit_offset_and_exponent.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute exponent for element unit. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.7.unit_offset_and_exponent.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.7.unit_offset_and_exponent.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.7.unit_offset_and_exponent.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.7.unit_offset_and_siblings_1](../models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_1.cellml): Error detected correctly.
* Expected: ```Extra element unit```
* Output: ```Invalid or unsupported CellML file. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element unit in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.2.7.unit_offset_and_siblings_2](../models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_2.cellml): Error detected correctly.
* Expected: ```Extra element unit```
* Output: ```Invalid or unsupported CellML file. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element unit in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_2.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_2.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_2.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

🔴 [5.4.2.7.unit_offset_non_zero_and_exponent_one](../models_1_0/valid/5.4.2.7.unit_offset_non_zero_and_exponent_one.cellml): **Valid file failed validation.**
* Output: ```'units'```

[5.4.2.7.unit_offset_zero_and_exponent](../models_1_0/valid/5.4.2.7.unit_offset_zero_and_exponent.cellml): Valid file passed validation.

[5.4.2.7.unit_offset_zero_and_siblings](../models_1_0/valid/5.4.2.7.unit_offset_zero_and_siblings.cellml): Valid file passed validation.


---

#### 5.5.2

🔴 [5.5.2.boolean_arithmetic_divide](../models_1_0/booleans/5.5.2.boolean_arithmetic_divide.cellml): **Valid file failed validation.**
* Output: ```BooleanAtom not allowed in this context.```

🔴 [5.5.2.boolean_arithmetic_minus](../models_1_0/booleans/5.5.2.boolean_arithmetic_minus.cellml): **Valid file failed validation.**
* Output: ```BooleanAtom not allowed in this context.```

[5.5.2.boolean_arithmetic_plus](../models_1_0/booleans/5.5.2.boolean_arithmetic_plus.cellml): Valid file passed validation.

🔴 [5.5.2.boolean_arithmetic_power_1](../models_1_0/booleans/5.5.2.boolean_arithmetic_power_1.cellml): **Valid file failed validation.**
* Output: ```BooleanAtom not allowed in this context.```

🔴 [5.5.2.boolean_arithmetic_power_2](../models_1_0/booleans/5.5.2.boolean_arithmetic_power_2.cellml): **Valid file failed validation.**
* Output: ```BooleanAtom not allowed in this context.```

🔴 [5.5.2.boolean_arithmetic_root_1](../models_1_0/booleans/5.5.2.boolean_arithmetic_root_1.cellml): **Valid file failed validation.**
* Output: ```BooleanAtom not allowed in this context.```

🔴 [5.5.2.boolean_arithmetic_root_2](../models_1_0/booleans/5.5.2.boolean_arithmetic_root_2.cellml): **Valid file failed validation.**
* Output: ```BooleanAtom not allowed in this context.```

🔴 [5.5.2.boolean_arithmetic_times](../models_1_0/booleans/5.5.2.boolean_arithmetic_times.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'as_base_exp'```

[5.5.2.boolean_compare_eq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_eq_operand_error.cellml): Valid file passed validation.

🔴 [5.5.2.boolean_compare_geq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_geq_operand_error.cellml): **Valid file failed validation.**
* Output: ```Can only compare inequalities with Expr```

🔴 [5.5.2.boolean_compare_gt_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_gt_operand_error.cellml): **Valid file failed validation.**
* Output: ```Can only compare inequalities with Expr```

🔴 [5.5.2.boolean_compare_leq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_leq_operand_error.cellml): **Valid file failed validation.**
* Output: ```Can only compare inequalities with Expr```

🔴 [5.5.2.boolean_compare_lt_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_lt_operand_error.cellml): **Valid file failed validation.**
* Output: ```Can only compare inequalities with Expr```

[5.5.2.boolean_compare_neq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_neq_operand_error.cellml): Valid file passed validation.

🔴 [5.5.2.boolean_derivatives_1](../models_1_0/booleans/5.5.2.boolean_derivatives_1.cellml): **Valid file failed validation.**
* Output: ```The argument `equation` must be a sympy.Eq.```

🔴 [5.5.2.boolean_derivatives_2](../models_1_0/booleans/5.5.2.boolean_derivatives_2.cellml): **Valid file failed validation.**
* Output: ```Equation LHS should be a derivative or variable, not 0```

🔴 [5.5.2.boolean_function_abs](../models_1_0/booleans/5.5.2.boolean_function_abs.cellml): **Valid file failed validation.**
* Output: ```Bad argument type for Abs(): <class 'sympy.logic.boolalg.BooleanTrue'>```

🔴 [5.5.2.boolean_function_ceiling](../models_1_0/booleans/5.5.2.boolean_function_ceiling.cellml): **Valid file failed validation.**
* Output: ```bad operand type for unary -: 'BooleanTrue'```

[5.5.2.boolean_function_exp](../models_1_0/booleans/5.5.2.boolean_function_exp.cellml): Valid file passed validation.

🔴 [5.5.2.boolean_function_factorial](../models_1_0/booleans/5.5.2.boolean_function_factorial.cellml): **Valid file failed validation.**
* Output: ```No handler for element <factorial>```

🔴 [5.5.2.boolean_function_floor](../models_1_0/booleans/5.5.2.boolean_function_floor.cellml): **Valid file failed validation.**
* Output: ```bad operand type for unary -: 'BooleanTrue'```

🔴 [5.5.2.boolean_function_ln](../models_1_0/booleans/5.5.2.boolean_function_ln.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'as_coefficient'```

🔴 [5.5.2.boolean_function_log_1](../models_1_0/booleans/5.5.2.boolean_function_log_1.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'as_coefficient'```

🔴 [5.5.2.boolean_function_log_2](../models_1_0/booleans/5.5.2.boolean_function_log_2.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'as_coefficient'```

[5.5.2.boolean_logic_and_operand_error](../models_1_0/booleans/5.5.2.boolean_logic_and_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_logic_not_operand_error](../models_1_0/booleans/5.5.2.boolean_logic_not_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_logic_or_operand_error](../models_1_0/booleans/5.5.2.boolean_logic_or_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_logic_xor_operand_error](../models_1_0/booleans/5.5.2.boolean_logic_xor_operand_error.cellml): Valid file passed validation.

🔴 [5.5.2.boolean_trig_arccos](../models_1_0/booleans/5.5.2.boolean_trig_arccos.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'could_extract_minus_sign'```

[5.5.2.boolean_trig_arccosh](../models_1_0/booleans/5.5.2.boolean_trig_arccosh.cellml): Valid file passed validation.

🔴 [5.5.2.boolean_trig_arccot](../models_1_0/booleans/5.5.2.boolean_trig_arccot.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'could_extract_minus_sign'```

🔴 [5.5.2.boolean_trig_arccoth](../models_1_0/booleans/5.5.2.boolean_trig_arccoth.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'as_coefficient'```

🔴 [5.5.2.boolean_trig_arccsc](../models_1_0/booleans/5.5.2.boolean_trig_arccsc.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'could_extract_minus_sign'```

[5.5.2.boolean_trig_arccsch](../models_1_0/booleans/5.5.2.boolean_trig_arccsch.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arcsec](../models_1_0/booleans/5.5.2.boolean_trig_arcsec.cellml): Valid file passed validation.

[5.5.2.boolean_trig_arcsech](../models_1_0/booleans/5.5.2.boolean_trig_arcsech.cellml): Valid file passed validation.

🔴 [5.5.2.boolean_trig_arcsin](../models_1_0/booleans/5.5.2.boolean_trig_arcsin.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'could_extract_minus_sign'```

🔴 [5.5.2.boolean_trig_arcsinh](../models_1_0/booleans/5.5.2.boolean_trig_arcsinh.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'as_coefficient'```

🔴 [5.5.2.boolean_trig_arctan](../models_1_0/booleans/5.5.2.boolean_trig_arctan.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'could_extract_minus_sign'```

🔴 [5.5.2.boolean_trig_arctanh](../models_1_0/booleans/5.5.2.boolean_trig_arctanh.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'as_coefficient'```

🔴 [5.5.2.boolean_trig_cos](../models_1_0/booleans/5.5.2.boolean_trig_cos.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'could_extract_minus_sign'```

🔴 [5.5.2.boolean_trig_cosh](../models_1_0/booleans/5.5.2.boolean_trig_cosh.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'as_coefficient'```

🔴 [5.5.2.boolean_trig_cot](../models_1_0/booleans/5.5.2.boolean_trig_cot.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'could_extract_minus_sign'```

🔴 [5.5.2.boolean_trig_coth](../models_1_0/booleans/5.5.2.boolean_trig_coth.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'as_coefficient'```

🔴 [5.5.2.boolean_trig_csc](../models_1_0/booleans/5.5.2.boolean_trig_csc.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'could_extract_minus_sign'```

🔴 [5.5.2.boolean_trig_csch](../models_1_0/booleans/5.5.2.boolean_trig_csch.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'could_extract_minus_sign'```

🔴 [5.5.2.boolean_trig_sec](../models_1_0/booleans/5.5.2.boolean_trig_sec.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'could_extract_minus_sign'```

🔴 [5.5.2.boolean_trig_sech](../models_1_0/booleans/5.5.2.boolean_trig_sech.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'could_extract_minus_sign'```

🔴 [5.5.2.boolean_trig_sin](../models_1_0/booleans/5.5.2.boolean_trig_sin.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'could_extract_minus_sign'```

🔴 [5.5.2.boolean_trig_sinh](../models_1_0/booleans/5.5.2.boolean_trig_sinh.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'as_coefficient'```

🔴 [5.5.2.boolean_trig_tan](../models_1_0/booleans/5.5.2.boolean_trig_tan.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'could_extract_minus_sign'```

🔴 [5.5.2.boolean_trig_tanh](../models_1_0/booleans/5.5.2.boolean_trig_tanh.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'as_coefficient'```

[5.5.2.boolean_variable_1](../models_1_0/booleans/5.5.2.boolean_variable_1.cellml): Valid file passed validation.

[5.5.2.boolean_variable_2](../models_1_0/booleans/5.5.2.boolean_variable_2.cellml): Valid file passed validation.

[5.5.2.boolean_variable_3](../models_1_0/booleans/5.5.2.boolean_variable_3.cellml): Valid file passed validation.


---

## 6. Grouping

##### 6.4.1.1

[6.4.1.1.group_component_ref_missing_1](../models_1_0/invalid/6.4.1.1.group_component_ref_missing_1.cellml): Error detected correctly.
* Expected: ```Element group failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_component_ref_missing_1.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element relationship_ref, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_component_ref_missing_1.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_component_ref_missing_1.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_component_ref_missing_1.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_component_ref_missing_2](../models_1_0/invalid/6.4.1.1.group_component_ref_missing_2.cellml): Error detected correctly.
* Expected: ```Element group failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_component_ref_missing_2.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element relationship_ref, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_component_ref_missing_2.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_component_ref_missing_2.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_component_ref_missing_2.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_component_ref_multiple](../models_1_0/valid/6.4.1.1.group_component_ref_multiple.cellml): Valid file passed validation.

[6.4.1.1.group_component_ref_single](../models_1_0/valid/6.4.1.1.group_component_ref_single.cellml): Valid file passed validation.

[6.4.1.1.group_empty](../models_1_0/invalid/6.4.1.1.group_empty.cellml): Error detected correctly.
* Expected: ```Expecting an element relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_empty.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element relationship_ref, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_empty.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_empty.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_empty.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_only_extensions](../models_1_0/invalid/6.4.1.1.group_only_extensions.cellml): Error detected correctly.
* Expected: ```Expecting an element relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_only_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element relationship_ref, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_only_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_only_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_only_extensions.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_relationship_ref_missing_1](../models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_1.cellml): Error detected correctly.
* Expected: ```Expecting an element relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_1.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element relationship_ref, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_1.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_1.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_1.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_relationship_ref_missing_2](../models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_2.cellml): Error detected correctly.
* Expected: ```Expecting an element relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_2.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element relationship_ref, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_2.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_2.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_2.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_with_component](../models_1_0/invalid/6.4.1.1.group_with_component.cellml): Error detected correctly.
* Expected: ```Element group has extra content: component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_component.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: component. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_with_connection](../models_1_0/invalid/6.4.1.1.group_with_connection.cellml): Error detected correctly.
* Expected: ```Element group has extra content: connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_connection.cellml:17:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: connection. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_connection.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_with_group](../models_1_0/invalid/6.4.1.1.group_with_group.cellml): Error detected correctly.
* Expected: ```Element group has extra content: group```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_group.cellml:15:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: group. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_group.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_with_map_components](../models_1_0/invalid/6.4.1.1.group_with_map_components.cellml): Error detected correctly.
* Expected: ```Element group has extra content: map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_map_components.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: map_components. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_with_map_variables](../models_1_0/invalid/6.4.1.1.group_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element group has extra content: map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_map_variables.cellml:17:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: map_variables. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_map_variables.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_with_math](../models_1_0/invalid/6.4.1.1.group_with_math.cellml): Error detected correctly.
* Expected: ```Element group has extra content: math```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_math.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: math. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_math.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_with_model](../models_1_0/invalid/6.4.1.1.group_with_model.cellml): Error detected correctly.
* Expected: ```Element group has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_model.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: model. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_with_reaction](../models_1_0/invalid/6.4.1.1.group_with_reaction.cellml): Error detected correctly.
* Expected: ```Element group has extra content: reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_reaction.cellml:15:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: reaction. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_reaction.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_with_role](../models_1_0/invalid/6.4.1.1.group_with_role.cellml): Error detected correctly.
* Expected: ```Element group has extra content: role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_role.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: role. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_role.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_with_unit](../models_1_0/invalid/6.4.1.1.group_with_unit.cellml): Error detected correctly.
* Expected: ```Element group failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element relationship_ref, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_unit.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_unit.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_with_units](../models_1_0/invalid/6.4.1.1.group_with_units.cellml): Error detected correctly.
* Expected: ```Element group has extra content: units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_units.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: units. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_with_variable](../models_1_0/invalid/6.4.1.1.group_with_variable.cellml): Error detected correctly.
* Expected: ```Element group has extra content: variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_variable.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.1.1.group_with_variable_ref](../models_1_0/invalid/6.4.1.1.group_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element group has extra content: variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_variable_ref.cellml:15:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element group has extra content: variable_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.1.1.group_with_variable_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

#### 6.4.1

[6.4.1.group_child_order_1](../models_1_0/valid/6.4.1.group_child_order_1.cellml): Valid file passed validation.

[6.4.1.group_child_order_2](../models_1_0/valid/6.4.1.group_child_order_2.cellml): Valid file passed validation.


---

##### 6.4.2.1

[6.4.2.1.relationship_ref_name](../models_1_0/valid/6.4.2.1.relationship_ref_name.cellml): Valid file passed validation.

[6.4.2.1.relationship_ref_relationship_1](../models_1_0/valid/6.4.2.1.relationship_ref_relationship_1.cellml): Valid file passed validation.

🔴 [6.4.2.1.relationship_ref_relationship_2](../models_1_0/valid/6.4.2.1.relationship_ref_relationship_2.cellml): **Valid file failed validation.**
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.2.1.relationship_ref_relationship_2.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.2.1.relationship_ref_relationship_2.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element relationship_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.2.1.relationship_ref_relationship_2.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.2.1.relationship_ref_relationship_2.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.2.1.relationship_ref_relationship_2.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_relationship_missing](../models_1_0/invalid/6.4.2.1.relationship_ref_relationship_missing.cellml): Error detected correctly.
* Expected: ```Element relationship_ref failed to validate```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_relationship_missing.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_relationship_missing.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element relationship_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_relationship_missing.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_relationship_missing.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_relationship_missing.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_component](../models_1_0/invalid/6.4.2.1.relationship_ref_with_component.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_component.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: component. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_component_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: component_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_component_ref.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: component_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_component_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_component_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_component_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_connection](../models_1_0/invalid/6.4.2.1.relationship_ref_with_connection.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_connection.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: connection. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_connection.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_connection.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_connection.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_group](../models_1_0/invalid/6.4.2.1.relationship_ref_with_group.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: group```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_group.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: group. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_group.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_group.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_group.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_map_components](../models_1_0/invalid/6.4.2.1.relationship_ref_with_map_components.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_map_components.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: map_components. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_map_variables](../models_1_0/invalid/6.4.2.1.relationship_ref_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_map_variables.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: map_variables. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_map_variables.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_map_variables.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_map_variables.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_math](../models_1_0/invalid/6.4.2.1.relationship_ref_with_math.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: math```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_math.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: math. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_math.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_math.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_math.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_model](../models_1_0/invalid/6.4.2.1.relationship_ref_with_model.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_model.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: model. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_reaction](../models_1_0/invalid/6.4.2.1.relationship_ref_with_reaction.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_reaction.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: reaction. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_reaction.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_reaction.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_reaction.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_relationship_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_relationship_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: relationship_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_role](../models_1_0/invalid/6.4.2.1.relationship_ref_with_role.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_role.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: role. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_role.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_role.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_role.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_unit](../models_1_0/invalid/6.4.2.1.relationship_ref_with_unit.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: unit```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_unit.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: unit. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_units](../models_1_0/invalid/6.4.2.1.relationship_ref_with_units.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_units.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: units. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_variable](../models_1_0/invalid/6.4.2.1.relationship_ref_with_variable.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_variable.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: variable. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.1.relationship_ref_with_variable_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element relationship_ref has extra content: variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_variable_ref.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element relationship_ref has extra content: variable_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_variable_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_variable_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.1.relationship_ref_with_variable_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 6.4.2.2

[6.4.2.2.relationship_ref_relationship_invalid](../models_1_0/invalid/6.4.2.2.relationship_ref_relationship_invalid.cellml): Error detected correctly.
* Expected: ```Element relationship_ref failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.2.relationship_ref_relationship_invalid.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.2.relationship_ref_relationship_invalid.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element relationship_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.2.relationship_ref_relationship_invalid.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.2.relationship_ref_relationship_invalid.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.2.relationship_ref_relationship_invalid.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 6.4.2.3

[6.4.2.3.relationship_ref_name_invalid](../models_1_0/invalid/6.4.2.3.relationship_ref_name_invalid.cellml): Error detected correctly.
* Expected: ```Invalid attribute name for element relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.3.relationship_ref_name_invalid.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute name for element relationship_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.3.relationship_ref_name_invalid.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.3.relationship_ref_name_invalid.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.3.relationship_ref_name_invalid.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.3.relationship_ref_name_not_unique_model_wide](../models_1_0/valid/6.4.2.3.relationship_ref_name_not_unique_model_wide.cellml): Valid file passed validation.


---

##### 6.4.2.4

[6.4.2.4.relationship_ref_encapsulation_duplicate](../models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_duplicate.cellml): Error detected correctly.
* Expected: ```Invalid attribute name for element relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_duplicate.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute name for element relationship_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_duplicate.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_duplicate.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_duplicate.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.2.4.relationship_ref_encapsulation_named](../models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_named.cellml): Error detected correctly.
* Expected: ```Invalid attribute name for element relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_named.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute name for element relationship_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_named.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_named.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_named.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 6.4.2.5

🔶 [6.4.2.5.relationship_ref_duplicate_named](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_named.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Expecting exactly 1 relationship_ref tag per group, got 2!```

🔶 [6.4.2.5.relationship_ref_duplicate_unnamed_1](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_unnamed_1.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Expecting exactly 1 relationship_ref tag per group, got 2!```

🔶 [6.4.2.5.relationship_ref_duplicate_unnamed_2](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_unnamed_2.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Expecting exactly 1 relationship_ref tag per group, got 2!```

🔴 [6.4.2.5.relationship_ref_multiple_1](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_1.cellml): **Valid file failed validation.**
* Output: ```Expecting exactly 1 relationship_ref tag per group, got 2!```

🔴 [6.4.2.5.relationship_ref_multiple_2](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_2.cellml): **Valid file failed validation.**
* Output: ```Expecting exactly 1 relationship_ref tag per group, got 2!```

🔴 [6.4.2.5.relationship_ref_multiple_3](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_3.cellml): **Valid file failed validation.**
* Output: ```Expecting exactly 1 relationship_ref tag per group, got 3!```


---

##### 6.4.3.1

[6.4.3.1.component_ref_component_missing](../models_1_0/invalid/6.4.3.1.component_ref_component_missing.cellml): Error detected correctly.
* Expected: ```Element component_ref failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_component_missing.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_component_missing.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component_ref in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_component_missing.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_component_missing.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_component_missing.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_nesting](../models_1_0/valid/6.4.3.1.component_ref_nesting.cellml): Valid file passed validation.

[6.4.3.1.component_ref_with_component](../models_1_0/invalid/6.4.3.1.component_ref_with_component.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_component.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: component. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_with_connection](../models_1_0/invalid/6.4.3.1.component_ref_with_connection.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_connection.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: connection. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_connection.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_connection.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_connection.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_with_group](../models_1_0/invalid/6.4.3.1.component_ref_with_group.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: group```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_group.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: group. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_group.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_group.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_group.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_with_map_components](../models_1_0/invalid/6.4.3.1.component_ref_with_map_components.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_map_components.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: map_components. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_with_map_variables](../models_1_0/invalid/6.4.3.1.component_ref_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_map_variables.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: map_variables. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_map_variables.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_map_variables.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_map_variables.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_with_math](../models_1_0/invalid/6.4.3.1.component_ref_with_math.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: math```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_math.cellml:15:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: math. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_math.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_math.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_math.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_with_model](../models_1_0/invalid/6.4.3.1.component_ref_with_model.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_model.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: model. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_with_reaction](../models_1_0/invalid/6.4.3.1.component_ref_with_reaction.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_reaction.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: reaction. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_reaction.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_reaction.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_reaction.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_with_relationship_ref](../models_1_0/invalid/6.4.3.1.component_ref_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_relationship_ref.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: relationship_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_with_role](../models_1_0/invalid/6.4.3.1.component_ref_with_role.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_role.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: role. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_role.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_role.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_role.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_with_unit](../models_1_0/invalid/6.4.3.1.component_ref_with_unit.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: unit```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_unit.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: unit. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_with_units](../models_1_0/invalid/6.4.3.1.component_ref_with_units.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_units.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: units. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_with_variable](../models_1_0/invalid/6.4.3.1.component_ref_with_variable.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_variable.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: variable. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.1.component_ref_with_variable_ref](../models_1_0/invalid/6.4.3.1.component_ref_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element component_ref has extra content: variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_variable_ref.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element component_ref has extra content: variable_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_variable_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_variable_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.1.component_ref_with_variable_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


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

[6.4.3.2.component_ref_duplicate_child_3](../models_1_0/invalid/6.4.3.2.component_ref_duplicate_child_3.cellml): Error detected correctly.
* Expected: ```already added```
* Output: ```Encapsulated component B already added!```

[6.4.3.2.component_ref_duplicate_child_4](../models_1_0/invalid/6.4.3.2.component_ref_duplicate_child_4.cellml): Error detected correctly.
* Expected: ```Parent of component C```
* Output: ```Parent of component C already B. Cannot set A: multiple parents not allowed!```

🔵 [6.4.3.2.component_ref_no_children_containment](../models_1_0/invalid/6.4.3.2.component_ref_no_children_containment.cellml): **Error not detected.**

🔵 [6.4.3.2.component_ref_no_children_encapsulation](../models_1_0/invalid/6.4.3.2.component_ref_no_children_encapsulation.cellml): **Error not detected.**

🔴 [6.4.3.2.component_ref_no_children_extension](../models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml): **Valid file failed validation.**
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element relationship_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.2.component_ref_overlapping_containment](../models_1_0/valid/6.4.3.2.component_ref_overlapping_containment.cellml): Valid file passed validation.

[6.4.3.2.component_ref_overlapping_encapsulation](../models_1_0/invalid/6.4.3.2.component_ref_overlapping_encapsulation.cellml): Error detected correctly.
* Expected: ```Parent of component B already A```
* Output: ```Parent of component B already A. Cannot set C: multiple parents not allowed!```

[6.4.3.2.component_ref_split_named](../models_1_0/valid/6.4.3.2.component_ref_split_named.cellml): Valid file passed validation.

[6.4.3.2.component_ref_split_unnamed_1](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_1.cellml): Valid file passed validation.

[6.4.3.2.component_ref_split_unnamed_2](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_2.cellml): Valid file passed validation.


---

##### 6.4.3.3

[6.4.3.3.component_ref_component_invalid](../models_1_0/invalid/6.4.3.3.component_ref_component_invalid.cellml): Error detected correctly.
* Expected: ```Element component_ref failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.3.component_ref_component_invalid.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.3.component_ref_component_invalid.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component_ref in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.3.component_ref_component_invalid.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.3.component_ref_component_invalid.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/6.4.3.3.component_ref_component_invalid.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

🔵 [6.4.3.3.component_ref_component_nonexistent_1](../models_1_0/invalid/6.4.3.3.component_ref_component_nonexistent_1.cellml): **Error not detected.**

🔵 [6.4.3.3.component_ref_component_nonexistent_2](../models_1_0/invalid/6.4.3.3.component_ref_component_nonexistent_2.cellml): **Error not detected.**


---

## 7. Reactions

##### 7.4.1.1

[7.4.1.1.reaction_variable_ref_missing](../models_1_0/invalid/7.4.1.1.reaction_variable_ref_missing.cellml): Error detected correctly.
* Expected: ```Expecting an element variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_variable_ref_missing.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element variable_ref, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_variable_ref_missing.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_variable_ref_missing.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_variable_ref_missing.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_variable_ref_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_component](../models_1_0/invalid/7.4.1.1.reaction_with_component.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_component.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: component. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_component_ref](../models_1_0/invalid/7.4.1.1.reaction_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: component_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_component_ref.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: component_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_component_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_connection](../models_1_0/invalid/7.4.1.1.reaction_with_connection.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_connection.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: connection. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_connection.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_connection.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_group](../models_1_0/invalid/7.4.1.1.reaction_with_group.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: group```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_group.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: group. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_group.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_map_components](../models_1_0/invalid/7.4.1.1.reaction_with_map_components.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_map_components.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: map_components. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_map_variables](../models_1_0/invalid/7.4.1.1.reaction_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_map_variables.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: map_variables. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_map_variables.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_math](../models_1_0/invalid/7.4.1.1.reaction_with_math.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: math```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_math.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: math. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_math.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_model](../models_1_0/invalid/7.4.1.1.reaction_with_model.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_model.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: model. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_reaction](../models_1_0/invalid/7.4.1.1.reaction_with_reaction.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_reaction.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: reaction. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_reaction.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_reaction.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_relationship_ref](../models_1_0/invalid/7.4.1.1.reaction_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_relationship_ref.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: relationship_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_role](../models_1_0/invalid/7.4.1.1.reaction_with_role.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_role.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: role. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_role.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_role.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_unit](../models_1_0/invalid/7.4.1.1.reaction_with_unit.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: unit```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_unit.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: unit. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_units](../models_1_0/invalid/7.4.1.1.reaction_with_units.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_units.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: units. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.1.1.reaction_with_variable](../models_1_0/invalid/7.4.1.1.reaction_with_variable.cellml): Error detected correctly.
* Expected: ```Element reaction has extra content: variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_variable.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element reaction has extra content: variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.1.reaction_with_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 7.4.1.2

[7.4.1.2.reaction_reversible_invalid](../models_1_0/invalid/7.4.1.2.reaction_reversible_invalid.cellml): Error detected correctly.
* Expected: ```Invalid attribute reversible for element reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.2.reaction_reversible_invalid.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute reversible for element reaction. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.2.reaction_reversible_invalid.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.2.reaction_reversible_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

🔴 [7.4.1.2.reaction_reversible_no](../models_1_0/valid/7.4.1.2.reaction_reversible_no.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

🔴 [7.4.1.2.reaction_reversible_yes](../models_1_0/valid/7.4.1.2.reaction_reversible_yes.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```


---

##### 7.4.1.3

[7.4.1.3.reaction_encapsulating_delta_variable](../models_1_0/invalid/7.4.1.3.reaction_encapsulating_delta_variable.cellml): Error detected correctly.
* Expected: ```Invalid attribute delta_variable for element role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.3.reaction_encapsulating_delta_variable.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute delta_variable for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.3.reaction_encapsulating_delta_variable.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.3.reaction_encapsulating_delta_variable.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.3.reaction_encapsulating_delta_variable.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.3.reaction_encapsulating_delta_variable.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.1.3.reaction_encapsulating_delta_variable.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 7.4.2.1

[7.4.2.1.variable_ref_role_missing](../models_1_0/invalid/7.4.2.1.variable_ref_role_missing.cellml): Error detected correctly.
* Expected: ```Expecting an element role, got nothing```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_role_missing.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element role, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_role_missing.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_role_missing.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_role_missing.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_role_missing.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_role_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_variable_missing](../models_1_0/invalid/7.4.2.1.variable_ref_variable_missing.cellml): Error detected correctly.
* Expected: ```Element variable_ref failed to validate content```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_variable_missing.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_variable_missing.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_variable_missing.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_variable_missing.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_variable_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_component](../models_1_0/invalid/7.4.2.1.variable_ref_with_component.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_component.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: component. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_component_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: component_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_component_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: component_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_component_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_component_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_component_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_connection](../models_1_0/invalid/7.4.2.1.variable_ref_with_connection.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_connection.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: connection. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_connection.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_connection.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_connection.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_connection.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_group](../models_1_0/invalid/7.4.2.1.variable_ref_with_group.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: group```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_group.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: group. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_group.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_group.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_group.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_map_components](../models_1_0/invalid/7.4.2.1.variable_ref_with_map_components.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_map_components.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: map_components. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_map_variables](../models_1_0/invalid/7.4.2.1.variable_ref_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_map_variables.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: map_variables. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_map_variables.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_map_variables.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_map_variables.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_math](../models_1_0/invalid/7.4.2.1.variable_ref_with_math.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: math```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_math.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: math. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_math.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_math.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_math.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_model](../models_1_0/invalid/7.4.2.1.variable_ref_with_model.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_model.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: model. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_reaction](../models_1_0/invalid/7.4.2.1.variable_ref_with_reaction.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_reaction.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: reaction. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_reaction.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_reaction.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_reaction.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_reaction.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_relationship_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_relationship_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: relationship_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_unit](../models_1_0/invalid/7.4.2.1.variable_ref_with_unit.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: unit```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_unit.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: unit. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_units](../models_1_0/invalid/7.4.2.1.variable_ref_with_units.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_units.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: units. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_variable](../models_1_0/invalid/7.4.2.1.variable_ref_with_variable.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_variable.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: variable. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.2.1.variable_ref_with_variable_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element variable_ref has extra content: variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_variable_ref.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element variable_ref has extra content: variable_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_variable_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_variable_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_variable_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.2.1.variable_ref_with_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 7.4.2.2

🔶 [7.4.2.2.variable_ref_variable_duplicate](../models_1_0/invalid/7.4.2.2.variable_ref_variable_duplicate.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

🔶 [7.4.2.2.variable_ref_variable_hidden](../models_1_0/invalid/7.4.2.2.variable_ref_variable_hidden.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```

🔶 [7.4.2.2.variable_ref_variable_nonexistent](../models_1_0/invalid/7.4.2.2.variable_ref_variable_nonexistent.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component A).```


---

##### 7.4.3.1

[7.4.3.1.role_role_missing](../models_1_0/invalid/7.4.3.1.role_role_missing.cellml): Error detected correctly.
* Expected: ```Element role failed to validate attributes```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_role_missing.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_role_missing.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element role failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_role_missing.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_role_missing.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_role_missing.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_role_missing.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_component](../models_1_0/invalid/7.4.3.1.role_with_component.cellml): Error detected correctly.
* Expected: ```Element role has extra content: component```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_component.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: component. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_component.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_component.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_component.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_component.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_component.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_component_ref](../models_1_0/invalid/7.4.3.1.role_with_component_ref.cellml): Error detected correctly.
* Expected: ```Element role has extra content: component_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_component_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: component_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_component_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_component_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_component_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_component_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_component_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_connection](../models_1_0/invalid/7.4.3.1.role_with_connection.cellml): Error detected correctly.
* Expected: ```Element role has extra content: connection```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_connection.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: connection. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_connection.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_connection.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_connection.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_connection.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_connection.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_group](../models_1_0/invalid/7.4.3.1.role_with_group.cellml): Error detected correctly.
* Expected: ```Element role has extra content: group```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_group.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: group. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_group.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_group.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_group.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_group.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_group.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_map_components](../models_1_0/invalid/7.4.3.1.role_with_map_components.cellml): Error detected correctly.
* Expected: ```Element role has extra content: map_components```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_map_components.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: map_components. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_map_components.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_map_components.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_map_components.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_map_components.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_map_variables](../models_1_0/invalid/7.4.3.1.role_with_map_variables.cellml): Error detected correctly.
* Expected: ```Element role has extra content: map_variables```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_map_variables.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: map_variables. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_map_variables.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_map_variables.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_map_variables.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_map_variables.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_map_variables.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_model](../models_1_0/invalid/7.4.3.1.role_with_model.cellml): Error detected correctly.
* Expected: ```Element role has extra content: model```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_model.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: model. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_model.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_model.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_model.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_model.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_model.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_reaction](../models_1_0/invalid/7.4.3.1.role_with_reaction.cellml): Error detected correctly.
* Expected: ```Element role has extra content: reaction```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_reaction.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: reaction. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_reaction.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_reaction.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_reaction.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_reaction.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_reaction.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_relationship_ref](../models_1_0/invalid/7.4.3.1.role_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```Element role has extra content: relationship_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_relationship_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: relationship_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_relationship_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_relationship_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_relationship_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_relationship_ref.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_relationship_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_role](../models_1_0/invalid/7.4.3.1.role_with_role.cellml): Error detected correctly.
* Expected: ```Element role has extra content: role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_role.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_role.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_role.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_role.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_role.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_role.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_unit](../models_1_0/invalid/7.4.3.1.role_with_unit.cellml): Error detected correctly.
* Expected: ```Element role has extra content: unit```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_unit.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: unit. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_unit.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_unit.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_unit.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_unit.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_units](../models_1_0/invalid/7.4.3.1.role_with_units.cellml): Error detected correctly.
* Expected: ```Element role has extra content: units```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_units.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: units. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_units.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_units.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_units.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_units.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_units.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_variable](../models_1_0/invalid/7.4.3.1.role_with_variable.cellml): Error detected correctly.
* Expected: ```Element role has extra content: variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_variable.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: variable. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_variable.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_variable.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_variable.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_variable.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_variable.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.1.role_with_variable_ref](../models_1_0/invalid/7.4.3.1.role_with_variable_ref.cellml): Error detected correctly.
* Expected: ```Element role has extra content: variable_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_variable_ref.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_EXTRACONTENT: Element role has extra content: variable_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_variable_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_variable_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_variable_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_variable_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.1.role_with_variable_ref.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 7.4.3.2

[7.4.3.2.role_role_invalid](../models_1_0/invalid/7.4.3.2.role_role_invalid.cellml): Error detected correctly.
* Expected: ```Element role failed to validate attributes```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.2.role_role_invalid.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.2.role_role_invalid.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element role failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.2.role_role_invalid.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.2.role_role_invalid.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.2.role_role_invalid.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.2.role_role_invalid.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 7.4.3.3

🔶 [7.4.3.3.reaction_multiple_rates](../models_1_0/invalid/7.4.3.3.reaction_multiple_rates.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component x).```

[7.4.3.3.role_rate_with_delta_variable](../models_1_0/invalid/7.4.3.3.role_rate_with_delta_variable.cellml): Error detected correctly.
* Expected: ```Invalid attribute delta_variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_delta_variable.cellml:24:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_delta_variable.cellml:24:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element math, got nothing. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_delta_variable.cellml:24:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute delta_variable for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_delta_variable.cellml:23:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_delta_variable.cellml:23:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_delta_variable.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.3.role_rate_with_multiple_roles](../models_1_0/invalid/7.4.3.3.role_rate_with_multiple_roles.cellml): Error detected correctly.
* Expected: ```Extra element role```
* Output: ```Invalid or unsupported CellML file. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element role in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_multiple_roles.cellml:32:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable_ref in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_multiple_roles.cellml:22:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_multiple_roles.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.3.role_rate_with_stoichiometry](../models_1_0/invalid/7.4.3.3.role_rate_with_stoichiometry.cellml): Error detected correctly.
* Expected: ```Invalid attribute stoichiometry for element role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_stoichiometry.cellml:23:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_stoichiometry.cellml:23:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element role failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_stoichiometry.cellml:23:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute stoichiometry for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_stoichiometry.cellml:22:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_stoichiometry.cellml:22:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.3.role_rate_with_stoichiometry.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 7.4.3.4

[7.4.3.4.role_direction_invalid](../models_1_0/invalid/7.4.3.4.role_direction_invalid.cellml): Error detected correctly.
* Expected: ```Invalid attribute direction for element role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.4.role_direction_invalid.cellml:24:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute direction for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.4.role_direction_invalid.cellml:24:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.4.role_direction_invalid.cellml:23:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.4.role_direction_invalid.cellml:23:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable_ref in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.4.role_direction_invalid.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 7.4.3.5

🔶 [7.4.3.5.role_direction_both_irreversible](../models_1_0/invalid/7.4.3.5.role_direction_both_irreversible.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component x).```

[7.4.3.5.role_direction_both_product](../models_1_0/invalid/7.4.3.5.role_direction_both_product.cellml): Error detected correctly.
* Expected: ```Invalid attribute direction for element role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_product.cellml:20:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute direction for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_product.cellml:20:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_product.cellml:19:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_product.cellml:19:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable_ref in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_product.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.5.role_direction_both_rate](../models_1_0/invalid/7.4.3.5.role_direction_both_rate.cellml): Error detected correctly.
* Expected: ```Invalid attribute direction for element role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_rate.cellml:23:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_rate.cellml:23:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element role failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_rate.cellml:23:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute direction for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_rate.cellml:22:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_rate.cellml:22:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_rate.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.5.role_direction_both_reactant](../models_1_0/invalid/7.4.3.5.role_direction_both_reactant.cellml): Error detected correctly.
* Expected: ```Invalid attribute direction for element role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_reactant.cellml:17:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute direction for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_reactant.cellml:17:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_reactant.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_reactant.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable_ref in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_both_reactant.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

🔶 [7.4.3.5.role_direction_reverse_irreversible](../models_1_0/invalid/7.4.3.5.role_direction_reverse_irreversible.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component x).```

[7.4.3.5.role_direction_reverse_product](../models_1_0/invalid/7.4.3.5.role_direction_reverse_product.cellml): Error detected correctly.
* Expected: ```Invalid attribute direction for element role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_product.cellml:20:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute direction for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_product.cellml:20:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_product.cellml:19:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_product.cellml:19:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable_ref in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_product.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.5.role_direction_reverse_rate](../models_1_0/invalid/7.4.3.5.role_direction_reverse_rate.cellml): Error detected correctly.
* Expected: ```Invalid attribute direction for element role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_rate.cellml:23:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_rate.cellml:23:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element role failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_rate.cellml:23:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute direction for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_rate.cellml:22:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_rate.cellml:22:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_rate.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.5.role_direction_reverse_reactant](../models_1_0/invalid/7.4.3.5.role_direction_reverse_reactant.cellml): Error detected correctly.
* Expected: ```Invalid attribute direction for element role```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_reactant.cellml:17:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute direction for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_reactant.cellml:17:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_reactant.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_reactant.cellml:16:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable_ref in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.5.role_direction_reverse_reactant.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

🔶 [7.4.3.5.role_direction_role_duplicate](../models_1_0/invalid/7.4.3.5.role_direction_role_duplicate.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component x).```


---

##### 7.4.3.6

🔶 [7.4.3.6.role_stoichiometry_invalid](../models_1_0/invalid/7.4.3.6.role_stoichiometry_invalid.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.6.role_stoichiometry_invalid.cellml:15:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute delta_variable for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.6.role_stoichiometry_invalid.cellml:15:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.6.role_stoichiometry_invalid.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.6.role_stoichiometry_invalid.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.6.role_stoichiometry_invalid.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.6.role_stoichiometry_invalid.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 7.4.3.7

[7.4.3.7.role_delta_variable_duplicate_1](../models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_1.cellml): Error detected correctly.
* Expected: ```Invalid attribute delta_variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_1.cellml:15:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute delta_variable for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_1.cellml:15:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_1.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_1.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_1.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_1.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.7.role_delta_variable_duplicate_2](../models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_2.cellml): Error detected correctly.
* Expected: ```Invalid attribute delta_variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_2.cellml:15:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute delta_variable for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_2.cellml:15:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_2.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_2.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_2.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_2.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.7.role_delta_variable_nonexistent_1](../models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_1.cellml): Error detected correctly.
* Expected: ```Invalid attribute delta_variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_1.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute delta_variable for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_1.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_1.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_1.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_1.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_1.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.7.role_delta_variable_nonexistent_2](../models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_2.cellml): Error detected correctly.
* Expected: ```Invalid attribute delta_variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_2.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute delta_variable for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_2.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_2.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_2.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_2.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_2.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 7.4.3.8

[7.4.3.8.role_delta_variable_activator](../models_1_0/invalid/7.4.3.8.role_delta_variable_activator.cellml): Error detected correctly.
* Expected: ```Invalid attribute delta_variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_activator.cellml:25:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute delta_variable for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_activator.cellml:25:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_activator.cellml:24:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_activator.cellml:24:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable_ref in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_activator.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.8.role_delta_variable_catalyst](../models_1_0/invalid/7.4.3.8.role_delta_variable_catalyst.cellml): Error detected correctly.
* Expected: ```Invalid attribute delta_variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_catalyst.cellml:25:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute delta_variable for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_catalyst.cellml:25:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_catalyst.cellml:24:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_catalyst.cellml:24:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable_ref in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_catalyst.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.8.role_delta_variable_inhibitor](../models_1_0/invalid/7.4.3.8.role_delta_variable_inhibitor.cellml): Error detected correctly.
* Expected: ```Invalid attribute delta_variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_inhibitor.cellml:25:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute delta_variable for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_inhibitor.cellml:25:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_inhibitor.cellml:24:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_inhibitor.cellml:24:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable_ref in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_inhibitor.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[7.4.3.8.role_delta_variable_modifier](../models_1_0/invalid/7.4.3.8.role_delta_variable_modifier.cellml): Error detected correctly.
* Expected: ```Invalid attribute delta_variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_modifier.cellml:25:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute delta_variable for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_modifier.cellml:25:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_modifier.cellml:24:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_modifier.cellml:24:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable_ref in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_modifier.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

🔶 [7.4.3.8.role_delta_variable_with_rate_and_math](../models_1_0/invalid/7.4.3.8.role_delta_variable_with_rate_and_math.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component x).```

🔶 [7.4.3.8.role_delta_variable_with_stoichiometry_no_rate](../models_1_0/invalid/7.4.3.8.role_delta_variable_with_stoichiometry_no_rate.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component x).```

[7.4.3.8.role_delta_variable_without_rate_or_math](../models_1_0/invalid/7.4.3.8.role_delta_variable_without_rate_or_math.cellml): Error detected correctly.
* Expected: ```Invalid attribute delta_variable```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_without_rate_or_math.cellml:15:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute delta_variable for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_without_rate_or_math.cellml:15:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_without_rate_or_math.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_without_rate_or_math.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_without_rate_or_math.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/7.4.3.8.role_delta_variable_without_rate_or_math.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

##### 7.4.3.9

🔶 [7.4.3.9.role_math_not_relevant](../models_1_0/invalid/7.4.3.9.role_math_not_relevant.cellml): **Invalid file failed for unexpected reason.**
* Output: ```Reactions are not supported (found in component x).```


---

#### 7.4.3

🔴 [7.4.3.reaction_all_roles_and_attributes](../models_1_0/valid/7.4.3.reaction_all_roles_and_attributes.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component reaction).```

🔴 [7.4.3.reaction_reversible_no](../models_1_0/valid/7.4.3.reaction_reversible_no.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component reaction).```

🔴 [7.4.3.reaction_simple](../models_1_0/valid/7.4.3.reaction_simple.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component x).```


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

🔴 [8.4.1.cmeta_id_in_reaction](../models_1_0/valid/8.4.1.cmeta_id_in_reaction.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

[8.4.1.cmeta_id_in_relationship_ref](../models_1_0/valid/8.4.1.cmeta_id_in_relationship_ref.cellml): Valid file passed validation.

🔴 [8.4.1.cmeta_id_in_role](../models_1_0/valid/8.4.1.cmeta_id_in_role.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

[8.4.1.cmeta_id_in_unit](../models_1_0/valid/8.4.1.cmeta_id_in_unit.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_units_1](../models_1_0/valid/8.4.1.cmeta_id_in_units_1.cellml): Valid file passed validation.

🔴 [8.4.1.cmeta_id_in_units_2](../models_1_0/valid/8.4.1.cmeta_id_in_units_2.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

[8.4.1.cmeta_id_in_variable](../models_1_0/valid/8.4.1.cmeta_id_in_variable.cellml): Valid file passed validation.

🔴 [8.4.1.cmeta_id_in_variable_ref](../models_1_0/valid/8.4.1.cmeta_id_in_variable_ref.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

[8.4.1.duplicate_cmeta_id_in_component](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_component.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_component.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element component. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_component.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[8.4.1.duplicate_cmeta_id_in_component_ref](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_component_ref.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_component_ref.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element component_ref. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component_ref in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_component_ref.cellml:14:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_component_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_component_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_component_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[8.4.1.duplicate_cmeta_id_in_connection](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_connection.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_connection.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element connection. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_connection.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[8.4.1.duplicate_cmeta_id_in_group](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_group.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_group.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element group. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_group.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[8.4.1.duplicate_cmeta_id_in_map_components](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_components.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_components.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element map_components. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_components.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_components.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_components.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[8.4.1.duplicate_cmeta_id_in_map_variables](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_variables.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_variables.cellml:15:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element map_variables. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_variables.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_variables.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element connection failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element connection in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_variables.cellml:13:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[8.4.1.duplicate_cmeta_id_in_model](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_model.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_model.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element model```

[8.4.1.duplicate_cmeta_id_in_reaction](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_reaction.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_reaction.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element reaction. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_reaction.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_reaction.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[8.4.1.duplicate_cmeta_id_in_relationship_ref](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_relationship_ref.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element relationship_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_relationship_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_relationship_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_relationship_ref.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[8.4.1.duplicate_cmeta_id_in_role](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_role.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_role.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element role. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_role.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_ATTRVALID: Element role failed to validate attributes. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_role.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_role.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element variable_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_role.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_role.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[8.4.1.duplicate_cmeta_id_in_unit](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_unit.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_unit.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_unit.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[8.4.1.duplicate_cmeta_id_in_units_1](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_units_1.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_units_1.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_units_1.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_units_1.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[8.4.1.duplicate_cmeta_id_in_units_2](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_units_2.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_units_2.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_units_2.cellml:8:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_units_2.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[8.4.1.duplicate_cmeta_id_in_variable](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element variable. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element variable in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[8.4.1.duplicate_cmeta_id_in_variable_ref](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable_ref.cellml): Error detected correctly.
* Expected: ```Invalid attribute id```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable_ref.cellml:10:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element variable_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element reaction failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element reaction in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable_ref.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable_ref.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```


---

#### 8.4.2

[8.4.2.rdf_in_component](../models_1_0/valid/8.4.2.rdf_in_component.cellml): Valid file passed validation.

[8.4.2.rdf_in_component_ref](../models_1_0/valid/8.4.2.rdf_in_component_ref.cellml): Valid file passed validation.

[8.4.2.rdf_in_connection](../models_1_0/valid/8.4.2.rdf_in_connection.cellml): Valid file passed validation.

[8.4.2.rdf_in_group](../models_1_0/valid/8.4.2.rdf_in_group.cellml): Valid file passed validation.

[8.4.2.rdf_in_map_components](../models_1_0/valid/8.4.2.rdf_in_map_components.cellml): Valid file passed validation.

[8.4.2.rdf_in_map_variables](../models_1_0/valid/8.4.2.rdf_in_map_variables.cellml): Valid file passed validation.

[8.4.2.rdf_in_model](../models_1_0/valid/8.4.2.rdf_in_model.cellml): Valid file passed validation.

🔴 [8.4.2.rdf_in_reaction](../models_1_0/valid/8.4.2.rdf_in_reaction.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

[8.4.2.rdf_in_relationship_ref](../models_1_0/valid/8.4.2.rdf_in_relationship_ref.cellml): Valid file passed validation.

🔴 [8.4.2.rdf_in_role](../models_1_0/valid/8.4.2.rdf_in_role.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

[8.4.2.rdf_in_unit](../models_1_0/valid/8.4.2.rdf_in_unit.cellml): Valid file passed validation.

🔴 [8.4.2.rdf_in_units_1](../models_1_0/valid/8.4.2.rdf_in_units_1.cellml): **Valid file failed validation.**
* Output: ```'units'```

🔴 [8.4.2.rdf_in_units_2](../models_1_0/valid/8.4.2.rdf_in_units_2.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

[8.4.2.rdf_in_variable](../models_1_0/valid/8.4.2.rdf_in_variable.cellml): Valid file passed validation.

🔴 [8.4.2.rdf_in_variable_ref](../models_1_0/valid/8.4.2.rdf_in_variable_ref.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```


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

🔴 [C.3.3.unit_checking_derivative_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_derivative_operand_error.cellml): **Valid file failed validation.**
* Output: ```Equation LHS should be a derivative or variable, not 0```

[C.3.3.unit_checking_function_exp_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_function_exp_operand_error.cellml): Valid file passed validation.

🔴 [C.3.3.unit_checking_function_factorial_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_function_factorial_operand_error.cellml): **Valid file failed validation.**
* Output: ```No handler for element <factorial>```

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

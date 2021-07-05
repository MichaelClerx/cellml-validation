# Myokit - CellML 1.0

Performance:
* 83% according to spec (772 out of 923)
* 341 out of 375 valid files passed
* 431 out of 548 invalid files detected

Issues:
* 34 valid files failed validation
* 15 invalid files passed validation
* 102 invalid files failed validation for the wrong reason

Results per category

(Valid passed, invalid failed, valid failed, invalid passed, invalid failed for wrong reason, percent classified correctly according to spec)

|Category|V Pass|I Fail|🔴 V Fail|🔵 I Pass|🔶 I Bad|Score|
|-|-|-|-|-|-|-|
|[0. Not mentioned in spec](#0-not-mentioned-in-spec)|6|10|0|0|0|100%|
|[2. Fundamentals](#2-fundamentals)|27|85|7|0|18|81%|
|[3. Model structure](#3-model-structure)|46|155|4|0|0|98%|
|[4. Mathematics](#4-mathematics)|42|18|8|0|2|85%|
|[5. Units](#5-units)|133|82|3|6|0|95%|
|[6. Grouping](#6-grouping)|17|69|0|9|0|90%|
|[7. Reactions](#7-reactions)|0|0|5|0|79|0%|
|[8. Metadata framework](#8-metadata-framework)|24|12|6|0|3|80%|
|[C. Advanced units functionality](#c-advanced-units-functionality)|46|0|1|0|0|97%|


---

## 0. Not mentioned in spec

### 0.0

[0.0.root_namespace_1](../models_1_0/valid/0.0.root_namespace_1.cellml): Valid file passed validation.

[0.0.root_namespace_2](../models_1_0/valid/0.0.root_namespace_2.cellml): Valid file passed validation.

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

🔴 [2.4.1.valid_identifiers](../models_1_0/valid/2.4.1.valid_identifiers.cellml): **Valid file failed validation.**
* Output: ```Error on line 16. Component name must be a valid CellML identifier (3.4.2.2).```


---

#### 2.4.2

[2.4.2.imaginary_attributes_1](../models_1_0/invalid/2.4.2.imaginary_attributes_1.cellml): Error detected correctly.
* Expected: ```Unexpected attribute fruit```
* Output: ```Error on line 7. Unexpected attribute fruit found in cellml:model[@name="imaginary_attributes_1"].```

[2.4.2.imaginary_attributes_2](../models_1_0/invalid/2.4.2.imaginary_attributes_2.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cellml:fruit```
* Output: ```Error on line 8. Unexpected attribute cellml:fruit found in cellml:model[@name="imaginary_attributes_2"].```

[2.4.2.imaginary_elements_1](../models_1_0/invalid/2.4.2.imaginary_elements_1.cellml): Error detected correctly.
* Expected: ```found element of type cellml:fruit```
* Output: ```Error on line 6. Unexpected content type in cellml:model[@name="imaginary_elements"], found element of type cellml:fruit.```

[2.4.2.imaginary_elements_2](../models_1_0/invalid/2.4.2.imaginary_elements_2.cellml): Error detected correctly.
* Expected: ```Imports are not allowed in CellML 1.0```
* Output: ```Error on line 8. Imports are not allowed in CellML 1.0.```


---

#### 2.4.3

[2.4.3.bad_cmeta_attribute_in_component](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_component.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cmeta:bob```
* Output: ```Error on line 8. Unexpected attribute cmeta:bob found in cellml:component[@name="A"].```

[2.4.3.bad_cmeta_attribute_in_component_ref](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cmeta:bob```
* Output: ```Error on line 13. Unexpected attribute cmeta:bob found in cellml:component_ref.```

[2.4.3.bad_cmeta_attribute_in_connection](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_connection.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cmeta:bob```
* Output: ```Error on line 14. Unexpected attribute cmeta:bob found in cellml:connection.```

[2.4.3.bad_cmeta_attribute_in_group](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_group.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cmeta:bob```
* Output: ```Error on line 10. Unexpected attribute cmeta:bob found in cellml:group.```

[2.4.3.bad_cmeta_attribute_in_map_components](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cmeta:bob```
* Output: ```Error on line 9. Unexpected attribute cmeta:bob found in cellml:map_components.```

[2.4.3.bad_cmeta_attribute_in_map_variables](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cmeta:bob```
* Output: ```Error on line 16. Unexpected attribute cmeta:bob found in cellml:map_variables.```

[2.4.3.bad_cmeta_attribute_in_model](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_model.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cmeta:bob```
* Output: ```Error on line 8. Unexpected attribute cmeta:bob found in cellml:model[@name="bad_cmeta_attribute_in_model"].```

🔶 [2.4.3.bad_cmeta_attribute_in_reaction](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_reaction.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 10. Reactions are not supported.```

[2.4.3.bad_cmeta_attribute_in_relationship_ref](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cmeta:bob```
* Output: ```Error on line 11. Unexpected attribute cmeta:bob found in cellml:relationship_ref.```

🔶 [2.4.3.bad_cmeta_attribute_in_role](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_role.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 10. Reactions are not supported.```

[2.4.3.bad_cmeta_attribute_in_unit](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_unit.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cmeta:bob```
* Output: ```Error on line 9. Unexpected attribute cmeta:bob found in cellml:unit.```

[2.4.3.bad_cmeta_attribute_in_units_1](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_units_1.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cmeta:bob```
* Output: ```Error on line 8. Unexpected attribute cmeta:bob found in cellml:units[@name="orange"].```

[2.4.3.bad_cmeta_attribute_in_units_2](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_units_2.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cmeta:bob```
* Output: ```Error on line 9. Unexpected attribute cmeta:bob found in cellml:units[@name="apple"].```

[2.4.3.bad_cmeta_attribute_in_variable](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_variable.cellml): Error detected correctly.
* Expected: ```Unexpected attribute cmeta:bob```
* Output: ```Error on line 9. Unexpected attribute cmeta:bob found in cellml:variable[@name="a"].```

🔶 [2.4.3.bad_cmeta_attribute_in_variable_ref](../models_1_0/invalid/2.4.3.bad_cmeta_attribute_in_variable_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 10. Reactions are not supported.```

[2.4.3.bad_rdf_element_in_component](../models_1_0/invalid/2.4.3.bad_rdf_element_in_component.cellml): Error detected correctly.
* Expected: ```found element of type rdf:Description```
* Output: ```Error on line 8. Unexpected content type in cellml:component[@name="A"], found element of type rdf:Description.```

[2.4.3.bad_rdf_element_in_component_ref](../models_1_0/invalid/2.4.3.bad_rdf_element_in_component_ref.cellml): Error detected correctly.
* Expected: ```found element of type rdf:Description```
* Output: ```Error on line 13. Unexpected content type in cellml:component_ref, found element of type rdf:Description.```

[2.4.3.bad_rdf_element_in_connection](../models_1_0/invalid/2.4.3.bad_rdf_element_in_connection.cellml): Error detected correctly.
* Expected: ```found element of type rdf:Description```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type rdf:Description.```

[2.4.3.bad_rdf_element_in_group](../models_1_0/invalid/2.4.3.bad_rdf_element_in_group.cellml): Error detected correctly.
* Expected: ```found element of type rdf:Description```
* Output: ```Error on line 14. Unexpected content type in cellml:group, found element of type rdf:Description.```

[2.4.3.bad_rdf_element_in_map_components](../models_1_0/invalid/2.4.3.bad_rdf_element_in_map_components.cellml): Error detected correctly.
* Expected: ```found element of type rdf:Description```
* Output: ```Error on line 9. Unexpected content type in cellml:map_components, found element of type rdf:Description.```

[2.4.3.bad_rdf_element_in_map_variables](../models_1_0/invalid/2.4.3.bad_rdf_element_in_map_variables.cellml): Error detected correctly.
* Expected: ```found element of type rdf:Description```
* Output: ```Error on line 16. Unexpected content type in cellml:map_variables, found element of type rdf:Description.```

[2.4.3.bad_rdf_element_in_model](../models_1_0/invalid/2.4.3.bad_rdf_element_in_model.cellml): Error detected correctly.
* Expected: ```found element of type rdf:Description```
* Output: ```Error on line 7. Unexpected content type in cellml:model[@name="cmeta_element_in_model"], found element of type rdf:Description.```

🔶 [2.4.3.bad_rdf_element_in_reaction](../models_1_0/invalid/2.4.3.bad_rdf_element_in_reaction.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.bad_rdf_element_in_relationship_ref](../models_1_0/invalid/2.4.3.bad_rdf_element_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```found element of type rdf:Description```
* Output: ```Error on line 11. Unexpected content type in cellml:relationship_ref, found element of type rdf:Description.```

🔶 [2.4.3.bad_rdf_element_in_role](../models_1_0/invalid/2.4.3.bad_rdf_element_in_role.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.bad_rdf_element_in_unit](../models_1_0/invalid/2.4.3.bad_rdf_element_in_unit.cellml): Error detected correctly.
* Expected: ```found element of type rdf:Description```
* Output: ```Error on line 9. Unexpected content type in cellml:unit, found element of type rdf:Description.```

[2.4.3.bad_rdf_element_in_units_1](../models_1_0/invalid/2.4.3.bad_rdf_element_in_units_1.cellml): Error detected correctly.
* Expected: ```found element of type rdf:Description```
* Output: ```Error on line 9. Unexpected content type in cellml:units[@name="orange"], found element of type rdf:Description.```

[2.4.3.bad_rdf_element_in_units_2](../models_1_0/invalid/2.4.3.bad_rdf_element_in_units_2.cellml): Error detected correctly.
* Expected: ```found element of type rdf:Description```
* Output: ```Error on line 10. Unexpected content type in cellml:units[@name="apple"], found element of type rdf:Description.```

[2.4.3.bad_rdf_element_in_variable](../models_1_0/invalid/2.4.3.bad_rdf_element_in_variable.cellml): Error detected correctly.
* Expected: ```found element of type rdf:Description```
* Output: ```Error on line 9. Unexpected content type in cellml:variable[@name="a"], found element of type rdf:Description.```

🔶 [2.4.3.bad_rdf_element_in_variable_ref](../models_1_0/invalid/2.4.3.bad_rdf_element_in_variable_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.cellml_attributes_inside_extensions](../models_1_0/invalid/2.4.3.cellml_attributes_inside_extensions.cellml): Error detected correctly.
* Expected: ```CellML attribute cellml:name found in extension element```
* Output: ```Error on line 8. CellML attribute cellml:name found in extension element {http://fruit.org}banana (2.4.3).```

[2.4.3.cellml_elements_inside_extensions](../models_1_0/invalid/2.4.3.cellml_elements_inside_extensions.cellml): Error detected correctly.
* Expected: ```CellML element cellml:component found inside extension element```
* Output: ```Error on line 9. CellML element cellml:component found inside extension element {http://fruit.org}banana (2.4.3).```

[2.4.3.cmeta_element_in_component](../models_1_0/invalid/2.4.3.cmeta_element_in_component.cellml): Error detected correctly.
* Expected: ```found element of type cmeta:species```
* Output: ```Error on line 8. Unexpected content type in cellml:component[@name="A"], found element of type cmeta:species.```

[2.4.3.cmeta_element_in_component_ref](../models_1_0/invalid/2.4.3.cmeta_element_in_component_ref.cellml): Error detected correctly.
* Expected: ```found element of type cmeta:species```
* Output: ```Error on line 13. Unexpected content type in cellml:component_ref, found element of type cmeta:species.```

[2.4.3.cmeta_element_in_connection](../models_1_0/invalid/2.4.3.cmeta_element_in_connection.cellml): Error detected correctly.
* Expected: ```found element of type cmeta:species```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type cmeta:species.```

[2.4.3.cmeta_element_in_group](../models_1_0/invalid/2.4.3.cmeta_element_in_group.cellml): Error detected correctly.
* Expected: ```found element of type cmeta:species```
* Output: ```Error on line 14. Unexpected content type in cellml:group, found element of type cmeta:species.```

[2.4.3.cmeta_element_in_map_components](../models_1_0/invalid/2.4.3.cmeta_element_in_map_components.cellml): Error detected correctly.
* Expected: ```found element of type cmeta:species```
* Output: ```Error on line 9. Unexpected content type in cellml:map_components, found element of type cmeta:species.```

[2.4.3.cmeta_element_in_map_variables](../models_1_0/invalid/2.4.3.cmeta_element_in_map_variables.cellml): Error detected correctly.
* Expected: ```found element of type cmeta:species```
* Output: ```Error on line 16. Unexpected content type in cellml:map_variables, found element of type cmeta:species.```

[2.4.3.cmeta_element_in_model](../models_1_0/invalid/2.4.3.cmeta_element_in_model.cellml): Error detected correctly.
* Expected: ```found element of type cmeta:species```
* Output: ```Error on line 7. Unexpected content type in cellml:model[@name="cmeta_element_in_model"], found element of type cmeta:species.```

🔶 [2.4.3.cmeta_element_in_reaction](../models_1_0/invalid/2.4.3.cmeta_element_in_reaction.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.cmeta_element_in_relationship_ref](../models_1_0/invalid/2.4.3.cmeta_element_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```found element of type cmeta:species```
* Output: ```Error on line 11. Unexpected content type in cellml:relationship_ref, found element of type cmeta:species.```

🔶 [2.4.3.cmeta_element_in_role](../models_1_0/invalid/2.4.3.cmeta_element_in_role.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.cmeta_element_in_unit](../models_1_0/invalid/2.4.3.cmeta_element_in_unit.cellml): Error detected correctly.
* Expected: ```found element of type cmeta:species```
* Output: ```Error on line 9. Unexpected content type in cellml:unit, found element of type cmeta:species.```

[2.4.3.cmeta_element_in_units_1](../models_1_0/invalid/2.4.3.cmeta_element_in_units_1.cellml): Error detected correctly.
* Expected: ```found element of type cmeta:species```
* Output: ```Error on line 9. Unexpected content type in cellml:units[@name="orange"], found element of type cmeta:species.```

[2.4.3.cmeta_element_in_units_2](../models_1_0/invalid/2.4.3.cmeta_element_in_units_2.cellml): Error detected correctly.
* Expected: ```found element of type cmeta:species```
* Output: ```Error on line 10. Unexpected content type in cellml:units[@name="apple"], found element of type cmeta:species.```

[2.4.3.cmeta_element_in_variable](../models_1_0/invalid/2.4.3.cmeta_element_in_variable.cellml): Error detected correctly.
* Expected: ```found element of type cmeta:species```
* Output: ```Error on line 9. Unexpected content type in cellml:variable[@name="a"], found element of type cmeta:species.```

🔶 [2.4.3.cmeta_element_in_variable_ref](../models_1_0/invalid/2.4.3.cmeta_element_in_variable_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.component_ref_with_extensions](../models_1_0/valid/2.4.3.component_ref_with_extensions.cellml): Valid file passed validation.

[2.4.3.component_with_extensions](../models_1_0/valid/2.4.3.component_with_extensions.cellml): Valid file passed validation.

[2.4.3.connection_with_extensions](../models_1_0/valid/2.4.3.connection_with_extensions.cellml): Valid file passed validation.

[2.4.3.group_with_extensions](../models_1_0/valid/2.4.3.group_with_extensions.cellml): Valid file passed validation.

[2.4.3.map_components_with_extensions](../models_1_0/valid/2.4.3.map_components_with_extensions.cellml): Valid file passed validation.

[2.4.3.map_variables_with_extensions](../models_1_0/valid/2.4.3.map_variables_with_extensions.cellml): Valid file passed validation.

[2.4.3.mathml_attribute_in_component](../models_1_0/invalid/2.4.3.mathml_attribute_in_component.cellml): Error detected correctly.
* Expected: ```Unexpected attribute mathml:sum```
* Output: ```Error on line 7. Unexpected attribute mathml:sum found in cellml:component[@name="A"].```

[2.4.3.mathml_attribute_in_component_ref](../models_1_0/invalid/2.4.3.mathml_attribute_in_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected attribute mathml:sum```
* Output: ```Error on line 12. Unexpected attribute mathml:sum found in cellml:component_ref.```

[2.4.3.mathml_attribute_in_connection](../models_1_0/invalid/2.4.3.mathml_attribute_in_connection.cellml): Error detected correctly.
* Expected: ```Unexpected attribute mathml:sum```
* Output: ```Error on line 13. Unexpected attribute mathml:sum found in cellml:connection.```

[2.4.3.mathml_attribute_in_group](../models_1_0/invalid/2.4.3.mathml_attribute_in_group.cellml): Error detected correctly.
* Expected: ```Unexpected attribute mathml:sum```
* Output: ```Error on line 9. Unexpected attribute mathml:sum found in cellml:group.```

[2.4.3.mathml_attribute_in_map_components](../models_1_0/invalid/2.4.3.mathml_attribute_in_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected attribute mathml:sum```
* Output: ```Error on line 8. Unexpected attribute mathml:sum found in cellml:map_components.```

[2.4.3.mathml_attribute_in_map_variables](../models_1_0/invalid/2.4.3.mathml_attribute_in_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected attribute mathml:sum```
* Output: ```Error on line 15. Unexpected attribute mathml:sum found in cellml:map_variables.```

[2.4.3.mathml_attribute_in_model](../models_1_0/invalid/2.4.3.mathml_attribute_in_model.cellml): Error detected correctly.
* Expected: ```Unexpected attribute mathml:sum```
* Output: ```Error on line 7. Unexpected attribute mathml:sum found in cellml:model[@name="mathml_attribute_in_model"].```

🔶 [2.4.3.mathml_attribute_in_reaction](../models_1_0/invalid/2.4.3.mathml_attribute_in_reaction.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.mathml_attribute_in_relationship_ref](../models_1_0/invalid/2.4.3.mathml_attribute_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected attribute mathml:sum```
* Output: ```Error on line 10. Unexpected attribute mathml:sum found in cellml:relationship_ref.```

🔶 [2.4.3.mathml_attribute_in_role](../models_1_0/invalid/2.4.3.mathml_attribute_in_role.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.mathml_attribute_in_unit](../models_1_0/invalid/2.4.3.mathml_attribute_in_unit.cellml): Error detected correctly.
* Expected: ```Unexpected attribute mathml:sum```
* Output: ```Error on line 8. Unexpected attribute mathml:sum found in cellml:unit.```

[2.4.3.mathml_attribute_in_units_1](../models_1_0/invalid/2.4.3.mathml_attribute_in_units_1.cellml): Error detected correctly.
* Expected: ```Unexpected attribute mathml:sum```
* Output: ```Error on line 7. Unexpected attribute mathml:sum found in cellml:units[@name="orange"].```

[2.4.3.mathml_attribute_in_units_2](../models_1_0/invalid/2.4.3.mathml_attribute_in_units_2.cellml): Error detected correctly.
* Expected: ```Unexpected attribute mathml:sum```
* Output: ```Error on line 8. Unexpected attribute mathml:sum found in cellml:units[@name="apple"].```

[2.4.3.mathml_attribute_in_variable](../models_1_0/invalid/2.4.3.mathml_attribute_in_variable.cellml): Error detected correctly.
* Expected: ```Unexpected attribute mathml:sum```
* Output: ```Error on line 8. Unexpected attribute mathml:sum found in cellml:variable[@name="a"].```

🔶 [2.4.3.mathml_attribute_in_variable_ref](../models_1_0/invalid/2.4.3.mathml_attribute_in_variable_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.model_with_extensions](../models_1_0/valid/2.4.3.model_with_extensions.cellml): Valid file passed validation.

[2.4.3.rdf_attribute_in_component](../models_1_0/invalid/2.4.3.rdf_attribute_in_component.cellml): Error detected correctly.
* Expected: ```Unexpected attribute rdf:parseType```
* Output: ```Error on line 7. Unexpected attribute rdf:parseType found in cellml:component[@name="A"].```

[2.4.3.rdf_attribute_in_component_ref](../models_1_0/invalid/2.4.3.rdf_attribute_in_component_ref.cellml): Error detected correctly.
* Expected: ```Unexpected attribute rdf:parseType```
* Output: ```Error on line 12. Unexpected attribute rdf:parseType found in cellml:component_ref.```

[2.4.3.rdf_attribute_in_connection](../models_1_0/invalid/2.4.3.rdf_attribute_in_connection.cellml): Error detected correctly.
* Expected: ```Unexpected attribute rdf:parseType```
* Output: ```Error on line 13. Unexpected attribute rdf:parseType found in cellml:connection.```

[2.4.3.rdf_attribute_in_group](../models_1_0/invalid/2.4.3.rdf_attribute_in_group.cellml): Error detected correctly.
* Expected: ```Unexpected attribute rdf:parseType```
* Output: ```Error on line 9. Unexpected attribute rdf:parseType found in cellml:group.```

[2.4.3.rdf_attribute_in_map_components](../models_1_0/invalid/2.4.3.rdf_attribute_in_map_components.cellml): Error detected correctly.
* Expected: ```Unexpected attribute rdf:parseType```
* Output: ```Error on line 8. Unexpected attribute rdf:parseType found in cellml:map_components.```

[2.4.3.rdf_attribute_in_map_variables](../models_1_0/invalid/2.4.3.rdf_attribute_in_map_variables.cellml): Error detected correctly.
* Expected: ```Unexpected attribute rdf:parseType```
* Output: ```Error on line 15. Unexpected attribute rdf:parseType found in cellml:map_variables.```

[2.4.3.rdf_attribute_in_model](../models_1_0/invalid/2.4.3.rdf_attribute_in_model.cellml): Error detected correctly.
* Expected: ```Unexpected attribute rdf:parseType```
* Output: ```Error on line 7. Unexpected attribute rdf:parseType found in cellml:model[@name="mathml_attribute_in_model"].```

🔶 [2.4.3.rdf_attribute_in_reaction](../models_1_0/invalid/2.4.3.rdf_attribute_in_reaction.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.rdf_attribute_in_relationship_ref](../models_1_0/invalid/2.4.3.rdf_attribute_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```Unexpected attribute rdf:parseType```
* Output: ```Error on line 10. Unexpected attribute rdf:parseType found in cellml:relationship_ref.```

🔶 [2.4.3.rdf_attribute_in_role](../models_1_0/invalid/2.4.3.rdf_attribute_in_role.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.rdf_attribute_in_unit](../models_1_0/invalid/2.4.3.rdf_attribute_in_unit.cellml): Error detected correctly.
* Expected: ```Unexpected attribute rdf:parseType```
* Output: ```Error on line 8. Unexpected attribute rdf:parseType found in cellml:unit.```

[2.4.3.rdf_attribute_in_units_1](../models_1_0/invalid/2.4.3.rdf_attribute_in_units_1.cellml): Error detected correctly.
* Expected: ```Unexpected attribute rdf:parseType```
* Output: ```Error on line 7. Unexpected attribute rdf:parseType found in cellml:units[@name="orange"].```

[2.4.3.rdf_attribute_in_units_2](../models_1_0/invalid/2.4.3.rdf_attribute_in_units_2.cellml): Error detected correctly.
* Expected: ```Unexpected attribute rdf:parseType```
* Output: ```Error on line 8. Unexpected attribute rdf:parseType found in cellml:units[@name="apple"].```

[2.4.3.rdf_attribute_in_variable](../models_1_0/invalid/2.4.3.rdf_attribute_in_variable.cellml): Error detected correctly.
* Expected: ```Unexpected attribute rdf:parseType```
* Output: ```Error on line 8. Unexpected attribute rdf:parseType found in cellml:variable[@name="a"].```

🔶 [2.4.3.rdf_attribute_in_variable_ref](../models_1_0/invalid/2.4.3.rdf_attribute_in_variable_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

🔴 [2.4.3.reaction_with_extensions](../models_1_0/valid/2.4.3.reaction_with_extensions.cellml): **Valid file failed validation.**
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.relationship_ref_with_extensions](../models_1_0/valid/2.4.3.relationship_ref_with_extensions.cellml): Valid file passed validation.

🔴 [2.4.3.role_with_extensions](../models_1_0/valid/2.4.3.role_with_extensions.cellml): **Valid file failed validation.**
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.unit_with_extensions](../models_1_0/valid/2.4.3.unit_with_extensions.cellml): Valid file passed validation.

[2.4.3.units_with_extensions](../models_1_0/valid/2.4.3.units_with_extensions.cellml): Valid file passed validation.

🔴 [2.4.3.variable_ref_with_extensions](../models_1_0/valid/2.4.3.variable_ref_with_extensions.cellml): **Valid file failed validation.**
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.variable_with_extensions](../models_1_0/valid/2.4.3.variable_with_extensions.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_component](../models_1_0/valid/2.4.3.xlink_href_in_component.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_component_ref](../models_1_0/valid/2.4.3.xlink_href_in_component_ref.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_connection](../models_1_0/valid/2.4.3.xlink_href_in_connection.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_group](../models_1_0/valid/2.4.3.xlink_href_in_group.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_map_components](../models_1_0/valid/2.4.3.xlink_href_in_map_components.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_map_variables](../models_1_0/valid/2.4.3.xlink_href_in_map_variables.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_model](../models_1_0/valid/2.4.3.xlink_href_in_model.cellml): Valid file passed validation.

🔴 [2.4.3.xlink_href_in_reaction](../models_1_0/valid/2.4.3.xlink_href_in_reaction.cellml): **Valid file failed validation.**
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.xlink_href_in_relationship_ref](../models_1_0/valid/2.4.3.xlink_href_in_relationship_ref.cellml): Valid file passed validation.

🔴 [2.4.3.xlink_href_in_role](../models_1_0/valid/2.4.3.xlink_href_in_role.cellml): **Valid file failed validation.**
* Output: ```Error on line 9. Reactions are not supported.```

[2.4.3.xlink_href_in_unit](../models_1_0/valid/2.4.3.xlink_href_in_unit.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_units_1](../models_1_0/valid/2.4.3.xlink_href_in_units_1.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_units_2](../models_1_0/valid/2.4.3.xlink_href_in_units_2.cellml): Valid file passed validation.

[2.4.3.xlink_href_in_variable](../models_1_0/valid/2.4.3.xlink_href_in_variable.cellml): Valid file passed validation.

🔴 [2.4.3.xlink_href_in_variable_ref](../models_1_0/valid/2.4.3.xlink_href_in_variable_ref.cellml): **Valid file failed validation.**
* Output: ```Error on line 9. Reactions are not supported.```


---

#### 2.4.4

[2.4.4.model_linux_line_breaks](../models_1_0/valid/2.4.4.model_linux_line_breaks.cellml): Valid file passed validation.

[2.4.4.model_windows_line_breaks](../models_1_0/valid/2.4.4.model_windows_line_breaks.cellml): Valid file passed validation.

[2.4.4.model_with_spaces](../models_1_0/valid/2.4.4.model_with_spaces.cellml): Valid file passed validation.

[2.4.4.model_with_tabs](../models_1_0/valid/2.4.4.model_with_tabs.cellml): Valid file passed validation.

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


---

## 3. Model structure

##### 3.4.1.1

[3.4.1.1.model_child_order_1](../models_1_0/valid/3.4.1.1.model_child_order_1.cellml): Valid file passed validation.

[3.4.1.1.model_child_order_2](../models_1_0/valid/3.4.1.1.model_child_order_2.cellml): Valid file passed validation.

[3.4.1.1.model_empty](../models_1_0/valid/3.4.1.1.model_empty.cellml): Valid file passed validation.

[3.4.1.1.model_name_missing](../models_1_0/invalid/3.4.1.1.model_name_missing.cellml): Error detected correctly.
* Expected: ```must have a name attribute```
* Output: ```Error on line 4. Model element must have a name attribute (3.4.1.1).```

[3.4.1.1.model_with_component_ref](../models_1_0/invalid/3.4.1.1.model_with_component_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component_ref```
* Output: ```Error on line 6. Unexpected content type in cellml:model[@name="model_with_component_ref"], found element of type cellml:component_ref.```

[3.4.1.1.model_with_components](../models_1_0/valid/3.4.1.1.model_with_components.cellml): Valid file passed validation.

[3.4.1.1.model_with_connections](../models_1_0/valid/3.4.1.1.model_with_connections.cellml): Valid file passed validation.

[3.4.1.1.model_with_groups](../models_1_0/valid/3.4.1.1.model_with_groups.cellml): Valid file passed validation.

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

[3.4.1.1.model_with_one_component](../models_1_0/valid/3.4.1.1.model_with_one_component.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_connection](../models_1_0/valid/3.4.1.1.model_with_one_connection.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_group](../models_1_0/valid/3.4.1.1.model_with_one_group.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_units](../models_1_0/valid/3.4.1.1.model_with_one_units.cellml): Valid file passed validation.

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

[3.4.1.1.model_with_units](../models_1_0/valid/3.4.1.1.model_with_units.cellml): Valid file passed validation.

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


---

##### 3.4.2.1

🔴 [3.4.2.1.component_child_order_1](../models_1_0/valid/3.4.2.1.component_child_order_1.cellml): **Valid file failed validation.**
* Output: ```Error on line 20. Reactions are not supported.```

🔴 [3.4.2.1.component_child_order_2](../models_1_0/valid/3.4.2.1.component_child_order_2.cellml): **Valid file failed validation.**
* Output: ```Error on line 10. Reactions are not supported.```

[3.4.2.1.component_empty](../models_1_0/valid/3.4.2.1.component_empty.cellml): Valid file passed validation.

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

[3.4.2.1.component_with_maths](../models_1_0/valid/3.4.2.1.component_with_maths.cellml): Valid file passed validation.

[3.4.2.1.component_with_model](../models_1_0/invalid/3.4.2.1.component_with_model.cellml): Error detected correctly.
* Expected: ```found element of type cellml:model```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="c1"], found element of type cellml:model.```

[3.4.2.1.component_with_one_math](../models_1_0/valid/3.4.2.1.component_with_one_math.cellml): Valid file passed validation.

🔴 [3.4.2.1.component_with_one_reaction](../models_1_0/valid/3.4.2.1.component_with_one_reaction.cellml): **Valid file failed validation.**
* Output: ```Error on line 8. Reactions are not supported.```

[3.4.2.1.component_with_one_units](../models_1_0/valid/3.4.2.1.component_with_one_units.cellml): Valid file passed validation.

[3.4.2.1.component_with_one_variable](../models_1_0/valid/3.4.2.1.component_with_one_variable.cellml): Valid file passed validation.

🔴 [3.4.2.1.component_with_reactions](../models_1_0/valid/3.4.2.1.component_with_reactions.cellml): **Valid file failed validation.**
* Output: ```Error on line 9. Reactions are not supported.```

[3.4.2.1.component_with_relationship_ref](../models_1_0/invalid/3.4.2.1.component_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:relationship_ref```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="component"], found element of type cellml:relationship_ref.```

[3.4.2.1.component_with_role](../models_1_0/invalid/3.4.2.1.component_with_role.cellml): Error detected correctly.
* Expected: ```found element of type cellml:role```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="component"], found element of type cellml:role.```

[3.4.2.1.component_with_unit](../models_1_0/invalid/3.4.2.1.component_with_unit.cellml): Error detected correctly.
* Expected: ```found element of type cellml:unit```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="component"], found element of type cellml:unit.```

[3.4.2.1.component_with_units](../models_1_0/valid/3.4.2.1.component_with_units.cellml): Valid file passed validation.

[3.4.2.1.component_with_variable_ref](../models_1_0/invalid/3.4.2.1.component_with_variable_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable_ref```
* Output: ```Error on line 7. Unexpected content type in cellml:component[@name="component"], found element of type cellml:variable_ref.```

[3.4.2.1.component_with_variables](../models_1_0/valid/3.4.2.1.component_with_variables.cellml): Valid file passed validation.


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

[3.4.3.1.variable_with_initial_value](../models_1_0/valid/3.4.3.1.variable_with_initial_value.cellml): Valid file passed validation.

[3.4.3.1.variable_with_interfaces](../models_1_0/valid/3.4.3.1.variable_with_interfaces.cellml): Valid file passed validation.

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

[3.4.3.1.variable_without_initial_value](../models_1_0/valid/3.4.3.1.variable_without_initial_value.cellml): Valid file passed validation.


---

##### 3.4.3.2

[3.4.3.2.variable_name_duplicate](../models_1_0/invalid/3.4.3.2.variable_name_duplicate.cellml): Error detected correctly.
* Expected: ```Variable name must be unique```
* Output: ```Error on line 8. Variable name must be unique within Component (3.4.3.2).```

[3.4.3.2.variable_name_invalid](../models_1_0/invalid/3.4.3.2.variable_name_invalid.cellml): Error detected correctly.
* Expected: ```Variable name must be a valid CellML identifier```
* Output: ```Error on line 7. Variable name must be a valid CellML identifier (3.4.3.2).```

[3.4.3.2.variable_name_same_as_cousin](../models_1_0/valid/3.4.3.2.variable_name_same_as_cousin.cellml): Valid file passed validation.

[3.4.3.2.variable_name_same_as_parent](../models_1_0/valid/3.4.3.2.variable_name_same_as_parent.cellml): Valid file passed validation.


---

##### 3.4.3.3

[3.4.3.3.variable_units_component](../models_1_0/valid/3.4.3.3.variable_units_component.cellml): Valid file passed validation.

[3.4.3.3.variable_units_model](../models_1_0/valid/3.4.3.3.variable_units_model.cellml): Valid file passed validation.

[3.4.3.3.variable_units_other_component](../models_1_0/invalid/3.4.3.3.variable_units_other_component.cellml): Error detected correctly.
* Expected: ```must reference a units element```
* Output: ```Error on line 7. Variable units attribute must reference a units element in the current component or model, or one of the predefined units, found "oranges" (3.4.3.3).```

[3.4.3.3.variable_units_predefined](../models_1_0/valid/3.4.3.3.variable_units_predefined.cellml): Valid file passed validation.

[3.4.3.3.variable_units_unknown](../models_1_0/invalid/3.4.3.3.variable_units_unknown.cellml): Error detected correctly.
* Expected: ```must reference a units element```
* Output: ```Error on line 7. Variable units attribute must reference a units element in the current component or model, or one of the predefined units, found "oranges" (3.4.3.3).```


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

[3.4.4.1.connection_with_map_variables](../models_1_0/valid/3.4.4.1.connection_with_map_variables.cellml): Valid file passed validation.

[3.4.4.1.connection_with_math](../models_1_0/invalid/3.4.4.1.connection_with_math.cellml): Error detected correctly.
* Expected: ```found element of type mathml:math```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type mathml:math.```

[3.4.4.1.connection_with_model](../models_1_0/invalid/3.4.4.1.connection_with_model.cellml): Error detected correctly.
* Expected: ```found element of type cellml:model```
* Output: ```Error on line 16. Unexpected content type in cellml:connection, found element of type cellml:model.```

[3.4.4.1.connection_with_name_attribute](../models_1_0/invalid/3.4.4.1.connection_with_name_attribute.cellml): Error detected correctly.
* Expected: ```Unexpected attribute name```
* Output: ```Error on line 12. Unexpected attribute name found in cellml:connection.```

[3.4.4.1.connection_with_one_map_variables](../models_1_0/valid/3.4.4.1.connection_with_one_map_variables.cellml): Valid file passed validation.

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


---

##### 3.4.5.1

[3.4.5.1.connection_any_order_1](../models_1_0/valid/3.4.5.1.connection_any_order_1.cellml): Valid file passed validation.

[3.4.5.1.connection_any_order_2](../models_1_0/valid/3.4.5.1.connection_any_order_2.cellml): Valid file passed validation.

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

[3.4.6.1.map_variables_duplicate_1](../models_1_0/duplicate_connections/3.4.6.1.map_variables_duplicate_1.cellml): Error detected correctly.
* Expected: ```already connected```
* Output: ```Error on line 16. Invalid connection: Variable[@name="b"] in Component[@name="B"] is already connected to Variable[@name="a"] in Component[@name="A"].```

[3.4.6.1.map_variables_duplicate_2](../models_1_0/duplicate_connections/3.4.6.1.map_variables_duplicate_2.cellml): Error detected correctly.
* Expected: ```already connected```
* Output: ```Error on line 16. Invalid connection: Variable[@name="a"] in Component[@name="A"] is already connected to Variable[@name="b"] in Component[@name="B"].```

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


---

##### 3.4.6.4

[3.4.6.4.map_variables_chain_down](../models_1_0/valid/3.4.6.4.map_variables_chain_down.cellml): Valid file passed validation.

[3.4.6.4.map_variables_chain_up](../models_1_0/valid/3.4.6.4.map_variables_chain_up.cellml): Valid file passed validation.

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

[3.4.6.4.map_variables_hidden_aunt_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_aunt_1.cellml): Error detected correctly.
* Expected: ```between components that are siblings or have a parent-child```
* Output: ```Error on line 29. Connections can only be made between components that are siblings or have a parent-child (encapsulation) relationship (3.4.6.4).```

[3.4.6.4.map_variables_hidden_aunt_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_aunt_2.cellml): Error detected correctly.
* Expected: ```between components that are siblings or have a parent-child```
* Output: ```Error on line 29. Connections can only be made between components that are siblings or have a parent-child (encapsulation) relationship (3.4.6.4).```

[3.4.6.4.map_variables_hidden_cousins_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_1.cellml): Error detected correctly.
* Expected: ```between components that are siblings or have a parent-child```
* Output: ```Error on line 30. Connections can only be made between components that are siblings or have a parent-child (encapsulation) relationship (3.4.6.4).```

[3.4.6.4.map_variables_hidden_cousins_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_2.cellml): Error detected correctly.
* Expected: ```between components that are siblings or have a parent-child```
* Output: ```Error on line 30. Connections can only be made between components that are siblings or have a parent-child (encapsulation) relationship (3.4.6.4).```

[3.4.6.4.map_variables_hidden_cousins_3](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_3.cellml): Error detected correctly.
* Expected: ```between components that are siblings or have a parent-child```
* Output: ```Error on line 30. Connections can only be made between components that are siblings or have a parent-child (encapsulation) relationship (3.4.6.4).```

[3.4.6.4.map_variables_hidden_cousins_4](../models_1_0/invalid/3.4.6.4.map_variables_hidden_cousins_4.cellml): Error detected correctly.
* Expected: ```between components that are siblings or have a parent-child```
* Output: ```Error on line 30. Connections can only be made between components that are siblings or have a parent-child (encapsulation) relationship (3.4.6.4).```

[3.4.6.4.map_variables_hidden_grandchild_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandchild_1.cellml): Error detected correctly.
* Expected: ```between components that are siblings or have a parent-child```
* Output: ```Error on line 26. Connections can only be made between components that are siblings or have a parent-child (encapsulation) relationship (3.4.6.4).```

[3.4.6.4.map_variables_hidden_grandchild_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandchild_2.cellml): Error detected correctly.
* Expected: ```between components that are siblings or have a parent-child```
* Output: ```Error on line 26. Connections can only be made between components that are siblings or have a parent-child (encapsulation) relationship (3.4.6.4).```

[3.4.6.4.map_variables_hidden_grandparent_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandparent_1.cellml): Error detected correctly.
* Expected: ```between components that are siblings or have a parent-child```
* Output: ```Error on line 26. Connections can only be made between components that are siblings or have a parent-child (encapsulation) relationship (3.4.6.4).```

[3.4.6.4.map_variables_hidden_grandparent_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_grandparent_2.cellml): Error detected correctly.
* Expected: ```between components that are siblings or have a parent-child```
* Output: ```Error on line 26. Connections can only be made between components that are siblings or have a parent-child (encapsulation) relationship (3.4.6.4).```

[3.4.6.4.map_variables_hidden_niece_1](../models_1_0/invalid/3.4.6.4.map_variables_hidden_niece_1.cellml): Error detected correctly.
* Expected: ```between components that are siblings or have a parent-child```
* Output: ```Error on line 29. Connections can only be made between components that are siblings or have a parent-child (encapsulation) relationship (3.4.6.4).```

[3.4.6.4.map_variables_hidden_niece_2](../models_1_0/invalid/3.4.6.4.map_variables_hidden_niece_2.cellml): Error detected correctly.
* Expected: ```between components that are siblings or have a parent-child```
* Output: ```Error on line 29. Connections can only be made between components that are siblings or have a parent-child (encapsulation) relationship (3.4.6.4).```

[3.4.6.4.map_variables_nested_sibling_connection](../models_1_0/valid/3.4.6.4.map_variables_nested_sibling_connection.cellml): Valid file passed validation.

[3.4.6.4.map_variables_nested_sibling_private_in](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_in.cellml): Error detected correctly.
* Expected: ```public_interface of "none"```
* Output: ```Error on line 23. Invalid connection: Variable[@name="a"] in Component[@name="B"] has a public_interface of "out", while Variable[@name="a"] in Component[@name="C"] has a public_interface of "none" (3.4.6.4).```

[3.4.6.4.map_variables_nested_sibling_private_in_and_out](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_in_and_out.cellml): Error detected correctly.
* Expected: ```public_interface of "none"```
* Output: ```Error on line 23. Invalid connection: Variable[@name="a"] in Component[@name="B"] has a public_interface of "none", while Variable[@name="a"] in Component[@name="C"] has a public_interface of "none" (3.4.6.4).```

[3.4.6.4.map_variables_nested_sibling_private_out](../models_1_0/invalid/3.4.6.4.map_variables_nested_sibling_private_out.cellml): Error detected correctly.
* Expected: ```public_interface of "none"```
* Output: ```Error on line 23. Invalid connection: Variable[@name="a"] in Component[@name="B"] has a public_interface of "none", while Variable[@name="a"] in Component[@name="C"] has a public_interface of "in" (3.4.6.4).```

[3.4.6.4.map_variables_parent_connection_1](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_connection_2](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_in_to_in_1](../models_1_0/invalid/3.4.6.4.map_variables_parent_in_to_in_1.cellml): Error detected correctly.
* Expected: ```public_interface of "in"```
* Output: ```Error on line 22. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a private_interface of "in", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "in" (3.4.6.4).```

[3.4.6.4.map_variables_parent_in_to_in_2](../models_1_0/invalid/3.4.6.4.map_variables_parent_in_to_in_2.cellml): Error detected correctly.
* Expected: ```public_interface of "in"```
* Output: ```Error on line 22. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a private_interface of "in", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "in" (3.4.6.4).```

[3.4.6.4.map_variables_parent_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_multiple_out](../models_1_0/invalid/3.4.6.4.map_variables_parent_multiple_out.cellml): Error detected correctly.
* Expected: ```already connected```
* Output: ```Error on line 24. Invalid connection: Variable[@name="x"] in Component[@name="B"] has a private_interface of "in" and is already connected to a variable with an interface of "out".```

[3.4.6.4.map_variables_parent_out_to_out_1](../models_1_0/invalid/3.4.6.4.map_variables_parent_out_to_out_1.cellml): Error detected correctly.
* Expected: ```public_interface of "out"```
* Output: ```Error on line 23. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a private_interface of "out", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "out" (3.4.6.4).```

[3.4.6.4.map_variables_parent_out_to_out_2](../models_1_0/invalid/3.4.6.4.map_variables_parent_out_to_out_2.cellml): Error detected correctly.
* Expected: ```public_interface of "out"```
* Output: ```Error on line 23. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a private_interface of "out", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "out" (3.4.6.4).```

[3.4.6.4.map_variables_parent_public_in](../models_1_0/invalid/3.4.6.4.map_variables_parent_public_in.cellml): Error detected correctly.
* Expected: ```private_interface of "none"```
* Output: ```Error on line 23. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a private_interface of "none", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "out" (3.4.6.4).```

[3.4.6.4.map_variables_parent_public_out](../models_1_0/invalid/3.4.6.4.map_variables_parent_public_out.cellml): Error detected correctly.
* Expected: ```private_interface of "none"```
* Output: ```Error on line 23. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a private_interface of "none", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "in" (3.4.6.4).```

[3.4.6.4.map_variables_sibling_connection_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_connection_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_connection_3](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_3.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_in_to_in](../models_1_0/invalid/3.4.6.4.map_variables_sibling_in_to_in.cellml): Error detected correctly.
* Expected: ```public_interface of "in"```
* Output: ```Error on line 14. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a public_interface of "in", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "in" (3.4.6.4).```

[3.4.6.4.map_variables_sibling_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_multiple_out_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_multiple_out_1.cellml): Error detected correctly.
* Expected: ```already connected```
* Output: ```Error on line 16. Invalid connection: Variable[@name="x"] in Component[@name="B"] has a public_interface of "in" and is already connected to a variable with an interface of "out".```

[3.4.6.4.map_variables_sibling_multiple_out_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_multiple_out_2.cellml): Error detected correctly.
* Expected: ```already connected```
* Output: ```Error on line 21. Invalid connection: Variable[@name="a"] in Component[@name="C"] has a public_interface of "in" and is already connected to a variable with an interface of "out".```

[3.4.6.4.map_variables_sibling_mutual](../models_1_0/valid/3.4.6.4.map_variables_sibling_mutual.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_out_to_out](../models_1_0/invalid/3.4.6.4.map_variables_sibling_out_to_out.cellml): Error detected correctly.
* Expected: ```public_interface of "out"```
* Output: ```Error on line 14. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a public_interface of "out", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "out" (3.4.6.4).```

[3.4.6.4.map_variables_sibling_private_in_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_1.cellml): Error detected correctly.
* Expected: ```public_interface of "out"```
* Output: ```Error on line 14. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a public_interface of "none", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "out" (3.4.6.4).```

[3.4.6.4.map_variables_sibling_private_in_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_2.cellml): Error detected correctly.
* Expected: ```public_interface of "out"```
* Output: ```Error on line 14. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a public_interface of "out", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "out" (3.4.6.4).```

[3.4.6.4.map_variables_sibling_private_in_and_out](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_in_and_out.cellml): Error detected correctly.
* Expected: ```public_interface of "none"```
* Output: ```Error on line 14. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a public_interface of "none", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "none" (3.4.6.4).```

[3.4.6.4.map_variables_sibling_private_out_1](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_out_1.cellml): Error detected correctly.
* Expected: ```public_interface of "none"```
* Output: ```Error on line 14. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a public_interface of "in", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "none" (3.4.6.4).```

[3.4.6.4.map_variables_sibling_private_out_2](../models_1_0/invalid/3.4.6.4.map_variables_sibling_private_out_2.cellml): Error detected correctly.
* Expected: ```public_interface of "in"```
* Output: ```Error on line 14. Invalid connection: Variable[@name="a"] in Component[@name="A"] has a public_interface of "in", while Variable[@name="a"] in Component[@name="B"] has a public_interface of "in" (3.4.6.4).```

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
* Output: ```Error on line 21. Numbers in bases other than 10 are not supported.```

[4.2.3_2.4.mathml_numbers_integer_base](../models_1_0/numbers/4.2.3_2.4.mathml_numbers_integer_base.cellml): Valid file passed validation.

[4.2.3_2.5.mathml_numbers_e_notation](../models_1_0/numbers/4.2.3_2.5.mathml_numbers_e_notation.cellml): Valid file passed validation.

[4.2.3_2.6.mathml_numbers_rational](../models_1_0/numbers/4.2.3_2.6.mathml_numbers_rational.cellml): Valid file passed validation.

[4.2.3_3.1_mathml_arithmetic_binary](../models_1_0/valid/4.2.3_3.1_mathml_arithmetic_binary.cellml): Valid file passed validation.

[4.2.3_3.2_mathml_arithmetic_n_ary](../models_1_0/valid/4.2.3_3.2_mathml_arithmetic_n_ary.cellml): Valid file passed validation.

[4.2.3_3.2_mathml_arithmetic_unary](../models_1_0/valid/4.2.3_3.2_mathml_arithmetic_unary.cellml): Valid file passed validation.

[4.2.3_4.1_mathml_functions_basic](../models_1_0/valid/4.2.3_4.1_mathml_functions_basic.cellml): Valid file passed validation.

[4.2.3_4.2_mathml_functions_non_smooth](../models_1_0/valid/4.2.3_4.2_mathml_functions_non_smooth.cellml): Valid file passed validation.

🔴 [4.2.3_4.3_mathml_functions_factorial](../models_1_0/valid/4.2.3_4.3_mathml_functions_factorial.cellml): **Valid file failed validation.**
* Output: ```Error on line 15. Unsupported element in apply: {http://www.w3.org/1998/Math/MathML}factorial.```

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
* Expected: ```Unsupported element```
* Output: ```Error on line 13. Unsupported element: {http://www.w3.org/1998/Math/MathML}cake.```

🔶 [4.4.1.math_not_math_reaction](../models_1_0/invalid/4.4.1.math_not_math_reaction.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```


---

#### 4.4.2

[4.4.2.ci_no_whitespace](../models_1_0/valid/4.4.2.ci_no_whitespace.cellml): Valid file passed validation.

[4.4.2.ci_non_local_aunt](../models_1_0/invalid/4.4.2.ci_non_local_aunt.cellml): Error detected correctly.
* Expected: ```references in equation must name a variable from the local component```
* Output: ```Error on line 17. Unable to create Name: Error on line 17. Variable references in equation must name a variable from the local component (4.4.2.1).```

[4.4.2.ci_non_local_child](../models_1_0/invalid/4.4.2.ci_non_local_child.cellml): Error detected correctly.
* Expected: ```references in equation must name a variable from the local component```
* Output: ```Error on line 16. Unable to create Name: Error on line 16. Variable references in equation must name a variable from the local component (4.4.2.1).```

[4.4.2.ci_non_local_cousin](../models_1_0/invalid/4.4.2.ci_non_local_cousin.cellml): Error detected correctly.
* Expected: ```references in equation must name a variable from the local component```
* Output: ```Error on line 17. Unable to create Name: Error on line 17. Variable references in equation must name a variable from the local component (4.4.2.1).```

[4.4.2.ci_non_local_nested_sibling](../models_1_0/invalid/4.4.2.ci_non_local_nested_sibling.cellml): Error detected correctly.
* Expected: ```references in equation must name a variable from the local component```
* Output: ```Error on line 17. Unable to create Name: Error on line 17. Variable references in equation must name a variable from the local component (4.4.2.1).```

[4.4.2.ci_non_local_niece](../models_1_0/invalid/4.4.2.ci_non_local_niece.cellml): Error detected correctly.
* Expected: ```references in equation must name a variable from the local component```
* Output: ```Error on line 20. Unable to create Name: Error on line 20. Variable references in equation must name a variable from the local component (4.4.2.1).```

[4.4.2.ci_non_local_parent](../models_1_0/invalid/4.4.2.ci_non_local_parent.cellml): Error detected correctly.
* Expected: ```references in equation must name a variable from the local component```
* Output: ```Error on line 19. Unable to create Name: Error on line 19. Variable references in equation must name a variable from the local component (4.4.2.1).```

[4.4.2.ci_non_local_sibling](../models_1_0/invalid/4.4.2.ci_non_local_sibling.cellml): Error detected correctly.
* Expected: ```references in equation must name a variable from the local component```
* Output: ```Error on line 19. Unable to create Name: Error on line 19. Variable references in equation must name a variable from the local component (4.4.2.1).```

[4.4.2.ci_nonexistent](../models_1_0/invalid/4.4.2.ci_nonexistent.cellml): Error detected correctly.
* Expected: ```references in equation must name a variable from the local component```
* Output: ```Error on line 16. Unable to create Name: Error on line 16. Variable references in equation must name a variable from the local component (4.4.2.1).```

[4.4.2.ci_whitespace_1](../models_1_0/valid/4.4.2.ci_whitespace_1.cellml): Valid file passed validation.

[4.4.2.ci_whitespace_2](../models_1_0/valid/4.4.2.ci_whitespace_2.cellml): Valid file passed validation.

[4.4.2.ci_whitespace_3](../models_1_0/valid/4.4.2.ci_whitespace_3.cellml): Valid file passed validation.


---

##### 4.4.3.1

[4.4.3.1.cn_component_units](../models_1_0/valid/4.4.3.1.cn_component_units.cellml): Valid file passed validation.

[4.4.3.1.cn_model_units](../models_1_0/valid/4.4.3.1.cn_model_units.cellml): Valid file passed validation.

[4.4.3.1.cn_predefined_units](../models_1_0/valid/4.4.3.1.cn_predefined_units.cellml): Valid file passed validation.

[4.4.3.1.cn_units_missing](../models_1_0/invalid/4.4.3.1.cn_units_missing.cellml): Error detected correctly.
* Expected: ```must define a cellml:units attribute```
* Output: ```Error on line 13. Numbers inside MathML must define a cellml:units attribute (4.4.3.1).```


---

##### 4.4.3.2

[4.4.3.2.cn_units_nonexistent_1](../models_1_0/invalid/4.4.3.2.cn_units_nonexistent_1.cellml): Error detected correctly.
* Expected: ```Unknown unit```
* Output: ```Error on line 15. Unknown unit "wooster" referenced inside a MathML equation (4.4.3.2).```

[4.4.3.2.cn_units_nonexistent_2](../models_1_0/invalid/4.4.3.2.cn_units_nonexistent_2.cellml): Error detected correctly.
* Expected: ```Unknown unit```
* Output: ```Error on line 17. Unknown unit "wooster" referenced inside a MathML equation (4.4.3.2).```

[4.4.3.2.cn_units_parent_component](../models_1_0/invalid/4.4.3.2.cn_units_parent_component.cellml): Error detected correctly.
* Expected: ```Unknown unit```
* Output: ```Error on line 21. Unknown unit "wooster" referenced inside a MathML equation (4.4.3.2).```


---

#### 4.4.4

🔶 [4.4.4.dae_public_in](../models_1_0/invalid/4.4.4.dae_public_in.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 31. Invalid expression found on the left-hand side of an equation: Each equation must have either a single variable or a derivative of a single variable as its left-hand side, and each variable may only appear on a left-hand side once.```

[4.4.4.modify_nonexistent](../models_1_0/invalid/4.4.4.modify_nonexistent.cellml): Error detected correctly.
* Expected: ```references in equation must name a variable from the local component```
* Output: ```Error on line 11. Unable to create Name: Error on line 11. Variable references in equation must name a variable from the local component (4.4.2.1).```

[4.4.4.modify_private_in](../models_1_0/invalid/4.4.4.modify_private_in.cellml): Error detected correctly.
* Expected: ```which has private_interface="in"```
* Output: ```Error on line 10. An equation cannot be set for Variable[@name="x"] in Component[@name="A"], which has private_interface="in" (4.4.4).```

[4.4.4.modify_private_out](../models_1_0/valid/4.4.4.modify_private_out.cellml): Valid file passed validation.

[4.4.4.modify_public_in](../models_1_0/invalid/4.4.4.modify_public_in.cellml): Error detected correctly.
* Expected: ```which has public_interface="in"```
* Output: ```Error on line 13. An equation cannot be set for Variable[@name="x"] in Component[@name="AA"], which has public_interface="in" (4.4.4).```

[4.4.4.modify_public_out](../models_1_0/valid/4.4.4.modify_public_out.cellml): Valid file passed validation.


---

#### 4.5.1

[4.5.1.ordering_not_significant](../models_1_0/valid/4.5.1.ordering_not_significant.cellml): Valid file passed validation.


---

🔴 [4.algebraic_model](../models_1_0/valid/4.algebraic_model.cellml): **Valid file failed validation.**
* Output: ```Error on line 11. Invalid expression found on the left-hand side of an equation: Each equation must have either a single variable or a derivative of a single variable as its left-hand side, and each variable may only appear on a left-hand side once.```

🔴 [4.algebraic_ode_model](../models_1_0/valid/4.algebraic_ode_model.cellml): **Valid file failed validation.**
* Output: ```Error on line 11. Invalid expression found on the left-hand side of an equation: Each equation must have either a single variable or a derivative of a single variable as its left-hand side, and each variable may only appear on a left-hand side once.```

[4.math_and_initial_value](../models_1_0/invalid/4.math_and_initial_value.cellml): Error detected correctly.
* Expected: ```appear on a left-hand side once```
* Output: ```Error on line 10. Initial value and a defining equation found for non-state Variable[@name="x"] in Component[@name="A"]: Each equation must have either a single variable or a derivative of a single variable as its left-hand side, and each variable may only appear on a left-hand side once.```

[4.math_overdefined](../models_1_0/invalid/4.math_overdefined.cellml): Error detected correctly.
* Expected: ```appear on a left-hand side once```
* Output: ```Error on line 15. Two defining equations found for Variable[@name="x"] in Component[@name="A"]: Each equation must have either a single variable or a derivative of a single variable as its left-hand side, and each variable may only appear on a left-hand side once.```

🔴 [4.overdefined_direct_and_direct](../models_1_0/overdefined/4.overdefined_direct_and_direct.cellml): **Valid file failed validation.**
* Output: ```Error on line 15. Two defining equations found for Variable[@name="x"] in Component[@name="A"]: Each equation must have either a single variable or a derivative of a single variable as its left-hand side, and each variable may only appear on a left-hand side once.```

🔴 [4.overdefined_direct_and_initial](../models_1_0/overdefined/4.overdefined_direct_and_initial.cellml): **Valid file failed validation.**
* Output: ```Error on line 10. Initial value and a defining equation found for non-state Variable[@name="x"] in Component[@name="A"]: Each equation must have either a single variable or a derivative of a single variable as its left-hand side, and each variable may only appear on a left-hand side once.```

🔴 [4.overdefined_direct_and_ode](../models_1_0/overdefined/4.overdefined_direct_and_ode.cellml): **Valid file failed validation.**
* Output: ```Error on line 20. Two defining equations found for Variable[@name="x"] in Component[@name="A"]: Each equation must have either a single variable or a derivative of a single variable as its left-hand side, and each variable may only appear on a left-hand side once.```

🔴 [4.overdefined_ode_and_ode](../models_1_0/overdefined/4.overdefined_ode_and_ode.cellml): **Valid file failed validation.**
* Output: ```Error on line 26. Two defining equations found for Variable[@name="x"] in Component[@name="A"]: Each equation must have either a single variable or a derivative of a single variable as its left-hand side, and each variable may only appear on a left-hand side once.```


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
* Output: ```OK```


---

#### 5.2.7

[5.2.7.unit_checking_aliases](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_aliases.cellml): Valid file passed validation.

[5.2.7.unit_checking_arithmetic](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_arithmetic.cellml): Valid file passed validation.

[5.2.7.unit_checking_comparisons](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_comparisons.cellml): Valid file passed validation.

[5.2.7.unit_checking_derivatives](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_derivatives.cellml): Valid file passed validation.

[5.2.7.unit_checking_derivatives_degree](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_derivatives_degree.cellml): Valid file passed validation.

[5.2.7.unit_checking_dimensionless](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_dimensionless.cellml): Valid file passed validation.

🔴 [5.2.7.unit_checking_functions_factorial](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_functions_factorial.cellml): **Valid file failed validation.**
* Output: ```Error on line 14. Unsupported element in apply: {http://www.w3.org/1998/Math/MathML}factorial.```

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
* Output: ```OK```

[5.4.1.1.units_empty_1](../models_1_0/units_empty/5.4.1.1.units_empty_1.cellml): Error detected correctly.
* Expected: ```at least one child unit element```
* Output: ```Units element with base_units="no" must contain at least one child unit element.```

[5.4.1.1.units_empty_2](../models_1_0/units_empty/5.4.1.1.units_empty_2.cellml): Error detected correctly.
* Expected: ```at least one child unit element```
* Output: ```Units element with base_units="no" must contain at least one child unit element.```

[5.4.1.1.units_name_missing](../models_1_0/invalid/5.4.1.1.units_name_missing.cellml): Error detected correctly.
* Expected: ```Units element must have a name attribute```
* Output: ```Error on line 5. Units element must have a name attribute (5.4.1.1).```

[5.4.1.1.units_with_component](../models_1_0/invalid/5.4.1.1.units_with_component.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component```
* Output: ```Error on line 8. Unexpected content type in cellml:units[@name="wooster"], found element of type cellml:component.```

[5.4.1.1.units_with_component_ref](../models_1_0/invalid/5.4.1.1.units_with_component_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component_ref```
* Output: ```Error on line 8. Unexpected content type in cellml:units[@name="wooster"], found element of type cellml:component_ref.```

[5.4.1.1.units_with_connection](../models_1_0/invalid/5.4.1.1.units_with_connection.cellml): Error detected correctly.
* Expected: ```found element of type cellml:connection```
* Output: ```Error on line 14. Unexpected content type in cellml:units[@name="wooster"], found element of type cellml:connection.```

[5.4.1.1.units_with_group](../models_1_0/invalid/5.4.1.1.units_with_group.cellml): Error detected correctly.
* Expected: ```found element of type cellml:group```
* Output: ```Error on line 8. Unexpected content type in cellml:units[@name="wooster"], found element of type cellml:group.```

[5.4.1.1.units_with_map_components](../models_1_0/invalid/5.4.1.1.units_with_map_components.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_components```
* Output: ```Error on line 8. Unexpected content type in cellml:units[@name="wooster"], found element of type cellml:map_components.```

[5.4.1.1.units_with_map_variables](../models_1_0/invalid/5.4.1.1.units_with_map_variables.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_variables```
* Output: ```Error on line 8. Unexpected content type in cellml:units[@name="wooster"], found element of type cellml:map_variables.```

[5.4.1.1.units_with_math](../models_1_0/invalid/5.4.1.1.units_with_math.cellml): Error detected correctly.
* Expected: ```found element of type mathml:math```
* Output: ```Error on line 11. Unexpected content type in cellml:units[@name="wooster"], found element of type mathml:math.```

[5.4.1.1.units_with_model](../models_1_0/invalid/5.4.1.1.units_with_model.cellml): Error detected correctly.
* Expected: ```found element of type cellml:model```
* Output: ```Error on line 8. Unexpected content type in cellml:units[@name="wooster"], found element of type cellml:model.```

[5.4.1.1.units_with_reaction](../models_1_0/invalid/5.4.1.1.units_with_reaction.cellml): Error detected correctly.
* Expected: ```found element of type cellml:reaction```
* Output: ```Error on line 9. Unexpected content type in cellml:units[@name="wooster"], found element of type cellml:reaction.```

[5.4.1.1.units_with_relationship_ref](../models_1_0/invalid/5.4.1.1.units_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:relationship_ref```
* Output: ```Error on line 8. Unexpected content type in cellml:units[@name="wooster"], found element of type cellml:relationship_ref.```

[5.4.1.1.units_with_role](../models_1_0/invalid/5.4.1.1.units_with_role.cellml): Error detected correctly.
* Expected: ```found element of type cellml:role```
* Output: ```Error on line 8. Unexpected content type in cellml:units[@name="wooster"], found element of type cellml:role.```

[5.4.1.1.units_with_unit_children](../models_1_0/valid/5.4.1.1.units_with_unit_children.cellml): Valid file passed validation.

[5.4.1.1.units_with_units](../models_1_0/invalid/5.4.1.1.units_with_units.cellml): Error detected correctly.
* Expected: ```found element of type cellml:units```
* Output: ```Error on line 8. Unexpected content type in cellml:units[@name="wooster"], found element of type cellml:units.```

[5.4.1.1.units_with_variable](../models_1_0/invalid/5.4.1.1.units_with_variable.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable```
* Output: ```Error on line 9. Unexpected content type in cellml:units[@name="wooster"], found element of type cellml:variable.```

[5.4.1.1.units_with_variable_ref](../models_1_0/invalid/5.4.1.1.units_with_variable_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable_ref```
* Output: ```Error on line 10. Unexpected content type in cellml:units[@name="wooster"], found element of type cellml:variable_ref.```


---

##### 5.4.1.2

[5.4.1.2.units_name_duplicate_1](../models_1_0/invalid/5.4.1.2.units_name_duplicate_1.cellml): Error detected correctly.
* Expected: ```Duplicate units definition```
* Output: ```Error on line 5. Duplicate units definition "wooster" in cellml:model.```

[5.4.1.2.units_name_duplicate_2](../models_1_0/invalid/5.4.1.2.units_name_duplicate_2.cellml): Error detected correctly.
* Expected: ```Duplicate units definition```
* Output: ```Error on line 6. Duplicate units definition "wooster" in cellml:component.```

[5.4.1.2.units_name_invalid](../models_1_0/invalid/5.4.1.2.units_name_invalid.cellml): Error detected correctly.
* Expected: ```Units name must be a valid CellML identifier```
* Output: ```Error on line 6. Units name must be a valid CellML identifier (5.4.1.2).```

[5.4.1.2.units_name_predefined_ampere](../models_1_0/invalid/5.4.1.2.units_name_predefined_ampere.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "ampere" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_becquerel](../models_1_0/invalid/5.4.1.2.units_name_predefined_becquerel.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "becquerel" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_candela](../models_1_0/invalid/5.4.1.2.units_name_predefined_candela.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "candela" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_celsius](../models_1_0/invalid/5.4.1.2.units_name_predefined_celsius.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "celsius" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_component_ampere](../models_1_0/invalid/5.4.1.2.units_name_predefined_component_ampere.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 6. Units name "ampere" overlaps with a predefined name in cellml:component (5.4.1.2).```

[5.4.1.2.units_name_predefined_coulomb](../models_1_0/invalid/5.4.1.2.units_name_predefined_coulomb.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "coulomb" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_dimensionless](../models_1_0/invalid/5.4.1.2.units_name_predefined_dimensionless.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "dimensionless" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_farad](../models_1_0/invalid/5.4.1.2.units_name_predefined_farad.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "farad" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_gram](../models_1_0/invalid/5.4.1.2.units_name_predefined_gram.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "gram" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_gray](../models_1_0/invalid/5.4.1.2.units_name_predefined_gray.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "gray" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_henry](../models_1_0/invalid/5.4.1.2.units_name_predefined_henry.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "henry" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_hertz](../models_1_0/invalid/5.4.1.2.units_name_predefined_hertz.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "hertz" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_joule](../models_1_0/invalid/5.4.1.2.units_name_predefined_joule.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "joule" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_katal](../models_1_0/invalid/5.4.1.2.units_name_predefined_katal.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "katal" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_kelvin](../models_1_0/invalid/5.4.1.2.units_name_predefined_kelvin.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "kelvin" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_kilogram](../models_1_0/invalid/5.4.1.2.units_name_predefined_kilogram.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "kilogram" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_liter](../models_1_0/invalid/5.4.1.2.units_name_predefined_liter.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "liter" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_litre](../models_1_0/invalid/5.4.1.2.units_name_predefined_litre.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "litre" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_lumen](../models_1_0/invalid/5.4.1.2.units_name_predefined_lumen.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "lumen" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_lux](../models_1_0/invalid/5.4.1.2.units_name_predefined_lux.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "lux" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_meter](../models_1_0/invalid/5.4.1.2.units_name_predefined_meter.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "meter" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_metre](../models_1_0/invalid/5.4.1.2.units_name_predefined_metre.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "metre" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_mole](../models_1_0/invalid/5.4.1.2.units_name_predefined_mole.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "mole" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_newton](../models_1_0/invalid/5.4.1.2.units_name_predefined_newton.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "newton" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_ohm](../models_1_0/invalid/5.4.1.2.units_name_predefined_ohm.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "ohm" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_pascal](../models_1_0/invalid/5.4.1.2.units_name_predefined_pascal.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "pascal" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_radian](../models_1_0/invalid/5.4.1.2.units_name_predefined_radian.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "radian" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_second](../models_1_0/invalid/5.4.1.2.units_name_predefined_second.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "second" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_siemens](../models_1_0/invalid/5.4.1.2.units_name_predefined_siemens.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "siemens" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_sievert](../models_1_0/invalid/5.4.1.2.units_name_predefined_sievert.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "sievert" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_steradian](../models_1_0/invalid/5.4.1.2.units_name_predefined_steradian.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "steradian" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_tesla](../models_1_0/invalid/5.4.1.2.units_name_predefined_tesla.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "tesla" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_volt](../models_1_0/invalid/5.4.1.2.units_name_predefined_volt.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "volt" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_watt](../models_1_0/invalid/5.4.1.2.units_name_predefined_watt.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "watt" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_name_predefined_weber](../models_1_0/invalid/5.4.1.2.units_name_predefined_weber.cellml): Error detected correctly.
* Expected: ```overlaps with a predefined name```
* Output: ```Error on line 5. Units name "weber" overlaps with a predefined name in cellml:model (5.4.1.2).```

[5.4.1.2.units_names_and_other_names](../models_1_0/valid/5.4.1.2.units_names_and_other_names.cellml): Valid file passed validation.

[5.4.1.2.units_shadowing_1](../models_1_0/valid/5.4.1.2.units_shadowing_1.cellml): Valid file passed validation.

[5.4.1.2.units_shadowing_2](../models_1_0/valid/5.4.1.2.units_shadowing_2.cellml): Valid file passed validation.


---

##### 5.4.1.3

[5.4.1.3.units_base_units_invalid](../models_1_0/invalid/5.4.1.3.units_base_units_invalid.cellml): Error detected correctly.
* Expected: ```Base units attribute must be either```
* Output: ```Error on line 6. Base units attribute must be either "yes" or "no".```


---

##### 5.4.2.1

[5.4.2.1.unit_offset_non_zero](../models_1_0/valid/5.4.2.1.unit_offset_non_zero.cellml): Valid file passed validation.

[5.4.2.1.unit_offset_zero](../models_1_0/valid/5.4.2.1.unit_offset_zero.cellml): Valid file passed validation.

[5.4.2.1.unit_prefix_exponent_multiplier](../models_1_0/valid/5.4.2.1.unit_prefix_exponent_multiplier.cellml): Valid file passed validation.

🔴 [5.4.2.1.unit_prefix_exponent_multiplier_huge](../models_1_0/valid/5.4.2.1.unit_prefix_exponent_multiplier_huge.cellml): **Valid file failed validation.**
* Output: ```Unit prefix too large: 10^10000.0```

[5.4.2.1.unit_units_missing](../models_1_0/invalid/5.4.2.1.unit_units_missing.cellml): Error detected correctly.
* Expected: ```must have a units attribute```
* Output: ```Error on line 5. Unit elements must have a units attribute (5.4.2.1).```

[5.4.2.1.unit_with_component](../models_1_0/invalid/5.4.2.1.unit_with_component.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component```
* Output: ```Error on line 8. Unexpected content type in cellml:unit, found element of type cellml:component.```

[5.4.2.1.unit_with_component_ref](../models_1_0/invalid/5.4.2.1.unit_with_component_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component_ref```
* Output: ```Error on line 8. Unexpected content type in cellml:unit, found element of type cellml:component_ref.```

[5.4.2.1.unit_with_connection](../models_1_0/invalid/5.4.2.1.unit_with_connection.cellml): Error detected correctly.
* Expected: ```found element of type cellml:connection```
* Output: ```Error on line 8. Unexpected content type in cellml:unit, found element of type cellml:connection.```

[5.4.2.1.unit_with_group](../models_1_0/invalid/5.4.2.1.unit_with_group.cellml): Error detected correctly.
* Expected: ```found element of type cellml:group```
* Output: ```Error on line 8. Unexpected content type in cellml:unit, found element of type cellml:group.```

[5.4.2.1.unit_with_map_components](../models_1_0/invalid/5.4.2.1.unit_with_map_components.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_components```
* Output: ```Error on line 8. Unexpected content type in cellml:unit, found element of type cellml:map_components.```

[5.4.2.1.unit_with_map_variables](../models_1_0/invalid/5.4.2.1.unit_with_map_variables.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_variables```
* Output: ```Error on line 8. Unexpected content type in cellml:unit, found element of type cellml:map_variables.```

[5.4.2.1.unit_with_math](../models_1_0/invalid/5.4.2.1.unit_with_math.cellml): Error detected correctly.
* Expected: ```found element of type mathml:math```
* Output: ```Error on line 9. Unexpected content type in cellml:unit, found element of type mathml:math.```

[5.4.2.1.unit_with_model](../models_1_0/invalid/5.4.2.1.unit_with_model.cellml): Error detected correctly.
* Expected: ```found element of type cellml:model```
* Output: ```Error on line 8. Unexpected content type in cellml:unit, found element of type cellml:model.```

[5.4.2.1.unit_with_reaction](../models_1_0/invalid/5.4.2.1.unit_with_reaction.cellml): Error detected correctly.
* Expected: ```found element of type cellml:reaction```
* Output: ```Error on line 10. Unexpected content type in cellml:unit, found element of type cellml:reaction.```

[5.4.2.1.unit_with_relationship_ref](../models_1_0/invalid/5.4.2.1.unit_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:relationship_ref```
* Output: ```Error on line 8. Unexpected content type in cellml:unit, found element of type cellml:relationship_ref.```

[5.4.2.1.unit_with_role](../models_1_0/invalid/5.4.2.1.unit_with_role.cellml): Error detected correctly.
* Expected: ```found element of type cellml:role```
* Output: ```Error on line 8. Unexpected content type in cellml:unit, found element of type cellml:role.```

[5.4.2.1.unit_with_unit](../models_1_0/invalid/5.4.2.1.unit_with_unit.cellml): Error detected correctly.
* Expected: ```found element of type cellml:unit```
* Output: ```Error on line 8. Unexpected content type in cellml:unit, found element of type cellml:unit.```

[5.4.2.1.unit_with_units](../models_1_0/invalid/5.4.2.1.unit_with_units.cellml): Error detected correctly.
* Expected: ```found element of type cellml:units```
* Output: ```Error on line 8. Unexpected content type in cellml:unit, found element of type cellml:units.```

[5.4.2.1.unit_with_variable](../models_1_0/invalid/5.4.2.1.unit_with_variable.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable```
* Output: ```Error on line 9. Unexpected content type in cellml:unit, found element of type cellml:variable.```

[5.4.2.1.unit_with_variable_ref](../models_1_0/invalid/5.4.2.1.unit_with_variable_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable_ref```
* Output: ```Error on line 10. Unexpected content type in cellml:unit, found element of type cellml:variable_ref.```


---

##### 5.4.2.2

[5.4.2.2.unit_cycle_1](../models_1_0/invalid/5.4.2.2.unit_cycle_1.cellml): Error detected correctly.
* Expected: ```Unable to resolve network of units```
* Output: ```Error on line 5. Unable to resolve network of units in cellml:model (5.4.2.2).```

[5.4.2.2.unit_cycle_2](../models_1_0/invalid/5.4.2.2.unit_cycle_2.cellml): Error detected correctly.
* Expected: ```Unable to resolve network of units```
* Output: ```Error on line 5. Unable to resolve network of units in cellml:model (5.4.2.2).```

[5.4.2.2.unit_cycle_3](../models_1_0/invalid/5.4.2.2.unit_cycle_3.cellml): Error detected correctly.
* Expected: ```Unable to resolve network of units```
* Output: ```Error on line 5. Unable to resolve network of units in cellml:model (5.4.2.2).```

[5.4.2.2.unit_units_invalid](../models_1_0/invalid/5.4.2.2.unit_units_invalid.cellml): Error detected correctly.
* Expected: ```Unable to resolve network of units```
* Output: ```Error on line 5. Unable to resolve network of units in cellml:model (5.4.2.2).```

[5.4.2.2.unit_units_local_1](../models_1_0/valid/5.4.2.2.unit_units_local_1.cellml): Valid file passed validation.

[5.4.2.2.unit_units_local_2](../models_1_0/valid/5.4.2.2.unit_units_local_2.cellml): Valid file passed validation.

[5.4.2.2.unit_units_local_3](../models_1_0/valid/5.4.2.2.unit_units_local_3.cellml): Valid file passed validation.

[5.4.2.2.unit_units_local_4](../models_1_0/valid/5.4.2.2.unit_units_local_4.cellml): Valid file passed validation.


---

##### 5.4.2.3

[5.4.2.3.unit_prefix_integer](../models_1_0/valid/5.4.2.3.unit_prefix_integer.cellml): Valid file passed validation.

[5.4.2.3.unit_prefix_named](../models_1_0/valid/5.4.2.3.unit_prefix_named.cellml): Valid file passed validation.

[5.4.2.3.unit_prefix_real](../models_1_0/invalid/5.4.2.3.unit_prefix_real.cellml): Error detected correctly.
* Expected: ```Units prefix must be a string from the list of known prefixes or```
* Output: ```Units prefix must be a string from the list of known prefixes or an integer (5.4.2.3).```

🔵 [5.4.2.3.unit_prefix_real_int](../models_1_0/invalid/5.4.2.3.unit_prefix_real_int.cellml): **Error not detected.**
* Output: ```OK```

[5.4.2.3.unit_prefix_spaces](../models_1_0/invalid/5.4.2.3.unit_prefix_spaces.cellml): Error detected correctly.
* Expected: ```Units prefix must be a string from the list of known prefixes or```
* Output: ```Units prefix must be a string from the list of known prefixes or an integer (5.4.2.3).```

[5.4.2.3.unit_prefix_unknown](../models_1_0/invalid/5.4.2.3.unit_prefix_unknown.cellml): Error detected correctly.
* Expected: ```Units prefix must be a string from the list of known prefixes or```
* Output: ```Units prefix must be a string from the list of known prefixes or an integer (5.4.2.3).```


---

##### 5.4.2.4

[5.4.2.4.unit_exponent_invalid](../models_1_0/invalid/5.4.2.4.unit_exponent_invalid.cellml): Error detected correctly.
* Expected: ```Unit exponent must be a real number```
* Output: ```Unit exponent must be a real number (5.4.2.4).```


---

##### 5.4.2.5

[5.4.2.5.unit_multiplier_invalid](../models_1_0/invalid/5.4.2.5.unit_multiplier_invalid.cellml): Error detected correctly.
* Expected: ```Unit multiplier must be a real number```
* Output: ```Unit multiplier must be a real number (5.4.2.5).```


---

##### 5.4.2.6

[5.4.2.6.unit_offset_invalid](../models_1_0/invalid/5.4.2.6.unit_offset_invalid.cellml): Error detected correctly.
* Expected: ```Unit offset must be a real number```
* Output: ```Error on line 7. Unit offset must be a real number (5.4.2.6).```


---

##### 5.4.2.7

🔵 [5.4.2.7.unit_offset_and_exponent](../models_1_0/invalid/5.4.2.7.unit_offset_and_exponent.cellml): **Error not detected.**
* Output: ```OK```

🔵 [5.4.2.7.unit_offset_and_siblings_1](../models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_1.cellml): **Error not detected.**
* Output: ```OK```

🔵 [5.4.2.7.unit_offset_and_siblings_2](../models_1_0/invalid/5.4.2.7.unit_offset_and_siblings_2.cellml): **Error not detected.**
* Output: ```OK```

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

🔴 [5.5.2.boolean_function_factorial](../models_1_0/booleans/5.5.2.boolean_function_factorial.cellml): **Valid file failed validation.**
* Output: ```Error on line 19. Unsupported element in apply: {http://www.w3.org/1998/Math/MathML}factorial.```

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
* Expected: ```Group must contain at least one component_ref```
* Output: ```Error on line 8. Group must contain at least one component_ref element (6.4.1.1).```

[6.4.1.1.group_component_ref_missing_2](../models_1_0/invalid/6.4.1.1.group_component_ref_missing_2.cellml): Error detected correctly.
* Expected: ```Group must contain at least one component_ref```
* Output: ```Error on line 9. Group must contain at least one component_ref element (6.4.1.1).```

[6.4.1.1.group_component_ref_multiple](../models_1_0/valid/6.4.1.1.group_component_ref_multiple.cellml): Valid file passed validation.

[6.4.1.1.group_component_ref_single](../models_1_0/valid/6.4.1.1.group_component_ref_single.cellml): Valid file passed validation.

[6.4.1.1.group_empty](../models_1_0/invalid/6.4.1.1.group_empty.cellml): Error detected correctly.
* Expected: ```Group must contain at least one component_ref```
* Output: ```Error on line 6. Group must contain at least one component_ref element (6.4.1.1).```

[6.4.1.1.group_only_extensions](../models_1_0/invalid/6.4.1.1.group_only_extensions.cellml): Error detected correctly.
* Expected: ```Group must contain at least one component_ref```
* Output: ```Error on line 7. Group must contain at least one component_ref element (6.4.1.1).```

[6.4.1.1.group_relationship_ref_missing_1](../models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_1.cellml): Error detected correctly.
* Expected: ```Group must contain at least one relationship_ref```
* Output: ```Error on line 8. Group must contain at least one relationship_ref element (6.4.1.1).```

[6.4.1.1.group_relationship_ref_missing_2](../models_1_0/invalid/6.4.1.1.group_relationship_ref_missing_2.cellml): Error detected correctly.
* Expected: ```Group must contain at least one relationship_ref```
* Output: ```Error on line 9. Group must contain at least one relationship_ref element (6.4.1.1).```

[6.4.1.1.group_with_component](../models_1_0/invalid/6.4.1.1.group_with_component.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component```
* Output: ```Error on line 13. Unexpected content type in cellml:group, found element of type cellml:component.```

[6.4.1.1.group_with_connection](../models_1_0/invalid/6.4.1.1.group_with_connection.cellml): Error detected correctly.
* Expected: ```found element of type cellml:connection```
* Output: ```Error on line 17. Unexpected content type in cellml:group, found element of type cellml:connection.```

[6.4.1.1.group_with_group](../models_1_0/invalid/6.4.1.1.group_with_group.cellml): Error detected correctly.
* Expected: ```found element of type cellml:group```
* Output: ```Error on line 15. Unexpected content type in cellml:group, found element of type cellml:group.```

[6.4.1.1.group_with_map_components](../models_1_0/invalid/6.4.1.1.group_with_map_components.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_components```
* Output: ```Error on line 13. Unexpected content type in cellml:group, found element of type cellml:map_components.```

[6.4.1.1.group_with_map_variables](../models_1_0/invalid/6.4.1.1.group_with_map_variables.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_variables```
* Output: ```Error on line 17. Unexpected content type in cellml:group, found element of type cellml:map_variables.```

[6.4.1.1.group_with_math](../models_1_0/invalid/6.4.1.1.group_with_math.cellml): Error detected correctly.
* Expected: ```found element of type mathml:math```
* Output: ```Error on line 16. Unexpected content type in cellml:group, found element of type mathml:math.```

[6.4.1.1.group_with_model](../models_1_0/invalid/6.4.1.1.group_with_model.cellml): Error detected correctly.
* Expected: ```found element of type cellml:model```
* Output: ```Error on line 13. Unexpected content type in cellml:group, found element of type cellml:model.```

[6.4.1.1.group_with_reaction](../models_1_0/invalid/6.4.1.1.group_with_reaction.cellml): Error detected correctly.
* Expected: ```found element of type cellml:reaction```
* Output: ```Error on line 15. Unexpected content type in cellml:group, found element of type cellml:reaction.```

[6.4.1.1.group_with_role](../models_1_0/invalid/6.4.1.1.group_with_role.cellml): Error detected correctly.
* Expected: ```found element of type cellml:role```
* Output: ```Error on line 13. Unexpected content type in cellml:group, found element of type cellml:role.```

[6.4.1.1.group_with_unit](../models_1_0/invalid/6.4.1.1.group_with_unit.cellml): Error detected correctly.
* Expected: ```found element of type cellml:unit```
* Output: ```Error on line 10. Unexpected content type in cellml:group, found element of type cellml:unit.```

[6.4.1.1.group_with_units](../models_1_0/invalid/6.4.1.1.group_with_units.cellml): Error detected correctly.
* Expected: ```found element of type cellml:units```
* Output: ```Error on line 13. Unexpected content type in cellml:group, found element of type cellml:units.```

[6.4.1.1.group_with_variable](../models_1_0/invalid/6.4.1.1.group_with_variable.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable```
* Output: ```Error on line 13. Unexpected content type in cellml:group, found element of type cellml:variable.```

[6.4.1.1.group_with_variable_ref](../models_1_0/invalid/6.4.1.1.group_with_variable_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable_ref```
* Output: ```Error on line 15. Unexpected content type in cellml:group, found element of type cellml:variable_ref.```


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
* Expected: ```Relationship_ref must define a relationship attribute```
* Output: ```Error on line 10. Relationship_ref must define a relationship attribute (6.4.2.1).```

[6.4.2.1.relationship_ref_with_component](../models_1_0/invalid/6.4.2.1.relationship_ref_with_component.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component```
* Output: ```Error on line 10. Unexpected content type in cellml:relationship_ref, found element of type cellml:component.```

[6.4.2.1.relationship_ref_with_component_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_component_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component_ref```
* Output: ```Error on line 13. Unexpected content type in cellml:relationship_ref, found element of type cellml:component_ref.```

[6.4.2.1.relationship_ref_with_connection](../models_1_0/invalid/6.4.2.1.relationship_ref_with_connection.cellml): Error detected correctly.
* Expected: ```found element of type cellml:connection```
* Output: ```Error on line 14. Unexpected content type in cellml:relationship_ref, found element of type cellml:connection.```

[6.4.2.1.relationship_ref_with_group](../models_1_0/invalid/6.4.2.1.relationship_ref_with_group.cellml): Error detected correctly.
* Expected: ```found element of type cellml:group```
* Output: ```Error on line 12. Unexpected content type in cellml:relationship_ref, found element of type cellml:group.```

[6.4.2.1.relationship_ref_with_map_components](../models_1_0/invalid/6.4.2.1.relationship_ref_with_map_components.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_components```
* Output: ```Error on line 10. Unexpected content type in cellml:relationship_ref, found element of type cellml:map_components.```

[6.4.2.1.relationship_ref_with_map_variables](../models_1_0/invalid/6.4.2.1.relationship_ref_with_map_variables.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_variables```
* Output: ```Error on line 14. Unexpected content type in cellml:relationship_ref, found element of type cellml:map_variables.```

[6.4.2.1.relationship_ref_with_math](../models_1_0/invalid/6.4.2.1.relationship_ref_with_math.cellml): Error detected correctly.
* Expected: ```found element of type mathml:math```
* Output: ```Error on line 13. Unexpected content type in cellml:relationship_ref, found element of type mathml:math.```

[6.4.2.1.relationship_ref_with_model](../models_1_0/invalid/6.4.2.1.relationship_ref_with_model.cellml): Error detected correctly.
* Expected: ```found element of type cellml:model```
* Output: ```Error on line 10. Unexpected content type in cellml:relationship_ref, found element of type cellml:model.```

[6.4.2.1.relationship_ref_with_reaction](../models_1_0/invalid/6.4.2.1.relationship_ref_with_reaction.cellml): Error detected correctly.
* Expected: ```found element of type cellml:reaction```
* Output: ```Error on line 12. Unexpected content type in cellml:relationship_ref, found element of type cellml:reaction.```

[6.4.2.1.relationship_ref_with_relationship_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:relationship_ref```
* Output: ```Error on line 10. Unexpected content type in cellml:relationship_ref, found element of type cellml:relationship_ref.```

[6.4.2.1.relationship_ref_with_role](../models_1_0/invalid/6.4.2.1.relationship_ref_with_role.cellml): Error detected correctly.
* Expected: ```found element of type cellml:role```
* Output: ```Error on line 10. Unexpected content type in cellml:relationship_ref, found element of type cellml:role.```

[6.4.2.1.relationship_ref_with_unit](../models_1_0/invalid/6.4.2.1.relationship_ref_with_unit.cellml): Error detected correctly.
* Expected: ```found element of type cellml:unit```
* Output: ```Error on line 10. Unexpected content type in cellml:relationship_ref, found element of type cellml:unit.```

[6.4.2.1.relationship_ref_with_units](../models_1_0/invalid/6.4.2.1.relationship_ref_with_units.cellml): Error detected correctly.
* Expected: ```found element of type cellml:units```
* Output: ```Error on line 10. Unexpected content type in cellml:relationship_ref, found element of type cellml:units.```

[6.4.2.1.relationship_ref_with_variable](../models_1_0/invalid/6.4.2.1.relationship_ref_with_variable.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable```
* Output: ```Error on line 10. Unexpected content type in cellml:relationship_ref, found element of type cellml:variable.```

[6.4.2.1.relationship_ref_with_variable_ref](../models_1_0/invalid/6.4.2.1.relationship_ref_with_variable_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable_ref```
* Output: ```Error on line 12. Unexpected content type in cellml:relationship_ref, found element of type cellml:variable_ref.```


---

##### 6.4.2.2

[6.4.2.2.relationship_ref_relationship_invalid](../models_1_0/invalid/6.4.2.2.relationship_ref_relationship_invalid.cellml): Error detected correctly.
* Expected: ```Unknown relationship type```
* Output: ```Error on line 9. Unknown relationship type: "howdy", expecting either "encapsulation" or "containment" (6.4.2.2).```


---

##### 6.4.2.3

[6.4.2.3.relationship_ref_name_invalid](../models_1_0/invalid/6.4.2.3.relationship_ref_name_invalid.cellml): Error detected correctly.
* Expected: ```must be a valid CellML identifier```
* Output: ```Error on line 9. Relationship_ref name must be a valid CellML identifier, but found "___" (6.4.2.3).```

[6.4.2.3.relationship_ref_name_not_unique_model_wide](../models_1_0/valid/6.4.2.3.relationship_ref_name_not_unique_model_wide.cellml): Valid file passed validation.


---

##### 6.4.2.4

[6.4.2.4.relationship_ref_encapsulation_duplicate](../models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_duplicate.cellml): Error detected correctly.
* Expected: ```Encapsulation relationships may not define a name```
* Output: ```Error on line 12. Encapsulation relationships may not define a name attribute (6.4.2.4).```

[6.4.2.4.relationship_ref_encapsulation_named](../models_1_0/invalid/6.4.2.4.relationship_ref_encapsulation_named.cellml): Error detected correctly.
* Expected: ```Encapsulation relationships may not define a name```
* Output: ```Error on line 9. Encapsulation relationships may not define a name attribute (6.4.2.4).```


---

##### 6.4.2.5

[6.4.2.5.relationship_ref_duplicate_named](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_named.cellml): Error detected correctly.
* Expected: ```must have a unique pair```
* Output: ```Error on line 13. Relationship_refs in each group must have a unique pair of (relationship, name) attributes (6.4.2.5).```

[6.4.2.5.relationship_ref_duplicate_unnamed_1](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_unnamed_1.cellml): Error detected correctly.
* Expected: ```must have a unique pair```
* Output: ```Error on line 13. Relationship_refs in each group must have a unique pair of (relationship, name) attributes (6.4.2.5).```

[6.4.2.5.relationship_ref_duplicate_unnamed_2](../models_1_0/invalid/6.4.2.5.relationship_ref_duplicate_unnamed_2.cellml): Error detected correctly.
* Expected: ```must have a unique pair```
* Output: ```Error on line 13. Relationship_refs in each group must have a unique pair of (relationship, name) attributes (6.4.2.5).```

[6.4.2.5.relationship_ref_multiple_1](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_1.cellml): Valid file passed validation.

[6.4.2.5.relationship_ref_multiple_2](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_2.cellml): Valid file passed validation.

[6.4.2.5.relationship_ref_multiple_3](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_3.cellml): Valid file passed validation.


---

##### 6.4.3.1

[6.4.3.1.component_ref_component_missing](../models_1_0/invalid/6.4.3.1.component_ref_component_missing.cellml): Error detected correctly.
* Expected: ```A component_ref must define a component attribute```
* Output: ```Error on line 11. A component_ref must define a component attribute (6.4.3.1).```

[6.4.3.1.component_ref_nesting](../models_1_0/valid/6.4.3.1.component_ref_nesting.cellml): Valid file passed validation.

[6.4.3.1.component_ref_with_component](../models_1_0/invalid/6.4.3.1.component_ref_with_component.cellml): Error detected correctly.
* Expected: ```found element of type cellml:component```
* Output: ```Error on line 12. Unexpected content type in cellml:component_ref, found element of type cellml:component.```

[6.4.3.1.component_ref_with_connection](../models_1_0/invalid/6.4.3.1.component_ref_with_connection.cellml): Error detected correctly.
* Expected: ```found element of type cellml:connection```
* Output: ```Error on line 16. Unexpected content type in cellml:component_ref, found element of type cellml:connection.```

[6.4.3.1.component_ref_with_group](../models_1_0/invalid/6.4.3.1.component_ref_with_group.cellml): Error detected correctly.
* Expected: ```found element of type cellml:group```
* Output: ```Error on line 14. Unexpected content type in cellml:component_ref, found element of type cellml:group.```

[6.4.3.1.component_ref_with_map_components](../models_1_0/invalid/6.4.3.1.component_ref_with_map_components.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_components```
* Output: ```Error on line 12. Unexpected content type in cellml:component_ref, found element of type cellml:map_components.```

[6.4.3.1.component_ref_with_map_variables](../models_1_0/invalid/6.4.3.1.component_ref_with_map_variables.cellml): Error detected correctly.
* Expected: ```found element of type cellml:map_variables```
* Output: ```Error on line 16. Unexpected content type in cellml:component_ref, found element of type cellml:map_variables.```

[6.4.3.1.component_ref_with_math](../models_1_0/invalid/6.4.3.1.component_ref_with_math.cellml): Error detected correctly.
* Expected: ```found element of type mathml:math```
* Output: ```Error on line 15. Unexpected content type in cellml:component_ref, found element of type mathml:math.```

[6.4.3.1.component_ref_with_model](../models_1_0/invalid/6.4.3.1.component_ref_with_model.cellml): Error detected correctly.
* Expected: ```found element of type cellml:model```
* Output: ```Error on line 12. Unexpected content type in cellml:component_ref, found element of type cellml:model.```

[6.4.3.1.component_ref_with_reaction](../models_1_0/invalid/6.4.3.1.component_ref_with_reaction.cellml): Error detected correctly.
* Expected: ```found element of type cellml:reaction```
* Output: ```Error on line 14. Unexpected content type in cellml:component_ref, found element of type cellml:reaction.```

[6.4.3.1.component_ref_with_relationship_ref](../models_1_0/invalid/6.4.3.1.component_ref_with_relationship_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:relationship_ref```
* Output: ```Error on line 12. Unexpected content type in cellml:component_ref, found element of type cellml:relationship_ref.```

[6.4.3.1.component_ref_with_role](../models_1_0/invalid/6.4.3.1.component_ref_with_role.cellml): Error detected correctly.
* Expected: ```found element of type cellml:role```
* Output: ```Error on line 12. Unexpected content type in cellml:component_ref, found element of type cellml:role.```

[6.4.3.1.component_ref_with_unit](../models_1_0/invalid/6.4.3.1.component_ref_with_unit.cellml): Error detected correctly.
* Expected: ```found element of type cellml:unit```
* Output: ```Error on line 12. Unexpected content type in cellml:component_ref, found element of type cellml:unit.```

[6.4.3.1.component_ref_with_units](../models_1_0/invalid/6.4.3.1.component_ref_with_units.cellml): Error detected correctly.
* Expected: ```found element of type cellml:units```
* Output: ```Error on line 12. Unexpected content type in cellml:component_ref, found element of type cellml:units.```

[6.4.3.1.component_ref_with_variable](../models_1_0/invalid/6.4.3.1.component_ref_with_variable.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable```
* Output: ```Error on line 12. Unexpected content type in cellml:component_ref, found element of type cellml:variable.```

[6.4.3.1.component_ref_with_variable_ref](../models_1_0/invalid/6.4.3.1.component_ref_with_variable_ref.cellml): Error detected correctly.
* Expected: ```found element of type cellml:variable_ref```
* Output: ```Error on line 14. Unexpected content type in cellml:component_ref, found element of type cellml:variable_ref.```


---

##### 6.4.3.2

🔵 [6.4.3.2.component_ref_children_declared_twice_1](../models_1_0/invalid/6.4.3.2.component_ref_children_declared_twice_1.cellml): **Error not detected.**
* Output: ```OK```

🔵 [6.4.3.2.component_ref_children_declared_twice_2](../models_1_0/invalid/6.4.3.2.component_ref_children_declared_twice_2.cellml): **Error not detected.**
* Output: ```OK```

🔵 [6.4.3.2.component_ref_children_declared_twice_3](../models_1_0/invalid/6.4.3.2.component_ref_children_declared_twice_3.cellml): **Error not detected.**
* Output: ```OK```

🔵 [6.4.3.2.component_ref_cycle_1](../models_1_0/invalid/6.4.3.2.component_ref_cycle_1.cellml): **Error not detected.**
* Output: ```OK```

🔵 [6.4.3.2.component_ref_cycle_2](../models_1_0/invalid/6.4.3.2.component_ref_cycle_2.cellml): **Error not detected.**
* Output: ```OK```

🔵 [6.4.3.2.component_ref_cycle_3](../models_1_0/invalid/6.4.3.2.component_ref_cycle_3.cellml): **Error not detected.**
* Output: ```OK```

🔵 [6.4.3.2.component_ref_cycle_4](../models_1_0/invalid/6.4.3.2.component_ref_cycle_4.cellml): **Error not detected.**
* Output: ```OK```

[6.4.3.2.component_ref_cycle_5](../models_1_0/invalid/6.4.3.2.component_ref_cycle_5.cellml): Error detected correctly.
* Expected: ```Encapsulation hierarchy cannot be circular```
* Output: ```Encapsulation hierarchy cannot be circular (6.4.3.2).```

[6.4.3.2.component_ref_cycle_6](../models_1_0/invalid/6.4.3.2.component_ref_cycle_6.cellml): Error detected correctly.
* Expected: ```Encapsulation hierarchy cannot be circular```
* Output: ```Encapsulation hierarchy cannot be circular (6.4.3.2).```

[6.4.3.2.component_ref_cycle_7](../models_1_0/invalid/6.4.3.2.component_ref_cycle_7.cellml): Error detected correctly.
* Expected: ```Encapsulation hierarchy cannot be circular```
* Output: ```Encapsulation hierarchy cannot be circular (6.4.3.2).```

[6.4.3.2.component_ref_cycle_8](../models_1_0/invalid/6.4.3.2.component_ref_cycle_8.cellml): Error detected correctly.
* Expected: ```Encapsulation hierarchy cannot be circular```
* Output: ```Encapsulation hierarchy cannot be circular (6.4.3.2).```

🔵 [6.4.3.2.component_ref_duplicate_child_1](../models_1_0/invalid/6.4.3.2.component_ref_duplicate_child_1.cellml): **Error not detected.**
* Output: ```OK```

🔵 [6.4.3.2.component_ref_duplicate_child_2](../models_1_0/invalid/6.4.3.2.component_ref_duplicate_child_2.cellml): **Error not detected.**
* Output: ```OK```

[6.4.3.2.component_ref_duplicate_child_3](../models_1_0/invalid/6.4.3.2.component_ref_duplicate_child_3.cellml): Error detected correctly.
* Expected: ```single encapsulation parent```
* Output: ```Error on line 12. A component can only have a single encapsulation parent: found Component[@name="B"] with parents Component[@name="A"] and Component[@name="A"] (6.4.3.2).```

[6.4.3.2.component_ref_duplicate_child_4](../models_1_0/invalid/6.4.3.2.component_ref_duplicate_child_4.cellml): Error detected correctly.
* Expected: ```single encapsulation parent```
* Output: ```Error on line 15. A component can only have a single encapsulation parent: found Component[@name="C"] with parents Component[@name="B"] and Component[@name="A"] (6.4.3.2).```

[6.4.3.2.component_ref_no_children_containment](../models_1_0/invalid/6.4.3.2.component_ref_no_children_containment.cellml): Error detected correctly.
* Expected: ```must have at least one child```
* Output: ```The first component_ref in an encapsulation or containment relationship must have at least one child (6.4.3.2).```

[6.4.3.2.component_ref_no_children_encapsulation](../models_1_0/invalid/6.4.3.2.component_ref_no_children_encapsulation.cellml): Error detected correctly.
* Expected: ```must have at least one child```
* Output: ```The first component_ref in an encapsulation or containment relationship must have at least one child (6.4.3.2).```

[6.4.3.2.component_ref_no_children_extension](../models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml): Valid file passed validation.

[6.4.3.2.component_ref_overlapping_containment](../models_1_0/valid/6.4.3.2.component_ref_overlapping_containment.cellml): Valid file passed validation.

[6.4.3.2.component_ref_overlapping_encapsulation](../models_1_0/invalid/6.4.3.2.component_ref_overlapping_encapsulation.cellml): Error detected correctly.
* Expected: ```can only have a single encapsulation parent```
* Output: ```Error on line 18. A component can only have a single encapsulation parent: found Component[@name="B"] with parents Component[@name="A"] and Component[@name="C"] (6.4.3.2).```

[6.4.3.2.component_ref_split_named](../models_1_0/valid/6.4.3.2.component_ref_split_named.cellml): Valid file passed validation.

[6.4.3.2.component_ref_split_unnamed_1](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_1.cellml): Valid file passed validation.

[6.4.3.2.component_ref_split_unnamed_2](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_2.cellml): Valid file passed validation.


---

##### 6.4.3.3

[6.4.3.3.component_ref_component_invalid](../models_1_0/invalid/6.4.3.3.component_ref_component_invalid.cellml): Error detected correctly.
* Expected: ```component attribute must reference a component in the same model```
* Output: ```Error on line 11. A component_ref's component attribute must reference a component in the same model, got "." (6.4.3.3).```

[6.4.3.3.component_ref_component_nonexistent_1](../models_1_0/invalid/6.4.3.3.component_ref_component_nonexistent_1.cellml): Error detected correctly.
* Expected: ```component attribute must reference a component in the same model```
* Output: ```Error on line 10. A component_ref's component attribute must reference a component in the same model, got "X" (6.4.3.3).```

[6.4.3.3.component_ref_component_nonexistent_2](../models_1_0/invalid/6.4.3.3.component_ref_component_nonexistent_2.cellml): Error detected correctly.
* Expected: ```component attribute must reference a component in the same model```
* Output: ```Error on line 11. A component_ref's component attribute must reference a component in the same model, got "C" (6.4.3.3).```


---

## 7. Reactions

##### 7.4.1.1

🔶 [7.4.1.1.reaction_variable_ref_missing](../models_1_0/invalid/7.4.1.1.reaction_variable_ref_missing.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_component](../models_1_0/invalid/7.4.1.1.reaction_with_component.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_component_ref](../models_1_0/invalid/7.4.1.1.reaction_with_component_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_connection](../models_1_0/invalid/7.4.1.1.reaction_with_connection.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_group](../models_1_0/invalid/7.4.1.1.reaction_with_group.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_map_components](../models_1_0/invalid/7.4.1.1.reaction_with_map_components.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_map_variables](../models_1_0/invalid/7.4.1.1.reaction_with_map_variables.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_math](../models_1_0/invalid/7.4.1.1.reaction_with_math.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_model](../models_1_0/invalid/7.4.1.1.reaction_with_model.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_reaction](../models_1_0/invalid/7.4.1.1.reaction_with_reaction.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_relationship_ref](../models_1_0/invalid/7.4.1.1.reaction_with_relationship_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_role](../models_1_0/invalid/7.4.1.1.reaction_with_role.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_unit](../models_1_0/invalid/7.4.1.1.reaction_with_unit.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_units](../models_1_0/invalid/7.4.1.1.reaction_with_units.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.1.1.reaction_with_variable](../models_1_0/invalid/7.4.1.1.reaction_with_variable.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```


---

##### 7.4.1.2

🔶 [7.4.1.2.reaction_reversible_invalid](../models_1_0/invalid/7.4.1.2.reaction_reversible_invalid.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔴 [7.4.1.2.reaction_reversible_no](../models_1_0/valid/7.4.1.2.reaction_reversible_no.cellml): **Valid file failed validation.**
* Output: ```Error on line 8. Reactions are not supported.```

🔴 [7.4.1.2.reaction_reversible_yes](../models_1_0/valid/7.4.1.2.reaction_reversible_yes.cellml): **Valid file failed validation.**
* Output: ```Error on line 8. Reactions are not supported.```


---

##### 7.4.1.3

🔶 [7.4.1.3.reaction_encapsulating_delta_variable](../models_1_0/invalid/7.4.1.3.reaction_encapsulating_delta_variable.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 10. Reactions are not supported.```


---

##### 7.4.2.1

🔶 [7.4.2.1.variable_ref_role_missing](../models_1_0/invalid/7.4.2.1.variable_ref_role_missing.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_variable_missing](../models_1_0/invalid/7.4.2.1.variable_ref_variable_missing.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_component](../models_1_0/invalid/7.4.2.1.variable_ref_with_component.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_component_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_component_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_connection](../models_1_0/invalid/7.4.2.1.variable_ref_with_connection.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_group](../models_1_0/invalid/7.4.2.1.variable_ref_with_group.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_map_components](../models_1_0/invalid/7.4.2.1.variable_ref_with_map_components.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_map_variables](../models_1_0/invalid/7.4.2.1.variable_ref_with_map_variables.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_math](../models_1_0/invalid/7.4.2.1.variable_ref_with_math.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_model](../models_1_0/invalid/7.4.2.1.variable_ref_with_model.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_reaction](../models_1_0/invalid/7.4.2.1.variable_ref_with_reaction.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_relationship_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_relationship_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_unit](../models_1_0/invalid/7.4.2.1.variable_ref_with_unit.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_units](../models_1_0/invalid/7.4.2.1.variable_ref_with_units.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_variable](../models_1_0/invalid/7.4.2.1.variable_ref_with_variable.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.1.variable_ref_with_variable_ref](../models_1_0/invalid/7.4.2.1.variable_ref_with_variable_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```


---

##### 7.4.2.2

🔶 [7.4.2.2.variable_ref_variable_duplicate](../models_1_0/invalid/7.4.2.2.variable_ref_variable_duplicate.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

🔶 [7.4.2.2.variable_ref_variable_hidden](../models_1_0/invalid/7.4.2.2.variable_ref_variable_hidden.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.2.2.variable_ref_variable_nonexistent](../models_1_0/invalid/7.4.2.2.variable_ref_variable_nonexistent.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```


---

##### 7.4.3.1

🔶 [7.4.3.1.role_role_missing](../models_1_0/invalid/7.4.3.1.role_role_missing.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.3.1.role_with_component](../models_1_0/invalid/7.4.3.1.role_with_component.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.3.1.role_with_component_ref](../models_1_0/invalid/7.4.3.1.role_with_component_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.3.1.role_with_connection](../models_1_0/invalid/7.4.3.1.role_with_connection.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.3.1.role_with_group](../models_1_0/invalid/7.4.3.1.role_with_group.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.3.1.role_with_map_components](../models_1_0/invalid/7.4.3.1.role_with_map_components.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.3.1.role_with_map_variables](../models_1_0/invalid/7.4.3.1.role_with_map_variables.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.3.1.role_with_model](../models_1_0/invalid/7.4.3.1.role_with_model.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.3.1.role_with_reaction](../models_1_0/invalid/7.4.3.1.role_with_reaction.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

🔶 [7.4.3.1.role_with_relationship_ref](../models_1_0/invalid/7.4.3.1.role_with_relationship_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.3.1.role_with_role](../models_1_0/invalid/7.4.3.1.role_with_role.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

🔶 [7.4.3.1.role_with_unit](../models_1_0/invalid/7.4.3.1.role_with_unit.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.3.1.role_with_units](../models_1_0/invalid/7.4.3.1.role_with_units.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.3.1.role_with_variable](../models_1_0/invalid/7.4.3.1.role_with_variable.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```

🔶 [7.4.3.1.role_with_variable_ref](../models_1_0/invalid/7.4.3.1.role_with_variable_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```


---

##### 7.4.3.2

🔶 [7.4.3.2.role_role_invalid](../models_1_0/invalid/7.4.3.2.role_role_invalid.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 8. Reactions are not supported.```


---

##### 7.4.3.3

🔶 [7.4.3.3.reaction_multiple_rates](../models_1_0/invalid/7.4.3.3.reaction_multiple_rates.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 13. Reactions are not supported.```

🔶 [7.4.3.3.role_rate_with_delta_variable](../models_1_0/invalid/7.4.3.3.role_rate_with_delta_variable.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 13. Reactions are not supported.```

🔶 [7.4.3.3.role_rate_with_multiple_roles](../models_1_0/invalid/7.4.3.3.role_rate_with_multiple_roles.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 12. Reactions are not supported.```

🔶 [7.4.3.3.role_rate_with_stoichiometry](../models_1_0/invalid/7.4.3.3.role_rate_with_stoichiometry.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 12. Reactions are not supported.```


---

##### 7.4.3.4

🔶 [7.4.3.4.role_direction_invalid](../models_1_0/invalid/7.4.3.4.role_direction_invalid.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 13. Reactions are not supported.```


---

##### 7.4.3.5

🔶 [7.4.3.5.role_direction_both_irreversible](../models_1_0/invalid/7.4.3.5.role_direction_both_irreversible.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 13. Reactions are not supported.```

🔶 [7.4.3.5.role_direction_both_product](../models_1_0/invalid/7.4.3.5.role_direction_both_product.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 12. Reactions are not supported.```

🔶 [7.4.3.5.role_direction_both_rate](../models_1_0/invalid/7.4.3.5.role_direction_both_rate.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 12. Reactions are not supported.```

🔶 [7.4.3.5.role_direction_both_reactant](../models_1_0/invalid/7.4.3.5.role_direction_both_reactant.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 12. Reactions are not supported.```

🔶 [7.4.3.5.role_direction_reverse_irreversible](../models_1_0/invalid/7.4.3.5.role_direction_reverse_irreversible.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 13. Reactions are not supported.```

🔶 [7.4.3.5.role_direction_reverse_product](../models_1_0/invalid/7.4.3.5.role_direction_reverse_product.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 12. Reactions are not supported.```

🔶 [7.4.3.5.role_direction_reverse_rate](../models_1_0/invalid/7.4.3.5.role_direction_reverse_rate.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 12. Reactions are not supported.```

🔶 [7.4.3.5.role_direction_reverse_reactant](../models_1_0/invalid/7.4.3.5.role_direction_reverse_reactant.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 12. Reactions are not supported.```

🔶 [7.4.3.5.role_direction_role_duplicate](../models_1_0/invalid/7.4.3.5.role_direction_role_duplicate.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 13. Reactions are not supported.```


---

##### 7.4.3.6

🔶 [7.4.3.6.role_stoichiometry_invalid](../models_1_0/invalid/7.4.3.6.role_stoichiometry_invalid.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 13. Reactions are not supported.```


---

##### 7.4.3.7

🔶 [7.4.3.7.role_delta_variable_duplicate_1](../models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_1.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 13. Reactions are not supported.```

🔶 [7.4.3.7.role_delta_variable_duplicate_2](../models_1_0/invalid/7.4.3.7.role_delta_variable_duplicate_2.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 13. Reactions are not supported.```

🔶 [7.4.3.7.role_delta_variable_nonexistent_1](../models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_1.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 12. Reactions are not supported.```

🔶 [7.4.3.7.role_delta_variable_nonexistent_2](../models_1_0/invalid/7.4.3.7.role_delta_variable_nonexistent_2.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 12. Reactions are not supported.```


---

##### 7.4.3.8

🔶 [7.4.3.8.role_delta_variable_activator](../models_1_0/invalid/7.4.3.8.role_delta_variable_activator.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 14. Reactions are not supported.```

🔶 [7.4.3.8.role_delta_variable_catalyst](../models_1_0/invalid/7.4.3.8.role_delta_variable_catalyst.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 14. Reactions are not supported.```

🔶 [7.4.3.8.role_delta_variable_inhibitor](../models_1_0/invalid/7.4.3.8.role_delta_variable_inhibitor.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 14. Reactions are not supported.```

🔶 [7.4.3.8.role_delta_variable_modifier](../models_1_0/invalid/7.4.3.8.role_delta_variable_modifier.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 14. Reactions are not supported.```

🔶 [7.4.3.8.role_delta_variable_with_rate_and_math](../models_1_0/invalid/7.4.3.8.role_delta_variable_with_rate_and_math.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 13. Reactions are not supported.```

🔶 [7.4.3.8.role_delta_variable_with_stoichiometry_no_rate](../models_1_0/invalid/7.4.3.8.role_delta_variable_with_stoichiometry_no_rate.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 12. Reactions are not supported.```

🔶 [7.4.3.8.role_delta_variable_without_rate_or_math](../models_1_0/invalid/7.4.3.8.role_delta_variable_without_rate_or_math.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 13. Reactions are not supported.```


---

##### 7.4.3.9

🔶 [7.4.3.9.role_math_not_relevant](../models_1_0/invalid/7.4.3.9.role_math_not_relevant.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 13. Reactions are not supported.```


---

#### 7.4.3

🔴 [7.4.3.reaction_all_roles_and_attributes](../models_1_0/valid/7.4.3.reaction_all_roles_and_attributes.cellml): **Valid file failed validation.**
* Output: ```Error on line 17. Reactions are not supported.```

🔴 [7.4.3.reaction_reversible_no](../models_1_0/valid/7.4.3.reaction_reversible_no.cellml): **Valid file failed validation.**
* Output: ```Error on line 15. Reactions are not supported.```

🔴 [7.4.3.reaction_simple](../models_1_0/valid/7.4.3.reaction_simple.cellml): **Valid file failed validation.**
* Output: ```Error on line 12. Reactions are not supported.```


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
* Output: ```Error on line 9. Reactions are not supported.```

[8.4.1.cmeta_id_in_relationship_ref](../models_1_0/valid/8.4.1.cmeta_id_in_relationship_ref.cellml): Valid file passed validation.

🔴 [8.4.1.cmeta_id_in_role](../models_1_0/valid/8.4.1.cmeta_id_in_role.cellml): **Valid file failed validation.**
* Output: ```Error on line 9. Reactions are not supported.```

[8.4.1.cmeta_id_in_unit](../models_1_0/valid/8.4.1.cmeta_id_in_unit.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_units_1](../models_1_0/valid/8.4.1.cmeta_id_in_units_1.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_units_2](../models_1_0/valid/8.4.1.cmeta_id_in_units_2.cellml): Valid file passed validation.

[8.4.1.cmeta_id_in_variable](../models_1_0/valid/8.4.1.cmeta_id_in_variable.cellml): Valid file passed validation.

🔴 [8.4.1.cmeta_id_in_variable_ref](../models_1_0/valid/8.4.1.cmeta_id_in_variable_ref.cellml): **Valid file failed validation.**
* Output: ```Error on line 9. Reactions are not supported.```

[8.4.1.duplicate_cmeta_id_in_component](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_component.cellml): Error detected correctly.
* Expected: ```Duplicate cmeta:id```
* Output: ```Error on line 8. Duplicate cmeta:id "a" (8.5.1).```

[8.4.1.duplicate_cmeta_id_in_component_ref](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_component_ref.cellml): Error detected correctly.
* Expected: ```Duplicate cmeta:id```
* Output: ```Error on line 14. Duplicate cmeta:id "y" (8.5.1).```

[8.4.1.duplicate_cmeta_id_in_connection](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_connection.cellml): Error detected correctly.
* Expected: ```Duplicate cmeta:id```
* Output: ```Error on line 13. Duplicate cmeta:id "hello" (8.5.1).```

[8.4.1.duplicate_cmeta_id_in_group](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_group.cellml): Error detected correctly.
* Expected: ```Duplicate cmeta:id```
* Output: ```Error on line 11. Duplicate cmeta:id "x" (8.5.1).```

[8.4.1.duplicate_cmeta_id_in_map_components](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_components.cellml): Error detected correctly.
* Expected: ```Duplicate cmeta:id```
* Output: ```Error on line 8. Duplicate cmeta:id "x" (8.5.1).```

[8.4.1.duplicate_cmeta_id_in_map_variables](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_map_variables.cellml): Error detected correctly.
* Expected: ```Duplicate cmeta:id```
* Output: ```Error on line 15. Duplicate cmeta:id "x" (8.5.1).```

[8.4.1.duplicate_cmeta_id_in_model](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_model.cellml): Error detected correctly.
* Expected: ```Duplicate cmeta:id```
* Output: ```Error on line 9. Duplicate cmeta:id "x" (8.5.1).```

🔶 [8.4.1.duplicate_cmeta_id_in_reaction](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_reaction.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

[8.4.1.duplicate_cmeta_id_in_relationship_ref](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_relationship_ref.cellml): Error detected correctly.
* Expected: ```Duplicate cmeta:id```
* Output: ```Error on line 12. Duplicate cmeta:id "x" (8.5.1).```

🔶 [8.4.1.duplicate_cmeta_id_in_role](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_role.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```

[8.4.1.duplicate_cmeta_id_in_unit](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_unit.cellml): Error detected correctly.
* Expected: ```Duplicate cmeta:id```
* Output: ```Error on line 8. Duplicate cmeta:id "apple" (8.5.1).```

[8.4.1.duplicate_cmeta_id_in_units_1](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_units_1.cellml): Error detected correctly.
* Expected: ```Duplicate cmeta:id```
* Output: ```Error on line 8. Duplicate cmeta:id "orange" (8.5.1).```

[8.4.1.duplicate_cmeta_id_in_units_2](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_units_2.cellml): Error detected correctly.
* Expected: ```Duplicate cmeta:id```
* Output: ```Error on line 8. Duplicate cmeta:id "apple" (8.5.1).```

[8.4.1.duplicate_cmeta_id_in_variable](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable.cellml): Error detected correctly.
* Expected: ```Duplicate cmeta:id```
* Output: ```Error on line 9. Duplicate cmeta:id "a" (8.5.1).```

🔶 [8.4.1.duplicate_cmeta_id_in_variable_ref](../models_1_0/invalid/8.4.1.duplicate_cmeta_id_in_variable_ref.cellml): **Invalid file failed for unexpected reason.**
* Expected: ```Expected error not set```
* Output: ```Error on line 9. Reactions are not supported.```


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
* Output: ```Error on line 11. Reactions are not supported.```

[8.4.2.rdf_in_relationship_ref](../models_1_0/valid/8.4.2.rdf_in_relationship_ref.cellml): Valid file passed validation.

🔴 [8.4.2.rdf_in_role](../models_1_0/valid/8.4.2.rdf_in_role.cellml): **Valid file failed validation.**
* Output: ```Error on line 11. Reactions are not supported.```

[8.4.2.rdf_in_unit](../models_1_0/valid/8.4.2.rdf_in_unit.cellml): Valid file passed validation.

[8.4.2.rdf_in_units_1](../models_1_0/valid/8.4.2.rdf_in_units_1.cellml): Valid file passed validation.

[8.4.2.rdf_in_units_2](../models_1_0/valid/8.4.2.rdf_in_units_2.cellml): Valid file passed validation.

[8.4.2.rdf_in_variable](../models_1_0/valid/8.4.2.rdf_in_variable.cellml): Valid file passed validation.

🔴 [8.4.2.rdf_in_variable_ref](../models_1_0/valid/8.4.2.rdf_in_variable_ref.cellml): **Valid file failed validation.**
* Output: ```Error on line 11. Reactions are not supported.```


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

🔴 [C.3.3.unit_checking_function_factorial_operand_error](../models_1_0/unit_checking_inconsistent/C.3.3.unit_checking_function_factorial_operand_error.cellml): **Valid file failed validation.**
* Output: ```Error on line 17. Unsupported element in apply: {http://www.w3.org/1998/Math/MathML}factorial.```

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

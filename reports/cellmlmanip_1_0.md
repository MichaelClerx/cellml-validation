# Cellmlmanip Validation - CellML 1.0

Performance:
* 72% according to spec (278 out of 384)
* 253 out of 351 valid files passed
* 25 out of 33 invalid files detected

Issues:
* 98 valid files failed validation
* 0 invalid files passed validation
* 8 invalid files failed validation for the wrong reason

Results per category

(Valid passed, invalid failed, valid failed, invalid passed, invalid failed for wrong reason, percent classified correctly according to spec)

|Category|V Pass|I Fail|🔴 V Fail|🔵 I Pass|🔶 I Bad|Score|
|-|-|-|-|-|-|-|
|[0. Not mentioned in spec](#0-not-mentioned-in-spec)|6|0|0|0|0|100%|
|[2. Fundamentals](#2-fundamentals)|13|0|6|0|0|68%|
|[3. Model structure](#3-model-structure)|43|0|7|0|0|86%|
|[4. Mathematics](#4-mathematics)|31|0|14|0|0|68%|
|[5. Units](#5-units)|85|1|49|0|0|63%|
|[6. Grouping](#6-grouping)|12|0|5|0|0|70%|
|[7. Reactions](#7-reactions)|0|23|5|0|8|63%|
|[8. Metadata framework](#8-metadata-framework)|20|1|10|0|0|67%|
|[C. Advanced units functionality](#c-advanced-units-functionality)|43|0|2|0|0|95%|


---

## 0. Not mentioned in spec

### 0.0

[0.0.root_namespace_1](../models_1_0/valid/0.0.root_namespace_1.cellml): Valid file passed validation.

[0.0.root_namespace_2](../models_1_0/valid/0.0.root_namespace_2.cellml): Valid file passed validation.


---

### 0.1

[0.1.real_numbers](../models_1_0/valid/0.1.real_numbers.cellml): Valid file passed validation.

[0.1.real_numbers_extreme](../models_1_0/valid/0.1.real_numbers_extreme.cellml): Valid file passed validation.


---

### 0.2

[0.2.component_name_same_as_model](../models_1_0/valid/0.2.component_name_same_as_model.cellml): Valid file passed validation.

[0.2.variable_name_same_as_model](../models_1_0/valid/0.2.variable_name_same_as_model.cellml): Valid file passed validation.


---

## 2. Fundamentals

#### 2.4.1

[2.4.1.valid_identifiers](../models_1_0/valid/2.4.1.valid_identifiers.cellml): Valid file passed validation.


---

#### 2.4.3

[2.4.3.component_ref_with_extensions](../models_1_0/valid/2.4.3.component_ref_with_extensions.cellml): Valid file passed validation.

[2.4.3.component_with_extensions](../models_1_0/valid/2.4.3.component_with_extensions.cellml): Valid file passed validation.

🔴 [2.4.3.connection_with_extensions](../models_1_0/valid/2.4.3.connection_with_extensions.cellml): **Valid file failed validation.**
* Output: ```<class 'AssertionError'> with no error message set.```

[2.4.3.group_with_extensions](../models_1_0/valid/2.4.3.group_with_extensions.cellml): Valid file passed validation.

[2.4.3.map_components_with_extensions](../models_1_0/valid/2.4.3.map_components_with_extensions.cellml): Valid file passed validation.

[2.4.3.map_variables_with_extensions](../models_1_0/valid/2.4.3.map_variables_with_extensions.cellml): Valid file passed validation.

[2.4.3.model_with_extensions](../models_1_0/valid/2.4.3.model_with_extensions.cellml): Valid file passed validation.

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


---

#### 2.4.4

[2.4.4.model_linux_line_breaks](../models_1_0/valid/2.4.4.model_linux_line_breaks.cellml): Valid file passed validation.

[2.4.4.model_windows_line_breaks](../models_1_0/valid/2.4.4.model_windows_line_breaks.cellml): Valid file passed validation.

[2.4.4.model_with_spaces](../models_1_0/valid/2.4.4.model_with_spaces.cellml): Valid file passed validation.

[2.4.4.model_with_tabs](../models_1_0/valid/2.4.4.model_with_tabs.cellml): Valid file passed validation.


---

## 3. Model structure

##### 3.4.1.1

[3.4.1.1.model_child_order_1](../models_1_0/valid/3.4.1.1.model_child_order_1.cellml): Valid file passed validation.

[3.4.1.1.model_child_order_2](../models_1_0/valid/3.4.1.1.model_child_order_2.cellml): Valid file passed validation.

[3.4.1.1.model_empty](../models_1_0/valid/3.4.1.1.model_empty.cellml): Valid file passed validation.

[3.4.1.1.model_with_components](../models_1_0/valid/3.4.1.1.model_with_components.cellml): Valid file passed validation.

[3.4.1.1.model_with_connections](../models_1_0/valid/3.4.1.1.model_with_connections.cellml): Valid file passed validation.

[3.4.1.1.model_with_groups](../models_1_0/valid/3.4.1.1.model_with_groups.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_component](../models_1_0/valid/3.4.1.1.model_with_one_component.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_connection](../models_1_0/valid/3.4.1.1.model_with_one_connection.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_group](../models_1_0/valid/3.4.1.1.model_with_one_group.cellml): Valid file passed validation.

[3.4.1.1.model_with_one_units](../models_1_0/valid/3.4.1.1.model_with_one_units.cellml): Valid file passed validation.

[3.4.1.1.model_with_units](../models_1_0/valid/3.4.1.1.model_with_units.cellml): Valid file passed validation.


---

##### 3.4.2.1

🔴 [3.4.2.1.component_child_order_1](../models_1_0/valid/3.4.2.1.component_child_order_1.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

🔴 [3.4.2.1.component_child_order_2](../models_1_0/valid/3.4.2.1.component_child_order_2.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

[3.4.2.1.component_empty](../models_1_0/valid/3.4.2.1.component_empty.cellml): Valid file passed validation.

[3.4.2.1.component_with_maths](../models_1_0/valid/3.4.2.1.component_with_maths.cellml): Valid file passed validation.

[3.4.2.1.component_with_one_math](../models_1_0/valid/3.4.2.1.component_with_one_math.cellml): Valid file passed validation.

🔴 [3.4.2.1.component_with_one_reaction](../models_1_0/valid/3.4.2.1.component_with_one_reaction.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

🔴 [3.4.2.1.component_with_one_units](../models_1_0/valid/3.4.2.1.component_with_one_units.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

[3.4.2.1.component_with_one_variable](../models_1_0/valid/3.4.2.1.component_with_one_variable.cellml): Valid file passed validation.

🔴 [3.4.2.1.component_with_reactions](../models_1_0/valid/3.4.2.1.component_with_reactions.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

🔴 [3.4.2.1.component_with_units](../models_1_0/valid/3.4.2.1.component_with_units.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

[3.4.2.1.component_with_variables](../models_1_0/valid/3.4.2.1.component_with_variables.cellml): Valid file passed validation.


---

##### 3.4.3.1

[3.4.3.1.variable_with_initial_value](../models_1_0/valid/3.4.3.1.variable_with_initial_value.cellml): Valid file passed validation.

[3.4.3.1.variable_with_interfaces](../models_1_0/valid/3.4.3.1.variable_with_interfaces.cellml): Valid file passed validation.

[3.4.3.1.variable_without_initial_value](../models_1_0/valid/3.4.3.1.variable_without_initial_value.cellml): Valid file passed validation.


---

##### 3.4.3.2

[3.4.3.2.variable_name_same_as_cousin](../models_1_0/valid/3.4.3.2.variable_name_same_as_cousin.cellml): Valid file passed validation.

[3.4.3.2.variable_name_same_as_parent](../models_1_0/valid/3.4.3.2.variable_name_same_as_parent.cellml): Valid file passed validation.


---

##### 3.4.3.3

🔴 [3.4.3.3.variable_units_component](../models_1_0/valid/3.4.3.3.variable_units_component.cellml): **Valid file failed validation.**
* Output: ```'Unknown unit oranges.'```

[3.4.3.3.variable_units_model](../models_1_0/valid/3.4.3.3.variable_units_model.cellml): Valid file passed validation.

[3.4.3.3.variable_units_predefined](../models_1_0/valid/3.4.3.3.variable_units_predefined.cellml): Valid file passed validation.


---

##### 3.4.4.1

[3.4.4.1.connection_with_map_variables](../models_1_0/valid/3.4.4.1.connection_with_map_variables.cellml): Valid file passed validation.

[3.4.4.1.connection_with_one_map_variables](../models_1_0/valid/3.4.4.1.connection_with_one_map_variables.cellml): Valid file passed validation.


---

##### 3.4.5.1

[3.4.5.1.connection_any_order_1](../models_1_0/valid/3.4.5.1.connection_any_order_1.cellml): Valid file passed validation.

[3.4.5.1.connection_any_order_2](../models_1_0/valid/3.4.5.1.connection_any_order_2.cellml): Valid file passed validation.


---

##### 3.4.6.4

[3.4.6.4.map_variables_chain_down](../models_1_0/valid/3.4.6.4.map_variables_chain_down.cellml): Valid file passed validation.

[3.4.6.4.map_variables_chain_up](../models_1_0/valid/3.4.6.4.map_variables_chain_up.cellml): Valid file passed validation.

[3.4.6.4.map_variables_nested_sibling_connection](../models_1_0/valid/3.4.6.4.map_variables_nested_sibling_connection.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_connection_1](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_connection_2](../models_1_0/valid/3.4.6.4.map_variables_parent_connection_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_parent_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_parent_multiple_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_connection_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_connection_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_connection_3](../models_1_0/valid/3.4.6.4.map_variables_sibling_connection_3.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_multiple_1](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_1.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_multiple_2](../models_1_0/valid/3.4.6.4.map_variables_sibling_multiple_2.cellml): Valid file passed validation.

[3.4.6.4.map_variables_sibling_mutual](../models_1_0/valid/3.4.6.4.map_variables_sibling_mutual.cellml): Valid file passed validation.

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

[4.2.3_7.1_mathml_pi](../models_1_0/valid/4.2.3_7.1_mathml_pi.cellml): Valid file passed validation.

[4.2.3_7.2_mathml_e](../models_1_0/valid/4.2.3_7.2_mathml_e.cellml): Valid file passed validation.

🔴 [4.2.3_7.3_mathml_nan_inf](../models_1_0/valid/4.2.3_7.3_mathml_nan_inf.cellml): **Valid file failed validation.**
* Output: ```The argument `equation` must be a sympy.Eq.```

🔴 [4.2.3_8.1_annotation](../models_1_0/valid/4.2.3_8.1_annotation.cellml): **Valid file failed validation.**
* Output: ```No handler for element <semantics>```

🔴 [4.2.3_8.2_annotation_xml](../models_1_0/valid/4.2.3_8.2_annotation_xml.cellml): **Valid file failed validation.**
* Output: ```'Unknown unit per_millisecond.'```


---

#### 4.4.2

[4.4.2.ci_no_whitespace](../models_1_0/valid/4.4.2.ci_no_whitespace.cellml): Valid file passed validation.

[4.4.2.ci_whitespace_1](../models_1_0/valid/4.4.2.ci_whitespace_1.cellml): Valid file passed validation.

[4.4.2.ci_whitespace_2](../models_1_0/valid/4.4.2.ci_whitespace_2.cellml): Valid file passed validation.

[4.4.2.ci_whitespace_3](../models_1_0/valid/4.4.2.ci_whitespace_3.cellml): Valid file passed validation.


---

##### 4.4.3.1

🔴 [4.4.3.1.cn_component_units](../models_1_0/valid/4.4.3.1.cn_component_units.cellml): **Valid file failed validation.**
* Output: ```'Unknown unit wooster.'```

[4.4.3.1.cn_model_units](../models_1_0/valid/4.4.3.1.cn_model_units.cellml): Valid file passed validation.

[4.4.3.1.cn_predefined_units](../models_1_0/valid/4.4.3.1.cn_predefined_units.cellml): Valid file passed validation.


---

#### 4.4.4

[4.4.4.modify_private_out](../models_1_0/valid/4.4.4.modify_private_out.cellml): Valid file passed validation.

[4.4.4.modify_public_out](../models_1_0/valid/4.4.4.modify_public_out.cellml): Valid file passed validation.


---

#### 4.5.1

[4.5.1.ordering_not_significant](../models_1_0/valid/4.5.1.ordering_not_significant.cellml): Valid file passed validation.


---

🔴 [4.algebraic_model](../models_1_0/valid/4.algebraic_model.cellml): **Valid file failed validation.**
* Output: ```Equation LHS should be a derivative or variable, not _A$x + _A$y```

🔴 [4.algebraic_ode_model](../models_1_0/valid/4.algebraic_ode_model.cellml): **Valid file failed validation.**
* Output: ```Equation LHS should be a derivative or variable, not 2.0```


---

## 5. Units

#### 5.2.1

[5.2.1.units_ampere](../models_1_0/valid/5.2.1.units_ampere.cellml): Valid file passed validation.

[5.2.1.units_becquerel](../models_1_0/valid/5.2.1.units_becquerel.cellml): Valid file passed validation.

[5.2.1.units_candela](../models_1_0/valid/5.2.1.units_candela.cellml): Valid file passed validation.

🔴 [5.2.1.units_celsius](../models_1_0/valid/5.2.1.units_celsius.cellml): **Valid file failed validation.**
* Output: ```'celsius' is not defined in the unit registry```

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

[5.2.7.unit_checking_piecewise](../models_1_0/unit_checking_consistent/5.2.7.unit_checking_piecewise.cellml): Valid file passed validation.

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
* Output: ```Cannot convert from 'store346_wooster' ([store346_wooster]) to 'dimensionless' (dimensionless)```

[5.2.7.unit_conversion_offset](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_offset.cellml): Valid file passed validation.

[5.2.7.unit_conversion_prefix](../models_1_0/unit_conversion_convertible/5.2.7.unit_conversion_prefix.cellml): Valid file passed validation.


---

##### 5.4.1.1

[5.4.1.1.units_base_units](../models_1_0/valid/5.4.1.1.units_base_units.cellml): Valid file passed validation.

🔴 [5.4.1.1.units_empty_1](../models_1_0/valid/5.4.1.1.units_empty_1.cellml): **Valid file failed validation.**
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/valid/5.4.1.1.units_empty_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element unit, got nothing. /home/michael/dev/cellml/validation/models_1_0/valid/5.4.1.1.units_empty_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/5.4.1.1.units_empty_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/5.4.1.1.units_empty_1.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

🔴 [5.4.1.1.units_empty_2](../models_1_0/valid/5.4.1.1.units_empty_2.cellml): **Valid file failed validation.**
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/valid/5.4.1.1.units_empty_2.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_NOELEM: Expecting an element unit, got nothing. /home/michael/dev/cellml/validation/models_1_0/valid/5.4.1.1.units_empty_2.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/5.4.1.1.units_empty_2.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element units failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element units in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/5.4.1.1.units_empty_2.cellml:7:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element component failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element component in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/5.4.1.1.units_empty_2.cellml:6:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[5.4.1.1.units_with_unit_children](../models_1_0/valid/5.4.1.1.units_with_unit_children.cellml): Valid file passed validation.


---

##### 5.4.1.2

🔴 [5.4.1.2.units_names_and_other_names](../models_1_0/valid/5.4.1.2.units_names_and_other_names.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component units_names_and_other_names).```

🔴 [5.4.1.2.units_shadowing_1](../models_1_0/valid/5.4.1.2.units_shadowing_1.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

🔴 [5.4.1.2.units_shadowing_2](../models_1_0/valid/5.4.1.2.units_shadowing_2.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```


---

##### 5.4.2.1

[5.4.2.1.unit_offset_non_zero](../models_1_0/valid/5.4.2.1.unit_offset_non_zero.cellml): Valid file passed validation.

[5.4.2.1.unit_offset_zero](../models_1_0/valid/5.4.2.1.unit_offset_zero.cellml): Valid file passed validation.

[5.4.2.1.unit_prefix_exponent_multiplier](../models_1_0/valid/5.4.2.1.unit_prefix_exponent_multiplier.cellml): Valid file passed validation.

[5.4.2.1.unit_prefix_exponent_multiplier_huge](../models_1_0/valid/5.4.2.1.unit_prefix_exponent_multiplier_huge.cellml): Valid file passed validation.


---

##### 5.4.2.2

🔴 [5.4.2.2.unit_units_local_1](../models_1_0/valid/5.4.2.2.unit_units_local_1.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```

🔴 [5.4.2.2.unit_units_local_2](../models_1_0/valid/5.4.2.2.unit_units_local_2.cellml): **Valid file failed validation.**
* Output: ```Defining units inside components is not supported (found in component A).```


---

##### 5.4.2.3

[5.4.2.3.unit_prefix_integer](../models_1_0/valid/5.4.2.3.unit_prefix_integer.cellml): Valid file passed validation.

[5.4.2.3.unit_prefix_named](../models_1_0/valid/5.4.2.3.unit_prefix_named.cellml): Valid file passed validation.


---

##### 5.4.2.7

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

[5.5.2.boolean_compare_geq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_geq_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_gt_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_gt_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_leq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_leq_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_lt_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_lt_operand_error.cellml): Valid file passed validation.

[5.5.2.boolean_compare_neq_operand_error](../models_1_0/booleans/5.5.2.boolean_compare_neq_operand_error.cellml): Valid file passed validation.

🔴 [5.5.2.boolean_derivatives_1](../models_1_0/booleans/5.5.2.boolean_derivatives_1.cellml): **Valid file failed validation.**
* Output: ```The argument `equation` must be a sympy.Eq.```

🔴 [5.5.2.boolean_derivatives_2](../models_1_0/booleans/5.5.2.boolean_derivatives_2.cellml): **Valid file failed validation.**
* Output: ```'BooleanTrue' object has no attribute 'is_scalar'```

🔴 [5.5.2.boolean_function_abs](../models_1_0/booleans/5.5.2.boolean_function_abs.cellml): **Valid file failed validation.**
* Output: ```Bad argument type for Abs(): <class 'sympy.logic.boolalg.BooleanTrue'>```

🔴 [5.5.2.boolean_function_ceiling](../models_1_0/booleans/5.5.2.boolean_function_ceiling.cellml): **Valid file failed validation.**
* Output: ```BooleanAtom not allowed in this context.```

[5.5.2.boolean_function_exp](../models_1_0/booleans/5.5.2.boolean_function_exp.cellml): Valid file passed validation.

🔴 [5.5.2.boolean_function_factorial](../models_1_0/booleans/5.5.2.boolean_function_factorial.cellml): **Valid file failed validation.**
* Output: ```No handler for element <factorial>```

🔴 [5.5.2.boolean_function_floor](../models_1_0/booleans/5.5.2.boolean_function_floor.cellml): **Valid file failed validation.**
* Output: ```BooleanAtom not allowed in this context.```

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

[6.4.1.1.group_component_ref_multiple](../models_1_0/valid/6.4.1.1.group_component_ref_multiple.cellml): Valid file passed validation.

[6.4.1.1.group_component_ref_single](../models_1_0/valid/6.4.1.1.group_component_ref_single.cellml): Valid file passed validation.


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


---

##### 6.4.2.3

[6.4.2.3.relationship_ref_name_not_unique_model_wide](../models_1_0/valid/6.4.2.3.relationship_ref_name_not_unique_model_wide.cellml): Valid file passed validation.


---

##### 6.4.2.5

🔴 [6.4.2.5.relationship_ref_multiple_1](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_1.cellml): **Valid file failed validation.**
* Output: ```<class 'AssertionError'> with no error message set.```

🔴 [6.4.2.5.relationship_ref_multiple_2](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_2.cellml): **Valid file failed validation.**
* Output: ```<class 'AssertionError'> with no error message set.```

🔴 [6.4.2.5.relationship_ref_multiple_3](../models_1_0/valid/6.4.2.5.relationship_ref_multiple_3.cellml): **Valid file failed validation.**
* Output: ```<class 'AssertionError'> with no error message set.```


---

##### 6.4.3.1

[6.4.3.1.component_ref_nesting](../models_1_0/valid/6.4.3.1.component_ref_nesting.cellml): Valid file passed validation.


---

##### 6.4.3.2

🔴 [6.4.3.2.component_ref_no_children_extension](../models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml): **Valid file failed validation.**
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml:12:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element relationship_ref failed to validate content. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/valid/6.4.3.2.component_ref_no_children_extension.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

[6.4.3.2.component_ref_overlapping_containment](../models_1_0/valid/6.4.3.2.component_ref_overlapping_containment.cellml): Valid file passed validation.

[6.4.3.2.component_ref_split_named](../models_1_0/valid/6.4.3.2.component_ref_split_named.cellml): Valid file passed validation.

[6.4.3.2.component_ref_split_unnamed_1](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_1.cellml): Valid file passed validation.

[6.4.3.2.component_ref_split_unnamed_2](../models_1_0/valid/6.4.3.2.component_ref_split_unnamed_2.cellml): Valid file passed validation.


---

## 7. Reactions

##### 7.4.1.2

🔴 [7.4.1.2.reaction_reversible_no](../models_1_0/valid/7.4.1.2.reaction_reversible_no.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```

🔴 [7.4.1.2.reaction_reversible_yes](../models_1_0/valid/7.4.1.2.reaction_reversible_yes.cellml): **Valid file failed validation.**
* Output: ```Reactions are not supported (found in component A).```


---

##### 7.4.3.1

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

[8.4.1.cmeta_id_duplicate](../models_1_0/invalid/8.4.1.cmeta_id_duplicate.cellml): Error detected correctly.
* Expected: ```Invalid attribute id for element component_ref```
* Output: ```Invalid or unsupported CellML file. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.cmeta_id_duplicate.cellml:11:0:ERROR:RELAXNGV:RELAXNG_ERR_INVALIDATTR: Invalid attribute id for element component_ref. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.cmeta_id_duplicate.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_INTERSEQ: Invalid sequence in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.cmeta_id_duplicate.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element group failed to validate content. <string>:0:0:ERROR:RELAXNGV:RELAXNG_ERR_INTEREXTRA: Extra element group in interleave. /home/michael/dev/cellml/validation/models_1_0/invalid/8.4.1.cmeta_id_duplicate.cellml:9:0:ERROR:RELAXNGV:RELAXNG_ERR_CONTENTVALID: Element model failed to validate content```

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


---

#### 8.4.2

[8.4.2.rdf_in_component](../models_1_0/valid/8.4.2.rdf_in_component.cellml): Valid file passed validation.

[8.4.2.rdf_in_component_ref](../models_1_0/valid/8.4.2.rdf_in_component_ref.cellml): Valid file passed validation.

🔴 [8.4.2.rdf_in_connection](../models_1_0/valid/8.4.2.rdf_in_connection.cellml): **Valid file failed validation.**
* Output: ```<class 'AssertionError'> with no error message set.```

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

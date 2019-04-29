#
# Tests CellML 1.0 validation with cellmlmanip
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import logging
import os
import pytest

import check
from . import shared
from .. import cellmlmanip_validation
from .report import Report_1_0 as Report


# Known instances where cellmlmanip says a valid file is invalid
false_negatives = {
    '4.algebraic_model': '',
    '4.algebraic_ode_model': '',
    '2.4.3.connection_with_extensions': '',
    '2.4.3.units_with_extensions': 'units',
    '3.4.3.1.variable_with_interfaces': 'None',
    '3.4.3.3.variable_units_component':
        'Cannot find unit <oranges> in unit registry',
    '3.4.4.1.connection_with_one_map_variables': 'None',
    '4.2.3_2.1.mathml_numbers_real':
        'Unimplemented type attribute for <cn>: real',
    '4.2.3_2.2.mathml_numbers_integer':
        'Unimplemented type attribute for <cn>: integer',
    '4.2.3_2.3.mathml_numbers_real_base':
        'Unimplemented type attribute for <cn>: real',
    '4.2.3_2.4.mathml_numbers_integer_base':
        'Unimplemented type attribute for <cn>: integer',
    '4.2.3_2.6.mathml_numbers_rational':
        'Unimplemented type attribute for <cn>: rational',
    '4.2.3_3.2_mathml_arithmetic_unary': '!= dimensionless',
    '4.2.3_4.1_mathml_functions_basic': '',
    '4.2.3_4.3_mathml_functions_factorial': '',
    '4.2.3_5.2_mathml_derivatives_degree': '',
    '4.2.3_5.4_mathml_derivatives_with_units_degree': '',
    '4.2.3_6.6_mathml_logic_binary_operators': '',
    '4.2.3_6.7_mathml_logic_constants':
        'BooleanAtom not allowed in this context',
    '4.2.3_7.1_mathml_pi': '',
    '4.2.3_7.2_mathml_e': '',
    '4.2.3_7.3_mathml_nan_inf': 'Equation expression must be equality',
    '4.2.3_8.1_annotation': 'No handler for element <semantics>',
    '4.2.3_8.2_annotation_xml': 'Cannot find unit <per_millisecond>',
    '4.4.3.1.cn_component_units': 'Cannot find unit <wooster>',
    '5.2.7.unit_checking_derivatives_degree': '',
    '5.2.7.unit_checking_dimensionless': '',
    '5.2.7.unit_checking_functions_factorial':
        'No handler for element <factorial>',
    '5.2.7.unit_checking_functions_non_smooth': 'TODO',
    '5.2.7.unit_checking_functions_power_and_root':
        'Cannot find unit <meter_cubic> in unit registry',
    '5.2.7.unit_checking_name_differs':
        'Cannot find unit <wooster> in unit registry',
    '5.2.7.unit_checking_internal_mismatch_1': '!= ampere',
    '5.2.7.unit_checking_internal_mismatch_2': '!= ampere',
    '5.2.7.unit_checking_internal_mismatch_3': '!= dimensionless',
    '5.2.7.unit_checking_internal_mismatch_4': '!= millivolt',
    '5.2.7.unit_checking_piecewise_multi_unit': '',
    'C.3.3.unit_checking_arithmetic_minus_operand_error_1': '',
    'C.3.3.unit_checking_arithmetic_minus_operand_error_2': '',
    'C.3.3.unit_checking_arithmetic_minus_operand_error_3': '',
    'C.3.3.unit_checking_arithmetic_plus_operand_error_1': '',
    'C.3.3.unit_checking_arithmetic_plus_operand_error_2': '',
    'C.3.3.unit_checking_arithmetic_plus_operand_error_3': '',
    'C.3.3.unit_checking_arithmetic_plus_operand_error_4': '',
    'C.3.3.unit_checking_arithmetic_power_operand_error': '',
    'C.3.3.unit_checking_arithmetic_root_operand_error': '',
    'C.3.3.unit_checking_derivative_operand_error': '',
    'C.3.3.unit_checking_function_exp_operand_error': '',
    'C.3.3.unit_checking_function_factorial_operand_error':
        'No handler for element <factorial>',
    'C.3.3.unit_checking_function_ln_operand_error':
        'log args not dimensionless',
    'C.3.3.unit_checking_function_log_operand_error_1': '',
    'C.3.3.unit_checking_function_log_operand_error_2':
        'log args not dimensionless',
    'C.3.3.unit_checking_trig_arccosh_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_arccos_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_arccoth_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_arccot_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_arccsch_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_arccsc_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_arcsech_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_arcsec_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_arcsinh_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_arcsin_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_arctanh_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_arctan_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_cosh_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_cos_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_coth_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_cot_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_csch_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_csc_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_sech_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_sec_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_sinh_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_sin_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_tanh_operand_error': 'TODO',
    'C.3.3.unit_checking_trig_tan_operand_error': 'TODO',
    '5.2.7.unit_conversion_dimensionless_multiplier_1': '!= dimensionless',
    '5.2.7.unit_conversion_dimensionless_multiplier_2': '!= dimensionless',
    '5.2.7.unit_conversion_less_obvious': '!= millijoule_per_meter',
    '5.2.7.unit_conversion_multiplier': '!= imperial_volt',
    '5.2.7.unit_conversion_offset': '!= uk_adult_shoe',
    '5.2.7.unit_conversion_prefix': '!= millivolt',
    '5.2.7.unit_conversion_inconvertible_1': '!= volt',
    '5.2.7.unit_conversion_new_base_units': '!= wooster',
    '5.4.1.2.units_shadowing_2': '!= newton',
    '5.4.2.3.unit_prefix_integer':
        'Cannot find unit <celsius> in unit registry',
    '5.4.2.3.unit_prefix_named':
        'Cannot find unit <celsius> in unit registry',
    '5.4.2.7.unit_offset_non_zero_and_exponent_one': 'units',
    '5.5.2.boolean_arithmetic_divide':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_arithmetic_minus':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_arithmetic_plus':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_arithmetic_power_1':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_arithmetic_power_2':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_arithmetic_root_1':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_arithmetic_root_2':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_arithmetic_times':
        "'BooleanTrue' object has no attribute 'as_base_exp'",
    '5.5.2.boolean_compare_eq_operand_error':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_compare_geq_operand_error':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_compare_gt_operand_error':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_compare_leq_operand_error':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_compare_lt_operand_error':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_derivatives_1': 'TODO',
    '5.5.2.boolean_derivatives_2': '',
    '5.5.2.boolean_function_abs':
        'Bad argument type for Abs()',
    '5.5.2.boolean_function_ceiling':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_function_exp':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_function_factorial':
        'No handler for element <factorial>',
    '5.5.2.boolean_function_floor':
        'BooleanAtom not allowed in this context',
    '5.5.2.boolean_function_ln':
        "'BooleanTrue' object has no attribute 'as_coefficient'",
    '5.5.2.boolean_function_log_1':
        "'BooleanTrue' object has no attribute 'as_coefficient'",
    '5.5.2.boolean_function_log_2':
        "'BooleanTrue' object has no attribute 'as_coefficient'",
    '5.5.2.boolean_logic_and_operand_error':
        'but must be a Relational',
    '5.5.2.boolean_trig_arccos':
        "'BooleanTrue' object has no attribute 'could_extract_minus_sign'",
    '5.5.2.boolean_trig_arccosh':
        "BooleanAtom not allowed in this context",
    '5.5.2.boolean_trig_arccot':
        "'BooleanTrue' object has no attribute 'could_extract_minus_sign'",
    '5.5.2.boolean_trig_arccoth':
        "'BooleanTrue' object has no attribute 'as_coefficient'",
    '5.5.2.boolean_trig_arccsc':
        "BooleanAtom not allowed in this context",
    '5.5.2.boolean_trig_arccsch':
        "BooleanAtom not allowed in this context",
    '5.5.2.boolean_trig_arcsec':
        "BooleanAtom not allowed in this context",
    '5.5.2.boolean_trig_arcsech':
        "BooleanAtom not allowed in this context",
    '5.5.2.boolean_trig_arcsin':
        "'BooleanTrue' object has no attribute 'could_extract_minus_sign'",
    '5.5.2.boolean_trig_arcsinh':
        "'BooleanTrue' object has no attribute 'as_coefficient'",
    '5.5.2.boolean_trig_arctan':
        "'BooleanTrue' object has no attribute 'could_extract_minus_sign'",
    '5.5.2.boolean_trig_arctanh':
        "'BooleanTrue' object has no attribute 'as_coefficient'",
    '5.5.2.boolean_trig_cos':
        "'BooleanTrue' object has no attribute 'could_extract_minus_sign'",
    '5.5.2.boolean_trig_cosh':
        "'BooleanTrue' object has no attribute 'as_coefficient'",
    '5.5.2.boolean_trig_cot':
        "'BooleanTrue' object has no attribute 'could_extract_minus_sign'",
    '5.5.2.boolean_trig_coth':
        "'BooleanTrue' object has no attribute 'as_coefficient'",
    '5.5.2.boolean_trig_csc':
        "'BooleanTrue' object has no attribute 'could_extract_minus_sign'",
    '5.5.2.boolean_trig_csch':
        "'BooleanTrue' object has no attribute 'could_extract_minus_sign'",
    '5.5.2.boolean_trig_sec':
        "'BooleanTrue' object has no attribute 'could_extract_minus_sign'",
    '5.5.2.boolean_trig_sech':
        "'BooleanTrue' object has no attribute 'could_extract_minus_sign'",
    '5.5.2.boolean_trig_sin':
        "'BooleanTrue' object has no attribute 'could_extract_minus_sign'",
    '5.5.2.boolean_trig_sinh':
        "'BooleanTrue' object has no attribute 'as_coefficient'",
    '5.5.2.boolean_trig_tan':
        "'BooleanTrue' object has no attribute 'could_extract_minus_sign'",
    '5.5.2.boolean_trig_tanh':
        "'BooleanTrue' object has no attribute 'as_coefficient'",
    '5.5.2.boolean_variable_1': 'TODO',
    '5.5.2.boolean_variable_2': 'TODO',
    '5.5.2.boolean_variable_3': 'TODO',
    '6.4.2.5.relationship_ref_multiple_1': '',
    '6.4.2.5.relationship_ref_multiple_2': '',
    '6.4.2.5.relationship_ref_multiple_3': '',
    '8.4.2.rdf_in_connection': '',
    '8.4.2.rdf_in_units_1': 'units',
}


# Expected error messages for invalid files.
expected_messages = {
    # Not in spec: Root node
    '0.0.root_node_two_elements': 'Extra content at the end of the document',
    '0.0.root_node_two_models': 'Extra content at the end of the document',
    # Not in spec: Real number format
    '0.1.real_number_invalid_1': 'could not convert string to float',
    '0.1.real_number_invalid_2': 'could not convert string to float',
    '0.1.real_number_invalid_3': 'could not convert string to float',
    '0.1.real_number_invalid_4': 'could not convert string to float',
    '0.1.real_number_invalid_5': 'could not convert string to float',
    '0.1.real_number_invalid_6': 'could not convert string to float',
    # 3.4.3.1 Variables must have a name attribute
    '3.4.3.1.variable_name_missing': "'name'",
    # 3.4.3.1 Variables must have a units attribute
    '3.4.3.1.variable_units_missing': 'add_variable() missing 1 required',
    # 3.4.3.2 A variable name must be unique with the component
    '3.4.3.2.variable_name_duplicate': 'already exists',
    # 3.4.3.3 A variable must reference known units
    '3.4.3.3.variable_units_unknown':
        'Cannot find unit <oranges> in unit registry',
    # 3.4.3.3 A variable cannot reference another component's units
    '3.4.3.3.variable_units_other_component':
        'Cannot find unit <oranges> in unit registry',
    # 3.4.3.7 The initial value (if present) must be a real number
    '3.4.3.7.variable_initial_value_empty':
        'could not convert string to float',
    '3.4.3.7.variable_initial_value_invalid':
        'could not convert string to float',
    #'3.4.4.1.connection_with_math':
    '3.4.4.1.connection_empty': 'list index out of range',
    # 3.4.5.1 A map_components must declare component_1 and component_2
    '3.4.5.1.map_components_component_1_missing':
        'unsupported operand type(s) for +',
    '3.4.5.1.map_components_component_2_missing':
        'unsupported operand type(s) for +',
    # 3.4.5.2 component_1 must refer to an existing component
    '3.4.5.2.map_components_component_1_nonexistent':
        'c$x',
    # 3.4.5.3 component_2 must refer to an existing component
    '3.4.5.3.map_components_component_2_nonexistent':
        'c$x',
    # 3.4.5.4 component_1 cannot match component_2
    '3.4.5.4.map_components_component_1_equals_2':
        'Cannot determine the source & target for connection',
    # 3.4.6.1 A map_variables must declare variable_1 and variable_2
    '3.4.6.1.map_variables_variable_1_missing': 'must be str, not NoneType',
    '3.4.6.1.map_variables_variable_2_missing': 'must be str, not NoneType',
    # 3.4.6.2 variable_1 must refer to an existing variable in component_1
    '3.4.6.2.map_variables_variable_1_nonexistent': 'c1$a',
    # 3.4.6.3 variable_2 must refer to an existing variable in component_2
    '3.4.6.3.map_variables_variable_2_nonexistent': 'c2$b',
    # 3.4.6.4 Interfaces and encapsulation
    '3.4.6.4.map_variables_child_multiple_out_1':
        'Target already assigned to',
    '3.4.6.4.map_variables_child_multiple_out_2':
        'Target already assigned to',
    '3.4.6.4.map_variables_child_out_to_out_1':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_child_out_to_out_2':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_child_private_in':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_child_private_out':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_hidden_aunt_1':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_hidden_aunt_2':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_hidden_cousins_1':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_hidden_cousins_2':
        'Cannot determine the source & target for connection',
    #'3.4.6.4.map_variables_hidden_cousins_3':
    #    'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_hidden_cousins_4':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_hidden_grandchild_1':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_hidden_grandchild_2':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_hidden_grandparent_1':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_hidden_grandparent_2':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_hidden_niece_1':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_hidden_niece_2':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_nested_sibling_private_in':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_nested_sibling_private_in_and_out':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_nested_sibling_private_out':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_parent_in_to_in_1':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_parent_in_to_in_2':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_parent_multiple_out':
        'Target already assigned',
    '3.4.6.4.map_variables_parent_out_to_out_1':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_parent_out_to_out_2':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_parent_public_in':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_parent_public_out':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_sibling_in_to_in':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_sibling_multiple_out_1':
        'Target already assigned',
    '3.4.6.4.map_variables_sibling_multiple_out_2':
        'Target already assigned',
    '3.4.6.4.map_variables_sibling_out_to_out':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_sibling_private_in_1':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_sibling_private_in_2':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_sibling_private_in_and_out':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_sibling_private_out_1':
        'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_sibling_private_out_2':
        'Cannot determine the source & target for connection',
    # 4.4.1 Bad math
    '4.4.1.math_not_math_component': 'No handler for element <cake>',
    # 4.4.2 Ci can only refer to local variables
    '4.4.2.ci_nonexistent': 'not found in symbol dict',
    '4.4.2.ci_non_local_aunt': 'not found in symbol dict',
    '4.4.2.ci_non_local_child': 'not found in symbol dict',
    '4.4.2.ci_non_local_cousin': 'not found in symbol dict',
    '4.4.2.ci_non_local_nested_sibling': 'not found in symbol dict',
    '4.4.2.ci_non_local_niece': 'not found in symbol dict',
    '4.4.2.ci_non_local_parent': 'not found in symbol dict',
    '4.4.2.ci_non_local_sibling': 'not found in symbol dict',
    # 4.4.3.1 A cn must have a cellml:units
    '4.4.3.1.cn_units_missing': 'cellml:units',
    # 4.4.3.2 A cn unit attribute must refer to a model, local component, or
    #         predefined unit
    '4.4.3.2.cn_units_nonexistent_1': 'Cannot find unit',
    '4.4.3.2.cn_units_nonexistent_2': 'Cannot find unit',
    '4.4.3.2.cn_units_parent_component': 'Cannot find unit',
    # 4.4.4 A mathml:math can only modify 'owned' variables
    '4.4.4.modify_nonexistent': 'A$x',
    # 5.4.1.1 Unitses must have a name
    '5.4.1.1.units_name_missing':
        'attribute name must be string',
    # 5.4.1.1 A units can only contain unit elements
    '5.4.1.1.units_with_component': 'units',
    '5.4.1.1.units_with_component_ref': 'units',
    '5.4.1.1.units_with_connection': 'units',
    '5.4.1.1.units_with_group': 'units',
    '5.4.1.1.units_with_map_components': 'units',
    '5.4.1.1.units_with_map_variables': 'units',
    '5.4.1.1.units_with_model': 'units',
    '5.4.1.1.units_with_relationship_ref': 'units',
    # 5.4.1.2 A units name must be a valid identifier
    '5.4.1.2.units_name_invalid':
        "'UnitRegistry' object has no attribute '_'",
    # 5.4.1.2 Units names cannot overlap with predefined ones
    '5.4.1.2.units_name_predefined_ampere': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_becquerel': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_candela': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_celsius': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_coulomb': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_dimensionless':
        'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_farad': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_gram': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_gray': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_henry': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_hertz': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_joule': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_katal': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_kelvin': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_kilogram': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_liter': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_litre': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_lumen': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_lux': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_meter': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_metre': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_mole': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_newton': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_ohm': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_pascal': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_radian': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_second': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_siemens': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_sievert': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_steradian': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_tesla': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_volt': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_watt': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_weber': 'Cannot redefine CellML unit',
    # 5.4.2.1 A unit must have a units attribute
    '5.4.2.1.unit_units_missing': 'units',
    # 5.4.2.2 A unit must refer to an existing units
    #'5.4.2.2.unit_units_invalid':
    # 5.4.2.2 A unit cannot refer to itself directly or indirectly
    #'5.4.2.2.unit_cycle_1':
    #'5.4.2.2.unit_cycle_2':
    #'5.4.2.2.unit_cycle_3':
    # 5.4.2.3 Allowed values of the prefix attribute
    '5.4.2.3.unit_prefix_spaces':
        "'e' is not defined in the unit registry",
    '5.4.2.3.unit_prefix_unknown':
        "'eflotta' is not defined in the unit registry",
    # 5.4.2.4 A unit exponent must be a real number
    '5.4.2.4.unit_exponent_invalid':
        "'yes' is not defined in the unit registry",
    # 5.4.2.5 A unit multiplier must be a real number
    '5.4.2.5.unit_multiplier_invalid':
        "'three' is not defined in the unit registry",
    # 6.4.3.2 Encapsulation relationships cannot overlap
    '6.4.3.2.component_ref_overlapping_encapsulation':
        'Parent of component B already A.',










}


# Invalid models for which validation is not expected to pick up the (correct)
# error.
known_issues = {
    # Not in spec: Root node
    '0.0.root_node_namespace_wrong',
    '0.0.root_node_not_model',
    # 2.4.1 CellML Identifiers
    '2.4.1.identifier_empty',
    '2.4.1.identifier_only_underscore',
    '2.4.1.identifier_unexpected_character_1',
    '2.4.1.identifier_unexpected_character_2',
    '2.4.1.identifier_unexpected_character_unicode',
    # 2.4.2. Allowable CellML elements and attributes
    '2.4.2.imaginary_attributes_1',
    '2.4.2.imaginary_attributes_2',
    '2.4.2.imaginary_elements',
    # 2.4.3 Elements/attributes in extension namespaces
    '2.4.3.cellml_attributes_inside_extensions',
    '2.4.3.cellml_elements_inside_extensions',
    # 2.4.4 Text in CellML elements
    '2.4.4.text_in_component',
    '2.4.4.text_in_component_ref',
    '2.4.4.text_in_connection',
    '2.4.4.text_in_group',
    '2.4.4.text_in_map_components',
    '2.4.4.text_in_map_variables',
    '2.4.4.text_in_model',
    '2.4.4.text_in_reaction',
    '2.4.4.text_in_relationship_ref',
    '2.4.4.text_in_role',
    '2.4.4.text_in_unit',
    '2.4.4.text_in_units_1',
    '2.4.4.text_in_units_2',
    '2.4.4.text_in_variable',
    '2.4.4.text_in_variable_ref',
    # 2.5.1 Identifiers are case sensitive
    '2.5.1.identifiers_are_case_sensitive',
    # 2.5.2 There are no attributes in the CellML namespace
    '2.5.2.attribute_in_cellml_namespace',
    # 3.4.1.1 Models contain only units, component, group, connection
    '3.4.1.1.model_with_component_ref',
    '3.4.1.1.model_with_map_components',
    '3.4.1.1.model_with_map_variables',
    '3.4.1.1.model_with_math',
    '3.4.1.1.model_with_model',
    '3.4.1.1.model_with_reaction',
    '3.4.1.1.model_with_relationship_ref',
    '3.4.1.1.model_with_role',
    '3.4.1.1.model_with_unit',
    '3.4.1.1.model_with_variable_ref',
    '3.4.1.1.model_with_variable',
    # 3.4.1.1 Models must have a name
    '3.4.1.1.model_name_missing',
    # 3.4.1.2 A model name must be a valid identifier
    '3.4.1.2.model_name_invalid',
    # 3.4.2.1 Components must have a name
    '3.4.2.1.component_name_missing',
    # 3.4.2.1 Components contain only units, variable, reaction, math
    '3.4.2.1.component_with_component',
    '3.4.2.1.component_with_component_ref',
    '3.4.2.1.component_with_connection',
    '3.4.2.1.component_with_group',
    '3.4.2.1.component_with_map_components',
    '3.4.2.1.component_with_map_variables',
    '3.4.2.1.component_with_model',
    '3.4.2.1.component_with_relationship_ref',
    '3.4.2.1.component_with_role',
    '3.4.2.1.component_with_unit',
    '3.4.2.1.component_with_variable_ref',
    # 3.4.2.2 A component name must be a valid identifier
    '3.4.2.2.component_name_invalid',
    # 3.4.2.2 Component names must be unique
    '3.4.2.2.component_name_duplicate',
    # 3.4.3.1 Variables can't contain any elements
    '3.4.3.1.variable_with_component',
    '3.4.3.1.variable_with_component_ref',
    '3.4.3.1.variable_with_connection',
    '3.4.3.1.variable_with_group',
    '3.4.3.1.variable_with_map_components',
    '3.4.3.1.variable_with_map_variables',
    '3.4.3.1.variable_with_math',
    '3.4.3.1.variable_with_model',
    '3.4.3.1.variable_with_reaction',
    '3.4.3.1.variable_with_relationship_ref',
    '3.4.3.1.variable_with_role',
    '3.4.3.1.variable_with_unit',
    '3.4.3.1.variable_with_units',
    '3.4.3.1.variable_with_variable_ref',
    '3.4.3.1.variable_with_variable',
    # 3.4.3.2 A variable name must be an identifier
    '3.4.3.2.variable_name_invalid',
    # 3.4.3.4 A public interface must be one of in/out/none
    '3.4.3.4.variable_interface_public_invalid',
    # 3.4.3.5 A private interface must be one of in/out/none
    '3.4.3.5.variable_interface_private_invalid',
    # 3.4.3.6 The private and public interface can't both be in
    '3.4.3.6.variable_interfaces_both_in',
    # 3.4.3.8 A variable can't have an initial value and an "in" interface
    '3.4.3.8.variable_interfaces_private_in_and_initial',
    '3.4.3.8.variable_interfaces_public_in_and_initial',
    # 3.4.4.1 A connection must contain exactly one map_components
    '3.4.4.1.connection_map_components_missing',
    '3.4.4.1.connection_map_components_multiple',
    # 3.4.4.1 A component must contain at least one map_variables
    '3.4.4.1.connection_map_variables_missing_1',
    '3.4.4.1.connection_map_variables_missing_2',
    # 3.4.4.1 A connection must have map_components and map_variables
    '3.4.4.1.connection_only_extensions',
    # 3.4.4.1 A connection can only contain map_components and map_variables
    '3.4.4.1.connection_with_component',
    '3.4.4.1.connection_with_component_ref',
    '3.4.4.1.connection_with_connection',
    '3.4.4.1.connection_with_group',
    #'3.4.4.1.connection_with_map_components':
    #'3.4.4.1.connection_with_map_variables',
    '3.4.4.1.connection_with_math',
    '3.4.4.1.connection_with_model',
    '3.4.4.1.connection_with_name_attribute',
    '3.4.4.1.connection_with_reaction',
    '3.4.4.1.connection_with_relationship_ref',
    '3.4.4.1.connection_with_role',
    '3.4.4.1.connection_with_unit',
    '3.4.4.1.connection_with_units',
    '3.4.4.1.connection_with_variable_ref',
    '3.4.4.1.connection_with_variable',
    # 3.4.5.1 A map_components cannot have cellml children or math
    '3.4.5.1.map_components_with_component',
    '3.4.5.1.map_components_with_component_ref',
    '3.4.5.1.map_components_with_connection',
    '3.4.5.1.map_components_with_group',
    '3.4.5.1.map_components_with_map_components',
    '3.4.5.1.map_components_with_map_variables',
    '3.4.5.1.map_components_with_math',
    '3.4.5.1.map_components_with_model',
    '3.4.5.1.map_components_with_reaction',
    '3.4.5.1.map_components_with_relationship_ref',
    '3.4.5.1.map_components_with_role',
    '3.4.5.1.map_components_with_unit',
    '3.4.5.1.map_components_with_units',
    '3.4.5.1.map_components_with_variable_ref',
    '3.4.5.1.map_components_with_variable',
    # 3.4.5.4 Each map_components in a model must be unique
    '3.4.5.4.map_components_duplicate_mirrored',
    '3.4.5.4.map_components_duplicate',
    # 3.4.6.1 A map_variables cannot have cellml children or math
    '3.4.6.1.map_variables_with_component',
    '3.4.6.1.map_variables_with_component_ref',
    '3.4.6.1.map_variables_with_connection',
    '3.4.6.1.map_variables_with_group',
    '3.4.6.1.map_variables_with_map_components',
    '3.4.6.1.map_variables_with_map_variables',
    '3.4.6.1.map_variables_with_math',
    '3.4.6.1.map_variables_with_model',
    '3.4.6.1.map_variables_with_reaction',
    '3.4.6.1.map_variables_with_relationship_ref',
    '3.4.6.1.map_variables_with_role',
    '3.4.6.1.map_variables_with_unit',
    '3.4.6.1.map_variables_with_units',
    '3.4.6.1.map_variables_with_variable_ref',
    '3.4.6.1.map_variables_with_variable',
    # 3.4.6.4 Interfaces and encapsulation
    '3.4.6.4.map_variables_hidden_cousins_3',
    # 4 Math can't be overdefined
    '4.math_and_initial_value',
    '4.math_overdefined',
    # 4.4.1 Bad math
    '4.4.1.math_not_math_reaction',
    # 4.4.4 A mathml:math can only modify 'owned' variables
    '4.4.4.modify_private_in',
    '4.4.4.modify_public_in',
    # CellML prefers deka over deca
    '5.2.2.unit_deca',
    # 5.4.1.1 A units with base_units="yes" can't have children
    '5.4.1.1.units_base_units_with_children',
    # 5.4.1.1 A units can only contain unit elements
    '5.4.1.1.units_with_math',
    '5.4.1.1.units_with_reaction',
    '5.4.1.1.units_with_role',
    '5.4.1.1.units_with_units',
    '5.4.1.1.units_with_variable_ref',
    '5.4.1.1.units_with_variable',
    # 5.4.1.2 Units names must be unique (within model or local component)
    '5.4.1.2.units_name_duplicate_1',
    '5.4.1.2.units_name_duplicate_2',
    # 5.4.1.2 Component units names cannot overlap with predefined ones
    '5.4.1.2.units_name_predefined_component_ampere',
    # 5.4.1.3 Units base_units attribute can only be yes or no
    '5.4.1.3.units_base_units_invalid',
    # 5.4.2.1 A unit cannot have CellML children
    '5.4.2.1.unit_with_component',
    '5.4.2.1.unit_with_component_ref',
    '5.4.2.1.unit_with_connection',
    '5.4.2.1.unit_with_group',
    '5.4.2.1.unit_with_map_components',
    '5.4.2.1.unit_with_map_variables',
    '5.4.2.1.unit_with_math',
    '5.4.2.1.unit_with_model',
    '5.4.2.1.unit_with_reaction',
    '5.4.2.1.unit_with_relationship_ref',
    '5.4.2.1.unit_with_role',
    '5.4.2.1.unit_with_unit',
    '5.4.2.1.unit_with_units',
    '5.4.2.1.unit_with_variable_ref',
    '5.4.2.1.unit_with_variable',
    # 5.4.2.3 Allowed values of the prefix attribute
    '5.4.2.3.unit_prefix_real',
    '5.4.2.3.unit_prefix_real_int',
    # 5.4.2.6 A unit offset must be a real number
    '5.4.2.6.unit_offset_invalid',
    # 5.4.2.7: A unit with a non-zero offset must have exponent 1
    '5.4.2.7.unit_offset_and_exponent',
    # 5.4.2.7: A unit with an offset can't have siblings
    '5.4.2.7.unit_offset_and_siblings_1',
    '5.4.2.7.unit_offset_and_siblings_2',
    # 6.4.1.1 A group must have at least one component_ref
    '6.4.1.1.group_component_ref_missing_1',
    '6.4.1.1.group_component_ref_missing_2',
    # 6.4.1.1 A group cannot be empty (extra test for missing comp_ref/rel_ref)
    '6.4.1.1.group_empty',
    '6.4.1.1.group_only_extensions',
    # 6.4.1.1 A group must have at least one relationship_ref
    '6.4.1.1.group_relationship_ref_missing_1',
    '6.4.1.1.group_relationship_ref_missing_2',
    # 6.4.1.1 A group can only contain component_refs and relationship_refs
    '6.4.1.1.group_with_component',
    '6.4.1.1.group_with_component_ref',
    '6.4.1.1.group_with_connection',
    '6.4.1.1.group_with_group',
    '6.4.1.1.group_with_map_components',
    '6.4.1.1.group_with_map_variables',
    '6.4.1.1.group_with_math',
    '6.4.1.1.group_with_model',
    '6.4.1.1.group_with_reaction',
    '6.4.1.1.group_with_relationship_ref',
    '6.4.1.1.group_with_role',
    '6.4.1.1.group_with_unit',
    '6.4.1.1.group_with_units',
    '6.4.1.1.group_with_variable_ref',
    '6.4.1.1.group_with_variable',
    # 6.4.2.1 A relationship_ref must define a relationship - although it can
    #         be either namespaceless, or in any extension namespace!
    '6.4.2.1.relationship_ref_relationship_missing',
    # 6.4.2.1 A relationship_ref cannot have any CellML children
    '6.4.2.1.relationship_ref_with_component',
    '6.4.2.1.relationship_ref_with_component_ref',
    '6.4.2.1.relationship_ref_with_connection',
    '6.4.2.1.relationship_ref_with_group',
    '6.4.2.1.relationship_ref_with_map_components',
    '6.4.2.1.relationship_ref_with_map_variables',
    '6.4.2.1.relationship_ref_with_math',
    '6.4.2.1.relationship_ref_with_model',
    '6.4.2.1.relationship_ref_with_reaction',
    '6.4.2.1.relationship_ref_with_relationship_ref',
    '6.4.2.1.relationship_ref_with_role',
    '6.4.2.1.relationship_ref_with_unit',
    '6.4.2.1.relationship_ref_with_units',
    '6.4.2.1.relationship_ref_with_variable_ref',
    '6.4.2.1.relationship_ref_with_variable',
    # 6.4.2.2 When not in a namespace, a relationship_ref's relationship must
    # be either containment or encapsulation.
    '6.4.2.2.relationship_ref_relationship_invalid',
    # 6.4.2.3 A relationship_ref name must be a cellml identifier
    '6.4.2.3.relationship_ref_name_invalid',
    # 6.4.2.4 An encapsulation can not be named
    '6.4.2.4.relationship_ref_encapsulation_duplicate',
    '6.4.2.4.relationship_ref_encapsulation_named',
    # 6.2.4.5 name/relationship pairs must be unique
    '6.4.2.5.relationship_ref_duplicate_named',
    '6.4.2.5.relationship_ref_duplicate_unnamed_1',
    '6.4.2.5.relationship_ref_duplicate_unnamed_2',
    # 6.4.3.1 A component_ref must define a component
    '6.4.3.1.component_ref_component_missing',
    # 6.4.3.1 A component_ref can only contain a component_ref
    '6.4.3.1.component_ref_with_component',
    '6.4.3.1.component_ref_with_connection',
    '6.4.3.1.component_ref_with_group',
    '6.4.3.1.component_ref_with_map_components',
    '6.4.3.1.component_ref_with_map_variables',
    '6.4.3.1.component_ref_with_math',
    '6.4.3.1.component_ref_with_model',
    '6.4.3.1.component_ref_with_reaction',
    '6.4.3.1.component_ref_with_relationship_ref',
    '6.4.3.1.component_ref_with_role',
    '6.4.3.1.component_ref_with_unit',
    '6.4.3.1.component_ref_with_units',
    '6.4.3.1.component_ref_with_variable_ref',
    '6.4.3.1.component_ref_with_variable',
    # 6.4.3.2 A component's children cannot be declared two places
    '6.4.3.2.component_ref_children_declared_twice_1',
    '6.4.3.2.component_ref_children_declared_twice_2',
    '6.4.3.2.component_ref_children_declared_twice_3',
    # 6.4.3.3 A hierarchy cannot be circular
    '6.4.3.2.component_ref_cycle_1',
    '6.4.3.2.component_ref_cycle_2',
    '6.4.3.2.component_ref_cycle_3',
    '6.4.3.2.component_ref_cycle_4',
    # 6.4.3.2 A component cannot be named twice in a single hierarchy
    '6.4.3.2.component_ref_duplicate_child_1',
    '6.4.3.2.component_ref_duplicate_child_2',
    # 6.4.3.2 The first component_ref in a containment must have children
    '6.4.3.2.component_ref_no_children_containment',
    # 6.4.3.2 The first component_ref in an encapsulation must have children
    '6.4.3.2.component_ref_no_children_encapsulation',
    # 6.4.3.3 A component attribute must be an identifier
    '6.4.3.3.component_ref_component_invalid',
    # 6.4.3.3 A component_ref must refer to an existing component
    '6.4.3.3.component_ref_component_nonexistent_1',
    '6.4.3.3.component_ref_component_nonexistent_2',
    # 7.4.1.1 A reaction must contain at least one variable_ref
    '7.4.1.1.reaction_variable_ref_missing',
    # 7.4.1.1 A reaction can only contain a variable_ref
    '7.4.1.1.reaction_with_component',
    '7.4.1.1.reaction_with_component_ref',
    '7.4.1.1.reaction_with_connection',
    '7.4.1.1.reaction_with_group',
    '7.4.1.1.reaction_with_map_components',
    '7.4.1.1.reaction_with_map_variables',
    '7.4.1.1.reaction_with_math',
    '7.4.1.1.reaction_with_model',
    '7.4.1.1.reaction_with_reaction',
    '7.4.1.1.reaction_with_relationship_ref',
    '7.4.1.1.reaction_with_role',
    '7.4.1.1.reaction_with_unit',
    '7.4.1.1.reaction_with_units',
    '7.4.1.1.reaction_with_variable',
    # 7.4.1.2 The reversible attribute can only be yes or no
    '7.4.1.2.reaction_reversible_invalid',
    # 7.4.1.3 A reaction in an encapsulating component cannot use
    # delta_variable attributes in its roles.
    '7.4.1.3.reaction_encapsulating_delta_variable',
    # 7.4.1.3 There's another rule about maths here that I don't understand
    # 7.4.2.1 A variable_ref must have at least one role
    '7.4.2.1.variable_ref_role_missing',
    '7.4.2.1.variable_ref_variable_missing',
    # 7.4.2.1 A variable_ref can only contain a role
    '7.4.2.1.variable_ref_with_component_ref',
    '7.4.2.1.variable_ref_with_component',
    '7.4.2.1.variable_ref_with_connection',
    '7.4.2.1.variable_ref_with_group',
    '7.4.2.1.variable_ref_with_map_components',
    '7.4.2.1.variable_ref_with_map_variables',
    '7.4.2.1.variable_ref_with_math',
    '7.4.2.1.variable_ref_with_model',
    '7.4.2.1.variable_ref_with_reaction',
    '7.4.2.1.variable_ref_with_relationship_ref',
    '7.4.2.1.variable_ref_with_unit',
    '7.4.2.1.variable_ref_with_units',
    '7.4.2.1.variable_ref_with_variable_ref',
    '7.4.2.1.variable_ref_with_variable',
    # 7.4.2.1 A variable_ref must refer to a local variable
    '7.4.2.2.variable_ref_variable_hidden',
    '7.4.2.2.variable_ref_variable_nonexistent',
    '7.4.2.2.variable_ref_variable_duplicate',
    # 7.4.3.1 A role must define a role attribute
    '7.4.3.1.role_role_missing',
    # 7.4.3.1 A role cannot contain any CellML children (only math)
    '7.4.3.1.role_with_component',
    '7.4.3.1.role_with_component_ref',
    '7.4.3.1.role_with_connection',
    '7.4.3.1.role_with_group',
    '7.4.3.1.role_with_map_components',
    '7.4.3.1.role_with_map_variables',
    '7.4.3.1.role_with_model',
    '7.4.3.1.role_with_reaction',
    '7.4.3.1.role_with_relationship_ref',
    '7.4.3.1.role_with_role',
    '7.4.3.1.role_with_unit',
    '7.4.3.1.role_with_units',
    '7.4.3.1.role_with_variable_ref',
    '7.4.3.1.role_with_variable',
    # 7.4.3.2 A role must define a valid role attribute
    '7.4.3.2.role_role_invalid',
    # 7.4.3.3 A reaction can only have a single rate
    '7.4.3.3.reaction_multiple_rates',
    # 7.4.3.3 A variable_ref with a rate can't have other roles
    '7.4.3.3.role_rate_with_multiple_roles',
    # 7.4.3.3 A role with attribute rate can't have a delta_variable attribute
    '7.4.3.3.role_rate_with_delta_variable',
    # 7.4.3.3 A role with attribute rate can't have a stoichiometry attribute
    '7.4.3.3.role_rate_with_stoichiometry',
    # 7.4.3.4 A direction can only be forward, reverse, or both
    '7.4.3.4.role_direction_invalid',
    # 7.4.3.5 A direction in an irreversible reaction must be forward
    '7.4.3.5.role_direction_both_irreversible',
    '7.4.3.5.role_direction_reverse_irreversible',
    # 7.4.3.5 A rate must have direction forward
    '7.4.3.5.role_direction_both_rate',
    '7.4.3.5.role_direction_reverse_rate',
    # 7.4.3.5 A reactant must have direction forward
    '7.4.3.5.role_direction_both_reactant',
    '7.4.3.5.role_direction_reverse_reactant',
    # 7.4.3.5 A product must have direction forward
    '7.4.3.5.role_direction_both_product',
    '7.4.3.5.role_direction_reverse_product',
    # 7.4.3.5 Each (role,direction) combination must be unique within a
    # variable_ref
    '7.4.3.5.role_direction_role_duplicate',
    # 7.4.3.6 Stoichiometry must be a real number
    '7.4.3.6.role_stoichiometry_invalid',
    # 7.4.3.7 The delta_variable must refer to a local variable
    '7.4.3.7.role_delta_variable_nonexistent_1',
    '7.4.3.7.role_delta_variable_nonexistent_2',
    # 7.4.3.7 The delta_variable must be unique component-wide
    '7.4.3.7.role_delta_variable_duplicate_1',
    '7.4.3.7.role_delta_variable_duplicate_2',
    # 7.4.3.8 A delta_variable can only appear on reactants or products
    # Note: rate is already checked in 7.4.3.3
    '7.4.3.8.role_delta_variable_activator',
    '7.4.3.8.role_delta_variable_catalyst',
    '7.4.3.8.role_delta_variable_inhibitor',
    '7.4.3.8.role_delta_variable_modifier',
    # 7.4.3.8 A delta_variable must have either a stoichiometry or math
    '7.4.3.8.role_delta_variable_without_rate_or_math',
    # 7.4.3.8 A delta_variable with a stoichiometry cannot have math
    '7.4.3.8.role_delta_variable_with_rate_and_math',
    # 7.4.3.8 A delta_variable with a stoichiometry must have a rate
    '7.4.3.8.role_delta_variable_with_stoichiometry_no_rate',
    # 7.4.3.9 The math in a role must be relevant to the variable_ref
    '7.4.3.9.role_math_not_relevant',
    # 8.4.1 Cmeta id's are unique
    '8.4.1.cmeta_id_duplicate',
}


@pytest.fixture
def log():
    """ Returns a logger object. """
    return logging.getLogger(__name__)


class TestCellmlmanip(object):
    """ Tests cellmlmanip validation. """

    @classmethod
    def setup_class(cls):
        cls._report = Report('Cellmlmanip Validation - CellML 1.0')

    @classmethod
    def teardown_class(cls):
        cls._report.render(
            os.path.join(check.REPORT_DIR, 'cellmlmanip_1_0.md'))

    @pytest.mark.parametrize(('name', 'path'), shared.list_passes_1_0())
    def test_valid_model(self, name, path, log):

        # Validate
        ok, msg = cellmlmanip_validation.parse(path)

        # Report
        report = self._report
        if ok:
            report.valid_passed(name, path)
        else:
            report.valid_failed(name, path, msg)

        # Check returned status
        if name in false_negatives:
            if ok:
                # Expected fail, but passed
                log.error('Unexpected pass for ' + name)
                pytest.xpass()
            else:
                # Failed, check if expected
                expected = false_negatives[name]
                if expected in msg:
                    # Expected failure occurred
                    pytest.xfail()
                else:
                    # Failed, but not in the way we expected
                    log.error('Unexpected error in ' + name)
                    log.error(msg)
                    log.error('Expected: ' + expected)
                    pytest.fail()

        elif not ok:
            # Unexpected fail
            log.error('Unexpected error in ' + name)
            log.error(msg)
            pytest.fail()


    @pytest.mark.parametrize(('name', 'path'), shared.list_fails_1_0())
    def test_invalid_model(self, name, path, log):

        report = self._report

        # Infinite loops
        if 'unit_cycle' in name or 'unit_units_invalid' in name:
            report.invalid_failed_incorrectly(
                name, path, 'unit cycle', 'Running test causes infinite loop')
            log.error('Infinite loop file not run')
            pytest.xfail()

        # See if there's an expected error for this model
        expected_error = expected_messages.get(name, None)
        expected_issue = name in known_issues

        # Validate model
        ok, msg = cellmlmanip_validation.parse(path)

        if ok:
            report.invalid_passed(name, path, expected_error or '')

            # Invalid model passed validation
            if expected_issue:
                # Known issue, xfail
                pytest.xfail()

            else:
                # Unexpected pass
                log.error('Unexpected pass in ' + name)
                if expected_error is not None:
                    log.error('Expected error: ' + expected_error)
                else:
                    log.error('No expected error set')
                pytest.fail()

        else:

            # Check if expected error set
            if expected_error is None:
                report.invalid_failed_incorrectly(name, path, '', msg)

                if expected_issue:
                    pytest.xfail()
                else:
                    log.error('Unexpected error in ' + name)
                    log.error(msg)
                    log.error('No expected error set')
                    pytest.fail()

            else:
                # Check if expected error found
                if expected_error in msg:
                    report.invalid_failed(name, path, expected_error, msg)
                else:
                    # Expected error not found
                    report.invalid_failed_incorrectly(
                        name, path, expected_error, msg)

                    if expected_issue:
                        # But we knew this would happen?
                        pytest.xfail()
                    else:
                        log.error('Unexpected error in ' + name)
                        log.error(msg)
                        log.error('Expected error: ' + expected_error)
                        pytest.fail()


#
# Tests CellML 1.0 validation with cellmlmanip
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import logging
import os
import pytest
import warnings

import check
from . import shared
from .. import cellmlmanip_validation as cm
from .report import Report_1_0 as Report


# Known instances where cellmlmanip says a valid file is invalid (or where
# errors occur)
false_negatives = {
    # Reactions
    '2.4.3.reaction_with_extensions': 'Reactions are not supported',
    '2.4.3.role_with_extensions': 'Reactions are not supported',
    '2.4.3.variable_ref_with_extensions': 'Reactions are not supported',
    '2.4.3.xlink_href_in_reaction': 'Reactions are not supported',
    '2.4.3.xlink_href_in_role': 'Reactions are not supported',
    '2.4.3.xlink_href_in_variable_ref': 'Reactions are not supported',
    # Component units
    '2.4.3.xlink_href_in_units_2': 'units inside components',
    # TODO Extension elements: These errors are both not the right errors
    '2.4.3.variable_with_extensions': 'unexpected keyword argument',
    '2.4.3.units_with_extensions': 'units',
    '2.4.3.xlink_href_in_variable': 'unexpected keyword argument',
    # Reactions
    '3.4.2.1.component_with_one_reaction': 'Reactions are not supported',
    '3.4.2.1.component_with_reactions': 'Reactions are not supported',
    # Component units are not supported
    '3.4.2.1.component_child_order_1': 'units inside components',
    '3.4.2.1.component_child_order_2': 'units inside components',
    '3.4.2.1.component_with_units': 'units inside components',
    '3.4.2.1.component_with_one_units': 'units inside components',
    '3.4.3.3.variable_units_component': 'Unknown unit <oranges>',
    # Algebraic models are not supported
    '4.algebraic_model': 'LHS should be a derivative or variable',
    '4.algebraic_ode_model': 'LHS should be a derivative or variable',
    # Overdefined models are not supported
    '4.overdefined_direct_and_direct': 'defined twice',
    '4.overdefined_direct_and_initial': 'defined twice',
    '4.overdefined_direct_and_ode': 'defined twice',
    '4.overdefined_ode_and_ode': 'defined twice',
    # Extended number types
    '4.2.3_2.1.mathml_numbers_real': 'Unimplemented type attribute for <cn>',
    '4.2.3_2.2.mathml_numbers_integer': 'Unimplemented type attribute for <c',
    '4.2.3_2.3.mathml_numbers_real_base': 'Unimplemented type attribute for',
    '4.2.3_2.4.mathml_numbers_integer_base': 'Unimplemented type attribute',
    '4.2.3_2.6.mathml_numbers_rational': 'Unimplemented type attribute for <c',
    # Factorial is not supported
    '4.2.3_4.3_mathml_functions_factorial': 'element <factorial>',
    # TODO Wrong error
    '4.2.3_5.2_mathml_derivatives_degree': 'not 0',
    '4.2.3_5.4_mathml_derivatives_with_units_degree': 'not 0',
    # Boolean literals
    '4.2.3_6.7_mathml_logic_constants': "'BooleanTrue' object has no attr",
    # TODO Nan and Inf support
    '4.2.3_7.3_mathml_nan_inf': 'must be a sympy.Eq',
    # Semantics annotations are not supported
    '4.2.3_8.1_annotation': 'No handler for element <semantics>',
    '4.2.3_8.2_annotation_xml': 'Unknown unit <per_millisecond>',
    # Component units are not supported
    '4.4.3.1.cn_component_units': 'Unknown unit <wooster>',
    # Celsius is not supported
    '5.2.1.units_celsius': 'celsius',
    # Compatible units
    '5.2.7.unit_conversion_dimensionless_exponent': 'maximum recursion depth',
    '5.2.7.unit_conversion_dimensionless_multiplier_1': 'maximum recursion',
    '5.2.7.unit_conversion_dimensionless_offset': 'maximum recursion depth',
    # Incompatible units
    '5.2.7.unit_conversion_inconvertible_1': 'Cannot convert',
    '5.2.7.unit_conversion_new_base_units': 'Cannot convert',
    #'5.2.7.unit_checking_internal_mismatch_1': '!= ampere',
    #'5.2.7.unit_checking_internal_mismatch_2': '!= ampere',
    #'5.2.7.unit_checking_internal_mismatch_3': '!= dimensionless',
    #'5.2.7.unit_checking_internal_mismatch_4': '!= millivolt',
    #'5.2.7.unit_checking_piecewise_multi_unit': 'Piecewise((',
    # TODO Wrong error
    '5.2.7.unit_checking_derivatives_degree': 'not 0',
    # Factorial is not supported
    '5.2.7.unit_checking_functions_factorial': 'for element <factorial>',
    # Component units are not supported
    '5.4.1.2.units_names_and_other_names': 'units inside components',
    '5.4.1.2.units_shadowing_1': 'units inside components',
    '5.4.1.2.units_shadowing_2': 'units inside components',
    '5.4.2.2.unit_units_local_1': 'units inside components',
    '5.4.2.2.unit_units_local_2': 'units inside components',
    '5.4.2.2.unit_units_local_4': 'nknown unit',
    # TODO Improve error message
    '5.4.2.7.unit_offset_non_zero_and_exponent_one': 'units',
    # Booleans are not allowed in equations
    '5.5.2.boolean_arithmetic_divide': 'BooleanAtom not allowed in this',
    '5.5.2.boolean_arithmetic_minus': 'BooleanAtom not allowed in this',
    # '5.5.2.boolean_arithmetic_plus': 'BooleanAtom not allowed in this',
    '5.5.2.boolean_arithmetic_power_1': 'BooleanAtom not allowed in this',
    '5.5.2.boolean_arithmetic_power_2': 'BooleanAtom not allowed in this',
    '5.5.2.boolean_arithmetic_root_1': 'BooleanAtom not allowed in this',
    '5.5.2.boolean_arithmetic_root_2': 'BooleanAtom not allowed in this',
    '5.5.2.boolean_arithmetic_times': "'BooleanTrue' object has no attribute",
    #'5.5.2.boolean_compare_eq_operand_error: '',
    #'5.5.2.boolean_compare_neq_operand_error: '',
    '5.5.2.boolean_compare_geq_operand_error': 'inequalities',
    '5.5.2.boolean_compare_gt_operand_error': 'inequalities',
    '5.5.2.boolean_compare_leq_operand_error': 'inequalities',
    '5.5.2.boolean_compare_lt_operand_error': 'inequalities',
    '5.5.2.boolean_function_abs': 'Bad argument type for Abs()',
    '5.5.2.boolean_function_ceiling': 'bad operand type',
    '5.5.2.boolean_function_floor': 'bad operand type',
    '5.5.2.boolean_function_ln': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_function_log_1': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_function_log_2': "'BooleanTrue' object has no attribute",
    # TODO Improve error message
    '5.5.2.boolean_derivatives_1': 'must be a sympy.Eq',
    '5.5.2.boolean_derivatives_2': 'should be a derivative or variable',
    '5.5.2.boolean_trig_arccos': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_arccot': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_arccoth': "'BooleanTrue' object has no attribute",
    #'5.5.2.boolean_trig_arccsc': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_arcsin': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_arcsinh': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_arctan': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_arctanh': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_cos': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_cosh': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_cot': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_coth': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_csc': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_csch': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_sec': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_sech': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_sin': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_sinh': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_tan': "'BooleanTrue' object has no attribute",
    '5.5.2.boolean_trig_tanh': "'BooleanTrue' object has no attribute",
    #'5.5.2.boolean_variable_1': 'True',
    #'5.5.2.boolean_variable_2': 'False',
    #'5.5.2.boolean_variable_3': 'Eq(_1.0',
    # Factorial is not supported
    '5.5.2.boolean_function_factorial': 'No handler for element <factorial>',
    # TODO Unexpected error
    '6.4.2.1.relationship_ref_relationship_2': 'Invalid or unsupported CellML',
    '6.4.2.5.relationship_ref_multiple_1': 'exactly 1 relationship_ref tag',
    '6.4.2.5.relationship_ref_multiple_2': 'exactly 1 relationship_ref tag',
    '6.4.2.5.relationship_ref_multiple_3': 'exactly 1 relationship_ref tag',
    '6.4.3.2.component_ref_no_children_extension': 'Invalid or unsupported',
    # Reactions are not supported
    '7.4.1.2.reaction_reversible_no': 'Reactions are not supported',
    '7.4.1.2.reaction_reversible_yes': 'Reactions are not supported',
    '7.4.3.reaction_all_roles_and_attributes': 'Reactions are not supported',
    '7.4.3.reaction_reversible_no': 'Reactions are not supported',
    '7.4.3.reaction_simple': 'Reactions are not supported',
    '8.4.1.cmeta_id_in_reaction': 'Reactions are not supported',
    '8.4.1.cmeta_id_in_role': 'Reactions are not supported',
    '8.4.1.cmeta_id_in_variable_ref': 'Reactions are not supported',
    # Component units are not supported
    '8.4.1.cmeta_id_in_units_2': 'units inside components',
    # Reactions are not supported
    '8.4.2.rdf_in_reaction': 'Reactions are not supported',
    '8.4.2.rdf_in_role': 'Reactions are not supported',
    '8.4.2.rdf_in_variable_ref': 'Reactions are not supported',
    # TODO Unexpected error
    '8.4.2.rdf_in_units_1': 'units',
    # Component units are not supported
    '8.4.2.rdf_in_units_2': 'units inside components',
    # Factorial is not supported
    'C.3.3.unit_checking_function_factorial_operand_error':
        'No handler for element <factorial>',
    # TODO Wrong error message
    'C.3.3.unit_checking_derivative_operand_error': 'not 0',
    # TODO Improve error message
    #'C.3.3.unit_checking_arithmetic_minus_operand_error_1': '_3.0 -',
    #'C.3.3.unit_checking_arithmetic_minus_operand_error_2': '-_1.2',
    #'C.3.3.unit_checking_arithmetic_minus_operand_error_3': '-_1.2',
    #'C.3.3.unit_checking_arithmetic_plus_operand_error_1': '_3.0 +',
    #'C.3.3.unit_checking_arithmetic_plus_operand_error_2': '_1.2 +',
    #'C.3.3.unit_checking_arithmetic_plus_operand_error_3': '_1.2 +',
    #'C.3.3.unit_checking_arithmetic_plus_operand_error_4': '_1.2 +',
    #'C.3.3.unit_checking_arithmetic_power_operand_error': '_3.4**_2.0',
    #'C.3.3.unit_checking_arithmetic_root_operand_error': '(\'_9.0**',
    #'C.3.3.unit_checking_function_exp_operand_error': 'exp(',
    #'C.3.3.unit_checking_function_ln_operand_error': 'log(',
    #'C.3.3.unit_checking_function_log_operand_error_1': 'log(',
    #'C.3.3.unit_checking_function_log_operand_error_2': 'log(',
    #'C.3.3.unit_checking_trig_arccos_operand_error': 'acos(',
    #'C.3.3.unit_checking_trig_arccosh_operand_error': 'acosh(',
    #'C.3.3.unit_checking_trig_arccot_operand_error': 'acot(',
    #'C.3.3.unit_checking_trig_arccoth_operand_error': 'acoth(',
    #'C.3.3.unit_checking_trig_arccsc_operand_error': 'acsc(',
    #'C.3.3.unit_checking_trig_arccsch_operand_error': 'acsch(',
    #'C.3.3.unit_checking_trig_arcsec_operand_error': 'asec(',
    #'C.3.3.unit_checking_trig_arcsech_operand_error': 'asech(',
    #'C.3.3.unit_checking_trig_arcsin_operand_error': 'asin(',
    #'C.3.3.unit_checking_trig_arcsinh_operand_error': 'asinh(',
    #'C.3.3.unit_checking_trig_arctan_operand_error': 'atan(',
    #'C.3.3.unit_checking_trig_arctanh_operand_error': 'atanh(',
    #'C.3.3.unit_checking_trig_cos_operand_error': 'cos(',
    #'C.3.3.unit_checking_trig_cosh_operand_error': 'cosh(',
    #'C.3.3.unit_checking_trig_cot_operand_error': 'cot(',
    #'C.3.3.unit_checking_trig_coth_operand_error': 'coth(',
    #'C.3.3.unit_checking_trig_csc_operand_error': 'csc(',
    #'C.3.3.unit_checking_trig_csch_operand_error': 'csch(',
    #'C.3.3.unit_checking_trig_sec_operand_error': 'sec(',
    #'C.3.3.unit_checking_trig_sech_operand_error': 'sech(',
    #'C.3.3.unit_checking_trig_sin_operand_error': 'sin(',
    #'C.3.3.unit_checking_trig_sinh_operand_error': 'sinh(',
    #'C.3.3.unit_checking_trig_tan_operand_error': 'tan(',
    #'C.3.3.unit_checking_trig_tanh_operand_error': 'tanh(',
}


# Expected error messages for invalid files.
expected_messages = {
    # Not in spec: Root node
    '0.0.root_node_namespace_wrong': 'Invalid or unsupported',
    '0.0.root_node_not_model': 'Invalid or unsupported',
    '0.0.root_node_two_elements': 'Extra content at the end of the document',
    '0.0.root_node_two_models': 'Extra content at the end of the document',
    # Not in spec: Real number format
    '0.1.real_number_invalid_1': 'Invalid or unsupported',
    '0.1.real_number_invalid_2': 'Invalid or unsupported',
    '0.1.real_number_invalid_3': 'Invalid or unsupported',
    '0.1.real_number_invalid_4': 'Invalid or unsupported',
    '0.1.real_number_invalid_5': 'Invalid or unsupported',
    '0.1.real_number_invalid_6': 'Invalid or unsupported',
    '0.1.real_number_invalid_7': 'Invalid or unsupported',
    '0.1.real_number_invalid_8': 'Invalid or unsupported',
    '0.1.real_number_invalid_9': 'Invalid or unsupported',
    # Malformed identifier
    '2.4.1.identifier_empty': 'Invalid or unsupported',
    '2.4.1.identifier_only_underscore': 'Invalid or unsupported',
    '2.4.1.identifier_unexpected_character_1': 'Invalid or unsupported',
    '2.4.1.identifier_unexpected_character_2': 'Invalid or unsupported',
    '2.4.1.identifier_unexpected_character_unicode': 'Invalid or unsupported',
    # 2.4.2. Allowable CellML elements and attributes
    '2.4.2.imaginary_attributes_1':
        'Invalid attribute fruit for element model',
    '2.4.2.imaginary_attributes_2':
        'Invalid attribute fruit for element model',
    '2.4.2.imaginary_elements_1':
        'Element model has extra content',
    '2.4.2.imaginary_elements_2':
        'Element model has extra content',
    # 2.4.3 cellml elements cannot contain rdf elements other than rdf:RDF
    '2.4.3.bad_rdf_element_in_component': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_component_ref': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_connection': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_group': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_map_components': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_map_variables': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_model': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_reaction': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_relationship_ref': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_role': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_unit': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_units_1': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_units_2': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_variable': 'Invalid or unsupported',
    '2.4.3.bad_rdf_element_in_variable_ref': 'Invalid or unsupported',
    # 2.4.3 Elements/attributes in extension namespaces
    '2.4.3.cellml_attributes_inside_extensions':
        'Element model failed to validate content',
    '2.4.3.cellml_elements_inside_extensions':
        'Element model failed to validate content',
    # 2.4.4 Text in CellML elements
    '2.4.4.text_in_component':
        'Element component has extra content: text',
    '2.4.4.text_in_component_ref':
        'Element component_ref has extra content: text',
    '2.4.4.text_in_connection':
        'Element connection has extra content: text',
    '2.4.4.text_in_group':
        'Element group has extra content: text',
    '2.4.4.text_in_map_components':
        'Element map_components has extra content: text',
    '2.4.4.text_in_map_variables':
        'Element map_variables has extra content: text',
    '2.4.4.text_in_model':
        'Element model has extra content: text',
    '2.4.4.text_in_reaction':
        'Element reaction has extra content: text',
    '2.4.4.text_in_relationship_ref':
        'Element relationship_ref has extra content: text',
    '2.4.4.text_in_role':
        'Element role has extra content: text',
    '2.4.4.text_in_unit':
        'Element unit has extra content: text',
    '2.4.4.text_in_units_1':
        'Element units has extra content: text',
    '2.4.4.text_in_units_2':
        'Element units has extra content: text',
    '2.4.4.text_in_variable':
        'Element variable has extra content: text',
    '2.4.4.text_in_variable_ref':
        'Element variable_ref has extra content: text',
    # 2.5.2 There are no attributes in the CellML namespace
    '2.5.2.attribute_in_cellml_namespace':
        'Element model failed to validate content',
    # 2.5.3 Extension namespaces again
    # 3.4.1.1 Models contain only units, component, group, connection
    '3.4.1.1.model_with_component_ref':
        'Element model has extra content: component_ref',
    '3.4.1.1.model_with_map_components':
        'Element model has extra content: map_components',
    '3.4.1.1.model_with_map_variables':
        'Element model has extra content: map_variables',
    '3.4.1.1.model_with_math':
        'Element model has extra content: math',
    '3.4.1.1.model_with_model':
        'Element model has extra content: model',
    '3.4.1.1.model_with_reaction':
        'Element model has extra content: reaction',
    '3.4.1.1.model_with_relationship_ref':
        'Element model has extra content: relationship_ref',
    '3.4.1.1.model_with_role':
        'Element model has extra content: role',
    '3.4.1.1.model_with_unit':
        'Element model has extra content: unit',
    '3.4.1.1.model_with_variable_ref':
        'Element model has extra content: variable_ref',
    '3.4.1.1.model_with_variable':
        'Element model has extra content: variable',
    # 3.4.1.1 Models must have a name
    '3.4.1.1.model_name_missing':
        'Element model failed to validate content',
    # 3.4.1.2 A model name must be a valid identifier
    '3.4.1.2.model_name_invalid':
        'Element model failed to validate content',
    # 3.4.2.1 Components contain only units, variable, reaction, math
    '3.4.2.1.component_with_component':
        'Element component has extra content: component',
    '3.4.2.1.component_with_component_ref':
        'Element component has extra content: component_ref',
    '3.4.2.1.component_with_connection':
        'Element component has extra content: connection',
    '3.4.2.1.component_with_group':
        'Element component has extra content: group',
    '3.4.2.1.component_with_map_components':
        'Element component has extra content: map_components',
    '3.4.2.1.component_with_map_variables':
        'Element component has extra content: map_variables',
    '3.4.2.1.component_with_model':
        'Element component has extra content: model',
    '3.4.2.1.component_with_relationship_ref':
        'Element component has extra content: relationship_ref',
    '3.4.2.1.component_with_role':
        'Element component has extra content: role',
    '3.4.2.1.component_with_unit':
        'Element component has extra content: unit',
    '3.4.2.1.component_with_variable_ref':
        'Element component has extra content: variable_ref',
    # 3.4.2.1 Components must have a name
    '3.4.2.1.component_name_missing':
        'Element component failed to validate content',
    # 3.4.2.2 A component name must be a valid identifier
    '3.4.2.2.component_name_invalid':
        'Element component failed to validate',
    # 3.4.3.1 Variables can't contain any elements
    '3.4.3.1.variable_with_component':
        'Element variable has extra content: component',
    '3.4.3.1.variable_with_component_ref':
        'Element variable has extra content: component_ref',
    '3.4.3.1.variable_with_connection':
        'Element variable has extra content: connection',
    '3.4.3.1.variable_with_group':
        'Element variable has extra content: group',
    '3.4.3.1.variable_with_map_components':
        'Element variable has extra content: map_component',
    '3.4.3.1.variable_with_map_variables':
        'Element variable has extra content: map_variables',
    '3.4.3.1.variable_with_math':
        'Element variable has extra content: math',
    '3.4.3.1.variable_with_model':
        'Element variable has extra content: model',
    '3.4.3.1.variable_with_reaction':
        'Element variable has extra content: reaction',
    '3.4.3.1.variable_with_relationship_ref':
        'Element variable has extra content: relationship_ref',
    '3.4.3.1.variable_with_role':
        'Element variable has extra content: role',
    '3.4.3.1.variable_with_unit':
        'Element variable has extra content: unit',
    '3.4.3.1.variable_with_units':
        'Element variable has extra content: units',
    '3.4.3.1.variable_with_variable':
        'Element variable has extra content: variable',
    '3.4.3.1.variable_with_variable_ref':
        'Element variable has extra content: variable_ref',
    # 3.4.3.1 Variables must have a name attribute
    '3.4.3.1.variable_name_missing':
        'Element variable failed to validate attributes',
    # 3.4.3.1 Variables must have a units attribute
    '3.4.3.1.variable_units_missing':
        'Element variable failed to validate attributes',
    # 3.4.3.2 A variable name must be an identifier
    '3.4.3.2.variable_name_invalid':
        'Element variable failed to validate attributes',
    # 3.4.3.2 A variable name must be unique with the component
    '3.4.3.2.variable_name_duplicate': 'already exists',
    # 3.4.3.3 A variable must reference known units
    '3.4.3.3.variable_units_unknown':
        'Unknown unit <oranges>',
    # 3.4.3.3 A variable cannot reference another component's units
    '3.4.3.3.variable_units_other_component':
        'Unknown unit <oranges>',
    # 3.4.3.4 A public interface must be one of in/out/none
    '3.4.3.4.variable_interface_public_invalid':
        'Invalid attribute public_interface for element variable',
    # 3.4.3.5 A private interface must be one of in/out/none
    '3.4.3.5.variable_interface_private_invalid':
        'Invalid attribute private_interface for element variable',
    # 3.4.3.6 The private and public interface can't both be in
    '3.4.3.6.variable_interfaces_both_in':
        'Invalid attribute public_interface for element variable',
    # 3.4.3.7 The initial value (if present) must be a real number
    '3.4.3.7.variable_initial_value_empty':
        'Invalid attribute initial_value for element variable',
    '3.4.3.7.variable_initial_value_invalid':
        'Invalid attribute initial_value for element variable',
    # 3.4.3.8 A variable can't have an initial value and an "in" interface
    '3.4.3.8.variable_interfaces_private_in_and_initial':
        'Invalid attribute initial_value for element variable',
    '3.4.3.8.variable_interfaces_public_in_and_initial':
        'Invalid attribute initial_value for element variable',
    # 3.4.4.1 A connection must contain exactly one map_components
    '3.4.4.1.connection_map_components_missing':
        'Expecting an element map_components',
    '3.4.4.1.connection_map_components_multiple':
        'Extra element map_components',
    # 3.4.4.1 A component must contain at least one map_variables
    '3.4.4.1.connection_map_variables_missing_2':
        'Expecting an element map_variables',
    '3.4.4.1.connection_map_variables_missing_1':
        'Expecting an element map_variables',
    # 3.4.4.1 A connection must have map_components and map_variables
    '3.4.4.1.connection_only_extensions':
        'Element connection failed to validate',
    '3.4.4.1.connection_with_math':
        'Element connection has extra content: math',
    '3.4.4.1.connection_empty':
        'Expecting an element map_components',
    # 3.4.4.1 A connection can only contain map_components and map_variables
    '3.4.4.1.connection_with_component':
        'Element connection has extra content: component',
    '3.4.4.1.connection_with_component_ref':
        'Element connection has extra content: component_ref',
    '3.4.4.1.connection_with_connection':
        'Element connection has extra content: connection',
    '3.4.4.1.connection_with_group':
        'Element connection has extra content: group',
    '3.4.4.1.connection_with_map_components':
        'Element connection has extra content: map_components',
    '3.4.4.1.connection_with_map_variables':
        'Element connection has extra content: map_variables',
    '3.4.4.1.connection_with_model':
        'Element connection has extra content: model',
    '3.4.4.1.connection_with_name_attribute':
        'Invalid attribute name for element connection',
    '3.4.4.1.connection_with_reaction':
        'Element connection has extra content: reaction',
    '3.4.4.1.connection_with_relationship_ref':
        'Element connection has extra content: relationship_ref',
    '3.4.4.1.connection_with_role':
        'Element connection has extra content: role',
    '3.4.4.1.connection_with_unit':
        'Element connection has extra content: unit',
    '3.4.4.1.connection_with_units':
        'Element connection has extra content: units',
    '3.4.4.1.connection_with_variable_ref':
        'Element connection has extra content: variable_ref',
    '3.4.4.1.connection_with_variable':
        'Element connection has extra content: variable',
    # 3.4.5.1 A map_components must declare component_1 and component_2
    '3.4.5.1.map_components_component_1_missing':
        'Element map_components failed to validate attributes',
    '3.4.5.1.map_components_component_2_missing':
        'Element map_components failed to validate attributes',
    # 3.4.5.1 A map_components cannot have cellml children or math
    '3.4.5.1.map_components_with_component':
        'Element map_components has extra content: component',
    '3.4.5.1.map_components_with_component_ref':
        'Element map_components has extra content: component_ref',
    '3.4.5.1.map_components_with_connection':
        'Element map_components has extra content: connection',
    '3.4.5.1.map_components_with_group':
        'Element map_components has extra content: group',
    '3.4.5.1.map_components_with_map_components':
        'Element map_components has extra content: map_components',
    '3.4.5.1.map_components_with_map_variables':
        'Element map_components has extra content: map_variables',
    '3.4.5.1.map_components_with_math':
        'Element map_components has extra content: math',
    '3.4.5.1.map_components_with_model':
        'Element map_components has extra content: model',
    '3.4.5.1.map_components_with_reaction':
        'Element map_components has extra content: reaction',
    '3.4.5.1.map_components_with_relationship_ref':
        'Element map_components has extra content: relationship_ref',
    '3.4.5.1.map_components_with_role':
        'Element map_components has extra content: role',
    '3.4.5.1.map_components_with_unit':
        'Element map_components has extra content: unit',
    '3.4.5.1.map_components_with_units':
        'Element map_components has extra content: units',
    '3.4.5.1.map_components_with_variable':
        'Element map_components has extra content: variable',
    '3.4.5.1.map_components_with_variable_ref':
        'Element map_components has extra content: variable_ref',
    # 3.4.5.2 component_1 must refer to an existing component
    # TODO: Fix error message
    '3.4.5.2.map_components_component_1_nonexistent':
        'c$x',
    # 3.4.5.3 component_2 must refer to an existing component
    # TODO: Fix error message
    '3.4.5.3.map_components_component_2_nonexistent':
        'c$x',
    # 3.4.5.4 component_1 cannot match component_2
    '3.4.5.4.map_components_component_1_equals_2':
        'Target already assigned to',
    # 3.4.6.1 A map_variables must declare variable_1 and variable_2
    '3.4.6.1.map_variables_variable_1_missing':
        'Element map_variables failed to validate attributes',
    '3.4.6.1.map_variables_variable_2_missing':
        'Element map_variables failed to validate attributes',
    # Duplicate connections are not allowed
    '3.4.6.1.map_variables_duplicate_1':
        'Target already assigned',
    '3.4.6.1.map_variables_duplicate_2':
        'Target already assigned',
    # 3.4.6.1 A map_variables cannot have cellml children or math
    '3.4.6.1.map_variables_with_component':
        'Element map_variables has extra content: component',
    '3.4.6.1.map_variables_with_component_ref':
        'Element map_variables has extra content: component_ref',
    '3.4.6.1.map_variables_with_connection':
        'Element map_variables has extra content: connection',
    '3.4.6.1.map_variables_with_group':
        'Element map_variables has extra content: group',
    '3.4.6.1.map_variables_with_map_components':
        'Element map_variables has extra content: map_components',
    '3.4.6.1.map_variables_with_map_variables':
        'Element map_variables has extra content: map_variables',
    '3.4.6.1.map_variables_with_math':
        'Element map_variables has extra content: math',
    '3.4.6.1.map_variables_with_model':
        'Element map_variables has extra content: model',
    '3.4.6.1.map_variables_with_reaction':
        'Element map_variables has extra content: reaction',
    '3.4.6.1.map_variables_with_relationship_ref':
        'Element map_variables has extra content: relationship_ref',
    '3.4.6.1.map_variables_with_role':
        'Element map_variables has extra content: role',
    '3.4.6.1.map_variables_with_unit':
        'Element map_variables has extra content: unit',
    '3.4.6.1.map_variables_with_units':
        'Element map_variables has extra content: units',
    '3.4.6.1.map_variables_with_variable':
        'Element map_variables has extra content: variable',
    '3.4.6.1.map_variables_with_variable_ref':
        'Element map_variables has extra content: variable_ref',
    # 3.4.6.2 variable_1 must refer to an existing variable in component_1
    #TODO Fix error message
    '3.4.6.2.map_variables_variable_1_nonexistent': 'c1$a',
    # 3.4.6.3 variable_2 must refer to an existing variable in component_2
    #TODO Fix error message
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
    #'3.4.6.4.map_variables_nested_sibling_private_in':
    #    'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_nested_sibling_private_in_and_out':
        'Target already assigned',
    '3.4.6.4.map_variables_nested_sibling_private_out':
        'Target already assigned',
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
        'Unable to add connections to the model',
    '3.4.6.4.map_variables_sibling_multiple_out_1':
        'Target already assigned',
    '3.4.6.4.map_variables_sibling_multiple_out_2':
        'Target already assigned',
    '3.4.6.4.map_variables_sibling_out_to_out':
        'Target already assigned',
    #'3.4.6.4.map_variables_sibling_private_in_1':
    #    'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_sibling_private_in_2':
        'Target already assigned',
    #'3.4.6.4.map_variables_sibling_private_in_and_out':
    #    'Cannot determine the source & target for connection',
    #'3.4.6.4.map_variables_sibling_private_out_1':
    #    'Cannot determine the source & target for connection',
    '3.4.6.4.map_variables_sibling_private_out_2':
        'Unable to add connections',
    # 4 Math can't be overdefined
    '4.math_and_initial_value': 'defined twice',
    '4.math_overdefined': 'defined twice',
    # 4.4.1 Bad math
    # These ones are a bit weird: it complains about the math having <apply>
    # instead of complaining about the extensions, but at least points in the
    # right direction...
    '4.4.1.math_not_math_component':
        'Element component failed to validate content',
    '4.4.1.math_not_math_reaction':
        'Element role failed to validate content',
    # 4.4.2 Ci can only refer to local variables
    '4.4.2.ci_non_local_aunt': 'not found in symbol dict',
    '4.4.2.ci_non_local_child': 'not found in symbol dict',
    '4.4.2.ci_non_local_cousin': 'not found in symbol dict',
    '4.4.2.ci_non_local_nested_sibling': 'not found in symbol dict',
    '4.4.2.ci_non_local_niece': 'not found in symbol dict',
    '4.4.2.ci_non_local_parent': 'not found in symbol dict',
    '4.4.2.ci_non_local_sibling': 'not found in symbol dict',
    '4.4.2.ci_nonexistent': 'not found in symbol dict',
    # 4.4.3.1 A cn must have a cellml:units
    '4.4.3.1.cn_units_missing':
        'Element component failed to validate content',
    # 4.4.3.2 A cn unit attribute must refer to a model, local component, or
    #         predefined unit
    '4.4.3.2.cn_units_nonexistent_1': 'Unknown unit',
    '4.4.3.2.cn_units_nonexistent_2':
        'Defining units inside components is not supported',
    # 4.4.4 A mathml:math can only modify 'owned' variables
    '4.4.4.modify_nonexistent': 'A$x not found',
    #'4.4.4.modify_private_in': 'Multiple definitions',
    #'4.4.4.modify_public_in': 'Multiple definitions',
    # 5.2.2 CellML prefers "deka" to "deca"
    '5.2.2.unit_deca':
        'Invalid attribute prefix for element unit',
    # 5.4.1.1 Unitses must have a name
    '5.4.1.1.units_name_missing':
        'Element units failed to validate content',
    # 5.4.1.1 A units with base_units="yes" can't have children
    '5.4.1.1.units_base_units_with_children':
        'Invalid attribute base_units for element units',
    # 5.4.1.1 A units with base_units="no" probably should have children
    '5.4.1.1.units_empty_1': 'Invalid or unsupported CellML file',
    '5.4.1.1.units_empty_2': 'Invalid or unsupported CellML file',
    # 5.4.1.1 A units can only contain unit elements
    '5.4.1.1.units_with_component':
        'Element units has extra content: component',
    '5.4.1.1.units_with_component_ref':
        'Element units has extra content: component_ref',
    '5.4.1.1.units_with_connection':
        'Element units has extra content: connection',
    '5.4.1.1.units_with_group':
        'Element units has extra content: group',
    '5.4.1.1.units_with_map_components':
        'Element units has extra content: map_components',
    '5.4.1.1.units_with_map_variables':
        'Element units has extra content: map_variables',
    '5.4.1.1.units_with_math':
        'Element units has extra content: math',
    '5.4.1.1.units_with_model':
        'Element units has extra content: model',
    '5.4.1.1.units_with_reaction':
        'Element units has extra content: reaction',
    '5.4.1.1.units_with_relationship_ref':
        'Element units has extra content: relationship_ref',
    '5.4.1.1.units_with_role':
        'Element units has extra content: role',
    '5.4.1.1.units_with_units':
        'Element units has extra content: units',
    '5.4.1.1.units_with_variable':
        'Element units has extra content: variable',
    '5.4.1.1.units_with_variable_ref':
        'Element units has extra content: variable_ref',
    # 5.4.1.2 A units name must be a valid identifier
    '5.4.1.2.units_name_invalid':
        'Element units failed to validate content',
    # 5.4.1.2 Units names cannot overlap with predefined ones
    '5.4.1.2.units_name_predefined_ampere': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_becquerel': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_candela': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_celsius': 'Unit <celsius> is not currently',
    '5.4.1.2.units_name_predefined_coulomb': 'Cannot redefine CellML unit',
    '5.4.1.2.units_name_predefined_dimensionless': 'Cannot redefine CellML',
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
    # 5.4.1.3 Units base_units attribute can only be yes or no
    '5.4.1.3.units_base_units_invalid':
        'Invalid attribute base_units',
    # 5.4.2.1 A unit must have a units attribute
    '5.4.2.1.unit_units_missing':
        'Element unit failed to validate attributes',
    # 5.4.2.1 A unit cannot have CellML children
    '5.4.2.1.unit_with_component':
        'Element unit has extra content: component',
    '5.4.2.1.unit_with_component_ref':
        'Element unit has extra content: component_ref',
    '5.4.2.1.unit_with_connection':
        'Element unit has extra content: connection',
    '5.4.2.1.unit_with_group':
        'Element unit has extra content: group',
    '5.4.2.1.unit_with_map_components':
        'Element unit has extra content: map_components',
    '5.4.2.1.unit_with_map_variables':
        'Element unit has extra content: map_variables',
    '5.4.2.1.unit_with_math':
        'Element unit has extra content: math',
    '5.4.2.1.unit_with_model':
        'Element unit has extra content: model',
    '5.4.2.1.unit_with_reaction':
        'Element unit has extra content: reaction',
    '5.4.2.1.unit_with_relationship_ref':
        'Element unit has extra content: relationship_ref',
    '5.4.2.1.unit_with_role':
        'Element unit has extra content: role',
    '5.4.2.1.unit_with_unit':
        'Element unit has extra content: unit',
    '5.4.2.1.unit_with_units':
        'Element unit has extra content: units',
    '5.4.2.1.unit_with_variable':
        'Element unit has extra content: variable',
    '5.4.2.1.unit_with_variable_ref':
        'Element unit has extra content: variable_ref',
    # 5.4.2.3 Allowed values of the prefix attribute
    '5.4.2.3.unit_prefix_real':
        'Invalid attribute prefix',
    '5.4.2.3.unit_prefix_real_int':
        'Invalid attribute prefix',
    '5.4.2.3.unit_prefix_e_notation_int':
        'Invalid attribute prefix',
    '5.4.2.3.unit_prefix_unknown':
        'Invalid attribute prefix',
    # 5.4.2.4 A unit exponent must be a real number
    '5.4.2.4.unit_exponent_invalid':
        'Invalid attribute exponent',
    # 5.4.2.5 A unit multiplier must be a real number
    '5.4.2.5.unit_multiplier_invalid':
        'Invalid attribute multiplier',
    # 5.4.2.6 A unit offset must be a real number
    '5.4.2.6.unit_offset_invalid':
        'Invalid attribute offset',
    # 5.4.2.7: A unit with a non-zero offset must have exponent 1
    '5.4.2.7.unit_offset_and_exponent':
        'Invalid attribute offset',
    # 5.4.2.7: A unit with an offset can't have siblings
    '5.4.2.7.unit_offset_and_siblings_1':
        'Extra element unit',
    '5.4.2.7.unit_offset_and_siblings_2':
        'Extra element unit',
    # 6.4.1.1 A group must have at least one component_ref
    '6.4.1.1.group_component_ref_missing_1':
        'Element group failed to validate content',
    '6.4.1.1.group_component_ref_missing_2':
        'Element group failed to validate content',
    # 6.4.1.1 A group must have at least one relationship_ref
    '6.4.1.1.group_relationship_ref_missing_1':
        'Expecting an element relationship_ref',
    '6.4.1.1.group_relationship_ref_missing_2':
        'Expecting an element relationship_ref',
    # 6.4.1.1 A group cannot be empty (extra test for missing comp_ref/rel_ref)
    '6.4.1.1.group_empty':
        'Expecting an element relationship_ref',
    '6.4.1.1.group_only_extensions':
        'Expecting an element relationship_ref',
    # 6.4.1.1 A group can only contain component_refs and relationship_refs
    '6.4.1.1.group_with_component':
        'Element group has extra content: component',
    '6.4.1.1.group_with_component_ref':
        'Element group has extra content: component_ref',
    '6.4.1.1.group_with_connection':
        'Element group has extra content: connection',
    '6.4.1.1.group_with_group':
        'Element group has extra content: group',
    '6.4.1.1.group_with_map_components':
        'Element group has extra content: map_components',
    '6.4.1.1.group_with_map_variables':
        'Element group has extra content: map_variables',
    '6.4.1.1.group_with_math':
        'Element group has extra content: math',
    '6.4.1.1.group_with_model':
        'Element group has extra content: model',
    '6.4.1.1.group_with_reaction':
        'Element group has extra content: reaction',
    '6.4.1.1.group_with_relationship_ref':
        'Element group has extra content: relationship_ref',
    '6.4.1.1.group_with_role':
        'Element group has extra content: role',
    '6.4.1.1.group_with_unit':
        'Element group failed to validate content',
    '6.4.1.1.group_with_units':
        'Element group has extra content: units',
    '6.4.1.1.group_with_variable_ref':
        'Element group has extra content: variable_ref',
    '6.4.1.1.group_with_variable':
        'Element group has extra content: variable',
    # 6.4.2.1 A relationship_ref must define a relationship - although it can
    #         be either namespaceless, or in any extension namespace!
    '6.4.2.1.relationship_ref_relationship_missing':
        'Element relationship_ref failed to validate',
    # 6.4.2.1 A relationship_ref cannot have any CellML children
    '6.4.2.1.relationship_ref_with_component':
        'Element relationship_ref has extra content: component',
    '6.4.2.1.relationship_ref_with_component_ref':
        'Element relationship_ref has extra content: component_ref',
    '6.4.2.1.relationship_ref_with_connection':
        'Element relationship_ref has extra content: connection',
    '6.4.2.1.relationship_ref_with_group':
        'Element relationship_ref has extra content: group',
    '6.4.2.1.relationship_ref_with_map_components':
        'Element relationship_ref has extra content: map_components',
    '6.4.2.1.relationship_ref_with_map_variables':
        'Element relationship_ref has extra content: map_variables',
    '6.4.2.1.relationship_ref_with_math':
        'Element relationship_ref has extra content: math',
    '6.4.2.1.relationship_ref_with_model':
        'Element relationship_ref has extra content: model',
    '6.4.2.1.relationship_ref_with_reaction':
        'Element relationship_ref has extra content: reaction',
    '6.4.2.1.relationship_ref_with_relationship_ref':
        'Element relationship_ref has extra content: relationship_ref',
    '6.4.2.1.relationship_ref_with_role':
        'Element relationship_ref has extra content: role',
    '6.4.2.1.relationship_ref_with_unit':
        'Element relationship_ref has extra content: unit',
    '6.4.2.1.relationship_ref_with_units':
        'Element relationship_ref has extra content: units',
    '6.4.2.1.relationship_ref_with_variable':
        'Element relationship_ref has extra content: variable',
    '6.4.2.1.relationship_ref_with_variable_ref':
        'Element relationship_ref has extra content: variable_ref',
    # 6.4.2.2 When not in a namespace, a relationship_ref's relationship must
    # be either containment or encapsulation.
    '6.4.2.2.relationship_ref_relationship_invalid':
        'Element relationship_ref failed to validate content',
    # 6.4.2.3 A relationship_ref name must be a cellml identifier
    '6.4.2.3.relationship_ref_name_invalid':
        'Invalid attribute name for element relationship_ref',
    # 6.4.2.4 An encapsulation can not be named
    '6.4.2.4.relationship_ref_encapsulation_duplicate':
        'Invalid attribute name for element relationship_ref',
    '6.4.2.4.relationship_ref_encapsulation_named':
        'Invalid attribute name for element relationship_ref',
    # 6.4.3.1 A component_ref must define a component
    # Message could be better!
    '6.4.3.1.component_ref_component_missing':
        'Element component_ref failed to validate content',
    # 6.4.3.1 A component_ref can only contain a component_ref
    '6.4.3.1.component_ref_with_component':
        'Element component_ref has extra content: component',
    '6.4.3.1.component_ref_with_connection':
        'Element component_ref has extra content: connection',
    '6.4.3.1.component_ref_with_group':
        'Element component_ref has extra content: group',
    '6.4.3.1.component_ref_with_map_components':
        'Element component_ref has extra content: map_components',
    '6.4.3.1.component_ref_with_map_variables':
        'Element component_ref has extra content: map_variables',
    '6.4.3.1.component_ref_with_math':
        'Element component_ref has extra content: math',
    '6.4.3.1.component_ref_with_model':
        'Element component_ref has extra content: model',
    '6.4.3.1.component_ref_with_reaction':
        'Element component_ref has extra content: reaction',
    '6.4.3.1.component_ref_with_relationship_ref':
        'Element component_ref has extra content: relationship_ref',
    '6.4.3.1.component_ref_with_role':
        'Element component_ref has extra content: role',
    '6.4.3.1.component_ref_with_unit':
        'Element component_ref has extra content: unit',
    '6.4.3.1.component_ref_with_units':
        'Element component_ref has extra content: units',
    '6.4.3.1.component_ref_with_variable':
        'Element component_ref has extra content: variable',
    '6.4.3.1.component_ref_with_variable_ref':
        'Element component_ref has extra content: variable_ref',
    # 6.4.3.2 A component cannot be named twice in a single hierarchy
    '6.4.3.2.component_ref_duplicate_child_3': 'already added',
    '6.4.3.2.component_ref_duplicate_child_4': 'Parent of component C',
    # 6.4.3.3 A component attribute must be an identifier
    '6.4.3.3.component_ref_component_invalid':
        'Element component_ref failed to validate content',
    # 6.4.3.2 Encapsulation relationships cannot overlap
    '6.4.3.2.component_ref_overlapping_encapsulation':
        'Parent of component B already A',
    # 7.4.1.1 A reaction must contain at least one variable_ref
    '7.4.1.1.reaction_variable_ref_missing':
        'Expecting an element variable_ref',
    # 7.4.1.1 A reaction can only contain a variable_ref
    '7.4.1.1.reaction_with_component':
        'Element reaction has extra content: component',
    '7.4.1.1.reaction_with_component_ref':
        'Element reaction has extra content: component_ref',
    '7.4.1.1.reaction_with_connection':
        'Element reaction has extra content: connection',
    '7.4.1.1.reaction_with_group':
        'Element reaction has extra content: group',
    '7.4.1.1.reaction_with_map_components':
        'Element reaction has extra content: map_components',
    '7.4.1.1.reaction_with_map_variables':
        'Element reaction has extra content: map_variables',
    '7.4.1.1.reaction_with_math':
        'Element reaction has extra content: math',
    '7.4.1.1.reaction_with_model':
        'Element reaction has extra content: model',
    '7.4.1.1.reaction_with_reaction':
        'Element reaction has extra content: reaction',
    '7.4.1.1.reaction_with_relationship_ref':
        'Element reaction has extra content: relationship_ref',
    '7.4.1.1.reaction_with_role':
        'Element reaction has extra content: role',
    '7.4.1.1.reaction_with_unit':
        'Element reaction has extra content: unit',
    '7.4.1.1.reaction_with_units':
        'Element reaction has extra content: units',
    '7.4.1.1.reaction_with_variable':
        'Element reaction has extra content: variable',
    # 7.4.1.2 The reversible attribute can only be yes or no
    '7.4.1.2.reaction_reversible_invalid':
        'Invalid attribute reversible for element reaction',
    # 7.4.1.3 A reaction in an encapsulating component cannot use
    # delta_variable attributes in its roles.
    '7.4.1.3.reaction_encapsulating_delta_variable':
        'Invalid attribute delta_variable for element role',
    # 7.4.1.3 There's another rule about maths here that I don't understand
    # 7.4.2.1 A variable_ref must have at least one role
    '7.4.2.1.variable_ref_role_missing':
        'Expecting an element role, got nothing',
    '7.4.2.1.variable_ref_variable_missing':
        'Element variable_ref failed to validate content',
    # 7.4.2.1 A variable_ref can only contain a role
    '7.4.2.1.variable_ref_with_component_ref':
        'Element variable_ref has extra content: component_ref',
    '7.4.2.1.variable_ref_with_component':
        'Element variable_ref has extra content: component',
    '7.4.2.1.variable_ref_with_connection':
        'Element variable_ref has extra content: connection',
    '7.4.2.1.variable_ref_with_group':
        'Element variable_ref has extra content: group',
    '7.4.2.1.variable_ref_with_map_components':
        'Element variable_ref has extra content: map_components',
    '7.4.2.1.variable_ref_with_map_variables':
        'Element variable_ref has extra content: map_variables',
    '7.4.2.1.variable_ref_with_math':
        'Element variable_ref has extra content: math',
    '7.4.2.1.variable_ref_with_model':
        'Element variable_ref has extra content: model',
    '7.4.2.1.variable_ref_with_reaction':
        'Element variable_ref has extra content: reaction',
    '7.4.2.1.variable_ref_with_relationship_ref':
        'Element variable_ref has extra content: relationship_ref',
    '7.4.2.1.variable_ref_with_unit':
        'Element variable_ref has extra content: unit',
    '7.4.2.1.variable_ref_with_units':
        'Element variable_ref has extra content: units',
    '7.4.2.1.variable_ref_with_variable':
        'Element variable_ref has extra content: variable',
    '7.4.2.1.variable_ref_with_variable_ref':
        'Element variable_ref has extra content: variable_ref',
    # 7.4.3.1 A role must define a role attribute
    '7.4.3.1.role_role_missing':
        'Element role failed to validate attributes',
    # 7.4.3.1 A role cannot contain any CellML children (only math)
    '7.4.3.1.role_with_component':
        'Element role has extra content: component',
    '7.4.3.1.role_with_component_ref':
        'Element role has extra content: component_ref',
    '7.4.3.1.role_with_connection':
        'Element role has extra content: connection',
    '7.4.3.1.role_with_group':
        'Element role has extra content: group',
    '7.4.3.1.role_with_map_components':
        'Element role has extra content: map_components',
    '7.4.3.1.role_with_map_variables':
        'Element role has extra content: map_variables',
    '7.4.3.1.role_with_model':
        'Element role has extra content: model',
    '7.4.3.1.role_with_reaction':
        'Element role has extra content: reaction',
    '7.4.3.1.role_with_relationship_ref':
        'Element role has extra content: relationship_ref',
    '7.4.3.1.role_with_role':
        'Element role has extra content: role',
    '7.4.3.1.role_with_unit':
        'Element role has extra content: unit',
    '7.4.3.1.role_with_units':
        'Element role has extra content: units',
    '7.4.3.1.role_with_variable_ref':
        'Element role has extra content: variable_ref',
    '7.4.3.1.role_with_variable':
        'Element role has extra content: variable',
    # 7.4.3.2 A role must define a valid role attribute
    '7.4.3.2.role_role_invalid':
        'Element role failed to validate attributes',
    # 7.4.3.3 A variable_ref with a rate can't have other roles
    '7.4.3.3.role_rate_with_multiple_roles':
        'Extra element role',
    # 7.4.3.3 A role with attribute rate can't have a delta_variable attribute
    '7.4.3.3.role_rate_with_delta_variable':
        'Invalid attribute delta_variable',
    # 7.4.3.3 A role with attribute rate can't have a stoichiometry attribute
    '7.4.3.3.role_rate_with_stoichiometry':
        'Invalid attribute stoichiometry for element role',
    # 7.4.3.4 A direction can only be forward, reverse, or both
    '7.4.3.4.role_direction_invalid':
        'Invalid attribute direction for element role',
    # 7.4.3.5 A rate must have direction forward
    '7.4.3.5.role_direction_both_rate':
        'Invalid attribute direction for element role',
    '7.4.3.5.role_direction_reverse_rate':
        'Invalid attribute direction for element role',
    # 7.4.3.5 A reactant must have direction forward
    '7.4.3.5.role_direction_both_reactant':
        'Invalid attribute direction for element role',
    '7.4.3.5.role_direction_reverse_reactant':
        'Invalid attribute direction for element role',
    # 7.4.3.5 A product must have direction forward
    '7.4.3.5.role_direction_both_product':
        'Invalid attribute direction for element role',
    '7.4.3.5.role_direction_reverse_product':
        'Invalid attribute direction for element role',
    # 7.4.3.7 The delta_variable must refer to a local variable
    '7.4.3.7.role_delta_variable_nonexistent_1':
        'Invalid attribute delta_variable',
    '7.4.3.7.role_delta_variable_nonexistent_2':
        'Invalid attribute delta_variable',
    # 7.4.3.7 The delta_variable must be unique component-wide
    '7.4.3.7.role_delta_variable_duplicate_1':
        'Invalid attribute delta_variable',
    '7.4.3.7.role_delta_variable_duplicate_2':
        'Invalid attribute delta_variable',
    # 7.4.3.8 A delta_variable can only appear on reactants or products
    # Note: rate is already checked in 7.4.3.3
    '7.4.3.8.role_delta_variable_activator':
        'Invalid attribute delta_variable',
    '7.4.3.8.role_delta_variable_catalyst':
        'Invalid attribute delta_variable',
    '7.4.3.8.role_delta_variable_inhibitor':
        'Invalid attribute delta_variable',
    '7.4.3.8.role_delta_variable_modifier':
        'Invalid attribute delta_variable',
    # 7.4.3.8 A delta_variable must have either a stoichiometry or math
    '7.4.3.8.role_delta_variable_without_rate_or_math':
        'Invalid attribute delta_variable',
    # 8.4.1 Cmeta id's are unique
    '8.4.1.cmeta_id_duplicate':
        'Invalid attribute id for element component_ref',
    # 8.4.1 cmeta:id attributes must have unique values
    '8.4.1.duplicate_cmeta_id_in_component': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_component_ref': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_connection': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_group': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_map_components': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_map_variables': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_model': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_reaction': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_relationship_ref': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_role': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_unit': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_units_1': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_units_2': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_variable': 'Invalid attribute id',
    '8.4.1.duplicate_cmeta_id_in_variable_ref': 'Invalid attribute id',
}


# Invalid models for which validation is not expected to pick up the (correct)
# error.
known_issues = {
    # 2.4.3 cellml elements cannot contain cmeta attributes other than cmeta:id
    '2.4.3.bad_cmeta_attribute_in_component',
    '2.4.3.bad_cmeta_attribute_in_component_ref',
    '2.4.3.bad_cmeta_attribute_in_connection',
    '2.4.3.bad_cmeta_attribute_in_group',
    '2.4.3.bad_cmeta_attribute_in_map_components',
    '2.4.3.bad_cmeta_attribute_in_map_variables',
    '2.4.3.bad_cmeta_attribute_in_model',
    '2.4.3.bad_cmeta_attribute_in_relationship_ref',
    '2.4.3.bad_cmeta_attribute_in_unit',
    '2.4.3.bad_cmeta_attribute_in_units_1',
    '2.4.3.bad_cmeta_attribute_in_units_2',
    #TODO Fix error message
    '2.4.3.bad_cmeta_attribute_in_variable',
    # Reactions
    '2.4.3.bad_cmeta_attribute_in_reaction',
    '2.4.3.bad_cmeta_attribute_in_role',
    '2.4.3.bad_cmeta_attribute_in_variable_ref',
    # 2.4.3 cellml elements cannot contain cmeta elements
    '2.4.3.cmeta_element_in_component',
    '2.4.3.cmeta_element_in_component_ref',
    '2.4.3.cmeta_element_in_group',
    '2.4.3.cmeta_element_in_map_components',
    '2.4.3.cmeta_element_in_map_variables',
    '2.4.3.cmeta_element_in_model',
    '2.4.3.cmeta_element_in_relationship_ref',
    '2.4.3.cmeta_element_in_unit',
    '2.4.3.cmeta_element_in_variable',
    #TODO Fix error message ('units')
    '2.4.3.cmeta_element_in_units_1',
    # Reactions
    '2.4.3.cmeta_element_in_reaction',
    '2.4.3.cmeta_element_in_role',
    '2.4.3.cmeta_element_in_variable_ref',
    # Component units
    '2.4.3.cmeta_element_in_units_2',
    #TODO: Fix error message (assertion error)
    '2.4.3.cmeta_element_in_connection',
    # 2.4.3 cellml elements cannot have mathml attributes
    '2.4.3.mathml_attribute_in_component',
    '2.4.3.mathml_attribute_in_component_ref',
    '2.4.3.mathml_attribute_in_connection',
    '2.4.3.mathml_attribute_in_group',
    '2.4.3.mathml_attribute_in_map_components',
    '2.4.3.mathml_attribute_in_map_variables',
    '2.4.3.mathml_attribute_in_model',
    '2.4.3.mathml_attribute_in_relationship_ref',
    '2.4.3.mathml_attribute_in_unit',
    '2.4.3.mathml_attribute_in_units_1',
    #TODO: Fix error message
    '2.4.3.mathml_attribute_in_variable',
    # Reactions
    '2.4.3.mathml_attribute_in_reaction',
    '2.4.3.mathml_attribute_in_role',
    '2.4.3.mathml_attribute_in_variable_ref',
    # Component units
    '2.4.3.mathml_attribute_in_units_2',
    # 2.4.3 cellml elements cannot have rdf attributes
    '2.4.3.rdf_attribute_in_component',
    '2.4.3.rdf_attribute_in_component_ref',
    '2.4.3.rdf_attribute_in_connection',
    '2.4.3.rdf_attribute_in_group',
    '2.4.3.rdf_attribute_in_map_components',
    '2.4.3.rdf_attribute_in_map_variables',
    '2.4.3.rdf_attribute_in_model',
    '2.4.3.rdf_attribute_in_relationship_ref',
    '2.4.3.rdf_attribute_in_unit',
    '2.4.3.rdf_attribute_in_units_1',
    #TODO: Fix error message
    '2.4.3.rdf_attribute_in_variable',
    # Reactions
    '2.4.3.rdf_attribute_in_reaction',
    '2.4.3.rdf_attribute_in_role',
    '2.4.3.rdf_attribute_in_variable_ref',
    # Component units
    '2.4.3.rdf_attribute_in_units_2',
    # 2.5.1 Identifiers are case sensitive
    #TODO Fix error message
    '2.5.1.identifiers_are_case_sensitive',
    # 3.4.2.2 Component names must be unique
    #TODO Should definitely catch this
    '3.4.2.2.component_name_duplicate',
    # 3.4.5.4 Each map_components in a model must be unique
    '3.4.5.4.map_components_duplicate',
    '3.4.5.4.map_components_duplicate_mirrored',
    # 3.4.6.4 Interfaces and encapsulation
    #TODO This should be fixed
    '3.4.6.4.map_variables_nested_sibling_private_in',
    '3.4.6.4.map_variables_sibling_private_in_1',
    '3.4.6.4.map_variables_sibling_private_in_and_out',
    '3.4.6.4.map_variables_sibling_private_out_1',
    #TODO This should be fixed
    '3.4.6.4.map_variables_hidden_cousins_3',
    # Component units
    '4.4.3.2.cn_units_parent_component',
    # DAEs are not supported
    '4.4.4.dae_public_in',
    #TODO This should be fixed
    '4.4.4.modify_private_in',
    '4.4.4.modify_public_in',
    # 5.4.1.2 Units names must be unique (within model or local component)
    #TODO This should be fixed
    '5.4.1.2.units_name_duplicate_1',
    # Component units
    '5.4.1.2.units_name_duplicate_2',
    # 5.4.1.2 Component units names cannot overlap with predefined ones
    # Component units
    '5.4.1.2.units_name_predefined_component_ampere',
    # TODO Fix error message
    '5.4.2.3.unit_prefix_spaces',
    # 6.2.4.5 name/relationship pairs must be unique
    '6.4.2.5.relationship_ref_duplicate_named',
    '6.4.2.5.relationship_ref_duplicate_unnamed_1',
    '6.4.2.5.relationship_ref_duplicate_unnamed_2',
    # 6.4.3.2 A component's children cannot be declared two places
    '6.4.3.2.component_ref_children_declared_twice_1',
    '6.4.3.2.component_ref_children_declared_twice_2',
    '6.4.3.2.component_ref_children_declared_twice_3',
    # 6.4.3.3 A hierarchy cannot be circular
    # These first tests are for containment relationships
    '6.4.3.2.component_ref_cycle_1',
    '6.4.3.2.component_ref_cycle_2',
    '6.4.3.2.component_ref_cycle_3',
    '6.4.3.2.component_ref_cycle_4',
    # TODO The next four are for encapsulation, and should be picked up
    '6.4.3.2.component_ref_cycle_5',
    '6.4.3.2.component_ref_cycle_6',
    '6.4.3.2.component_ref_cycle_7',
    '6.4.3.2.component_ref_cycle_8',
    # 6.4.3.2 A component cannot be named twice in a single hierarchy
    # TODO These two should be fixed
    '6.4.3.2.component_ref_duplicate_child_1',
    '6.4.3.2.component_ref_duplicate_child_2',
    # 6.4.3.2 The first component_ref in a containment must have children
    '6.4.3.2.component_ref_no_children_containment',
    # 6.4.3.2 The first component_ref in an encapsulation must have children
    # TODO This should probably be fixed
    '6.4.3.2.component_ref_no_children_encapsulation',
    # 6.4.3.3 A component_ref must refer to an existing component
    # TODO These two should be fixed
    '6.4.3.3.component_ref_component_nonexistent_1',
    '6.4.3.3.component_ref_component_nonexistent_2',
    # 7.4.2.1 A variable_ref must refer to a local variable
    '7.4.2.2.variable_ref_variable_hidden',
    '7.4.2.2.variable_ref_variable_nonexistent',
    '7.4.2.2.variable_ref_variable_duplicate',
    # 7.4.3.3 A reaction can only have a single rate
    '7.4.3.3.reaction_multiple_rates',
    # 7.4.3.5 A direction in an irreversible reaction must be forward
    '7.4.3.5.role_direction_both_irreversible',
    '7.4.3.5.role_direction_reverse_irreversible',
    # 7.4.3.5 Each (role,direction) combination must be unique within a
    # variable_ref
    '7.4.3.5.role_direction_role_duplicate',
    # 7.4.3.6 Stoichiometry must be a real number
    # This is an (unimportant) issue in the RelaxNG pre-validation
    '7.4.3.6.role_stoichiometry_invalid',
    # These result in "Reactions are not supported"
    # 7.4.3.8 A delta_variable with a stoichiometry cannot have math
    '7.4.3.8.role_delta_variable_with_rate_and_math',
    # 7.4.3.8 A delta_variable with a stoichiometry must have a rate
    '7.4.3.8.role_delta_variable_with_stoichiometry_no_rate',
    # 7.4.3.9 The math in a role must be relevant to the variable_ref
    '7.4.3.9.role_math_not_relevant',
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

    @pytest.mark.skipif(not cm.supported(), reason='Cellmlmanip not found')
    @pytest.mark.parametrize(('name', 'path'), shared.list_passes_1_0())
    def test_valid_model(self, name, path, log):

        # Validate
        with warnings.catch_warnings() as w:
            warnings.filterwarnings('ignore', category=DeprecationWarning)
            ok, msg = cm.parse(path)

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
                pytest.fail()
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

    @pytest.mark.skipif(not cm.supported(), reason='Cellmlmanip not found')
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
        ok, msg = cm.parse(path)

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


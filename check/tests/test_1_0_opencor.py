#
# Tests CellML 1.0 validation with OpenCOR, based on the CellML API.
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import logging
import os
import pytest

import check
from . import shared
from .. import opencor_validation as opencor
from .report import Report_1_0 as Report


# Known instances where OpenCOR says a valid file is invalid
false_negatives = {
    # These are valid in 1.0 and invalid 1.1, but OpenCOR doesn't make a
    # distinction in this case
    '2.4.3.xlink_href_in_component': 'Unexpected attribute',
    '2.4.3.xlink_href_in_component_ref': 'Unexpected attribute',
    '2.4.3.xlink_href_in_connection': 'Unexpected attribute',
    '2.4.3.xlink_href_in_group': 'Unexpected attribute',
    '2.4.3.xlink_href_in_map_components': 'Unexpected attribute',
    '2.4.3.xlink_href_in_map_variables': 'Unexpected attribute',
    '2.4.3.xlink_href_in_model': 'Unexpected attribute',
    '2.4.3.xlink_href_in_reaction': 'Unexpected attribute',
    '2.4.3.xlink_href_in_role': 'Unexpected attribute',
    '2.4.3.xlink_href_in_unit': 'Unexpected attribute',
    '2.4.3.xlink_href_in_units_1': 'Unexpected attribute',
    '2.4.3.xlink_href_in_units_2': 'Unexpected attribute',
    '2.4.3.xlink_href_in_variable': 'Unexpected attribute',
    '2.4.3.xlink_href_in_variable_ref': 'Unexpected attribute',
    # CellML API uses 1.1 rule about having to have at least one letter
    '2.4.1.valid_identifiers':
        'identifier must contain at least one letter',

    # CellML API doesn't like annotations?
    '4.2.3_8.1_annotation':
        'Text should not be present',
    '4.2.3_8.2_annotation_xml':
        'Text should not be present',

    # Extension relationships are apparently not supported
    '6.4.3.2.component_ref_no_children_extension':
        'does not have any child component_ref elements',

    # Bases other than 10
    '4.2.3_2.3.mathml_numbers_real_base':
        'invalid constant representation',
    '4.2.3_2.4.mathml_numbers_integer_base':
        'invalid constant representation',

    # Rational numbers aren't supported
    '4.2.3_2.6.mathml_numbers_rational':
        'shouldn\'t have element children',

    # The CellML API is OK (but not great) with booleans
    # (OK, but not great)
    #'5.5.2.boolean_arithmetic_divide',
    #'5.5.2.boolean_arithmetic_minus',
    #'5.5.2.boolean_arithmetic_plus',
    #'5.5.2.boolean_arithmetic_power_1',
    '5.5.2.boolean_arithmetic_power_2':
        'to have the same units',
    #'5.5.2.boolean_arithmetic_root_1',
    '5.5.2.boolean_arithmetic_root_2':
        'qualifier should be in dimensionless units',
    #'5.5.2.boolean_arithmetic_times',
    #'5.5.2.boolean_compare_eq_operand_error',
    #'5.5.2.boolean_compare_geq_operand_error',
    #'5.5.2.boolean_compare_gt_operand_error',
    #'5.5.2.boolean_compare_leq_operand_error',
    #'5.5.2.boolean_compare_lt_operand_error',
    #'5.5.2.boolean_compare_neq_operand_error',
    #'5.5.2.boolean_derivatives_1',
    '5.5.2.boolean_derivatives_2':
        'qualifier should be in dimensionless units',
    #'5.5.2.boolean_function_abs',
    #'5.5.2.boolean_function_ceiling',
    #'5.5.2.boolean_function_exp',
    #'5.5.2.boolean_function_factorial',
    #'5.5.2.boolean_function_floor',
    #'5.5.2.boolean_function_ln',
    #'5.5.2.boolean_function_log_1',
    #'5.5.2.boolean_function_log_2',
    #'5.5.2.boolean_logic_and_operand_error',
    #'5.5.2.boolean_logic_not_operand_error',
    #'5.5.2.boolean_logic_or_operand_error',
    #'5.5.2.boolean_logic_xor_operand_error',
    #'5.5.2.boolean_trig_arccos',
    #'5.5.2.boolean_trig_arccosh',
    #'5.5.2.boolean_trig_arccot',
    #'5.5.2.boolean_trig_arccoth',
    #'5.5.2.boolean_trig_arccsc',
    #'5.5.2.boolean_trig_arccsch',
    #'5.5.2.boolean_trig_arcsec',
    #'5.5.2.boolean_trig_arcsech',
    #'5.5.2.boolean_trig_arcsin',
    #'5.5.2.boolean_trig_arcsinh',
    #'5.5.2.boolean_trig_arctan',
    #'5.5.2.boolean_trig_arctanh',
    #'5.5.2.boolean_trig_cos',
    #'5.5.2.boolean_trig_cosh',
    #'5.5.2.boolean_trig_cot',
    #'5.5.2.boolean_trig_coth',
    #'5.5.2.boolean_trig_csc',
    #'5.5.2.boolean_trig_csch',
    #'5.5.2.boolean_trig_sec',
    #'5.5.2.boolean_trig_sech',
    #'5.5.2.boolean_trig_sin',
    #'5.5.2.boolean_trig_sinh',
    #'5.5.2.boolean_trig_tan',
    #'5.5.2.boolean_trig_tanh',
    #'5.5.2.boolean_variable_1',
    #'5.5.2.boolean_variable_2',
    #'5.5.2.boolean_variable_3',

    # CellML API picks up on bad units, but tends to just warn
    #'5.2.7.unit_checking_internal_mismatch_1',
    #'5.2.7.unit_checking_internal_mismatch_2',
    #'5.2.7.unit_checking_internal_mismatch_3',
    #'5.2.7.unit_checking_internal_mismatch_4',
    #'5.2.7.unit_checking_piecewise_multi_unit':
    #'C.3.3.unit_checking_arithmetic_minus_operand_error_1',
    #'C.3.3.unit_checking_arithmetic_minus_operand_error_2',
    #'C.3.3.unit_checking_arithmetic_minus_operand_error_3',
    #'C.3.3.unit_checking_arithmetic_plus_operand_error_1',
    #'C.3.3.unit_checking_arithmetic_plus_operand_error_2',
    #'C.3.3.unit_checking_arithmetic_plus_operand_error_3',
    #'C.3.3.unit_checking_arithmetic_plus_operand_error_4',
    'C.3.3.unit_checking_arithmetic_power_operand_error':
        'Expected exponent to pow operator to be dimensionless',
    'C.3.3.unit_checking_arithmetic_root_operand_error':
        'Degree qualifier should be in dimensionless units',
    #'C.3.3.unit_checking_compare_eq_operand_mismatch',
    #'C.3.3.unit_checking_compare_geq_operand_mismatch',
    #'C.3.3.unit_checking_compare_gt_operand_mismatch',
    #'C.3.3.unit_checking_compare_leq_operand_mismatch',
    #'C.3.3.unit_checking_compare_lt_operand_mismatch',
    #'C.3.3.unit_checking_compare_neq_operand_mismatch',
    'C.3.3.unit_checking_derivative_operand_error':
        'Degree qualifier should be in dimensionless units',
    #'C.3.3.unit_checking_function_exp_operand_error',
    #'C.3.3.unit_checking_function_factorial_operand_error',
    #'C.3.3.unit_checking_function_ln_operand_error',
    #'C.3.3.unit_checking_function_log_operand_error_1',
    #'C.3.3.unit_checking_function_log_operand_error_2',
    #'C.3.3.unit_checking_trig_arccosh_operand_error',
    #'C.3.3.unit_checking_trig_arccos_operand_error',
    #'C.3.3.unit_checking_trig_arccoth_operand_error',
    #'C.3.3.unit_checking_trig_arccot_operand_error',
    #'C.3.3.unit_checking_trig_arccsch_operand_error',
    #'C.3.3.unit_checking_trig_arccsc_operand_error',
    #'C.3.3.unit_checking_trig_arcsech_operand_error',
    #'C.3.3.unit_checking_trig_arcsec_operand_error',
    #'C.3.3.unit_checking_trig_arcsinh_operand_error',
    #'C.3.3.unit_checking_trig_arcsin_operand_error',
    #'C.3.3.unit_checking_trig_arctanh_operand_error',
    #'C.3.3.unit_checking_trig_arctan_operand_error',
    #'C.3.3.unit_checking_trig_cosh_operand_error',
    #'C.3.3.unit_checking_trig_cos_operand_error',
    #'C.3.3.unit_checking_trig_coth_operand_error',
    #'C.3.3.unit_checking_trig_cot_operand_error',
    #'C.3.3.unit_checking_trig_csch_operand_error',
    #'C.3.3.unit_checking_trig_csc_operand_error',
    #'C.3.3.unit_checking_trig_sech_operand_error',
    #'C.3.3.unit_checking_trig_sec_operand_error',
    #'C.3.3.unit_checking_trig_sinh_operand_error',
    #'C.3.3.unit_checking_trig_sin_operand_error',
    #'C.3.3.unit_checking_trig_tanh_operand_error',
    #'C.3.3.unit_checking_trig_tan_operand_error',

    # Fails on some unit conversions...
    '5.2.7.unit_conversion_dimensionless_multiplier_2':
        'two variables which have dimensionally inconsistent units',
    '5.2.7.unit_conversion_less_obvious':
        'two variables which have dimensionally inconsistent units',
    '5.2.7.unit_conversion_multiplier':
        'two variables which have dimensionally inconsistent units',
    '5.2.7.unit_conversion_offset':
        'two variables which have dimensionally inconsistent units',
    '5.2.7.unit_conversion_prefix':
        'two variables which have dimensionally inconsistent units',

    # OpenCOR can pick up on inconvertible units
    '5.2.7.unit_conversion_inconvertible_1':
        'two variables which have dimensionally inconsistent units',
    '5.2.7.unit_conversion_new_base_units':
        'two variables which have dimensionally inconsistent units',
}


# Expected error messages for invalid files.
expected_messages = {
    # Not in spec: Root node
    '0.0.root_node_namespace_wrong':
        'model is not CellML (wrong namespace)',
    '0.0.root_node_not_model':
        'model is not CellML (wrong element name)',
    '0.0.root_node_two_elements':
        'The model could not be loaded (badxml',
    '0.0.root_node_two_models':
        'The model could not be loaded (badxml',
    # Not in spec: Real number format
    '0.1.real_number_invalid_1':
        'Expected a real number, but didn\'t get one in a valid format',
    '0.1.real_number_invalid_2':
        'Expected a real number, but didn\'t get one in a valid format',
    '0.1.real_number_invalid_3':
        'Expected a real number, but didn\'t get one in a valid format',
    '0.1.real_number_invalid_4':
        'Expected a real number, but didn\'t get one in a valid format',
    '0.1.real_number_invalid_5':
        'Expected a real number, but didn\'t get one in a valid format',
    '0.1.real_number_invalid_6':
        'Expected a real number, but didn\'t get one in a valid format',
    # 2.4.1 CellML Identifiers
    '2.4.1.identifier_empty':
        'A valid CellML identifier must contain at least one letter',
    '2.4.1.identifier_only_underscore':
        'A valid CellML identifier must contain at least one letter',
    '2.4.1.identifier_unexpected_character_1':
        'A valid CellML identifier must only contain alphanumeric characters',
    # 2.4.2. Allowable CellML elements and attributes
    '2.4.2.imaginary_attributes_1':
        'Unexpected attribute fruit found',
    '2.4.2.imaginary_attributes_2':
        'Unexpected attribute fruit found',
    '2.4.2.imaginary_elements_1':
        'Unexpected element fruit found',
    '2.4.2.imaginary_elements_2':
        'Element import is invalid in this version of CellML',
    # 2.4.3 Elements/attributes in extension namespaces
    '2.4.3.mathml_attribute_in_component': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_component_ref': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_connection': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_group': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_map_components': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_map_variables': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_model': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_reaction': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_relationship_ref': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_role': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_unit': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_units_1': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_units_2': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_variable': 'Unexpected attribute',
    '2.4.3.mathml_attribute_in_variable_ref': 'Unexpected attribute',
    # 2.4.4 Text in CellML elements
    '2.4.4.text_in_component':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_component_ref':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_connection':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_group':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_map_components':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_map_variables':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_model':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_reaction':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_relationship_ref':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_role':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_unit':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_units_1':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_units_2':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_variable':
        'any characters that occur immediately within elements in the CellML',
    '2.4.4.text_in_variable_ref':
        'any characters that occur immediately within elements in the CellML',
    # 2.5.1 Identifiers are case sensitive
    '2.5.1.identifiers_are_case_sensitive':
        'Invalid component referenced by component_1 attribute',
    # 2.5.2 There are no attributes in the CellML namespace
    # 2.5.3 Extension namespaces again
    # 3.4.1.1 Models contain only units, component, group, connection
    '3.4.1.1.model_with_component_ref':
        'Unexpected element component_ref',
    '3.4.1.1.model_with_map_components':
        'Unexpected element map_components',
    '3.4.1.1.model_with_map_variables':
        'Unexpected element map_variables',
    '3.4.1.1.model_with_math':
        'Unexpected element math',
    '3.4.1.1.model_with_model':
        'Unexpected element model',
    '3.4.1.1.model_with_reaction':
        'Unexpected element reaction',
    '3.4.1.1.model_with_relationship_ref':
        'Unexpected element relationship_ref',
    '3.4.1.1.model_with_role':
        'Unexpected element role',
    '3.4.1.1.model_with_unit':
        'Unexpected element unit',
    '3.4.1.1.model_with_variable_ref':
        'Unexpected element variable_ref',
    '3.4.1.1.model_with_variable':
        'Unexpected element variable',
    # 3.4.1.1 Models must have a name
    '3.4.1.1.model_name_missing':
        'name attribute is required',
    # 3.4.1.2 A model name must be a valid identifier
    '3.4.1.2.model_name_invalid':
        'A valid CellML identifier must contain at least one letter',
    # 3.4.2.1 Components must have a name
    '3.4.2.1.component_name_missing':
        'name attribute is required',
    # 3.4.2.1 Components contain only units, variable, reaction, math
    '3.4.2.1.component_with_component':
        'Unexpected element component',
    '3.4.2.1.component_with_component_ref':
        'Unexpected element component_ref',
    '3.4.2.1.component_with_connection':
        'Unexpected element connection',
    '3.4.2.1.component_with_group':
        'Unexpected element group',
    '3.4.2.1.component_with_map_components':
        'Unexpected element map_components',
    '3.4.2.1.component_with_map_variables':
        'Unexpected element map_variables',
    '3.4.2.1.component_with_model':
        'Unexpected element model',
    '3.4.2.1.component_with_relationship_ref':
        'Unexpected element relationship_ref',
    '3.4.2.1.component_with_role':
        'Unexpected element role',
    '3.4.2.1.component_with_unit':
        'Unexpected element unit',
    '3.4.2.1.component_with_variable_ref':
        'Unexpected element variable_ref',
    # 3.4.2.2 Component names must be unique
    '3.4.2.2.component_name_duplicate':
        'More than one component in the model named',
    # 3.4.2.2 A component name must be a valid identifier
    '3.4.2.2.component_name_invalid':
        'A valid CellML identifier must contain at least one letter',
    # 3.4.3.1 Variables can't contain any elements
    '3.4.3.1.variable_with_component':
        'Unexpected element component',
    '3.4.3.1.variable_with_component_ref':
        'Unexpected element component_ref',
    '3.4.3.1.variable_with_connection':
        'Unexpected element connection',
    '3.4.3.1.variable_with_group':
        'Unexpected element group',
    '3.4.3.1.variable_with_map_components':
        'Unexpected element map_component',
    '3.4.3.1.variable_with_map_variables':
        'Unexpected element map_variables',
    '3.4.3.1.variable_with_math':
        'Unexpected element math',
    '3.4.3.1.variable_with_model':
        'Unexpected element model',
    '3.4.3.1.variable_with_reaction':
        'Unexpected element reaction',
    '3.4.3.1.variable_with_relationship_ref':
        'Unexpected element relationship_ref',
    '3.4.3.1.variable_with_role':
        'Unexpected element role',
    '3.4.3.1.variable_with_unit':
        'Unexpected element unit',
    '3.4.3.1.variable_with_units':
        'Unexpected element units',
    '3.4.3.1.variable_with_variable':
        'Unexpected element variable',
    '3.4.3.1.variable_with_variable_ref':
        'Unexpected element variable_ref',
    # 3.4.3.1 Variables must have a name attribute
    '3.4.3.1.variable_name_missing':
        'name attribute is required',
    # 3.4.3.1 Variables must have a units attribute
    '3.4.3.1.variable_units_missing':
        'MUST define a units attribute',
    # 3.4.3.2 A variable name must be an identifier
    '3.4.3.2.variable_name_invalid':
        'A valid CellML identifier must only contain alphanumeric',
    # 3.4.3.2 A variable name must be unique with the component
    '3.4.3.2.variable_name_duplicate':
        'There is more than one variable in the same component called',
    # 3.4.3.3 A variable must reference known units
    '3.4.3.3.variable_units_unknown':
        'Invalid units on variable',
    # 3.4.3.3 A variable cannot reference another component's units
    '3.4.3.3.variable_units_other_component':
        'Invalid units on variable',
    # 3.4.3.4 A public interface must be one of in/out/none
    '3.4.3.4.variable_interface_public_invalid':
        'the value of the public_interface / private_interface attribute MUST',
    # 3.4.3.5 A private interface must be one of in/out/none
    '3.4.3.5.variable_interface_private_invalid':
        'the value of the public_interface / private_interface attribute MUST',
    # 3.4.3.6 The private and public interface can't both be in
    '3.4.3.6.variable_interfaces_both_in':
        'Cannot have two in interfaces on variable',
    # 3.4.3.7 The initial value (if present) must be a real number
    '3.4.3.7.variable_initial_value_empty':
        'Expected a real number',
    '3.4.3.7.variable_initial_value_invalid':
        'Expected a real number',
    # 3.4.3.8 A variable can't have an initial value and an "in" interface
    '3.4.3.8.variable_interfaces_private_in_and_initial':
        'cannot have initial value',
    '3.4.3.8.variable_interfaces_public_in_and_initial':
        'cannot have initial value',
    # 3.4.4.1 A connection must contain exactly one map_components
    '3.4.4.1.connection_map_components_missing':
        'MUST contain exactly one',
    '3.4.4.1.connection_map_components_multiple':
        'MUST contain exactly one',
    # 3.4.4.1 A component must contain at least one map_variables
    '3.4.4.1.connection_map_variables_missing_1':
        'MUST contain at least one',
    '3.4.4.1.connection_map_variables_missing_2':
        'MUST contain at least one',
    # 3.4.4.1 A connection must have map_components and map_variables
    '3.4.4.1.connection_only_extensions':
        'MUST contain at least one',
    '3.4.4.1.connection_with_math':
        'Unexpected element math',
    '3.4.4.1.connection_empty':
        'element MUST contain at least one',
    # 3.4.4.1 A connection cannot have attributes
    '3.4.4.1.connection_with_name_attribute':
        'Unexpected attribute name',
    # 3.4.4.1 A connection can only contain map_components and map_variables
    '3.4.4.1.connection_with_component':
        'Unexpected element component',
    '3.4.4.1.connection_with_component_ref':
        'Unexpected element component_ref',
    '3.4.4.1.connection_with_connection':
        'Unexpected element connection',
    '3.4.4.1.connection_with_group':
        'Unexpected element group',
    '3.4.4.1.connection_with_map_components':
        'Unexpected element map_components',
    '3.4.4.1.connection_with_map_variables':
        'Unexpected element map_variables',
    '3.4.4.1.connection_with_model':
        'Unexpected element model',
    '3.4.4.1.connection_with_reaction':
        'Unexpected element reaction',
    '3.4.4.1.connection_with_relationship_ref':
        'Unexpected element relationship_ref',
    '3.4.4.1.connection_with_role':
        'Unexpected element role',
    '3.4.4.1.connection_with_unit':
        'Unexpected element unit',
    '3.4.4.1.connection_with_units':
        'Unexpected element units',
    '3.4.4.1.connection_with_variable_ref':
        'Unexpected element variable_ref',
    '3.4.4.1.connection_with_variable':
        'Unexpected element variable',
    # 3.4.5.1 A map_components must declare component_1 and component_2
    '3.4.5.1.map_components_component_1_missing':
        'element MUST define a component_1 attribute',
    '3.4.5.1.map_components_component_2_missing':
        'element MUST define a component_2 attribute',
    # 3.4.5.1 A map_components cannot have cellml children or math
    '3.4.5.1.map_components_with_component':
        'Unexpected element component',
    '3.4.5.1.map_components_with_component_ref':
        'Unexpected element component_ref',
    '3.4.5.1.map_components_with_connection':
        'Unexpected element connection',
    '3.4.5.1.map_components_with_group':
        'Unexpected element group',
    '3.4.5.1.map_components_with_map_components':
        'Unexpected element map_components',
    '3.4.5.1.map_components_with_map_variables':
        'Unexpected element map_variables',
    '3.4.5.1.map_components_with_math':
        'Unexpected element math',
    '3.4.5.1.map_components_with_model':
        'Unexpected element model',
    '3.4.5.1.map_components_with_reaction':
        'Unexpected element reaction',
    '3.4.5.1.map_components_with_relationship_ref':
        'Unexpected element relationship_ref',
    '3.4.5.1.map_components_with_role':
        'Unexpected element role',
    '3.4.5.1.map_components_with_unit':
        'Unexpected element unit',
    '3.4.5.1.map_components_with_units':
        'Unexpected element units',
    '3.4.5.1.map_components_with_variable':
        'Unexpected element variable',
    '3.4.5.1.map_components_with_variable_ref':
        'Unexpected element variable_ref',
    # 3.4.5.2 component_1 must refer to an existing component
    '3.4.5.2.map_components_component_1_nonexistent':
        'Component_1 attribute doesn\'t refer to a valid component',
    # 3.4.5.3 component_2 must refer to an existing component
    '3.4.5.3.map_components_component_2_nonexistent':
        'Component_2 attribute doesn\'t refer to a valid component',
    # 3.4.5.4 component_1 cannot match component_2
    '3.4.5.4.map_components_component_1_equals_2':
        'Cannot connect a component to itself',
    # 3.4.5.4 Each map_components in a model must be unique
    '3.4.5.4.map_components_duplicate':
        'There is more than one connection element for the same pair',
    '3.4.5.4.map_components_duplicate_mirrored':
        'There is more than one connection element for the same pair',
    # 3.4.6.1 A map_variables must declare variable_1 and variable_2
    '3.4.6.1.map_variables_variable_1_missing':
        'MUST define a variable_1 attribute',
    '3.4.6.1.map_variables_variable_2_missing':
        'MUST define a variable_2 attribute',
    # 3.4.6.1 A map_variables cannot have cellml children or math
    '3.4.6.1.map_variables_with_component':
        'Unexpected element component',
    '3.4.6.1.map_variables_with_component_ref':
        'Unexpected element component_ref',
    '3.4.6.1.map_variables_with_connection':
        'Unexpected element connection',
    '3.4.6.1.map_variables_with_group':
        'Unexpected element group',
    '3.4.6.1.map_variables_with_map_components':
        'Unexpected element map_components',
    '3.4.6.1.map_variables_with_map_variables':
        'Unexpected element map_variables',
    '3.4.6.1.map_variables_with_math':
        'Unexpected element math',
    '3.4.6.1.map_variables_with_model':
        'Unexpected element model',
    '3.4.6.1.map_variables_with_reaction':
        'Unexpected element reaction',
    '3.4.6.1.map_variables_with_relationship_ref':
        'Unexpected element relationship_ref',
    '3.4.6.1.map_variables_with_role':
        'Unexpected element role',
    '3.4.6.1.map_variables_with_unit':
        'Unexpected element unit',
    '3.4.6.1.map_variables_with_units':
        'Unexpected element units',
    '3.4.6.1.map_variables_with_variable':
        'Unexpected element variable',
    '3.4.6.1.map_variables_with_variable_ref':
        'Unexpected element variable_ref',
    # 3.4.6.2 variable_1 must refer to an existing variable in component_1
    '3.4.6.2.map_variables_variable_1_nonexistent':
        'Variable_1 attribute doesn\'t refer to a valid variable',
    # 3.4.6.3 variable_2 must refer to an existing variable in component_2
    '3.4.6.3.map_variables_variable_2_nonexistent':
        'Variable_2 attribute doesn\'t refer to a valid variable',
    # 3.4.6.4 Interfaces and encapsulation
    '3.4.6.4.map_variables_child_multiple_out_1':
        'More than one connection to in interface of variable',
    '3.4.6.4.map_variables_child_multiple_out_2':
        'More than one connection to in interface of variable',
    '3.4.6.4.map_variables_child_out_to_out_1':
        'also has public interface of out',
    '3.4.6.4.map_variables_child_out_to_out_2':
        'also has public interface of out',
    '3.4.6.4.map_variables_child_private_in':
        'Mapping variable_2 which has public interface of none',
    '3.4.6.4.map_variables_child_private_out':
        'Mapping variable_2 which has public interface of none',
    '3.4.6.4.map_variables_hidden_aunt_1':
        'in the hidden set of each other',
    '3.4.6.4.map_variables_hidden_aunt_2':
        'in the hidden set of each other',
    '3.4.6.4.map_variables_hidden_cousins_1':
        'in the hidden set of each other',
    '3.4.6.4.map_variables_hidden_cousins_2':
        'in the hidden set of each other',
    '3.4.6.4.map_variables_hidden_cousins_3':
        'in the hidden set of each other',
    '3.4.6.4.map_variables_hidden_cousins_4':
        'in the hidden set of each other',
    '3.4.6.4.map_variables_hidden_grandchild_1':
        'in the hidden set of each other',
    '3.4.6.4.map_variables_hidden_grandchild_2':
        'in the hidden set of each other',
    '3.4.6.4.map_variables_hidden_grandparent_1':
        'in the hidden set of each other',
    '3.4.6.4.map_variables_hidden_grandparent_2':
        'in the hidden set of each other',
    '3.4.6.4.map_variables_hidden_niece_1':
        'in the hidden set of each other',
    '3.4.6.4.map_variables_hidden_niece_2':
        'in the hidden set of each other',
    '3.4.6.4.map_variables_nested_sibling_private_in':
        'public interface of none',
    '3.4.6.4.map_variables_nested_sibling_private_in_and_out':
        'also has public interface of out',
    '3.4.6.4.map_variables_nested_sibling_private_out':
        'public interface of none',
    '3.4.6.4.map_variables_parent_in_to_in_1':
        'also has public interface of in',
    '3.4.6.4.map_variables_parent_in_to_in_2':
        'also has public interface of in',
    '3.4.6.4.map_variables_parent_multiple_out':
        'More than one connection to in interface of variable',
    '3.4.6.4.map_variables_parent_out_to_out_1':
        'also has public interface of out',
    '3.4.6.4.map_variables_parent_out_to_out_2':
        'also has public interface of out',
    '3.4.6.4.map_variables_parent_public_in':
        'has private interface of none',
    '3.4.6.4.map_variables_parent_public_out':
        'has private interface of none',
    '3.4.6.4.map_variables_sibling_in_to_in':
        'also has public interface of in',
    '3.4.6.4.map_variables_sibling_multiple_out_1':
        'More than one connection to in interface of variable',
    '3.4.6.4.map_variables_sibling_multiple_out_2':
        'More than one connection to in interface of variable',
    '3.4.6.4.map_variables_sibling_out_to_out':
        'also has public interface of out',
    '3.4.6.4.map_variables_sibling_private_in_1':
        'public interface of none',
    '3.4.6.4.map_variables_sibling_private_in_2':
        'also has public interface of out',
    '3.4.6.4.map_variables_sibling_private_in_and_out':
        'public interface of none',
    '3.4.6.4.map_variables_sibling_private_out_1':
        'public interface of none',
    '3.4.6.4.map_variables_sibling_private_out_2':
        'also has public interface of in',
    # 4.4.1 Bad math
    '4.4.1.math_not_math_component':
        'cake was not expected in this context',
    # 4.4.2 Ci can only refer to local variables
    '4.4.2.ci_nonexistent':
        'ci element references variable which doesn\'t exist',
    '4.4.2.ci_non_local_aunt':
        'ci element references variable which doesn\'t exist',
    '4.4.2.ci_non_local_child':
        'ci element references variable which doesn\'t exist',
    '4.4.2.ci_non_local_cousin':
        'ci element references variable which doesn\'t exist',
    '4.4.2.ci_non_local_nested_sibling':
        'ci element references variable which doesn\'t exist',
    '4.4.2.ci_non_local_niece':
        'ci element references variable which doesn\'t exist',
    '4.4.2.ci_non_local_parent':
        'ci element references variable which doesn\'t exist',
    '4.4.2.ci_non_local_sibling':
        'ci element references variable which doesn\'t exist',
    # 4.4.3.1 A cn must have a cellml:units
    '4.4.3.1.cn_units_missing':
        'MathML cn elements must have CellML units attribute',
    # 4.4.3.2 A cn unit attribute must refer to a model, local component, or
    #         predefined unit
    '4.4.3.2.cn_units_nonexistent_1':
        'MathML cn element has invalid units',
    '4.4.3.2.cn_units_nonexistent_2':
        'MathML cn element has invalid units',
    '4.4.3.2.cn_units_parent_component':
        'MathML cn element has invalid units',
    # 4.4.4 A mathml:math can only modify 'owned' variables
    '4.4.4.modify_nonexistent':
        'ci element references variable which doesn\'t exist',
    # 5.4.1.1 Unitses must have a name
    '5.4.1.1.units_name_missing':
        'the name attribute is required here',
    # 5.4.1.1 A units can only contain unit elements
    '5.4.1.1.units_with_component':
        'Unexpected element component',
    '5.4.1.1.units_with_component_ref':
        'Unexpected element component_ref',
    '5.4.1.1.units_with_connection':
        'Unexpected element connection',
    '5.4.1.1.units_with_group':
        'Unexpected element group',
    '5.4.1.1.units_with_map_components':
        'Unexpected element map_components',
    '5.4.1.1.units_with_map_variables':
        'Unexpected element map_variables',
    '5.4.1.1.units_with_math':
        'Unexpected element math',
    '5.4.1.1.units_with_model':
        'Unexpected element model',
    '5.4.1.1.units_with_reaction':
        'Unexpected element reaction',
    '5.4.1.1.units_with_relationship_ref':
        'Unexpected element relationship_ref',
    '5.4.1.1.units_with_role':
        'Unexpected element role',
    '5.4.1.1.units_with_units':
        'Unexpected element units',
    '5.4.1.1.units_with_variable':
        'Unexpected element variable',
    '5.4.1.1.units_with_variable_ref':
        'Unexpected element variable_ref',
    # 5.4.1.2 A units name must be a valid identifier
    '5.4.1.2.units_name_invalid':
        'A valid CellML identifier must contain at least one letter',
    # 5.4.1.2 Units names must be unique (within model or local component)
    '5.4.1.2.units_name_duplicate_1':
        'More than one units in the model named',
    '5.4.1.2.units_name_duplicate_2':
        'More than one units in the component named',
    # 5.4.1.2 Units names cannot overlap with predefined ones
    '5.4.1.2.units_name_predefined_ampere':
        'Units in the model uses reserved name ampere',
    '5.4.1.2.units_name_predefined_becquerel':
        'Units in the model uses reserved name becquerel',
    '5.4.1.2.units_name_predefined_candela':
        'Units in the model uses reserved name candela',
    '5.4.1.2.units_name_predefined_celsius':
        'Units in the model uses reserved name celsius',
    '5.4.1.2.units_name_predefined_coulomb':
        'Units in the model uses reserved name coulomb',
    '5.4.1.2.units_name_predefined_dimensionless':
        'Units in the model uses reserved name dimensionless',
    '5.4.1.2.units_name_predefined_farad':
        'Units in the model uses reserved name farad',
    '5.4.1.2.units_name_predefined_gram':
        'Units in the model uses reserved name gram',
    '5.4.1.2.units_name_predefined_gray':
        'Units in the model uses reserved name gray',
    '5.4.1.2.units_name_predefined_henry':
        'Units in the model uses reserved name henry',
    '5.4.1.2.units_name_predefined_hertz':
        'Units in the model uses reserved name hertz',
    '5.4.1.2.units_name_predefined_joule':
        'Units in the model uses reserved name joule',
    '5.4.1.2.units_name_predefined_katal':
        'Units in the model uses reserved name katal',
    '5.4.1.2.units_name_predefined_kelvin':
        'Units in the model uses reserved name kelvin',
    '5.4.1.2.units_name_predefined_kilogram':
        'Units in the model uses reserved name kilogram',
    '5.4.1.2.units_name_predefined_liter':
        'Units in the model uses reserved name liter',
    '5.4.1.2.units_name_predefined_litre':
        'Units in the model uses reserved name litre',
    '5.4.1.2.units_name_predefined_lumen':
        'Units in the model uses reserved name lumen',
    '5.4.1.2.units_name_predefined_lux':
        'Units in the model uses reserved name lux',
    '5.4.1.2.units_name_predefined_meter':
        'Units in the model uses reserved name meter',
    '5.4.1.2.units_name_predefined_metre':
        'Units in the model uses reserved name metre',
    '5.4.1.2.units_name_predefined_mole':
        'Units in the model uses reserved name mole',
    '5.4.1.2.units_name_predefined_newton':
        'Units in the model uses reserved name newton',
    '5.4.1.2.units_name_predefined_ohm':
        'Units in the model uses reserved name ohm',
    '5.4.1.2.units_name_predefined_pascal':
        'Units in the model uses reserved name pascal',
    '5.4.1.2.units_name_predefined_radian':
        'Units in the model uses reserved name radian',
    '5.4.1.2.units_name_predefined_second':
        'Units in the model uses reserved name second',
    '5.4.1.2.units_name_predefined_siemens':
        'Units in the model uses reserved name siemens',
    '5.4.1.2.units_name_predefined_sievert':
        'Units in the model uses reserved name sievert',
    '5.4.1.2.units_name_predefined_steradian':
        'Units in the model uses reserved name steradian',
    '5.4.1.2.units_name_predefined_tesla':
        'Units in the model uses reserved name tesla',
    '5.4.1.2.units_name_predefined_volt':
        'Units in the model uses reserved name volt',
    '5.4.1.2.units_name_predefined_watt':
        'Units in the model uses reserved name watt',
    '5.4.1.2.units_name_predefined_weber':
        'Units in the model uses reserved name weber',
    # 5.4.1.2 Component units names cannot overlap with predefined ones
    '5.4.1.2.units_name_predefined_component_ampere':
        'Units in the component uses reserved name ampere',
    # 5.4.1.3 Units base_units attribute can only be yes or no
    '5.4.1.3.units_base_units_invalid':
        'the value of the base_units attribute MUST be',
    # 5.4.2.1 A unit must have a units attribute
    '5.4.2.1.unit_units_missing':
        'MUST define a units attribute',
    # 5.4.2.1 A unit cannot have CellML children
    '5.4.2.1.unit_with_component':
        'Unexpected element component',
    '5.4.2.1.unit_with_component_ref':
        'Unexpected element component_ref',
    '5.4.2.1.unit_with_connection':
        'Unexpected element connection',
    '5.4.2.1.unit_with_group':
        'Unexpected element group',
    '5.4.2.1.unit_with_map_components':
        'Unexpected element map_components',
    '5.4.2.1.unit_with_map_variables':
        'Unexpected element map_variables',
    '5.4.2.1.unit_with_math':
        'Unexpected element math',
    '5.4.2.1.unit_with_model':
        'Unexpected element model',
    '5.4.2.1.unit_with_reaction':
        'Unexpected element reaction',
    '5.4.2.1.unit_with_relationship_ref':
        'Unexpected element relationship_ref',
    '5.4.2.1.unit_with_role':
        'Unexpected element role',
    '5.4.2.1.unit_with_unit':
        'Unexpected element unit',
    '5.4.2.1.unit_with_units':
        'Unexpected element units',
    '5.4.2.1.unit_with_variable':
        'Unexpected element variable',
    '5.4.2.1.unit_with_variable_ref':
        'Unexpected element variable_ref',
    # 5.4.2.2 A unit must refer to an existing units
    '5.4.2.2.unit_units_invalid':
        'units could not be found',
    # 5.4.2.2 A unit cannot refer to itself directly or indirectly
    '5.4.2.2.unit_cycle_1':
        'Units are defined circularly',
    '5.4.2.2.unit_cycle_2':
        'Units are defined circularly',
    '5.4.2.2.unit_cycle_3':
        'Units are defined circularly',
    # 6.4.1.1 A group must have at least one component_ref
    '6.4.1.1.group_component_ref_missing_1':
        'MUST contain at least one',
    '6.4.1.1.group_component_ref_missing_2':
        'MUST contain at least one',
    # 6.4.1.1 A group must have at least one relationship_ref
    '6.4.1.1.group_relationship_ref_missing_1':
        'MUST contain at least one',
    '6.4.1.1.group_relationship_ref_missing_2':
        'MUST contain at least one',
    # 6.4.1.1 A group cannot be empty (extra test for missing comp_ref/rel_ref)
    '6.4.1.1.group_empty':
        'MUST contain at least one',
    '6.4.1.1.group_only_extensions':
        'MUST contain at least one',
    # 6.4.1.1 A group can only contain component_refs and relationship_refs
    '6.4.1.1.group_with_component':
        'Unexpected element component',
    '6.4.1.1.group_with_component_ref':
        'Unexpected element component_ref',
    '6.4.1.1.group_with_connection':
        'Unexpected element connection',
    '6.4.1.1.group_with_group':
        'Unexpected element group',
    '6.4.1.1.group_with_map_components':
        'Unexpected element map_components',
    '6.4.1.1.group_with_map_variables':
        'Unexpected element map_variables',
    '6.4.1.1.group_with_math':
        'Unexpected element math',
    '6.4.1.1.group_with_model':
        'Unexpected element model',
    '6.4.1.1.group_with_reaction':
        'Unexpected element reaction',
    '6.4.1.1.group_with_relationship_ref':
        'Unexpected element relationship_ref',
    '6.4.1.1.group_with_role':
        'Unexpected element role',
    '6.4.1.1.group_with_unit':
        'Unexpected element unit',
    '6.4.1.1.group_with_units':
        'Unexpected element units',
    '6.4.1.1.group_with_variable_ref':
        'Unexpected element variable_ref',
    '6.4.1.1.group_with_variable':
        'Unexpected element variable',
    # 6.4.2.1 A relationship_ref must define a relationship - although it can
    #         be either namespaceless, or in any extension namespace!
    '6.4.2.1.relationship_ref_relationship_missing':
        'Relationship attribute is mandatory',
    # 6.4.2.1 A relationship_ref cannot have any CellML children
    '6.4.2.1.relationship_ref_with_component':
        'Unexpected element component',
    '6.4.2.1.relationship_ref_with_component_ref':
        'Unexpected element component_ref',
    '6.4.2.1.relationship_ref_with_connection':
        'Unexpected element connection',
    '6.4.2.1.relationship_ref_with_group':
        'Unexpected element group',
    '6.4.2.1.relationship_ref_with_map_components':
        'Unexpected element map_components',
    '6.4.2.1.relationship_ref_with_map_variables':
        'Unexpected element map_variables',
    '6.4.2.1.relationship_ref_with_math':
        'Unexpected element math',
    '6.4.2.1.relationship_ref_with_model':
        'Unexpected element model',
    '6.4.2.1.relationship_ref_with_reaction':
        'Unexpected element reaction',
    '6.4.2.1.relationship_ref_with_relationship_ref':
        'Unexpected element relationship_ref',
    '6.4.2.1.relationship_ref_with_role':
        'Unexpected element role',
    '6.4.2.1.relationship_ref_with_unit':
        'Unexpected element unit',
    '6.4.2.1.relationship_ref_with_units':
        'Unexpected element units',
    '6.4.2.1.relationship_ref_with_variable':
        'Unexpected element variable',
    '6.4.2.1.relationship_ref_with_variable_ref':
        'Unexpected element variable_ref',
    # 6.4.2.2 When not in a namespace, a relationship_ref's relationship must
    # be either containment or encapsulation.
    '6.4.2.2.relationship_ref_relationship_invalid':
        'The value of a relationship attribute in the CellML namespace',
    # 6.4.2.3 A relationship_ref name must be a cellml identifier
    '6.4.2.3.relationship_ref_name_invalid':
        'A valid CellML identifier must contain at least one letter',
    # 6.4.2.4 An encapsulation can not be named
    '6.4.2.4.relationship_ref_encapsulation_duplicate':
        'A name attribute must not be defined',
    '6.4.2.4.relationship_ref_encapsulation_named':
        'A name attribute must not be defined',
    # 6.4.2.5 name/relationship pairs must be unique
    '6.4.2.5.relationship_ref_duplicate_named':
        'Duplicate relationship_ref within group',
    '6.4.2.5.relationship_ref_duplicate_unnamed_1':
        'Duplicate relationship_ref within group',
    '6.4.2.5.relationship_ref_duplicate_unnamed_2':
        'Duplicate relationship_ref within group',
    # 6.4.3.1 A component_ref must define a component
    '6.4.3.1.component_ref_component_missing':
        'must define a component attribute',
    # 6.4.3.1 A component_ref can only contain a component_ref
    '6.4.3.1.component_ref_with_component':
        'Unexpected element component',
    '6.4.3.1.component_ref_with_connection':
        'Unexpected element connection',
    '6.4.3.1.component_ref_with_group':
        'Unexpected element group',
    '6.4.3.1.component_ref_with_map_components':
        'Unexpected element map_components',
    '6.4.3.1.component_ref_with_map_variables':
        'Unexpected element map_variables',
    '6.4.3.1.component_ref_with_math':
        'Unexpected element math',
    '6.4.3.1.component_ref_with_model':
        'Unexpected element model',
    '6.4.3.1.component_ref_with_reaction':
        'Unexpected element reaction',
    '6.4.3.1.component_ref_with_relationship_ref':
        'Unexpected element relationship_ref',
    '6.4.3.1.component_ref_with_role':
        'Unexpected element role',
    '6.4.3.1.component_ref_with_unit':
        'Unexpected element unit',
    '6.4.3.1.component_ref_with_units':
        'Unexpected element units',
    '6.4.3.1.component_ref_with_variable':
        'Unexpected element variable',
    '6.4.3.1.component_ref_with_variable_ref':
        'Unexpected element variable_ref',
    # 6.4.3.2 A component's children cannot be declared two places
    '6.4.3.2.component_ref_children_declared_twice_1':
        'elements that reference a given component may contain further',
    '6.4.3.2.component_ref_children_declared_twice_2':
        'elements that reference a given component may contain further',
    '6.4.3.2.component_ref_children_declared_twice_3':
        'elements that reference a given component may contain further',
    # 6.4.3.2 The first component_ref in a containment must have children
    '6.4.3.2.component_ref_no_children_containment':
        'does not have any child component_ref elements',
    # 6.4.3.2 The first component_ref in an encapsulation must have children
    '6.4.3.2.component_ref_no_children_encapsulation':
        'does not have any child component_ref elements',
    # 6.4.3.3 A component attribute must be an identifier
    '6.4.3.3.component_ref_component_invalid':
        'A valid CellML identifier must contain at least',
    # 6.4.3.3 A component_ref must refer to an existing component
    '6.4.3.3.component_ref_component_nonexistent_1':
        'Component_ref element references component which does not exist',
    '6.4.3.3.component_ref_component_nonexistent_2':
        'Component_ref element references component which does not exist',
    # 7.4.1.1 A reaction must contain at least one variable_ref
    '7.4.1.1.reaction_variable_ref_missing':
        'must contain at least one',
    # 7.4.1.1 A reaction can only contain a variable_ref
    '7.4.1.1.reaction_with_component':
        'Unexpected element component',
    '7.4.1.1.reaction_with_component_ref':
        'Unexpected element component_ref',
    '7.4.1.1.reaction_with_connection':
        'Unexpected element connection',
    '7.4.1.1.reaction_with_group':
        'Unexpected element group',
    '7.4.1.1.reaction_with_map_components':
        'Unexpected element map_components',
    '7.4.1.1.reaction_with_map_variables':
        'Unexpected element map_variables',
    '7.4.1.1.reaction_with_math':
        'Unexpected element math',
    '7.4.1.1.reaction_with_model':
        'Unexpected element model',
    '7.4.1.1.reaction_with_reaction':
        'Unexpected element reaction',
    '7.4.1.1.reaction_with_relationship_ref':
        'Unexpected element relationship_ref',
    '7.4.1.1.reaction_with_role':
        'Unexpected element role',
    '7.4.1.1.reaction_with_unit':
        'Unexpected element unit',
    '7.4.1.1.reaction_with_units':
        'Unexpected element units',
    '7.4.1.1.reaction_with_variable':
        'Unexpected element variable',
    # 7.4.1.2 The reversible attribute can only be yes or no
    '7.4.1.2.reaction_reversible_invalid':
        'the reversible attribute must have a value of "yes" or "no"',
    # 7.4.1.3 There's another rule about maths here that I don't understand
    # 7.4.2.1 A variable_ref must have at least one role
    '7.4.2.1.variable_ref_role_missing':
        'must contain at least one',
    '7.4.2.1.variable_ref_variable_missing':
        'must define a variable attribute',
    # 7.4.2.1 A variable_ref can only contain a role
    '7.4.2.1.variable_ref_with_component_ref':
        'Unexpected element component_ref',
    '7.4.2.1.variable_ref_with_component':
        'Unexpected element component',
    '7.4.2.1.variable_ref_with_connection':
        'Unexpected element connection',
    '7.4.2.1.variable_ref_with_group':
        'Unexpected element group',
    '7.4.2.1.variable_ref_with_map_components':
        'Unexpected element map_components',
    '7.4.2.1.variable_ref_with_map_variables':
        'Unexpected element map_variables',
    '7.4.2.1.variable_ref_with_math':
        'Unexpected element math',
    '7.4.2.1.variable_ref_with_model':
        'Unexpected element model',
    '7.4.2.1.variable_ref_with_reaction':
        'Unexpected element reaction',
    '7.4.2.1.variable_ref_with_relationship_ref':
        'Unexpected element relationship_ref',
    '7.4.2.1.variable_ref_with_unit':
        'Unexpected element unit',
    '7.4.2.1.variable_ref_with_units':
        'Unexpected element units',
    '7.4.2.1.variable_ref_with_variable':
        'Unexpected element variable',
    '7.4.2.1.variable_ref_with_variable_ref':
        'Unexpected element variable_ref',
    # 7.4.3.1 A role must define a role attribute
    '7.4.3.1.role_role_missing':
        'must define a role attribute',
    # 7.4.3.1 A role cannot contain any CellML children (only math)
    '7.4.3.1.role_with_component':
        'Unexpected element component',
    '7.4.3.1.role_with_component_ref':
        'Unexpected element component_ref',
    '7.4.3.1.role_with_connection':
        'Unexpected element connection',
    '7.4.3.1.role_with_group':
        'Unexpected element group',
    '7.4.3.1.role_with_map_components':
        'Unexpected element map_components',
    '7.4.3.1.role_with_map_variables':
        'Unexpected element map_variables',
    '7.4.3.1.role_with_model':
        'Unexpected element model',
    '7.4.3.1.role_with_reaction':
        'Unexpected element reaction',
    '7.4.3.1.role_with_relationship_ref':
        'Unexpected element relationship_ref',
    '7.4.3.1.role_with_role':
        'Unexpected element role',
    '7.4.3.1.role_with_unit':
        'Unexpected element unit',
    '7.4.3.1.role_with_units':
        'Unexpected element units',
    '7.4.3.1.role_with_variable_ref':
        'Unexpected element variable_ref',
    '7.4.3.1.role_with_variable':
        'Unexpected element variable',
    # 7.4.3.2 A role must define a valid role attribute
    '7.4.3.2.role_role_invalid':
        'must take one of the following seven values',
    # 7.4.3.4 A direction can only be forward, reverse, or both
    '7.4.3.4.role_direction_invalid':
        'the direction attribute must take one of the following',
    # 7.4.3.6 Stoichiometry must be a real number
    '7.4.3.6.role_stoichiometry_invalid':
        'Expected a real number',
}


# Invalid models for which validation is not expected to pick up the (correct)
# error.
known_issues = {
    # CellML API allows letters with accents in identifiers
    '2.4.1.identifier_unexpected_character_2',
    # CellML API allows any unicode character
    '2.4.1.identifier_unexpected_character_unicode',
    # CellML namespace attributes inside extensions are not detected
    '2.4.3.cellml_attributes_inside_extensions',
    # CellML elements inside extensions are not detected
    '2.4.3.cellml_elements_inside_extensions',
    # Invalid cmeta attributes are not detected
    '2.4.3.bad_cmeta_attribute_in_component',
    '2.4.3.bad_cmeta_attribute_in_component_ref',
    '2.4.3.bad_cmeta_attribute_in_connection',
    '2.4.3.bad_cmeta_attribute_in_group',
    '2.4.3.bad_cmeta_attribute_in_map_components',
    '2.4.3.bad_cmeta_attribute_in_map_variables',
    '2.4.3.bad_cmeta_attribute_in_model',
    '2.4.3.bad_cmeta_attribute_in_reaction',
    '2.4.3.bad_cmeta_attribute_in_relationship_ref',
    '2.4.3.bad_cmeta_attribute_in_role',
    '2.4.3.bad_cmeta_attribute_in_unit',
    '2.4.3.bad_cmeta_attribute_in_units_1',
    '2.4.3.bad_cmeta_attribute_in_units_2',
    '2.4.3.bad_cmeta_attribute_in_variable',
    '2.4.3.bad_cmeta_attribute_in_variable_ref',
    # Invalid rdf elements are not detected
    '2.4.3.bad_rdf_element_in_component',
    '2.4.3.bad_rdf_element_in_component_ref',
    '2.4.3.bad_rdf_element_in_connection',
    '2.4.3.bad_rdf_element_in_group',
    '2.4.3.bad_rdf_element_in_map_components',
    '2.4.3.bad_rdf_element_in_map_variables',
    '2.4.3.bad_rdf_element_in_model',
    '2.4.3.bad_rdf_element_in_reaction',
    '2.4.3.bad_rdf_element_in_relationship_ref',
    '2.4.3.bad_rdf_element_in_role',
    '2.4.3.bad_rdf_element_in_unit',
    '2.4.3.bad_rdf_element_in_units_1',
    '2.4.3.bad_rdf_element_in_units_2',
    '2.4.3.bad_rdf_element_in_variable',
    '2.4.3.bad_rdf_element_in_variable_ref',
    # Invalid cmeta elements are not detected
    '2.4.3.cmeta_element_in_component',
    '2.4.3.cmeta_element_in_component_ref',
    '2.4.3.cmeta_element_in_connection',
    '2.4.3.cmeta_element_in_group',
    '2.4.3.cmeta_element_in_map_components',
    '2.4.3.cmeta_element_in_map_variables',
    '2.4.3.cmeta_element_in_model',
    '2.4.3.cmeta_element_in_reaction',
    '2.4.3.cmeta_element_in_relationship_ref',
    '2.4.3.cmeta_element_in_role',
    '2.4.3.cmeta_element_in_unit',
    '2.4.3.cmeta_element_in_units_1',
    '2.4.3.cmeta_element_in_units_2',
    '2.4.3.cmeta_element_in_variable',
    '2.4.3.cmeta_element_in_variable_ref',
    # Unexpected pass for bad mathml attribute
    '2.4.3.mathml_attribute_in_relationship_ref',
    # Bad top-level RDF elements are not detected
    '2.4.3.rdf_attribute_in_component',
    '2.4.3.rdf_attribute_in_component_ref',
    '2.4.3.rdf_attribute_in_connection',
    '2.4.3.rdf_attribute_in_group',
    '2.4.3.rdf_attribute_in_map_components',
    '2.4.3.rdf_attribute_in_map_variables',
    '2.4.3.rdf_attribute_in_model',
    '2.4.3.rdf_attribute_in_reaction',
    '2.4.3.rdf_attribute_in_relationship_ref',
    '2.4.3.rdf_attribute_in_role',
    '2.4.3.rdf_attribute_in_unit',
    '2.4.3.rdf_attribute_in_units_1',
    '2.4.3.rdf_attribute_in_units_2',
    '2.4.3.rdf_attribute_in_variable',
    '2.4.3.rdf_attribute_in_variable_ref',
    # API doesn't complain about attributes in the CellML namespace
    '2.5.2.attribute_in_cellml_namespace',
    # 4.4.1 Bad math
    '4.4.1.math_not_math_reaction',
    # 4.4.4 A mathml:math can only modify 'owned' variables
    '4.4.4.modify_private_in',
    '4.4.4.modify_public_in',
    # 4 Math can't be overdefined
    '4.math_and_initial_value',
    '4.math_overdefined',
    # 5.2.2 CellML prefers "deka" over "deca"
    # Causes error message code to break
    '5.2.2.unit_deca',
    # 5.4.1.1 A units with base_units="yes" can't have children
    '5.4.1.1.units_base_units_with_children',
    # OpenCOR doesn't mind if base_units="no" don't have children
    '5.4.1.1.units_empty_1',
    '5.4.1.1.units_empty_2',
    # 5.4.2.3 Allowed values of the prefix attribute
    # Causes error message code to break
    '5.4.2.3.unit_prefix_real',
    '5.4.2.3.unit_prefix_real_int',
    '5.4.2.3.unit_prefix_spaces',
    '5.4.2.3.unit_prefix_unknown',
    # 5.4.2.4 A unit exponent must be a real number
    # Causes error message code to break
    '5.4.2.4.unit_exponent_invalid',
    # 5.4.2.5 A unit multiplier must be a real number
    # Causes error message code to break
    '5.4.2.5.unit_multiplier_invalid',
    # 5.4.2.6 A unit offset must be a real number
    # Causes error message code to break
    '5.4.2.6.unit_offset_invalid',
    # 5.4.2.7: A unit with a non-zero offset must have exponent 1
    '5.4.2.7.unit_offset_and_exponent',
    # 5.4.2.7: A unit with an offset can't have siblings
    '5.4.2.7.unit_offset_and_siblings_1',
    '5.4.2.7.unit_offset_and_siblings_2',
    # 6.4.3.2 A hierarchy cannot be circular
    '6.4.3.2.component_ref_cycle_1',
    '6.4.3.2.component_ref_cycle_2',
    '6.4.3.2.component_ref_cycle_3',
    '6.4.3.2.component_ref_cycle_4',
    '6.4.3.2.component_ref_cycle_5',
    '6.4.3.2.component_ref_cycle_6',
    '6.4.3.2.component_ref_cycle_7',
    '6.4.3.2.component_ref_cycle_8',
    # 6.4.3.2 A component cannot be named twice in a single hierarchy
    '6.4.3.2.component_ref_duplicate_child_1',
    '6.4.3.2.component_ref_duplicate_child_2',
    '6.4.3.2.component_ref_duplicate_child_3',
    '6.4.3.2.component_ref_duplicate_child_4',
    # 6.4.3.2 Encapsulation relationships cannot overlap
    '6.4.3.2.component_ref_overlapping_encapsulation',
    # 7.4.1.3 A reaction in an encapsulating component cannot use
    # delta_variable attributes in its roles.
    '7.4.1.3.reaction_encapsulating_delta_variable',
    # 7.4.2.2 A variable_ref must refer to a local variable
    '7.4.2.2.variable_ref_variable_hidden',
    '7.4.2.2.variable_ref_variable_nonexistent',
    '7.4.2.2.variable_ref_variable_duplicate',
    # 7.4.3.3 A reaction can only have a single rate
    '7.4.3.3.reaction_multiple_rates',
    # 7.4.3.3 A variable_ref with a rate can't have other roles
    '7.4.3.3.role_rate_with_multiple_roles',
    # 7.4.3.3 A role with attribute rate can't have a delta_variable attribute
    '7.4.3.3.role_rate_with_delta_variable',
    # 7.4.3.3 A role with attribute rate can't have a stoichiometry attribute
    '7.4.3.3.role_rate_with_stoichiometry',
    # 7.4.3.5 A direction in an irreversible reaction must be forward
    '7.4.3.5.role_direction_both_irreversible',
    '7.4.3.5.role_direction_reverse_irreversible',
    # 7.4.3.5 Each (role,direction) combination must be unique within a
    # variable_ref
    '7.4.3.5.role_direction_role_duplicate',
    # 7.4.3.5 A rate must have direction forward
    '7.4.3.5.role_direction_both_rate',
    '7.4.3.5.role_direction_reverse_rate',
    # 7.4.3.5 A reactant must have direction forward
    '7.4.3.5.role_direction_both_reactant',
    '7.4.3.5.role_direction_reverse_reactant',
    # 7.4.3.5 A product must have direction forward
    '7.4.3.5.role_direction_both_product',
    '7.4.3.5.role_direction_reverse_product',
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
    # 8.4.1 cmeta ids are not checked for uniqueness
    '8.4.1.duplicate_cmeta_id_in_component',
    '8.4.1.duplicate_cmeta_id_in_component_ref',
    '8.4.1.duplicate_cmeta_id_in_connection',
    '8.4.1.duplicate_cmeta_id_in_group',
    '8.4.1.duplicate_cmeta_id_in_map_components',
    '8.4.1.duplicate_cmeta_id_in_map_variables',
    '8.4.1.duplicate_cmeta_id_in_model',
    '8.4.1.duplicate_cmeta_id_in_reaction',
    '8.4.1.duplicate_cmeta_id_in_relationship_ref',
    '8.4.1.duplicate_cmeta_id_in_role',
    '8.4.1.duplicate_cmeta_id_in_unit',
    '8.4.1.duplicate_cmeta_id_in_units_1',
    '8.4.1.duplicate_cmeta_id_in_units_2',
    '8.4.1.duplicate_cmeta_id_in_variable',
    '8.4.1.duplicate_cmeta_id_in_variable_ref',
}


@pytest.fixture
def log():
    """ Returns a logger object. """
    return logging.getLogger(__name__)


class TestOpenCOR(object):
    """ Tests TestOpenCOR validation. """

    @classmethod
    def setup_class(cls):
        cls._report = Report('OpenCOR / CellML API Validation - CellML 1.0')

    @classmethod
    def teardown_class(cls):
        cls._report.render(
            os.path.join(check.REPORT_DIR, 'opencor_1_0.md'))

    @pytest.mark.skipif(not opencor.supported(), reason='OpenCOR not found')
    @pytest.mark.parametrize(('name', 'path'), shared.list_passes_1_0())
    def test_valid_model(self, name, path, log):
        report = self._report

        # Validate
        ret, out, err = opencor.parse(path)
        msg = out.splitlines() + err.splitlines()
        lmsg = '\n'.join(msg)

        # Report
        if ret == 0:
            report.valid_passed(name, path, lmsg)
        else:
            report.valid_failed(name, path, lmsg)

        # Check returned status
        if name in false_negatives:
            if ret == 0:
                # Expected fail, but passed
                log.error('Unexpected pass for ' + name)
                for line in msg:
                    log.error(line)
                pytest.xpass()
            else:
                # Failed, check if expected
                expected = false_negatives[name]
                expected_found = False
                for line in msg:
                    if expected in line:
                        expected_found = True
                        break
                if expected_found:
                    # Expected failure occurred
                    pytest.xfail()
                else:
                    # Failed, but not in the way we expected
                    log.error('Unexpected error in ' + name)
                    for line in msg:
                        log.error(line)
                    log.error('Expected: ' + expected)
                    pytest.fail()

        elif ret != 0:
            # Unexpected fail
            log.error('Unexpected error in ' + name)
            for line in msg:
                log.error(line)
            pytest.fail()

    @pytest.mark.skipif(not opencor.supported(), reason='OpenCOR not found')
    @pytest.mark.parametrize(('name', 'path'), shared.list_fails_1_0())
    def test_invalid_model(self, name, path, log):
        report = self._report

        # See if there's an expected error for this model
        expected_error = expected_messages.get(name, None)
        expected_issue = name in known_issues

        # Validate model
        ret, out, err = opencor.parse(path)
        msg = out.splitlines() + err.splitlines()
        lmsg = '\n'.join(msg)

        if ret == 0:
            report.invalid_passed(name, path, expected_error, lmsg)

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
                report.invalid_failed_incorrectly(
                    name, path, 'Expected error not set', lmsg)

                if expected_issue:
                    pytest.xfail()
                else:
                    log.error('Unexpected error in ' + name)
                    for line in msg:
                        log.error(line)
                    log.error('No expected error set')
                    pytest.fail()

            else:

                # Scan logged errors for expected one
                expected_found = False
                for line in msg:
                    if expected_error in line:
                        expected_found = True
                        break

                # Check if found
                if expected_found:
                    report.invalid_failed(name, path, expected_error, lmsg)
                else:
                    # Expected error not found
                    report.invalid_failed_incorrectly(
                        name, path, expected_error, lmsg)

                    if expected_issue:
                        # But we knew this would happen?
                        pytest.xfail()
                    else:
                        log.error('Unexpected error in ' + name)
                        for line in msg:
                            log.error(line)
                        log.error('Expected error: ' + expected_error)
                        pytest.fail()


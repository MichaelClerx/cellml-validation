#
# Tests CellML 1.0 schema validation
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import logging
import os
import pytest
from lxml import etree

import check
from . import shared
from .report import Report_1_0 as Report


# Expected instances where the schema says a valid file is invalid
false_negatives = {}


# Expected error messages
expected_messages = {
    # Not in spec: Root node
    '0.0.root_node_not_model':
        "No matching global declaration available for the validation root",
    '0.0.root_node_two_elements':
        "Extra content at the end of the document",
    '0.0.root_node_two_models':
        "Extra content at the end of the document",
    '0.0.root_node_namespace_wrong':
        "No matching global declaration available for the validation root",
    # Not in spec: Real number format
    '0.1.real_number_invalid_1':
        "not a valid value of the atomic type 'cellml:real_number'",
    '0.1.real_number_invalid_2':
        "not a valid value of the atomic type 'cellml:real_number'",
    '0.1.real_number_invalid_3':
        "not a valid value of the atomic type 'cellml:real_number'",
    '0.1.real_number_invalid_4':
        "not a valid value of the atomic type 'cellml:real_number'",
    '0.1.real_number_invalid_5':
        "not a valid value of the atomic type 'cellml:real_number'",
    '0.1.real_number_invalid_6':
        "not a valid value of the atomic type 'cellml:real_number'",
    # 2.4.1 CellML Identifiers
    '2.4.1.identifier_empty':
        #"'name': '' is not a valid value",
        "not a valid value of the atomic type 'cellml:identifier'",
    '2.4.1.identifier_only_underscore':
        "not a valid value of the atomic type 'cellml:identifier'",
    '2.4.1.identifier_unexpected_character_1':
        "not a valid value of the atomic type 'cellml:identifier'",
    '2.4.1.identifier_unexpected_character_2':
        "not a valid value of the atomic type 'cellml:identifier'",
    '2.4.1.identifier_unexpected_character_unicode':
        "not a valid value of the atomic type 'cellml:identifier'",
    # 2.4.2. Allowable CellML elements and attributes
    '2.4.2.imaginary_attributes_1':
        "The attribute 'fruit' is not allowed",
    '2.4.2.imaginary_attributes_2':
        "The attribute 'cellml:fruit' is not allowed",
    '2.4.2.imaginary_elements':
        "Element 'cellml:fruit': This element is not expected",
    # 2.4.4 Text in CellML elements
    '2.4.4.text_in_component':
        "Element 'cellml:component': Character content other than white",
    '2.4.4.text_in_component_ref':
        "Element 'cellml:component_ref': Character content other than white",
    '2.4.4.text_in_connection':
        "Element 'cellml:connection': Character content other than white",
    '2.4.4.text_in_group':
        "Element 'cellml:group': Character content other than white",
    '2.4.4.text_in_map_components':
        "Element 'cellml:map_components': Character content other than white",
    '2.4.4.text_in_map_variables':
        "Element 'cellml:map_variables': Character content other than white",
    '2.4.4.text_in_model':
        "Element 'cellml:model': Character content other than white",
    '2.4.4.text_in_reaction':
        "Element 'cellml:reaction': Character content other than white",
    '2.4.4.text_in_relationship_ref':
        "Element 'cellml:relationship_ref': Character content other than",
    '2.4.4.text_in_role':
        "Element 'cellml:role': Character content other than white",
    '2.4.4.text_in_unit':
        "Element 'cellml:unit': Character content other than white",
    '2.4.4.text_in_units_1':
        "Element 'cellml:units': Character content other than white",
    '2.4.4.text_in_units_2':
        "Element 'cellml:units': Character content other than white",
    '2.4.4.text_in_variable':
        "Element 'cellml:variable': Character content other than white",
    '2.4.4.text_in_variable_ref':
        "Element 'cellml:variable_ref': Character content other than white",
    # 2.5.1 Identifiers are case sensitive
    '2.5.1.identifiers_are_case_sensitive':
        "No match found for key-sequence",
    # 2.5.2 There are no attributes in the CellML namespace
    '2.5.2.attribute_in_cellml_namespace':
        "The attribute 'cellml:private_interface' is not allowed",
    # 2.5.3 Extension namespaces again
    # 3.4.1.1 Models contain only units, component, group, connection
    '3.4.1.1.model_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '3.4.1.1.model_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '3.4.1.1.model_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '3.4.1.1.model_with_model':
        "Element 'cellml:model': This element is not expected",
    '3.4.1.1.model_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    '3.4.1.1.model_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '3.4.1.1.model_with_role':
        "Element 'cellml:role': This element is not expected",
    '3.4.1.1.model_with_unit':
        "Element 'cellml:unit': This element is not expected",
    '3.4.1.1.model_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    '3.4.1.1.model_with_variable':
        "Element 'cellml:variable': This element is not expected",
    # 3.4.1.1 Models must have a name
    '3.4.1.1.model_name_missing':
        "Element 'cellml:model': The attribute 'name' is required",
    # 3.4.1.2 A model name must be a valid identifier
    '3.4.1.2.model_name_invalid':
        "not a valid value of the atomic type 'cellml:identifier'",
    # 3.4.2.1 Components contain only units, variable, reaction, math
    '3.4.2.1.component_with_component':
        "Element 'cellml:component': This element is not expected",
    '3.4.2.1.component_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '3.4.2.1.component_with_connection':
        "Element 'cellml:connection': This element is not expected",
    '3.4.2.1.component_with_group':
        "Element 'cellml:group': This element is not expected",
    '3.4.2.1.component_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '3.4.2.1.component_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '3.4.2.1.component_with_model':
        "Element 'cellml:model': This element is not expected",
    '3.4.2.1.component_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '3.4.2.1.component_with_role':
        "Element 'cellml:role': This element is not expected",
    '3.4.2.1.component_with_unit':
        "Element 'cellml:unit': This element is not expected",
    '3.4.2.1.component_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    # 3.4.2.1 Components must have a name
    '3.4.2.1.component_name_missing':
        "Element 'cellml:component': The attribute 'name' is required",
    # 3.4.2.2 A component name must be a valid identifier
    '3.4.2.2.component_name_invalid':
        "not a valid value of the atomic type 'cellml:identifier'",
    # 3.4.2.2 Component names must be unique
    '3.4.2.2.component_name_duplicate':
        "Duplicate key-sequence ['c1']",
    # 3.4.3.1 Variables can't contain any elements
    '3.4.3.1.variable_with_component':
        "Element 'cellml:component': This element is not expected",
    '3.4.3.1.variable_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '3.4.3.1.variable_with_connection':
        "Element 'cellml:connection': This element is not expected",
    '3.4.3.1.variable_with_group':
        "Element 'cellml:group': This element is not expected",
    '3.4.3.1.variable_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '3.4.3.1.variable_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '3.4.3.1.variable_with_model':
        "Element 'cellml:model': This element is not expected",
    '3.4.3.1.variable_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    '3.4.3.1.variable_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '3.4.3.1.variable_with_role':
        "Element 'cellml:role': This element is not expected",
    '3.4.3.1.variable_with_unit':
        "Element 'cellml:unit': This element is not expected",
    '3.4.3.1.variable_with_units':
        "Element 'cellml:units': This element is not expected",
    '3.4.3.1.variable_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    '3.4.3.1.variable_with_variable':
        "Element 'cellml:variable': This element is not expected",
    # 3.4.3.1 Variables must have a name attribute
    '3.4.3.1.variable_name_missing':
        "The attribute 'name' is required but missing",
    # 3.4.3.1 Variables must have a units attribute
    '3.4.3.1.variable_units_missing':
        "Element 'cellml:variable': The attribute 'units' is required",
    # 3.4.3.2 A variable name must be an identifier
    '3.4.3.2.variable_name_invalid':
        "not a valid value of the atomic type 'cellml:identifier'",
    # 3.4.3.2 A variable name must be unique with the component
    '3.4.3.2.variable_name_duplicate':
        "Element 'cellml:variable': Duplicate key-sequence",
    # 3.4.3.4 A public interface must be one of in/out/none
    '3.4.3.4.variable_interface_public_invalid':
        "not an element of the set",
    # 3.4.3.5 A private interface must be one of in/out/none
    '3.4.3.5.variable_interface_private_invalid':
        "not an element of the set",
    # 3.4.3.7 The initial value (if present) must be a real number
    '3.4.3.7.variable_initial_value_empty':
        "not a valid value of the atomic type 'cellml:real_number'",
    '3.4.3.7.variable_initial_value_invalid':
        "not a valid value of the atomic type 'cellml:real_number'",
    # 3.4.4.1 A connection must have map_components and map_variables
    '3.4.4.1.connection_empty':
        "Element 'cellml:connection': Missing child element(s).",
    # 3.4.4.1 A connection can only contain map_components and map_variables
    '3.4.4.1.connection_with_component':
        "Element 'cellml:component': This element is not expected",
    '3.4.4.1.connection_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '3.4.4.1.connection_with_connection':
        "Element 'cellml:connection': This element is not expected",
    '3.4.4.1.connection_with_group':
        "Element 'cellml:group': This element is not expected",
    '3.4.4.1.connection_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '3.4.4.1.connection_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '3.4.4.1.connection_with_model':
        "Element 'cellml:model': This element is not expected",
    '3.4.4.1.connection_with_name_attribute':
        "Element 'cellml:connection', attribute 'name'",
    '3.4.4.1.connection_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    '3.4.4.1.connection_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '3.4.4.1.connection_with_role':
        "Element 'cellml:role': This element is not expected",
    '3.4.4.1.connection_with_unit':
        "Element 'cellml:unit': This element is not expected",
    '3.4.4.1.connection_with_units':
        "Element 'cellml:units': This element is not expected",
    '3.4.4.1.connection_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    '3.4.4.1.connection_with_variable':
        "Element 'cellml:variable': This element is not expected",
    # 3.4.5.1 A map_components must declare component_1 and component_2
    '3.4.5.1.map_components_component_1_missing':
        "Element 'cellml:map_components': The attribute 'component_1' is req",
    '3.4.5.1.map_components_component_2_missing':
        "Element 'cellml:map_components': The attribute 'component_2' is req",
    # 3.4.5.1 A map_components cannot have cellml children or math
    '3.4.5.1.map_components_with_component':
        "Element 'cellml:component': This element is not expected",
    '3.4.5.1.map_components_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '3.4.5.1.map_components_with_connection':
        "Element 'cellml:connection': This element is not expected",
    '3.4.5.1.map_components_with_group':
        "Element 'cellml:group': This element is not expected",
    '3.4.5.1.map_components_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '3.4.5.1.map_components_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '3.4.5.1.map_components_with_model':
        "Element 'cellml:model': This element is not expected",
    '3.4.5.1.map_components_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    '3.4.5.1.map_components_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '3.4.5.1.map_components_with_role':
        "Element 'cellml:role': This element is not expected",
    '3.4.5.1.map_components_with_unit':
        "Element 'cellml:unit': This element is not expected",
    '3.4.5.1.map_components_with_units':
        "Element 'cellml:units': This element is not expected",
    '3.4.5.1.map_components_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    '3.4.5.1.map_components_with_variable':
        "Element 'cellml:variable': This element is not expected",
    # 3.4.5.2 component_1 must refer to an existing component
    '3.4.5.2.map_components_component_1_nonexistent':
        "Element 'cellml:map_components': No match found for key-sequence",
    # 3.4.5.3 component_2 must refer to an existing component
    '3.4.5.3.map_components_component_2_nonexistent':
        "Element 'cellml:map_components': No match found for key-sequence",
    # 3.4.5.4 Each map_components in a model must be unique
    '3.4.5.4.map_components_duplicate':
        "Element 'cellml:map_components': Duplicate key-sequence",
    # 3.4.6.1 A map_variables must declare variable_1 and variable_2
    '3.4.6.1.map_variables_variable_1_missing':
        "Element 'cellml:map_variables': The attribute 'variable_1' is req",
    '3.4.6.1.map_variables_variable_2_missing':
        "Element 'cellml:map_variables': The attribute 'variable_2' is req",
    # 3.4.6.1 A map_variables cannot have cellml children or math
    '3.4.6.1.map_variables_with_component':
        "Element 'cellml:component': This element is not expected",
    '3.4.6.1.map_variables_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '3.4.6.1.map_variables_with_connection':
        "Element 'cellml:connection': This element is not expected",
    '3.4.6.1.map_variables_with_group':
        "Element 'cellml:group': This element is not expected",
    '3.4.6.1.map_variables_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '3.4.6.1.map_variables_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '3.4.6.1.map_variables_with_model':
        "Element 'cellml:model': This element is not expected",
    '3.4.6.1.map_variables_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    '3.4.6.1.map_variables_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '3.4.6.1.map_variables_with_role':
        "Element 'cellml:role': This element is not expected",
    '3.4.6.1.map_variables_with_unit':
        "Element 'cellml:unit': This element is not expected",
    '3.4.6.1.map_variables_with_units':
        "Element 'cellml:units': This element is not expected",
    '3.4.6.1.map_variables_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    '3.4.6.1.map_variables_with_variable':
        "Element 'cellml:variable': This element is not expected",
    # 4.4.1 Bad math
    '4.4.1.math_not_math_component':
        "cake': This element is not expected.",
    '4.4.1.math_not_math_reaction':
        "cake': This element is not expected.",
    # 5.2.2 CellML prefers "deka" over "deca"
    '5.2.2.unit_deca':
        "'deca' is not a valid value of the union type 'cellml:unit_prefix'",
    # 5.4.1.1 Unitses must have a name
    '5.4.1.1.units_name_missing':
        "Element 'cellml:units': The attribute 'name' is required",
    # 5.4.1.1 A units can only contain unit elements
    '5.4.1.1.units_with_component':
        "Element 'cellml:component': This element is not expected",
    '5.4.1.1.units_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '5.4.1.1.units_with_connection':
        "Element 'cellml:connection': This element is not expected",
    '5.4.1.1.units_with_group':
        "Element 'cellml:group': This element is not expected",
    '5.4.1.1.units_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '5.4.1.1.units_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '5.4.1.1.units_with_model':
        "Element 'cellml:model': This element is not expected",
    '5.4.1.1.units_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    '5.4.1.1.units_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '5.4.1.1.units_with_role':
        "Element 'cellml:role': This element is not expected",
    '5.4.1.1.units_with_units':
        "Element 'cellml:units': This element is not expected",
    '5.4.1.1.units_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    '5.4.1.1.units_with_variable':
        "Element 'cellml:variable': This element is not expected",
    # 5.4.1.2 A units name must be a valid identifier
    '5.4.1.2.units_name_invalid':
        "not a valid value of the atomic type 'cellml:identifier'",
    # 5.4.1.2 Units names must be unique (within model or local component)
    '5.4.1.2.units_name_duplicate_1':
        "Element 'cellml:units': Duplicate key-sequence",
    '5.4.1.2.units_name_duplicate_2':
        "Element 'cellml:units': Duplicate key-sequence",
    # 5.4.1.3 Units base_units attribute can only be yes or no
    '5.4.1.3.units_base_units_invalid':
        "not an element of the set",
    # 5.4.2.1 A unit must have a units attribute
    '5.4.2.1.unit_units_missing':
        "Element 'cellml:unit': The attribute 'units' is required",
    # 5.4.2.1 A unit cannot have CellML children
    '5.4.2.1.unit_with_component':
        "Element 'cellml:component': This element is not expected",
    '5.4.2.1.unit_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '5.4.2.1.unit_with_connection':
        "Element 'cellml:connection': This element is not expected",
    '5.4.2.1.unit_with_group':
        "Element 'cellml:group': This element is not expected",
    '5.4.2.1.unit_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '5.4.2.1.unit_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '5.4.2.1.unit_with_model':
        "Element 'cellml:model': This element is not expected",
    '5.4.2.1.unit_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    '5.4.2.1.unit_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '5.4.2.1.unit_with_role':
        "Element 'cellml:role': This element is not expected",
    '5.4.2.1.unit_with_unit':
        "Element 'cellml:unit': This element is not expected",
    '5.4.2.1.unit_with_units':
        "Element 'cellml:units': This element is not expected",
    '5.4.2.1.unit_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    '5.4.2.1.unit_with_variable':
        "Element 'cellml:variable': This element is not expected",
    # 5.4.2.3 Allowed values of the prefix attribute
    '5.4.2.3.unit_prefix_real':
        "not a valid value of the union type 'cellml:unit_prefix'",
    '5.4.2.3.unit_prefix_real_int':
        "not a valid value of the union type 'cellml:unit_prefix'",
    '5.4.2.3.unit_prefix_spaces':
        "not a valid value of the union type 'cellml:unit_prefix'",
    '5.4.2.3.unit_prefix_unknown':
        "not a valid value of the union type 'cellml:unit_prefix'",
    # 5.4.2.4 A unit exponent must be a real number
    '5.4.2.4.unit_exponent_invalid':
        "not a valid value of the atomic type 'cellml:real_number'",
    # 5.4.2.5 A unit multiplier must be a real number
    '5.4.2.5.unit_multiplier_invalid':
        "not a valid value of the atomic type 'cellml:real_number'",
    # 5.4.2.6 A unit offset must be a real number
    '5.4.2.6.unit_offset_invalid':
        "not a valid value of the atomic type 'cellml:real_number'",
    # 6.4.1.1 A group cannot be empty (extra test for missing comp_ref/rel_ref)
    '6.4.1.1.group_empty':
        "Element 'cellml:group': Missing child element(s)",
    # 6.4.1.1 A group can only contain component_refs and relationship_refs
    '6.4.1.1.group_with_component':
        "Element 'cellml:component': This element is not expected",
    '6.4.1.1.group_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '6.4.1.1.group_with_connection':
        "Element 'cellml:connection': This element is not expected",
    '6.4.1.1.group_with_group':
        "Element 'cellml:group': This element is not expected",
    '6.4.1.1.group_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '6.4.1.1.group_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '6.4.1.1.group_with_model':
        "Element 'cellml:model': This element is not expected",
    '6.4.1.1.group_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    '6.4.1.1.group_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '6.4.1.1.group_with_role':
        "Element 'cellml:role': This element is not expected",
    '6.4.1.1.group_with_unit':
        "Element 'cellml:unit': This element is not expected",
    '6.4.1.1.group_with_units':
        "Element 'cellml:units': This element is not expected",
    '6.4.1.1.group_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    '6.4.1.1.group_with_variable':
        "Element 'cellml:variable': This element is not expected",
    # 6.4.2.1 A relationship_ref cannot have any CellML children
    '6.4.2.1.relationship_ref_with_component':
        "Element 'cellml:component': This element is not expected",
    '6.4.2.1.relationship_ref_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '6.4.2.1.relationship_ref_with_connection':
        "Element 'cellml:connection': This element is not expected",
    '6.4.2.1.relationship_ref_with_group':
        "Element 'cellml:group': This element is not expected",
    '6.4.2.1.relationship_ref_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '6.4.2.1.relationship_ref_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '6.4.2.1.relationship_ref_with_model':
        "Element 'cellml:model': This element is not expected",
    '6.4.2.1.relationship_ref_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    '6.4.2.1.relationship_ref_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '6.4.2.1.relationship_ref_with_role':
        "Element 'cellml:role': This element is not expected",
    '6.4.2.1.relationship_ref_with_unit':
        "Element 'cellml:unit': This element is not expected",
    '6.4.2.1.relationship_ref_with_units':
        "Element 'cellml:units': This element is not expected",
    '6.4.2.1.relationship_ref_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    '6.4.2.1.relationship_ref_with_variable':
        "Element 'cellml:variable': This element is not expected",
    # 6.4.2.2 When not in a namespace, a relationship_ref's relationship must
    # be either containment or encapsulation.
    '6.4.2.2.relationship_ref_relationship_invalid':
        "not a valid value of the atomic type 'cellml:relationship'",
    # 6.4.2.3 A relationship_ref name must be a cellml identifier
    '6.4.2.3.relationship_ref_name_invalid':
        "not a valid value of the atomic type 'cellml:identifier'",
    # 6.2.4.5 name/relationship pairs must be unique
    '6.4.2.5.relationship_ref_duplicate_named':
        "Element 'cellml:relationship_ref': Duplicate key-sequence",
    # 6.4.3.1 A component_ref must define a component
    '6.4.3.1.component_ref_component_missing':
        "'cellml:component_ref': The attribute 'component' is required",
    # 6.4.3.1 A component_ref can only contain a component_ref
    '6.4.3.1.component_ref_with_component':
        "Element 'cellml:component': This element is not expected",
    '6.4.3.1.component_ref_with_connection':
        "Element 'cellml:connection': This element is not expected",
    '6.4.3.1.component_ref_with_group':
        "Element 'cellml:group': This element is not expected",
    '6.4.3.1.component_ref_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '6.4.3.1.component_ref_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '6.4.3.1.component_ref_with_model':
        "Element 'cellml:model': This element is not expected",
    '6.4.3.1.component_ref_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    '6.4.3.1.component_ref_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '6.4.3.1.component_ref_with_role':
        "Element 'cellml:role': This element is not expected",
    '6.4.3.1.component_ref_with_unit':
        "Element 'cellml:unit': This element is not expected",
    '6.4.3.1.component_ref_with_units':
        "Element 'cellml:units': This element is not expected",
    '6.4.3.1.component_ref_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    '6.4.3.1.component_ref_with_variable':
        "Element 'cellml:variable': This element is not expected",
    # 6.4.3.3 A component attribute must be an identifier
    '6.4.3.3.component_ref_component_invalid':
        "not a valid value of the atomic type 'cellml:identifier'",
    # 6.4.3.3 A component_ref must refer to an existing component
    '6.4.3.3.component_ref_component_nonexistent_1':
        "'cellml:component_ref': No match found for key-sequence",
    # 7.4.1.1 A reaction must contain at least one variable_ref
    '7.4.1.1.reaction_variable_ref_missing':
        "'cellml:reaction': Missing child element",
    # 7.4.1.1 A reaction can only contain a variable_ref
    '7.4.1.1.reaction_with_component':
        "Element 'cellml:component': This element is not expected",
    '7.4.1.1.reaction_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '7.4.1.1.reaction_with_connection':
        "Element 'cellml:connection': This element is not expected",
    '7.4.1.1.reaction_with_group':
        "Element 'cellml:group': This element is not expected",
    '7.4.1.1.reaction_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '7.4.1.1.reaction_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '7.4.1.1.reaction_with_model':
        "Element 'cellml:model': This element is not expected",
    '7.4.1.1.reaction_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    '7.4.1.1.reaction_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '7.4.1.1.reaction_with_role':
        "Element 'cellml:role': This element is not expected",
    '7.4.1.1.reaction_with_unit':
        "Element 'cellml:unit': This element is not expected",
    '7.4.1.1.reaction_with_units':
        "Element 'cellml:units': This element is not expected",
    '7.4.1.1.reaction_with_variable':
        "Element 'cellml:variable': This element is not expected",
    # 7.4.1.2 The reversible attribute can only be yes or no
    '7.4.1.2.reaction_reversible_invalid':
        "not an element of the set",
    # 7.4.1.3 There's another rule about maths here that I don't understand
    # 7.4.2.1 A variable_ref must have at least one role
    '7.4.2.1.variable_ref_role_missing':
        "Element 'cellml:variable_ref': Missing child element",
    '7.4.2.1.variable_ref_variable_missing':
        "Element 'cellml:variable_ref': The attribute 'variable' is required",
    # 7.4.2.1 A variable_ref can only contain a role
    '7.4.2.1.variable_ref_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '7.4.2.1.variable_ref_with_component':
        "Element 'cellml:component': This element is not expected",
    '7.4.2.1.variable_ref_with_connection':
        "Element 'cellml:connection': This element is not expected",
    '7.4.2.1.variable_ref_with_group':
        "Element 'cellml:group': This element is not expected",
    '7.4.2.1.variable_ref_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '7.4.2.1.variable_ref_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '7.4.2.1.variable_ref_with_model':
        "Element 'cellml:model': This element is not expected",
    '7.4.2.1.variable_ref_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    '7.4.2.1.variable_ref_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '7.4.2.1.variable_ref_with_unit':
        "Element 'cellml:unit': This element is not expected",
    '7.4.2.1.variable_ref_with_units':
        "Element 'cellml:units': This element is not expected",
    '7.4.2.1.variable_ref_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    '7.4.2.1.variable_ref_with_variable':
        "Element 'cellml:variable': This element is not expected",
    # 7.4.2.1 A variable_ref must refer to a local variable
    '7.4.2.2.variable_ref_variable_hidden':
        "Element 'cellml:variable_ref': No match found for key-sequence",
    '7.4.2.2.variable_ref_variable_nonexistent':
        "Element 'cellml:variable_ref': No match found for key-sequence",
    '7.4.2.2.variable_ref_variable_duplicate':
        "Element 'cellml:variable_ref': Duplicate key-sequence",
    # 7.4.3.1 A role must define a role attribute
    '7.4.3.1.role_role_missing':
        "Element 'cellml:role': The attribute 'role' is required",
    # 7.4.3.1 A role cannot contain any CellML children (only math)
    '7.4.3.1.role_with_component':
        "Element 'cellml:component': This element is not expected",
    '7.4.3.1.role_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '7.4.3.1.role_with_connection':
        "Element 'cellml:connection': This element is not expected",
    '7.4.3.1.role_with_group':
        "Element 'cellml:group': This element is not expected",
    '7.4.3.1.role_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '7.4.3.1.role_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '7.4.3.1.role_with_model':
        "Element 'cellml:model': This element is not expected",
    '7.4.3.1.role_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    '7.4.3.1.role_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    '7.4.3.1.role_with_role':
        "Element 'cellml:role': This element is not expected",
    '7.4.3.1.role_with_unit':
        "Element 'cellml:unit': This element is not expected",
    '7.4.3.1.role_with_units':
        "Element 'cellml:units': This element is not expected",
    '7.4.3.1.role_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    '7.4.3.1.role_with_variable':
        "Element 'cellml:variable': This element is not expected",
    # 7.4.3.2 A role must define a valid role attribute
    '7.4.3.2.role_role_invalid':
        "not a valid value of the atomic type 'cellml:species_role'",
    # 7.4.3.4 A direction can only be forward, reverse, or both
    '7.4.3.4.role_direction_invalid':
        "not a valid value of the atomic type 'cellml:reaction_direction'",
    # 7.4.3.5 Each (role,direction) combination must be unique within a
    # variable_ref
    '7.4.3.5.role_direction_role_duplicate':
        "Element 'cellml:role': Duplicate key-sequence",
    # 7.4.3.6 Stoichiometry must be a real number
    '7.4.3.6.role_stoichiometry_invalid':
        "not a valid value of the atomic type 'cellml:real_number'",
    # 7.4.3.7 The delta_variable must refer to a local variable
    '7.4.3.7.role_delta_variable_nonexistent_1':
        "Element 'cellml:role': No match found for key-sequence",
    '7.4.3.7.role_delta_variable_nonexistent_2':
        "Element 'cellml:role': No match found for key-sequence",
    # 7.4.3.7 The delta_variable must be unique component-wide
    '7.4.3.7.role_delta_variable_duplicate_1':
        "Element 'cellml:role': Duplicate key-sequence",
    '7.4.3.7.role_delta_variable_duplicate_2':
        "Element 'cellml:role': Duplicate key-sequence",
    # 8.4.1 Cmeta id's are unique
    # This is a bit odd, but is apparently the expected message, as the
    # uniqueness constraint is considered part of the atomic type xs:ID
    '8.4.1.cmeta_id_duplicate':
        "not a valid value of the atomic type 'xs:ID'"
}


# Invalid models for which validation is not expected to pick up the (correct)
# error.
known_issues = {
    # 2.4.3 Elements/attributes in extension namespaces
    '2.4.3.cellml_attributes_inside_extensions',
    '2.4.3.cellml_elements_inside_extensions',
    # 2.5.3 Extension namespaces again
    # 3.4.1.1 Models contain only units, component, group, connection
    '3.4.1.1.model_with_math',
    # 3.4.3.1 Variables can't contain any elements
    '3.4.3.1.variable_with_math',
    # 3.4.3.3 A variable must reference known units
    '3.4.3.3.variable_units_unknown',
    # 3.4.3.3 A variable cannot reference another component's units
    '3.4.3.3.variable_units_other_component',
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
    '3.4.4.1.connection_with_math',
    # 3.4.5.1 A map_components cannot have cellml children or math
    '3.4.5.1.map_components_with_math',
    # 3.4.5.4 component_1 cannot match component_2
    '3.4.5.4.map_components_component_1_equals_2',
    # 3.4.5.4 Each map_components in a model must be unique
    '3.4.5.4.map_components_duplicate_mirrored',
    # 3.4.6.1 A map_variables cannot have cellml children or math
    '3.4.6.1.map_variables_with_math',
    # 3.4.6.2 variable_1 must refer to an existing variable in component_1
    '3.4.6.2.map_variables_variable_1_nonexistent',
    # 3.4.6.3 variable_2 must refer to an existing variable in component_2
    '3.4.6.3.map_variables_variable_2_nonexistent',
    # 3.4.6.4 Interfaces and encapsulation
    '3.4.6.4.map_variables_child_multiple_out_1',
    '3.4.6.4.map_variables_child_multiple_out_2',
    '3.4.6.4.map_variables_child_out_to_out_1',
    '3.4.6.4.map_variables_child_out_to_out_2',
    '3.4.6.4.map_variables_child_private_in',
    '3.4.6.4.map_variables_child_private_out',
    '3.4.6.4.map_variables_hidden_aunt_1',
    '3.4.6.4.map_variables_hidden_aunt_2',
    '3.4.6.4.map_variables_hidden_cousins_1',
    '3.4.6.4.map_variables_hidden_cousins_2',
    '3.4.6.4.map_variables_hidden_cousins_3',
    '3.4.6.4.map_variables_hidden_cousins_4',
    '3.4.6.4.map_variables_hidden_grandchild_1',
    '3.4.6.4.map_variables_hidden_grandchild_2',
    '3.4.6.4.map_variables_hidden_grandparent_1',
    '3.4.6.4.map_variables_hidden_grandparent_2',
    '3.4.6.4.map_variables_hidden_niece_1',
    '3.4.6.4.map_variables_hidden_niece_2',
    '3.4.6.4.map_variables_nested_sibling_private_in',
    '3.4.6.4.map_variables_nested_sibling_private_in_and_out',
    '3.4.6.4.map_variables_nested_sibling_private_out',
    '3.4.6.4.map_variables_parent_in_to_in_1',
    '3.4.6.4.map_variables_parent_in_to_in_2',
    '3.4.6.4.map_variables_parent_multiple_out',
    '3.4.6.4.map_variables_parent_out_to_out_1',
    '3.4.6.4.map_variables_parent_out_to_out_2',
    '3.4.6.4.map_variables_parent_public_in',
    '3.4.6.4.map_variables_parent_public_out',
    '3.4.6.4.map_variables_sibling_in_to_in',
    '3.4.6.4.map_variables_sibling_multiple_out_1',
    '3.4.6.4.map_variables_sibling_multiple_out_2',
    '3.4.6.4.map_variables_sibling_out_to_out',
    '3.4.6.4.map_variables_sibling_private_in_1',
    '3.4.6.4.map_variables_sibling_private_in_2',
    '3.4.6.4.map_variables_sibling_private_in_and_out',
    '3.4.6.4.map_variables_sibling_private_out_1',
    '3.4.6.4.map_variables_sibling_private_out_2',
    # 4 Math can't be overdefined
    '4.math_and_initial_value',
    '4.math_overdefined',
    # 4.4.2 Ci can only refer to local variables
    '4.4.2.ci_nonexistent',
    '4.4.2.ci_non_local_aunt',
    '4.4.2.ci_non_local_child',
    '4.4.2.ci_non_local_cousin',
    '4.4.2.ci_non_local_nested_sibling',
    '4.4.2.ci_non_local_niece',
    '4.4.2.ci_non_local_parent',
    '4.4.2.ci_non_local_sibling',
    # 4.4.3.1 A cn must have a cellml:units
    '4.4.3.1.cn_units_missing',
    # 4.4.3.2 A cn unit attribute must refer to a model, local component, or
    #         predefined unit
    '4.4.3.2.cn_units_nonexistent_1',
    '4.4.3.2.cn_units_nonexistent_2',
    '4.4.3.2.cn_units_parent_component',
    # 4.4.4 A mathml:math can only modify 'owned' variables
    '4.4.4.modify_nonexistent',
    '4.4.4.modify_private_in',
    '4.4.4.modify_public_in',
    # 5.4.1.1 A units with base_units="yes" can't have children
    '5.4.1.1.units_base_units_with_children',
    # 5.4.1.1 A units can only contain unit elements
    '5.4.1.1.units_with_math',
    # 5.4.1.2 Units names cannot overlap with predefined ones
    '5.4.1.2.units_name_predefined_ampere',
    '5.4.1.2.units_name_predefined_becquerel',
    '5.4.1.2.units_name_predefined_candela',
    '5.4.1.2.units_name_predefined_celsius',
    '5.4.1.2.units_name_predefined_coulomb',
    '5.4.1.2.units_name_predefined_dimensionless',
    '5.4.1.2.units_name_predefined_farad',
    '5.4.1.2.units_name_predefined_gram',
    '5.4.1.2.units_name_predefined_gray',
    '5.4.1.2.units_name_predefined_henry',
    '5.4.1.2.units_name_predefined_hertz',
    '5.4.1.2.units_name_predefined_joule',
    '5.4.1.2.units_name_predefined_katal',
    '5.4.1.2.units_name_predefined_kelvin',
    '5.4.1.2.units_name_predefined_kilogram',
    '5.4.1.2.units_name_predefined_liter',
    '5.4.1.2.units_name_predefined_litre',
    '5.4.1.2.units_name_predefined_lumen',
    '5.4.1.2.units_name_predefined_lux',
    '5.4.1.2.units_name_predefined_meter',
    '5.4.1.2.units_name_predefined_metre',
    '5.4.1.2.units_name_predefined_mole',
    '5.4.1.2.units_name_predefined_newton',
    '5.4.1.2.units_name_predefined_ohm',
    '5.4.1.2.units_name_predefined_pascal',
    '5.4.1.2.units_name_predefined_radian',
    '5.4.1.2.units_name_predefined_second',
    '5.4.1.2.units_name_predefined_siemens',
    '5.4.1.2.units_name_predefined_sievert',
    '5.4.1.2.units_name_predefined_steradian',
    '5.4.1.2.units_name_predefined_tesla',
    '5.4.1.2.units_name_predefined_volt',
    '5.4.1.2.units_name_predefined_watt',
    '5.4.1.2.units_name_predefined_weber',
    # 5.4.1.2 Component units names cannot overlap with predefined ones
    '5.4.1.2.units_name_predefined_component_ampere',
    # 5.4.2.1 A unit cannot have CellML children
    '5.4.2.1.unit_with_math',
    # 5.4.2.2 A unit must refer to an existing units
    '5.4.2.2.unit_units_invalid',
    # 5.4.2.2 A unit cannot refer to itself directly or indirectly
    '5.4.2.2.unit_cycle_1',
    '5.4.2.2.unit_cycle_2',
    '5.4.2.2.unit_cycle_3',
    # 5.4.2.7: A unit with a non-zero offset must have exponent 1
    '5.4.2.7.unit_offset_and_exponent',
    # 5.4.2.7: A unit with an offset can't have siblings
    '5.4.2.7.unit_offset_and_siblings_1',
    '5.4.2.7.unit_offset_and_siblings_2',
    # 6.4.1.1 A group must have at least one component_ref
    '6.4.1.1.group_component_ref_missing_1',
    '6.4.1.1.group_component_ref_missing_2',
    # 6.4.1.1 A group must have at least one relationship_ref
    '6.4.1.1.group_relationship_ref_missing_1',
    '6.4.1.1.group_relationship_ref_missing_2',
    # 6.4.1.1 A group cannot be empty (extra test for missing comp_ref/rel_ref)
    '6.4.1.1.group_only_extensions',
    # 6.4.1.1 A group can only contain component_refs and relationship_refs
    '6.4.1.1.group_with_math',
    # 6.4.2.1 A relationship_ref must define a relationship - although it can
    #         be either namespaceless, or in any extension namespace!
    '6.4.2.1.relationship_ref_relationship_missing',
    # 6.4.2.1 A relationship_ref cannot have any CellML children
    '6.4.2.1.relationship_ref_with_math',
    # 6.4.2.4 An encapsulation can not be named
    '6.4.2.4.relationship_ref_encapsulation_duplicate',
    '6.4.2.4.relationship_ref_encapsulation_named',
    # 6.2.4.5 name/relationship pairs must be unique
    '6.4.2.5.relationship_ref_duplicate_unnamed_1',
    '6.4.2.5.relationship_ref_duplicate_unnamed_2',
    # 6.4.3.1 A component_ref can only contain a component_ref
    '6.4.3.1.component_ref_with_math',
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
    # 6.4.3.2 Encapsulation relationships cannot overlap
    '6.4.3.2.component_ref_overlapping_encapsulation',
    # 6.4.3.3 A component_ref must refer to an existing component
    '6.4.3.3.component_ref_component_nonexistent_2',
    '7.4.1.1.reaction_with_math',
    # 7.4.1.3 A reaction in an encapsulating component cannot use
    # delta_variable attributes in its roles.
    '7.4.1.3.reaction_encapsulating_delta_variable',
    # 7.4.2.1 A variable_ref can only contain a role
    '7.4.2.1.variable_ref_with_math',
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
    # 7.4.3.5 A rate must have direction forward
    '7.4.3.5.role_direction_both_rate',
    '7.4.3.5.role_direction_reverse_rate',
    # 7.4.3.5 A reactant must have direction forward
    '7.4.3.5.role_direction_both_reactant',
    '7.4.3.5.role_direction_reverse_reactant',
    # 7.4.3.5 A product must have direction forward
    '7.4.3.5.role_direction_both_product',
    '7.4.3.5.role_direction_reverse_product',
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
}


@pytest.fixture
def log():
    """ Returns a logger object. """
    return logging.getLogger(__name__)


@pytest.fixture
def parser():
    """ Returns a parser that can resolve schema locations. """
    parser = etree.XMLParser(no_network=True)
    parser.resolvers.add(check.SchemaResolver())
    return parser


@pytest.fixture
def validator(parser):
    """ Returns a parsed schema object. """
    filename = check.cellml_1_0('cellml_1_0.xsd')
    assert os.path.isfile(filename)
    return etree.XMLSchema(etree.parse(filename, parser))


class TestDTD(object):
    """ Tests the DTD validation. """

    @classmethod
    def setup_class(cls):
        cls._report = Report('Schema Validation - CellML 1.0')

    @classmethod
    def teardown_class(cls):
        cls._report.render(
            os.path.join(check.REPORT_DIR, 'schema_1_0.md'))

    @pytest.mark.parametrize(('name', 'path'), shared.list_passes_1_0())
    def test_valid_model(self, name, path, parser, validator, log):
        shared.assert_valid(
            self._report, name, path, parser, validator, false_negatives, log)

    @pytest.mark.parametrize(('name', 'path'), shared.list_fails_1_0())
    def test_invalid_model(self, name, path, parser, validator, log):
        shared.assert_invalid(
            self._report, name, path, parser, validator, expected_messages,
            known_issues, log)


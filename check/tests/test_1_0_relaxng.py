#
# Tests CellML 1.0 RelaxNG schema validation
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import logging
import os
import pytest
import re
from lxml import etree

import check


# Known instances where the RelaxNG schema says a valid file is invalid
# All to do with namespaces and extension elements
known_false_negatives = {
    # Units can probably be empty, even if not base units. The spec is not
    # explicit, but CellML 2 allows it. The Relax NG schema doesn't like empty
    # units elements though.
    '5.4.1.1.units_empty_1': 'Expecting an element unit',
    '5.4.1.1.units_empty_2': 'Expecting an element unit',
    # Extension relationship types
    '6.4.3.2.component_ref_no_children_extension': 'Invalid sequence',
    '6.4.2.1.relationship_ref_relationship_2': 'Invalid sequence',
}


# Expected error messages for invalid files.
# `None` indicates a known false positive
expected_errors = {
    # Not in spec: Root node
    '0.0.root_node_not_model':
        'Expecting element model',
    '0.0.root_node_two_elements':
        'Extra content at the end of the document',
    '0.0.root_node_two_models':
        'Extra content at the end of the document',
    '0.0.root_node_namespace_wrong':
        'Element model has wrong namespace',
    # Not in spec: Real number format
    '0.1.real_number_invalid_1':
        'Invalid attribute initial_value for element variable',
    '0.1.real_number_invalid_2':
        'Invalid attribute initial_value for element variable',
    '0.1.real_number_invalid_3':
        'Invalid attribute initial_value for element variable',
    '0.1.real_number_invalid_4':
        'Invalid attribute initial_value for element variable',
    '0.1.real_number_invalid_5':
        'Invalid attribute initial_value for element variable',
    '0.1.real_number_invalid_6':
        'Invalid attribute initial_value for element variable',
    # 2.4.1 CellML Identifiers
    '2.4.1.identifier_empty':
        'Element component failed to validate',
    '2.4.1.identifier_only_underscore':
        'Element component failed to validate',
    '2.4.1.identifier_unexpected_character':
        'Element component failed to validate',
    '2.4.1.identifier_unexpected_character_2':
        'Element component failed to validate',
    '2.4.1.identifier_unexpected_character_unicode':
        'Element component failed to validate',
    # 2.4.2. Allowable CellML elements and attributes
    '2.4.2.imaginary_attributes_1':
        'Invalid attribute fruit for element model',
    '2.4.2.imaginary_attributes_2':
        'Invalid attribute fruit for element model',
    '2.4.2.imaginary_elements':
        'Element model has extra content',
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
    # 2.5.1 Identifiers are case sensitive
    '2.5.1.identifiers_are_case_sensitive': None,        
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
    # 3.4.2.2 Component names must be unique
    '3.4.2.2.component_name_duplicate': None,
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
    '3.4.3.2.variable_name_duplicate': None,
    # 3.4.3.3 A variable must reference known units
    '3.4.3.3.variable_units_unknown': None,
    # 3.4.3.3 A variable cannot reference another component's units
    '3.4.3.3.variable_units_other_component': None,
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
    '3.4.5.2.map_components_component_1_nonexistent': None,
    # 3.4.5.3 component_2 must refer to an existing component
    '3.4.5.3.map_components_component_2_nonexistent': None,
    # 3.4.5.4 component_1 cannot match component_2
    '3.4.5.4.map_components_component_1_equals_2': None,
    # 3.4.5.4 Each map_components in a model must be unique
    '3.4.5.4.map_components_duplicate': None,
    '3.4.5.4.map_components_duplicate_mirrored': None,
    # 3.4.6.1 A map_variables must declare variable_1 and variable_2
    '3.4.6.1.map_variables_variable_1_missing':
        'Element map_variables failed to validate attributes',
    '3.4.6.1.map_variables_variable_2_missing':
        'Element map_variables failed to validate attributes',
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
    '3.4.6.2.map_variables_variable_1_nonexistent': None,
    # 3.4.6.3 variable_2 must refer to an existing variable in component_2
    '3.4.6.3.map_variables_variable_2_nonexistent': None,
    # 3.4.6.4 Interfaces and encapsulation
    '3.4.6.4.map_variables_child_multiple_out_1': None,
    '3.4.6.4.map_variables_child_multiple_out_2': None,
    '3.4.6.4.map_variables_child_out_to_out_1': None,
    '3.4.6.4.map_variables_child_out_to_out_2': None,
    '3.4.6.4.map_variables_child_private_in': None,
    '3.4.6.4.map_variables_child_private_out': None,
    '3.4.6.4.map_variables_hidden_aunt_1': None,
    '3.4.6.4.map_variables_hidden_aunt_2': None,
    '3.4.6.4.map_variables_hidden_cousins_1': None,
    '3.4.6.4.map_variables_hidden_cousins_2': None,
    '3.4.6.4.map_variables_hidden_cousins_3': None,
    '3.4.6.4.map_variables_hidden_cousins_4': None,
    '3.4.6.4.map_variables_hidden_grandchild_1': None,
    '3.4.6.4.map_variables_hidden_grandchild_2': None,
    '3.4.6.4.map_variables_hidden_grandparent_1': None,
    '3.4.6.4.map_variables_hidden_grandparent_2': None,
    '3.4.6.4.map_variables_hidden_niece_1': None,
    '3.4.6.4.map_variables_hidden_niece_2': None,
    '3.4.6.4.map_variables_nested_sibling_private_in': None,
    '3.4.6.4.map_variables_nested_sibling_private_in_and_out': None,
    '3.4.6.4.map_variables_nested_sibling_private_out': None,
    '3.4.6.4.map_variables_parent_in_to_in_1': None,
    '3.4.6.4.map_variables_parent_in_to_in_2': None,
    '3.4.6.4.map_variables_parent_multiple_out': None,
    '3.4.6.4.map_variables_parent_out_to_out_1': None,
    '3.4.6.4.map_variables_parent_out_to_out_2': None,
    '3.4.6.4.map_variables_parent_public_in': None,
    '3.4.6.4.map_variables_parent_public_out': None,
    '3.4.6.4.map_variables_sibling_in_to_in': None,
    '3.4.6.4.map_variables_sibling_multiple_out_1': None,
    '3.4.6.4.map_variables_sibling_multiple_out_2': None,
    '3.4.6.4.map_variables_sibling_out_to_out': None,
    '3.4.6.4.map_variables_sibling_private_in_1': None,
    '3.4.6.4.map_variables_sibling_private_in_2': None,
    '3.4.6.4.map_variables_sibling_private_in_and_out': None,
    '3.4.6.4.map_variables_sibling_private_out_1': None,
    '3.4.6.4.map_variables_sibling_private_out_2': None,
    # 4 Math can't be overdefined
    #'4.math_and_initial_value':
    #'4.math_overdefined':
    # 4.4.1 Bad math
    '4.4.1.math_not_math_component':
        'Element component failed to validate content',
    '4.4.1.math_not_math_reaction': 
        'Element role failed to validate content',
    # 4.4.2 Ci can only refer to local variables
    '4.4.2.ci_nonexistent': None,
    '4.4.2.ci_non_local_aunt': None,
    '4.4.2.ci_non_local_child': None,
    '4.4.2.ci_non_local_cousin': None,
    '4.4.2.ci_non_local_nested_sibling': None,
    '4.4.2.ci_non_local_niece': None,
    '4.4.2.ci_non_local_parent': None,
    '4.4.2.ci_non_local_sibling': None,
    # 4.4.3.1 A cn must have a cellml:units
    #'4.4.3.1.cn_units_missing':
    # 4.4.3.2 A cn unit attribute must refer to a model, local component, or
    #         predefined unit
    #'4.4.3.2.cn_units_nonexistent_1':
    #'4.4.3.2.cn_units_nonexistent_2':
    #'4.4.3.2.cn_units_parent_component':
    # 4.4.4 A mathml:math can only modify 'owned' variables
    #'4.4.4.modify_nonexistent':
    #'4.4.4.modify_private_in':
    #'4.4.4.modify_public_in':
    # 5.4.1.1 Unitses must have a name
    #'5.4.1.1.units_name_missing':
    # 5.4.1.1 A units with base_units="yes" can't have children
    #'5.4.1.1.units_base_units_with_children':
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
        'Element units has extra content: unit',    
    '5.4.1.1.units_with_units':
        'Element units has extra content: units',    
    '5.4.1.1.units_with_variable':
        'Element units has extra content: variable',    
    '5.4.1.1.units_with_variable_ref':
        'Element units has extra content: variable_ref',    
    # 5.4.1.2 A units name must be a valid identifier
    #'5.4.1.2.units_name_invalid':
    # 5.4.1.2 Units names must be unique (within model or local component)
    #'5.4.1.2.units_name_duplicate_1':
    #'5.4.1.2.units_name_duplicate_2':
    # 5.4.1.2 Units names cannot overlap with predefined ones
    #'5.4.1.2.units_name_predefined_ampere':
    #'5.4.1.2.units_name_predefined_becquerel':
    #'5.4.1.2.units_name_predefined_candela':
    #'5.4.1.2.units_name_predefined_celsius':
    #'5.4.1.2.units_name_predefined_coulomb':
    #'5.4.1.2.units_name_predefined_dimensionless':
    #'5.4.1.2.units_name_predefined_farad':
    #'5.4.1.2.units_name_predefined_gram':
    #'5.4.1.2.units_name_predefined_gray':
    #'5.4.1.2.units_name_predefined_henry':
    #'5.4.1.2.units_name_predefined_hertz':
    #'5.4.1.2.units_name_predefined_joule':
    #'5.4.1.2.units_name_predefined_katal':
    #'5.4.1.2.units_name_predefined_kelvin':
    #'5.4.1.2.units_name_predefined_kilogram':
    #'5.4.1.2.units_name_predefined_liter':
    #'5.4.1.2.units_name_predefined_litre':
    #'5.4.1.2.units_name_predefined_lumen':
    #'5.4.1.2.units_name_predefined_lux':
    #'5.4.1.2.units_name_predefined_meter':
    #'5.4.1.2.units_name_predefined_metre':
    #'5.4.1.2.units_name_predefined_mole':
    #'5.4.1.2.units_name_predefined_newton':
    #'5.4.1.2.units_name_predefined_ohm':
    #'5.4.1.2.units_name_predefined_pascal':
    #'5.4.1.2.units_name_predefined_radian':
    #'5.4.1.2.units_name_predefined_second':
    #'5.4.1.2.units_name_predefined_siemens':
    #'5.4.1.2.units_name_predefined_sievert':
    #'5.4.1.2.units_name_predefined_steradian':
    #'5.4.1.2.units_name_predefined_tesla':
    #'5.4.1.2.units_name_predefined_volt':
    #'5.4.1.2.units_name_predefined_watt':
    #'5.4.1.2.units_name_predefined_weber':
    # 5.4.1.2 Component units names cannot overlap with predefined ones
    #'5.4.1.2.units_name_predefined_component_ampere':
    # 5.4.1.3 Units base_units attribute can only be yes or no
    #'5.4.1.3.units_base_units_invalid':
    # 5.4.2.1 A unit must have a units attribute
    #'5.4.2.1.unit_units_missing':
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
    # 5.4.2.2 A unit must refer to an existing units
    #'5.4.2.2.unit_units_invalid':
    # 5.4.2.2 A unit cannot refer to itself directly or indirectly
    #'5.4.2.2.unit_cycle_1':
    #'5.4.2.2.unit_cycle_2':
    #'5.4.2.2.unit_cycle_3':
    # 5.4.2.3 Allowed values of the prefix attribute
    #'5.4.2.3.unit_prefix_real':
    #'5.4.2.3.unit_prefix_real_int':
    #'5.4.2.3.unit_prefix_spaces':
    #'5.4.2.3.unit_prefix_unknown':
    # 5.4.2.4 A unit exponent must be a real number
    #'5.4.2.4.unit_exponent_invalid':
    # 5.4.2.5 A unit multiplier must be a real number
    #'5.4.2.5.unit_multiplier_invalid':
    # 5.4.2.6 A unit offset must be a real number
    #'5.4.2.6.unit_offset_invalid':
    # 5.4.2.7: A unit with a non-zero offset must have exponent 1
    #'5.4.2.7.unit_offset_and_exponent':
    # 5.4.2.7: A unit with an offset can't have siblings
    #'5.4.2.7.unit_offset_and_siblings_1':
    #'5.4.2.7.unit_offset_and_siblings_2':
    # 6.4.1.1 A group must have at least one component_ref
    #'6.4.1.1.group_component_ref_missing':
    # 6.4.1.1 A group must have at least one relationship_ref
    #'6.4.1.1.group_relationship_ref_missing':
    # 6.4.1.1 A group cannot be empty (extra test for missing comp_ref/rel_ref)
    #'6.4.1.1.group_empty':
    #'6.4.1.1.group_only_extensions':
    # 6.4.1.1 A group can only contain component_refs and relationship_refs
    '6.4.1.1.group_with_component':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_component_ref':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_connection':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_group':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_map_components':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_map_variables':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_math':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_model':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_reaction':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_relationship_ref':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_role':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_unit':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_units':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_variable_ref':
        'Element group has extra content: variable',    
    '6.4.1.1.group_with_variable':
        'Element group has extra content: variable',    
    # 6.4.2.1 A relationship_ref must define a relationship - although it can
    #         be either namespaceless, or in any extension namespace!
    #'6.4.2.1.relationship_ref_relationship_missing':
    # 6.4.2.1 A relationship_ref cannot have any CellML children
    '6.4.2.1.relationship_ref_with_component':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_component_ref':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_connection':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_group':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_map_components':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_map_variables':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_math':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_model':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_reaction':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_relationship_ref':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_role':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_unit':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_units':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_variable_ref':
        'Element relationship_ref has extra content: variable',    
    '6.4.2.1.relationship_ref_with_variable':
        'Element relationship_ref has extra content: variable',    
    # 6.4.2.2 When not in a namespace, a relationship_ref's relationship must
    # be either containment or encapsulation.
    #'6.4.2.2.relationship_ref_relationship_invalid':
    # 6.4.2.3 A relationship_ref name must be a cellml identifier
    #'6.4.2.3.relationship_ref_name_invalid':
    # 6.4.2.4 An encapsulation can not be named
    #'6.4.2.4.relationship_ref_encapsulation_duplicate':
    #'6.4.2.4.relationship_ref_encapsulation_named':
    # 6.2.4.5 name/relationship pairs must be unique
    #'6.4.2.5.relationship_ref_duplicate_named':
    #'6.4.2.5.relationship_ref_duplicate_unnamed_1':
    #'6.4.2.5.relationship_ref_duplicate_unnamed_2':
    # 6.4.3.1 A component_ref must define a component
    #'6.4.3.1.component_ref_component_missing':
    # 6.4.3.1 A component_ref can only contain a component_ref
    '6.4.3.1.component_ref_with_component':
        'Element component_ref has extra content: variable',    
    '6.4.3.1.component_ref_with_connection':
        'Element component_ref has extra content: variable',    
    '6.4.3.1.component_ref_with_group':
        'Element component_ref has extra content: variable',    
    '6.4.3.1.component_ref_with_map_components':
        'Element component_ref has extra content: variable',    
    '6.4.3.1.component_ref_with_map_variables':
        'Element component_ref has extra content: variable',    
    '6.4.3.1.component_ref_with_math':
        'Element component_ref has extra content: variable',    
    '6.4.3.1.component_ref_with_model':
        'Element component_ref has extra content: variable',    
    '6.4.3.1.component_ref_with_reaction':
        'Element component_ref has extra content: variable',    
    '6.4.3.1.component_ref_with_relationship_ref':
        'Element component_ref has extra content: variable',    
    '6.4.3.1.component_ref_with_role':
        'Element component_ref has extra content: variable',    
    '6.4.3.1.component_ref_with_unit':
        'Element component_ref has extra content: variable',    
    '6.4.3.1.component_ref_with_units':
        'Element component_ref has extra content: variable',    
    '6.4.3.1.component_ref_with_variable_ref':
        'Element component_ref has extra content: variable',    
    '6.4.3.1.component_ref_with_variable':
        'Element component_ref has extra content: variable',    
    # 6.4.3.2 A component's children cannot be declared two places
    #'6.4.3.2.component_ref_children_declared_twice_1':
    #'6.4.3.2.component_ref_children_declared_twice_2':
    #'6.4.3.2.component_ref_children_declared_twice_3':
    # 6.4.3.3 A hierarchy cannot be circular
    #'6.4.3.2.component_ref_cycle_1':
    #'6.4.3.2.component_ref_cycle_2':
    #'6.4.3.2.component_ref_cycle_3':
    #'6.4.3.2.component_ref_cycle_4':
    # 6.4.3.2 A component cannot be named twice in a single hierarchy
    #'6.4.3.2.component_ref_duplicate_child_1':
    #'6.4.3.2.component_ref_duplicate_child_2':
    # 6.4.3.2 The first component_ref in a containment must have children
    #'6.4.3.2.component_ref_no_children_containment':
    # 6.4.3.2 The first component_ref in an encapsulation must have children
    #'6.4.3.2.component_ref_no_children_encapsulation':
    # 6.4.3.2 Encapsulation relationships cannot overlap
    #'6.4.3.2.component_ref_overlapping_encapsulation':
    # 6.4.3.3 A component attribute must be an identifier
    #'6.4.3.3.component_ref_component_invalid':
    # 6.4.3.3 A component_ref must refer to an existing component
    #'6.4.3.3.component_ref_component_nonexistent_1':
    #'6.4.3.3.component_ref_component_nonexistent_2':
    # 7.4.1.1 A reaction must contain at least one variable_ref
    #'7.4.1.1.reaction_variable_ref_missing':
    # 7.4.1.1 A reaction can only contain a variable_ref
    '7.4.1.1.reaction_with_component':
        'Element reaction has extra content: variable',    
    '7.4.1.1.reaction_with_component_ref':
        'Element reaction has extra content: variable',    
    '7.4.1.1.reaction_with_connection':
        'Element reaction has extra content: variable',    
    '7.4.1.1.reaction_with_group':
        'Element reaction has extra content: variable',    
    '7.4.1.1.reaction_with_map_components':
        'Element reaction has extra content: variable',    
    '7.4.1.1.reaction_with_map_variables':
        'Element reaction has extra content: variable',    
    '7.4.1.1.reaction_with_math':
        'Element reaction has extra content: variable',    
    '7.4.1.1.reaction_with_model':
        'Element reaction has extra content: variable',    
    '7.4.1.1.reaction_with_reaction':
        'Element reaction has extra content: variable',    
    '7.4.1.1.reaction_with_relationship_ref':
        'Element reaction has extra content: variable',    
    '7.4.1.1.reaction_with_role':
        'Element reaction has extra content: variable',    
    '7.4.1.1.reaction_with_unit':
        'Element reaction has extra content: variable',    
    '7.4.1.1.reaction_with_units':
        'Element reaction has extra content: variable',    
    '7.4.1.1.reaction_with_variable':
        'Element reaction has extra content: variable',    
    # 7.4.1.2 The reversible attribute can only be yes or no
    #'7.4.1.2.reaction_reversible_invalid':
    # 7.4.1.3 A reaction in an encapsulating component cannot use
    # delta_variable attributes in its roles.
    #'7.4.1.3.reaction_encapsulating_delta_variable':
    # 7.4.1.3 There's another rule about maths here that I don't understand
    # 7.4.2.1 A variable_ref must have at least one role
    #'7.4.2.1.variable_ref_role_missing':
    #'7.4.2.1.variable_ref_variable_missing':
    # 7.4.2.1 A variable_ref can only contain a role
    '7.4.2.1.variable_ref_with_component_ref':
        'Element variable_ref has extra content: variable',    
    '7.4.2.1.variable_ref_with_component':
        'Element variable_ref has extra content: variable',    
    '7.4.2.1.variable_ref_with_connection':
        'Element variable_ref has extra content: variable',    
    '7.4.2.1.variable_ref_with_group':
        'Element variable_ref has extra content: variable',    
    '7.4.2.1.variable_ref_with_map_components':
        'Element variable_ref has extra content: variable',    
    '7.4.2.1.variable_ref_with_map_variables':
        'Element variable_ref has extra content: variable',    
    '7.4.2.1.variable_ref_with_math':
        'Element variable_ref has extra content: variable',    
    '7.4.2.1.variable_ref_with_model':
        'Element variable_ref has extra content: variable',    
    '7.4.2.1.variable_ref_with_reaction':
        'Element variable_ref has extra content: variable',    
    '7.4.2.1.variable_ref_with_relationship_ref':
        'Element variable_ref has extra content: variable',    
    '7.4.2.1.variable_ref_with_unit':
        'Element variable_ref has extra content: variable',    
    '7.4.2.1.variable_ref_with_units':
        'Element variable_ref has extra content: variable',    
    '7.4.2.1.variable_ref_with_variable':
        'Element variable_ref has extra content: variable',    
    '7.4.2.1.variable_ref_with_variable_ref':
        'Element variable_ref has extra content: variable',    
    # 7.4.2.1 A variable_ref must refer to a local variable
    #'7.4.2.2.variable_ref_variable_hidden':
    #'7.4.2.2.variable_ref_variable_nonexistent':
    #'7.4.2.2.variable_ref_variable_duplicate':
    # 7.4.3.1 A role must define a role attribute
    #'7.4.3.1.role_role_missing':
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
    #'7.4.3.2.role_role_invalid':
    # 7.4.3.3 A reaction can only have a single rate
    #'7.4.3.3.reaction_multiple_rates':
    # 7.4.3.3 A variable_ref with a rate can't have other roles
    #'7.4.3.3.role_rate_with_multiple_roles':
    # 7.4.3.3 A role with attribute rate can't have a delta_variable attribute
    #'7.4.3.3.role_rate_with_delta_variable':
    # 7.4.3.3 A role with attribute rate can't have a stoichiometry attribute
    #'7.4.3.3.role_rate_with_stoichiometry':
    # 7.4.3.4 A direction can only be forward, reverse, or both
    #'7.4.3.4.role_direction_invalid':
    # 7.4.3.5 A direction in an irreversible reaction must be forward
    #'7.4.3.5.role_direction_both_irreversible':
    #'7.4.3.5.role_direction_reverse_irreversible':
    # 7.4.3.5 A rate must have direction forward
    #'7.4.3.5.role_direction_both_rate':
    #'7.4.3.5.role_direction_reverse_rate':
    # 7.4.3.5 A reactant must have direction forward
    #'7.4.3.5.role_direction_both_reactant':
    #'7.4.3.5.role_direction_reverse_reactant':
    # 7.4.3.5 A product must have direction forward
    #'7.4.3.5.role_direction_both_product':
    #'7.4.3.5.role_direction_reverse_product':
    # 7.4.3.5 Each (role,direction) combination must be unique within a
    # variable_ref
    #'7.4.3.5.role_direction_role_duplicate':
    # 7.4.3.6 Stoichiometry must be a real number
    #'7.4.3.6.role_stoichiometry_invalid':
    # 7.4.3.7 The delta_variable must refer to a local variable
    #'7.4.3.7.role_delta_variable_nonexistent_1':
    #'7.4.3.7.role_delta_variable_nonexistent_2':
    # 7.4.3.7 The delta_variable must be unique component-wide
    #'7.4.3.7.role_delta_variable_duplicate_1':
    #'7.4.3.7.role_delta_variable_duplicate_2':
    # 7.4.3.8 A delta_variable can only appear on reactants or products
    # Note: rate is already checked in 7.4.3.3
    #'7.4.3.8.role_delta_variable_activator':
    #'7.4.3.8.role_delta_variable_catalyst':
    #'7.4.3.8.role_delta_variable_inhibitor':
    #'7.4.3.8.role_delta_variable_modifier':
    # 7.4.3.8 A delta_variable must have either a stoichiometry or math
    #'7.4.3.8.role_delta_variable_without_rate_or_math':
    # 7.4.3.8 A delta_variable with a stoichiometry cannot have math
    #'7.4.3.8.role_delta_variable_with_rate_and_math':
    # 7.4.3.8 A delta_variable with a stoichiometry must have a rate
    #'7.4.3.8.role_delta_variable_with_stoichiometry_no_rate':
    # 7.4.3.9 The math in a role must be relevant to the variable_ref
    #'7.4.3.9.role_math_not_relevant':
    # 8.4.1 Cmeta id's are unique
    '8.4.1.cmeta_id_duplicate':
        'Invalid attribute id for element component_ref',
}


@pytest.fixture
def log():
    """ Returns a logger object. """
    return logging.getLogger(__name__)


@pytest.fixture
def parser():
    """ Returns an XML parser. """
    return etree.XMLParser(no_network=False)


@pytest.fixture
def relaxng(parser):
    """ Returns a CellML 1.0 RelaxNG object. """
    filename = check.cellml_1_0('cellml_1_0.rng')
    assert os.path.isfile(filename)
    return etree.RelaxNG(etree.parse(filename, parser))


def list_models(subdir):
    """
    Scans a path (without recursing into subdirectories) and returns a list of
    tuples ``(name, path)`` representing each file.
    """
    files = []
    subdir = check.model_1_0(subdir)
    for filename in os.listdir(subdir):
        name, ext = os.path.splitext(filename)
        if ext == '.cellml':
            files.append(pytest.param(
                name, os.path.join(subdir, filename), id=name))

    files.sort(key=lambda x: x[0])
    return files


def list_passes():
    """
    Returns a list of ``pytest.param`` objects for models that should pass.
    """
    # Valid models
    files = list_models('valid')

    # Numbers are all valid MathML2, so should pass schema validation
    files += list_models('numbers')

    # Types are not checked in schema, should pass
    files += list_models('booleans')

    # Units do not affect validity, so these should all pass
    files += list_models('unit_checking_consistent')
    files += list_models('unit_checking_inconsistent')
    files += list_models('unit_conversion_convertible')
    files += list_models('unit_conversion_inconvertible')

    return []
    return files


@pytest.mark.parametrize(('name', 'path'), list_passes())
def test_valid_model(name, path, parser, relaxng, log):
    """
    Checks that a model validates.
    """

    # Parse and validate
    xml = etree.parse(path, parser)
    valid = relaxng.validate(xml)

    # See if there's an expected false negative for this
    try:
        expected = known_false_negatives[name]
    except KeyError:
        expected = None

    if valid:
        # Let the user know if a listed false negative is actually handled
        # correctly
        if expected is not None:
            log.error('Valid file passed validation, but was expected to fail')
            log.error('Expected: ' + expected)
            pytest.fail()

    else:

        # Log error
        e = relaxng.error_log[0]
        error = e.message
        log.info('Error on line ' + str(e.line) + ': ' + error)

        # Check if we were expecting to fail
        if expected is None:
            log.error('Unexpected error in ' + name)
            log.error('Returned: ' + error)

            # Assert valid, raising a detailed error message
            relaxng.assertValid(xml)

        else:
            # Check if it was the expected fail
            r = re.compile(re.escape(expected))
            if r.search(error) is None:
                log.error('Unexpected error in valid file ' + name)
                log.error('Expected: ' + expected)
                log.error('Returned: ' + error)
                pytest.fail()
            pytest.xfail()


def list_fails():
    """
    Returns a list of ``pytest.param`` objects for models that should fail.
    """
    return list_models('invalid')[160:200]


@pytest.mark.parametrize(('name', 'path'), list_fails())
def test_invalid_model(name, path, parser, relaxng, log):
    """
    Checks that a model doesn't validate, and for the right reason.
    """

    # Parse and validate
    try:
        xml = etree.parse(path, parser)
    except etree.XMLSyntaxError as e:

        # Log detected error
        errors = [str(e)]
        log.info('Error during parsing: ' + errors[0])
        valid = False

    else:
        # Validate
        valid = relaxng.validate(xml)

        if valid:
            if expected_errors.get(name, '') is None:
                pytest.xfail('Known false negative')
                return
            else:
                errors = ['No error raised']
        else:
            # Log detected error
            errors = [e.message for e in relaxng.error_log]
            e = relaxng.error_log[0]
            log.info('Error on line ' + str(e.line) + ': ' + e.message)

    # Test correct error was raised
    expected = expected_errors.get(name, '')
    if expected == '':
        expected = 'No expected error set'
    if expected is None:
        expected = 'Expected xfail, but found other error instead'
    log.info('Expected error: ' + expected)
    r = re.compile(re.escape(expected))
    for e in errors:
        if r.search(e) is not None:
            return
    if valid:
        log.error('Model passed validation unexpectedly: ' + name)
        log.error('Expected: ' + expected)
    else:
        log.error('Unexpected error in ' + name)
        for e in errors:
            log.error('Returned: ' + e)
    pytest.fail()


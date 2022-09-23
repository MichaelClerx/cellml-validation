#
# Tests CellML 1.0 validation with Myokit (CellML revamp)
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import logging
import os
import pytest
import warnings

import check
from . import shared
from .. import myokit_validation as myokit
from .report import Report_1_0 as Report


# Known instances where Myokit says a valid file is invalid
false_negatives = {
    # Myokit uses stricter rules for identifiers
    '2.4.1.valid_identifiers':
        'must be a valid CellML identifier',
    # No reaction support
    '2.4.3.reaction_with_extensions':
        'Reactions are not supported.',
    '2.4.3.role_with_extensions':
        'Reactions are not supported.',
    '2.4.3.variable_ref_with_extensions':
        'Reactions are not supported.',
    # No reaction support
    '2.4.3.xlink_href_in_reaction':
        'Reactions are not supported.',
    '2.4.3.xlink_href_in_role':
        'Reactions are not supported.',
    '2.4.3.xlink_href_in_variable_ref':
        'Reactions are not supported.',
    # No reaction support
    '3.4.2.1.component_child_order_1':
        'Reactions are not supported.',
    '3.4.2.1.component_child_order_2':
        'Reactions are not supported.',
    '3.4.2.1.component_with_one_reaction':
        'Reactions are not supported.',
    '3.4.2.1.component_with_reactions':
        'Reactions are not supported.',
    # Bases other than 10
    '4.2.3_2.3.mathml_numbers_real_base':
        'bases other than 10',
    # Factorial is not supported
    '4.2.3_4.3_mathml_functions_factorial':
        'Unsupported element in apply',
    # Only likes assignment form
    '4.algebraic_model':
        'Invalid expression found on the left-hand side of an equation',
    '4.algebraic_ode_model':
        'Invalid expression found on the left-hand side of an equation',
    # Overdefined models
    '4.overdefined_direct_and_direct':
        'Two defining equations',
    '4.overdefined_direct_and_initial':
        'Initial value and a defining equation',
    '4.overdefined_direct_and_ode':
        'Two defining equations',
    '4.overdefined_ode_and_ode':
        'Two defining equations',
    # Factorial is not supported
    '5.2.7.unit_checking_functions_factorial':
        'Unsupported element in apply',
    # Non-zero offsets are not supported
    '5.4.2.1.unit_prefix_exponent_multiplier_huge':
        'Unit prefix too large',
    # Factorials are not supported
    '5.5.2.boolean_function_factorial':
        'Unsupported element in apply',
    # No reaction support
    '7.4.1.2.reaction_reversible_no':
        'Reactions are not supported.',
    '7.4.1.2.reaction_reversible_yes':
        'Reactions are not supported.',
    '7.4.3.reaction_all_roles_and_attributes':
        'Reactions are not supported.',
    '7.4.3.reaction_reversible_no':
        'Reactions are not supported.',
    '7.4.3.reaction_simple':
        'Reactions are not supported.',
    '8.4.1.cmeta_id_in_reaction':
        'Reactions are not supported.',
    '8.4.1.cmeta_id_in_role':
        'Reactions are not supported.',
    '8.4.1.cmeta_id_in_variable_ref':
        'Reactions are not supported.',
    '8.4.2.rdf_in_reaction':
        'Reactions are not supported.',
    '8.4.2.rdf_in_role':
        'Reactions are not supported.',
    '8.4.2.rdf_in_variable_ref':
        'Reactions are not supported.',
    # Factorial is not supported
    'C.3.3.unit_checking_function_factorial_operand_error':
        'Unsupported element in apply',
}


# Expected error messages for invalid files.
expected_messages = {
    # Not in spec: Root node
    '0.0.root_node_namespace_wrong':
        'Root node must be in CellML',
    '0.0.root_node_not_model':
        'Root node must be a CellML model',
    '0.0.root_node_two_elements':
        #'junk after document element', # etree
        'Extra content at the end of the document',
    '0.0.root_node_two_models':
        #'junk after document element',
        'Extra content at the end of the document',
    # Not in spec: Real number format
    '0.1.real_number_invalid_1':
        'must be a real number',
    '0.1.real_number_invalid_2':
        'must be a real number',
    '0.1.real_number_invalid_3':
        'must be a real number',
    '0.1.real_number_invalid_4':
        'must be a real number',
    '0.1.real_number_invalid_5':
        'must be a real number',
    '0.1.real_number_invalid_6':
        'must be a real number',
    # 2.4.1 CellML Identifiers
    '2.4.1.identifier_empty':
        'valid CellML identifier',
    '2.4.1.identifier_only_underscore':
        'valid CellML identifier',
    '2.4.1.identifier_unexpected_character_1':
        'valid CellML identifier',
    '2.4.1.identifier_unexpected_character_2':
        'valid CellML identifier',
    '2.4.1.identifier_unexpected_character_unicode':
        'valid CellML identifier',
    # 2.4.2. Allowable CellML elements and attributes
    '2.4.2.imaginary_attributes_1':
        'Unexpected attribute fruit',
    '2.4.2.imaginary_attributes_2':
        'Unexpected attribute cellml:fruit',
    '2.4.2.imaginary_elements_1':
        'found element of type cellml:fruit',
    '2.4.2.imaginary_elements_2':
        'Imports are not allowed in CellML 1.0',
    # 2.4.3 Elements/attributes in extension namespaces
    '2.4.3.cellml_elements_inside_extensions':
        'CellML element cellml:component found inside extension element',
    '2.4.3.cellml_attributes_inside_extensions':
        'CellML attribute cellml:name found in extension element',
    # 2.4.3 cellml elements cannot contain cmeta attributes other than cmeta:id
    '2.4.3.bad_cmeta_attribute_in_component':
        'Unexpected attribute cmeta:bob',
    '2.4.3.bad_cmeta_attribute_in_component_ref':
        'Unexpected attribute cmeta:bob',
    '2.4.3.bad_cmeta_attribute_in_connection':
        'Unexpected attribute cmeta:bob',
    '2.4.3.bad_cmeta_attribute_in_group':
        'Unexpected attribute cmeta:bob',
    '2.4.3.bad_cmeta_attribute_in_map_components':
        'Unexpected attribute cmeta:bob',
    '2.4.3.bad_cmeta_attribute_in_map_variables':
        'Unexpected attribute cmeta:bob',
    '2.4.3.bad_cmeta_attribute_in_model':
        'Unexpected attribute cmeta:bob',
    '2.4.3.bad_cmeta_attribute_in_relationship_ref':
        'Unexpected attribute cmeta:bob',
    '2.4.3.bad_cmeta_attribute_in_unit':
        'Unexpected attribute cmeta:bob',
    '2.4.3.bad_cmeta_attribute_in_units_1':
        'Unexpected attribute cmeta:bob',
    '2.4.3.bad_cmeta_attribute_in_units_2':
        'Unexpected attribute cmeta:bob',
    '2.4.3.bad_cmeta_attribute_in_variable':
        'Unexpected attribute cmeta:bob',
    # 2.4.3 cellml elements cannot contain rdf elements other than rdf:RDF
    '2.4.3.bad_rdf_element_in_component':
        'found element of type rdf:Description',
    '2.4.3.bad_rdf_element_in_component_ref':
        'found element of type rdf:Description',
    '2.4.3.bad_rdf_element_in_connection':
        'found element of type rdf:Description',
    '2.4.3.bad_rdf_element_in_group':
        'found element of type rdf:Description',
    '2.4.3.bad_rdf_element_in_map_components':
        'found element of type rdf:Description',
    '2.4.3.bad_rdf_element_in_map_variables':
        'found element of type rdf:Description',
    '2.4.3.bad_rdf_element_in_model':
        'found element of type rdf:Description',
    '2.4.3.bad_rdf_element_in_relationship_ref':
        'found element of type rdf:Description',
    '2.4.3.bad_rdf_element_in_unit':
        'found element of type rdf:Description',
    '2.4.3.bad_rdf_element_in_units_1':
        'found element of type rdf:Description',
    '2.4.3.bad_rdf_element_in_units_2':
        'found element of type rdf:Description',
    '2.4.3.bad_rdf_element_in_variable':
        'found element of type rdf:Description',
    # 2.4.3 cellml elements cannot contain cmeta elements
    '2.4.3.cmeta_element_in_component':
        'found element of type cmeta:species',
    '2.4.3.cmeta_element_in_component_ref':
        'found element of type cmeta:species',
    '2.4.3.cmeta_element_in_connection':
        'found element of type cmeta:species',
    '2.4.3.cmeta_element_in_group':
        'found element of type cmeta:species',
    '2.4.3.cmeta_element_in_map_components':
        'found element of type cmeta:species',
    '2.4.3.cmeta_element_in_map_variables':
        'found element of type cmeta:species',
    '2.4.3.cmeta_element_in_model':
        'found element of type cmeta:species',
    '2.4.3.cmeta_element_in_relationship_ref':
        'found element of type cmeta:species',
    '2.4.3.cmeta_element_in_unit':
        'found element of type cmeta:species',
    '2.4.3.cmeta_element_in_units_1':
        'found element of type cmeta:species',
    '2.4.3.cmeta_element_in_units_2':
        'found element of type cmeta:species',
    '2.4.3.cmeta_element_in_variable':
        'found element of type cmeta:species',
    # 2.4.3 cellml elements cannot have mathml attributes
    '2.4.3.mathml_attribute_in_component':
        'Unexpected attribute mathml:sum',
    '2.4.3.mathml_attribute_in_component_ref':
        'Unexpected attribute mathml:sum',
    '2.4.3.mathml_attribute_in_connection':
        'Unexpected attribute mathml:sum',
    '2.4.3.mathml_attribute_in_group':
        'Unexpected attribute mathml:sum',
    '2.4.3.mathml_attribute_in_map_components':
        'Unexpected attribute mathml:sum',
    '2.4.3.mathml_attribute_in_map_variables':
        'Unexpected attribute mathml:sum',
    '2.4.3.mathml_attribute_in_model':
        'Unexpected attribute mathml:sum',
    '2.4.3.mathml_attribute_in_relationship_ref':
        'Unexpected attribute mathml:sum',
    '2.4.3.mathml_attribute_in_unit':
        'Unexpected attribute mathml:sum',
    '2.4.3.mathml_attribute_in_units_1':
        'Unexpected attribute mathml:sum',
    '2.4.3.mathml_attribute_in_units_2':
        'Unexpected attribute mathml:sum',
    '2.4.3.mathml_attribute_in_variable':
        'Unexpected attribute mathml:sum',
    # 2.4.3 cellml elements cannot have rdf attributes
    '2.4.3.rdf_attribute_in_component':
        'Unexpected attribute rdf:parseType',
    '2.4.3.rdf_attribute_in_component_ref':
        'Unexpected attribute rdf:parseType',
    '2.4.3.rdf_attribute_in_connection':
        'Unexpected attribute rdf:parseType',
    '2.4.3.rdf_attribute_in_group':
        'Unexpected attribute rdf:parseType',
    '2.4.3.rdf_attribute_in_map_components':
        'Unexpected attribute rdf:parseType',
    '2.4.3.rdf_attribute_in_map_variables':
        'Unexpected attribute rdf:parseType',
    '2.4.3.rdf_attribute_in_model':
        'Unexpected attribute rdf:parseType',
    '2.4.3.rdf_attribute_in_relationship_ref':
        'Unexpected attribute rdf:parseType',
    '2.4.3.rdf_attribute_in_unit':
        'Unexpected attribute rdf:parseType',
    '2.4.3.rdf_attribute_in_units_1':
        'Unexpected attribute rdf:parseType',
    '2.4.3.rdf_attribute_in_units_2':
        'Unexpected attribute rdf:parseType',
    '2.4.3.rdf_attribute_in_variable':
        'Unexpected attribute rdf:parseType',

    # 2.4.4 Text in CellML elements
    '2.4.4.text_in_component':
        'Text found in cellml:component',
    '2.4.4.text_in_component_ref':
        'Text found in cellml:component_ref',
    '2.4.4.text_in_connection':
        'Text found in cellml:connection',
    '2.4.4.text_in_group':
        'Text found in cellml:group',
    '2.4.4.text_in_map_components':
        'Text found in cellml:map_components',
    '2.4.4.text_in_map_variables':
        'Text found in cellml:map_variables',
    '2.4.4.text_in_model':
        'Text found in cellml:model',
    '2.4.4.text_in_relationship_ref':
        'Text found in cellml:relationship_ref',
    '2.4.4.text_in_unit':
        'Text found in cellml:unit',
    '2.4.4.text_in_units_1':
        'Text found in cellml:units',
    '2.4.4.text_in_units_2':
        'Text found in cellml:units',
    '2.4.4.text_in_variable':
        'Text found in cellml:variable',
    # 2.5.1 Identifiers are case sensitive
    '2.5.1.identifiers_are_case_sensitive':
        'must refer to a component in the current model',
    # 2.5.2 Attributes in the CellML namespace
    '2.5.2.attribute_in_cellml_namespace':
        'Unexpected attribute cellml:private_interface',
    # 2.5.3 Extension namespaces again
    # 3.4.1.1 Models contain only units, component, group, connection
    '3.4.1.1.model_with_component_ref':
        'found element of type cellml:component_ref',
    '3.4.1.1.model_with_map_components':
        'found element of type cellml:map_components',
    '3.4.1.1.model_with_map_variables':
        'found element of type cellml:map_variables',
    '3.4.1.1.model_with_math':
        'found element of type mathml:math',
    '3.4.1.1.model_with_model':
        'found element of type cellml:model',
    '3.4.1.1.model_with_reaction':
        'found element of type cellml:reaction',
    '3.4.1.1.model_with_relationship_ref':
        'found element of type cellml:relationship_ref',
    '3.4.1.1.model_with_role':
        'found element of type cellml:role',
    '3.4.1.1.model_with_unit':
        'found element of type cellml:unit',
    '3.4.1.1.model_with_variable_ref':
        'found element of type cellml:variable_ref',
    '3.4.1.1.model_with_variable':
        'found element of type cellml:variable',
    # 3.4.1.1 Models must have a name
    '3.4.1.1.model_name_missing':
        'must have a name attribute',
    # 3.4.1.2 A model name must be a valid identifier
    '3.4.1.2.model_name_invalid':
        'Model name must be a valid CellML identifier',
    # 3.4.2.1 Components must have a name
    '3.4.2.1.component_name_missing':
        'Component element must have a name attribute',
    # 3.4.2.1 Components contain only units, variable, reaction, math
    '3.4.2.1.component_with_component':
        'found element of type cellml:component',
    '3.4.2.1.component_with_component_ref':
        'found element of type cellml:component_ref',
    '3.4.2.1.component_with_connection':
        'found element of type cellml:connection',
    '3.4.2.1.component_with_group':
        'found element of type cellml:group',
    '3.4.2.1.component_with_map_components':
        'found element of type cellml:map_components',
    '3.4.2.1.component_with_map_variables':
        'found element of type cellml:map_variables',
    '3.4.2.1.component_with_model':
        'found element of type cellml:model',
    '3.4.2.1.component_with_relationship_ref':
        'found element of type cellml:relationship_ref',
    '3.4.2.1.component_with_role':
        'found element of type cellml:role',
    '3.4.2.1.component_with_unit':
        'found element of type cellml:unit',
    '3.4.2.1.component_with_variable_ref':
        'found element of type cellml:variable_ref',
    # 3.4.2.2 Component names must be unique
    '3.4.2.2.component_name_duplicate':
        'Component name must be unique',
    # 3.4.2.2 A component name must be a valid identifier
    '3.4.2.2.component_name_invalid':
        'Component name must be a valid CellML identifier',
    # 3.4.3.1 Variables can't contain any elements
    '3.4.3.1.variable_with_component':
        'found element of type cellml:component',
    '3.4.3.1.variable_with_component_ref':
        'found element of type cellml:component_ref',
    '3.4.3.1.variable_with_connection':
        'found element of type cellml:connection',
    '3.4.3.1.variable_with_group':
        'found element of type cellml:group',
    '3.4.3.1.variable_with_map_components':
        'found element of type cellml:map_components',
    '3.4.3.1.variable_with_map_variables':
        'found element of type cellml:map_variables',
    '3.4.3.1.variable_with_math':
        'found element of type mathml:math',
    '3.4.3.1.variable_with_model':
        'found element of type cellml:model',
    '3.4.3.1.variable_with_reaction':
        'found element of type cellml:reaction',
    '3.4.3.1.variable_with_relationship_ref':
        'found element of type cellml:relationship_ref',
    '3.4.3.1.variable_with_role':
        'found element of type cellml:role',
    '3.4.3.1.variable_with_unit':
        'found element of type cellml:unit',
    '3.4.3.1.variable_with_units':
        'found element of type cellml:units',
    '3.4.3.1.variable_with_variable':
        'found element of type cellml:variable',
    '3.4.3.1.variable_with_variable_ref':
        'found element of type cellml:variable_ref',
    # 3.4.3.1 Variables must have a name attribute
    '3.4.3.1.variable_name_missing':
        'Variable element must have a name attribute',
    # 3.4.3.1 Variables must have a units attribute
    '3.4.3.1.variable_units_missing':
        'Variable element must have a units attribute',
    # 3.4.3.2 A variable name must be an identifier
    '3.4.3.2.variable_name_invalid':
        'Variable name must be a valid CellML identifier',
    # 3.4.3.2 A variable name must be unique with the component
    '3.4.3.2.variable_name_duplicate':
        'Variable name must be unique',
    # 3.4.3.3 A variable must reference known units
    '3.4.3.3.variable_units_unknown':
        'must reference a units element',
    # 3.4.3.3 A variable cannot reference another component's units
    '3.4.3.3.variable_units_other_component':
        'must reference a units element',
    # 3.4.3.4 A public interface must be one of in/out/none
    '3.4.3.4.variable_interface_public_invalid':
        'Public interface must be',
    # 3.4.3.5 A private interface must be one of in/out/none
    '3.4.3.5.variable_interface_private_invalid':
        'Private interface must be',
    # 3.4.3.6 The private and public interface can't both be in
    '3.4.3.6.variable_interfaces_both_in':
        'can not both be "in"',
    # 3.4.3.7 The initial value (if present) must be a real number
    '3.4.3.7.variable_initial_value_empty':
        'initial_value must be a real number',
    '3.4.3.7.variable_initial_value_invalid':
        'initial_value must be a real number',
    # 3.4.3.8 A variable can't have an initial value and an "in" interface
    '3.4.3.8.variable_interfaces_private_in_and_initial':
        'initial value cannot be set',
    '3.4.3.8.variable_interfaces_public_in_and_initial':
        'initial value cannot be set',
    # 3.4.4.1 A connection must contain exactly one map_components
    '3.4.4.1.connection_map_components_missing':
        'exactly one map_components',
    '3.4.4.1.connection_map_components_multiple':
        'exactly one map_components',
    # 3.4.4.1 A component must contain at least one map_variables
    '3.4.4.1.connection_map_variables_missing_1':
        'at least one map_variables',
    '3.4.4.1.connection_map_variables_missing_2':
        'at least one map_variables',
    # 3.4.4.1 A connection must have map_components and map_variables
    '3.4.4.1.connection_only_extensions':
        'exactly one map_components',
    '3.4.4.1.connection_with_math':
        'found element of type mathml:math',
    '3.4.4.1.connection_empty':
        'exactly one map_component',
    # 3.4.4.1 A connection cannot have attributes
    '3.4.4.1.connection_with_name_attribute':
        'Unexpected attribute name',
    # 3.4.4.1 A connection can only contain map_components and map_variables
    '3.4.4.1.connection_with_component':
        'found element of type cellml:component',
    '3.4.4.1.connection_with_component_ref':
        'found element of type cellml:component_ref',
    '3.4.4.1.connection_with_connection':
        'found element of type cellml:connection',
    '3.4.4.1.connection_with_group':
        'found element of type cellml:group',
    '3.4.4.1.connection_with_map_components':
        'found element of type cellml:map_components',
    '3.4.4.1.connection_with_map_variables':
        'found element of type cellml:map_variables',
    '3.4.4.1.connection_with_model':
        'found element of type cellml:model',
    '3.4.4.1.connection_with_reaction':
        'found element of type cellml:reaction',
    '3.4.4.1.connection_with_relationship_ref':
        'found element of type cellml:relationship_ref',
    '3.4.4.1.connection_with_role':
        'found element of type cellml:role',
    '3.4.4.1.connection_with_unit':
        'found element of type cellml:unit',
    '3.4.4.1.connection_with_units':
        'found element of type cellml:units',
    '3.4.4.1.connection_with_variable_ref':
        'found element of type cellml:variable_ref',
    '3.4.4.1.connection_with_variable':
        'found element of type cellml:variable',
    # 3.4.5.1 A map_components must declare component_1 and component_2
    '3.4.5.1.map_components_component_1_missing':
        'must define a component_1 attribute',
    '3.4.5.1.map_components_component_2_missing':
        'must define a component_2 attribute',
    # 3.4.5.1 A map_components cannot have cellml children or math
    '3.4.5.1.map_components_with_component':
        'found element of type cellml:component',
    '3.4.5.1.map_components_with_component_ref':
        'found element of type cellml:component_ref',
    '3.4.5.1.map_components_with_connection':
        'found element of type cellml:connection',
    '3.4.5.1.map_components_with_group':
        'found element of type cellml:group',
    '3.4.5.1.map_components_with_map_components':
        'found element of type cellml:map_components',
    '3.4.5.1.map_components_with_map_variables':
        'found element of type cellml:map_variables',
    '3.4.5.1.map_components_with_math':
        'found element of type mathml:math',
    '3.4.5.1.map_components_with_model':
        'found element of type cellml:model',
    '3.4.5.1.map_components_with_reaction':
        'found element of type cellml:reaction',
    '3.4.5.1.map_components_with_relationship_ref':
        'found element of type cellml:relationship_ref',
    '3.4.5.1.map_components_with_role':
        'found element of type cellml:role',
    '3.4.5.1.map_components_with_unit':
        'found element of type cellml:unit',
    '3.4.5.1.map_components_with_units':
        'found element of type cellml:units',
    '3.4.5.1.map_components_with_variable':
        'found element of type cellml:variable',
    '3.4.5.1.map_components_with_variable_ref':
        'found element of type cellml:variable_ref',
    # 3.4.5.2 component_1 must refer to an existing component
    '3.4.5.2.map_components_component_1_nonexistent':
        'component_1 attribute must refer to a component in the current model',
    # 3.4.5.3 component_2 must refer to an existing component
    '3.4.5.3.map_components_component_2_nonexistent':
        'component_2 attribute must refer to a component in the current model',
    # 3.4.5.4 component_1 cannot match component_2
    '3.4.5.4.map_components_component_1_equals_2':
        'must be different',
    # 3.4.5.4 Each map_components in a model must be unique
    '3.4.5.4.map_components_duplicate':
        'Each connection in a model must connect a unique pair',
    '3.4.5.4.map_components_duplicate_mirrored':
        'Each connection in a model must connect a unique pair',
    # 3.4.6.1 A map_variables must declare variable_1 and variable_2
    '3.4.6.1.map_variables_variable_1_missing':
        'must define a variable_1 attribute',
    '3.4.6.1.map_variables_variable_2_missing':
        'must define a variable_2 attribute',
    # Duplicate connections are not allowed
    '3.4.6.1.map_variables_duplicate_1':
        'already connected',
    '3.4.6.1.map_variables_duplicate_2':
        'already connected',
    # 3.4.6.1 A map_variables cannot have cellml children or math
    '3.4.6.1.map_variables_with_component':
        'found element of type cellml:component',
    '3.4.6.1.map_variables_with_component_ref':
        'found element of type cellml:component_ref',
    '3.4.6.1.map_variables_with_connection':
        'found element of type cellml:connection',
    '3.4.6.1.map_variables_with_group':
        'found element of type cellml:group',
    '3.4.6.1.map_variables_with_map_components':
        'found element of type cellml:map_components',
    '3.4.6.1.map_variables_with_map_variables':
        'found element of type cellml:map_variables',
    '3.4.6.1.map_variables_with_math':
        'found element of type mathml:math',
    '3.4.6.1.map_variables_with_model':
        'found element of type cellml:model',
    '3.4.6.1.map_variables_with_reaction':
        'found element of type cellml:reaction',
    '3.4.6.1.map_variables_with_relationship_ref':
        'found element of type cellml:relationship_ref',
    '3.4.6.1.map_variables_with_role':
        'found element of type cellml:role',
    '3.4.6.1.map_variables_with_unit':
        'found element of type cellml:unit',
    '3.4.6.1.map_variables_with_units':
        'found element of type cellml:units',
    '3.4.6.1.map_variables_with_variable':
        'found element of type cellml:variable',
    '3.4.6.1.map_variables_with_variable_ref':
        'found element of type cellml:variable_ref',
    # 3.4.6.2 variable_1 must refer to an existing variable in component_1
    '3.4.6.2.map_variables_variable_1_nonexistent':
        'variable_1 attribute must refer to a variable',
    # 3.4.6.3 variable_2 must refer to an existing variable in component_2
    '3.4.6.3.map_variables_variable_2_nonexistent':
        'variable_2 attribute must refer to a variable',
    # 3.4.6.4 Interfaces and encapsulation
    '3.4.6.4.map_variables_child_multiple_out_1':
        'already connected',
    '3.4.6.4.map_variables_child_multiple_out_2':
        'already connected',
    '3.4.6.4.map_variables_child_out_to_out_1':
        'private_interface of "out", while',
    '3.4.6.4.map_variables_child_out_to_out_2':
        'private_interface of "out", while',
    '3.4.6.4.map_variables_child_private_in':
        'public_interface of "none"',
    '3.4.6.4.map_variables_child_private_out':
        'public_interface of "none"',
    '3.4.6.4.map_variables_hidden_aunt_1':
        'between components that are siblings or have a parent-child',
    '3.4.6.4.map_variables_hidden_aunt_2':
        'between components that are siblings or have a parent-child',
    '3.4.6.4.map_variables_hidden_cousins_1':
        'between components that are siblings or have a parent-child',
    '3.4.6.4.map_variables_hidden_cousins_2':
        'between components that are siblings or have a parent-child',
    '3.4.6.4.map_variables_hidden_cousins_3':
        'between components that are siblings or have a parent-child',
    '3.4.6.4.map_variables_hidden_cousins_4':
        'between components that are siblings or have a parent-child',
    '3.4.6.4.map_variables_hidden_grandchild_1':
        'between components that are siblings or have a parent-child',
    '3.4.6.4.map_variables_hidden_grandchild_2':
        'between components that are siblings or have a parent-child',
    '3.4.6.4.map_variables_hidden_grandparent_1':
        'between components that are siblings or have a parent-child',
    '3.4.6.4.map_variables_hidden_grandparent_2':
        'between components that are siblings or have a parent-child',
    '3.4.6.4.map_variables_hidden_niece_1':
        'between components that are siblings or have a parent-child',
    '3.4.6.4.map_variables_hidden_niece_2':
        'between components that are siblings or have a parent-child',
    '3.4.6.4.map_variables_nested_sibling_private_in':
        'public_interface of "none"',
    '3.4.6.4.map_variables_nested_sibling_private_in_and_out':
        'public_interface of "none"',
    '3.4.6.4.map_variables_nested_sibling_private_out':
        'public_interface of "none"',
    '3.4.6.4.map_variables_parent_in_to_in_1':
        'public_interface of "in"',
    '3.4.6.4.map_variables_parent_in_to_in_2':
        'public_interface of "in"',
    '3.4.6.4.map_variables_parent_multiple_out':
        'already connected',
    '3.4.6.4.map_variables_parent_out_to_out_1':
        'public_interface of "out"',
    '3.4.6.4.map_variables_parent_out_to_out_2':
        'public_interface of "out"',
    '3.4.6.4.map_variables_parent_public_in':
        'private_interface of "none"',
    '3.4.6.4.map_variables_parent_public_out':
        'private_interface of "none"',
    '3.4.6.4.map_variables_sibling_in_to_in':
        'public_interface of "in"',
    '3.4.6.4.map_variables_sibling_multiple_out_1':
        'already connected',
    '3.4.6.4.map_variables_sibling_multiple_out_2':
        'already connected',
    '3.4.6.4.map_variables_sibling_out_to_out':
        'public_interface of "out"',
    '3.4.6.4.map_variables_sibling_private_in_1':
        'public_interface of "out"',
    '3.4.6.4.map_variables_sibling_private_in_2':
        'public_interface of "out"',
    '3.4.6.4.map_variables_sibling_private_in_and_out':
        'public_interface of "none"',
    '3.4.6.4.map_variables_sibling_private_out_1':
        'public_interface of "none"',
    '3.4.6.4.map_variables_sibling_private_out_2':
        'public_interface of "in"',
    # 4.4.1 Bad math
    '4.4.1.math_not_math_component':
        'Unsupported element',
    # 4.4.2 Ci can only refer to local variables
    '4.4.2.ci_nonexistent':
        'references in equation must name a variable from the local component',
    '4.4.2.ci_non_local_aunt':
        'references in equation must name a variable from the local component',
    '4.4.2.ci_non_local_child':
        'references in equation must name a variable from the local component',
    '4.4.2.ci_non_local_cousin':
        'references in equation must name a variable from the local component',
    '4.4.2.ci_non_local_nested_sibling':
        'references in equation must name a variable from the local component',
    '4.4.2.ci_non_local_niece':
        'references in equation must name a variable from the local component',
    '4.4.2.ci_non_local_parent':
        'references in equation must name a variable from the local component',
    '4.4.2.ci_non_local_sibling':
        'references in equation must name a variable from the local component',
    # 4.4.3.1 A cn must have a cellml:units
    '4.4.3.1.cn_units_missing':
        'must define a cellml:units attribute',
    # 4.4.3.2 A cn unit attribute must refer to a model, local component, or
    #         predefined unit
    '4.4.3.2.cn_units_nonexistent_1':
        'Unknown unit',
    '4.4.3.2.cn_units_nonexistent_2':
        'Unknown unit',
    '4.4.3.2.cn_units_parent_component':
        'Unknown unit',
    # 4.4.4 A mathml:math can only modify 'owned' variables
    '4.4.4.modify_nonexistent':
        'references in equation must name a variable from the local component',
    # 4.4.4 A mathml:math can only modify 'owned' variables
    '4.4.4.modify_private_in':
        'which has private_interface="in"',
    '4.4.4.modify_public_in':
        'which has public_interface="in"',
    # 4 Math can't be overdefined
    '4.math_and_initial_value':
        'appear on a left-hand side once',
    '4.math_overdefined':
        'appear on a left-hand side once',
    # 5.4.1.1 Unitses must have a name
    '5.4.1.1.units_name_missing':
        'Units element must have a name attribute',
    # 5.4.1.1 A units with base_units="no" probably should have children
    '5.4.1.1.units_empty_1': 'at least one child unit element',
    '5.4.1.1.units_empty_2': 'at least one child unit element',
    # 5.4.1.1 A units can only contain unit elements
    '5.4.1.1.units_with_component':
        'found element of type cellml:component',
    '5.4.1.1.units_with_component_ref':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_connection':
        'found element of type cellml:connection',
    '5.4.1.1.units_with_group':
        'found element of type cellml:group',
    '5.4.1.1.units_with_map_components':
        'found element of type cellml:map_components',
    '5.4.1.1.units_with_map_variables':
        'found element of type cellml:map_variables',
    '5.4.1.1.units_with_math':
        'found element of type mathml:math',
    '5.4.1.1.units_with_model':
        'found element of type cellml:model',
    '5.4.1.1.units_with_reaction':
        'found element of type cellml:reaction',
    '5.4.1.1.units_with_relationship_ref':
        'found element of type cellml:relationship_ref',
    '5.4.1.1.units_with_role':
        'found element of type cellml:role',
    '5.4.1.1.units_with_units':
        'found element of type cellml:units',
    '5.4.1.1.units_with_variable':
        'found element of type cellml:variable',
    '5.4.1.1.units_with_variable_ref':
        'found element of type cellml:variable_ref',
    # 5.4.1.2 A units name must be a valid identifier
    '5.4.1.2.units_name_invalid':
        'Units name must be a valid CellML identifier',
    # 5.4.1.2 Units names must be unique (within model or local component)
    '5.4.1.2.units_name_duplicate_1':
        'Duplicate units definition',
    '5.4.1.2.units_name_duplicate_2':
        'Duplicate units definition',
    # 5.4.1.2 Units names cannot overlap with predefined ones
    '5.4.1.2.units_name_predefined_ampere':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_becquerel':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_candela':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_celsius':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_coulomb':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_dimensionless':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_farad':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_gram':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_gray':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_henry':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_hertz':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_joule':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_katal':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_kelvin':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_kilogram':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_liter':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_litre':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_lumen':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_lux':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_meter':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_metre':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_mole':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_newton':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_ohm':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_pascal':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_radian':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_second':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_siemens':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_sievert':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_steradian':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_tesla':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_volt':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_watt':
        'overlaps with a predefined name',
    '5.4.1.2.units_name_predefined_weber':
        'overlaps with a predefined name',
    # 5.4.1.2 Component units names cannot overlap with predefined ones
    '5.4.1.2.units_name_predefined_component_ampere':
        'overlaps with a predefined name',
    # 5.4.1.3 Units base_units attribute can only be yes or no
    '5.4.1.3.units_base_units_invalid':
        'Base units attribute must be either',
    # 5.4.2.1 A unit must have a units attribute
    '5.4.2.1.unit_units_missing':
        'must have a units attribute',
    # 5.4.2.1 A unit cannot have CellML children
    '5.4.2.1.unit_with_component':
        'found element of type cellml:component',
    '5.4.2.1.unit_with_component_ref':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_connection':
        'found element of type cellml:connection',
    '5.4.2.1.unit_with_group':
        'found element of type cellml:group',
    '5.4.2.1.unit_with_map_components':
        'found element of type cellml:map_components',
    '5.4.2.1.unit_with_map_variables':
        'found element of type cellml:map_variables',
    '5.4.2.1.unit_with_math':
        'found element of type mathml:math',
    '5.4.2.1.unit_with_model':
        'found element of type cellml:model',
    '5.4.2.1.unit_with_reaction':
        'found element of type cellml:reaction',
    '5.4.2.1.unit_with_relationship_ref':
        'found element of type cellml:relationship_ref',
    '5.4.2.1.unit_with_role':
        'found element of type cellml:role',
    '5.4.2.1.unit_with_unit':
        'found element of type cellml:unit',
    '5.4.2.1.unit_with_units':
        'found element of type cellml:units',
    '5.4.2.1.unit_with_variable':
        'found element of type cellml:variable',
    '5.4.2.1.unit_with_variable_ref':
        'found element of type cellml:variable_ref',
    # 5.4.2.2 A unit cannot refer to itself directly or indirectly
    '5.4.2.2.unit_cycle_1':
        'Unable to resolve network of units',
    '5.4.2.2.unit_cycle_2':
        'Unable to resolve network of units',
    '5.4.2.2.unit_cycle_3':
        'Unable to resolve network of units',
    # 5.4.2.2 A unit must refer to an existing units
    '5.4.2.2.unit_units_invalid':
        'Unable to resolve network of units',
    # 5.4.2.3 Allowed values of the prefix attribute
    '5.4.2.3.unit_prefix_real':
        'Units prefix must be a string from the list of known prefixes or',
    '5.4.2.3.unit_prefix_spaces':
        'Units prefix must be a string from the list of known prefixes or',
    '5.4.2.3.unit_prefix_unknown':
        'Units prefix must be a string from the list of known prefixes or',
    # 5.4.2.4 A unit exponent must be a real number
    '5.4.2.4.unit_exponent_invalid':
        'Unit exponent must be a real number',
    # 5.4.2.5 A unit multiplier must be a real number
    '5.4.2.5.unit_multiplier_invalid':
        'Unit multiplier must be a real number',
    # 5.4.2.6 A unit offset must be a real number
    '5.4.2.6.unit_offset_invalid':
        'Unit offset must be a real number',
    # 6.4.1.1 A group must have at least one component_ref
    '6.4.1.1.group_component_ref_missing_1':
        'Group must contain at least one component_ref',
    '6.4.1.1.group_component_ref_missing_2':
        'Group must contain at least one component_ref',
    # 6.4.1.1 A group must have at least one relationship_ref
    '6.4.1.1.group_relationship_ref_missing_1':
        'Group must contain at least one relationship_ref',
    '6.4.1.1.group_relationship_ref_missing_2':
        'Group must contain at least one relationship_ref',
    # 6.4.1.1 A group cannot be empty (extra test for missing comp_ref/rel_ref)
    '6.4.1.1.group_empty':
        'Group must contain at least one component_ref',
    '6.4.1.1.group_only_extensions':
        'Group must contain at least one component_ref',
    # 6.4.1.1 A group can only contain component_refs and relationship_refs
    '6.4.1.1.group_with_component':
        'found element of type cellml:component',
    '6.4.1.1.group_with_component_ref':
        'found element of type cellml:component_ref',
    '6.4.1.1.group_with_connection':
        'found element of type cellml:connection',
    '6.4.1.1.group_with_group':
        'found element of type cellml:group',
    '6.4.1.1.group_with_map_components':
        'found element of type cellml:map_components',
    '6.4.1.1.group_with_map_variables':
        'found element of type cellml:map_variables',
    '6.4.1.1.group_with_math':
        'found element of type mathml:math',
    '6.4.1.1.group_with_model':
        'found element of type cellml:model',
    '6.4.1.1.group_with_reaction':
        'found element of type cellml:reaction',
    '6.4.1.1.group_with_relationship_ref':
        'found element of type cellml:relationship_ref',
    '6.4.1.1.group_with_role':
        'found element of type cellml:role',
    '6.4.1.1.group_with_unit':
        'found element of type cellml:unit',
    '6.4.1.1.group_with_units':
        'found element of type cellml:units',
    '6.4.1.1.group_with_variable_ref':
        'found element of type cellml:variable_ref',
    '6.4.1.1.group_with_variable':
        'found element of type cellml:variable',
    # 6.4.2.1 A relationship_ref must define a relationship - although it can
    #         be either namespaceless, or in any extension namespace!
    '6.4.2.1.relationship_ref_relationship_missing':
        'Relationship_ref must define a relationship attribute',
    # 6.4.2.1 A relationship_ref cannot have any CellML children
    '6.4.2.1.relationship_ref_with_component':
        'found element of type cellml:component',
    '6.4.2.1.relationship_ref_with_component_ref':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_connection':
        'found element of type cellml:connection',
    '6.4.2.1.relationship_ref_with_group':
        'found element of type cellml:group',
    '6.4.2.1.relationship_ref_with_map_components':
        'found element of type cellml:map_components',
    '6.4.2.1.relationship_ref_with_map_variables':
        'found element of type cellml:map_variables',
    '6.4.2.1.relationship_ref_with_math':
        'found element of type mathml:math',
    '6.4.2.1.relationship_ref_with_model':
        'found element of type cellml:model',
    '6.4.2.1.relationship_ref_with_reaction':
        'found element of type cellml:reaction',
    '6.4.2.1.relationship_ref_with_relationship_ref':
        'found element of type cellml:relationship_ref',
    '6.4.2.1.relationship_ref_with_role':
        'found element of type cellml:role',
    '6.4.2.1.relationship_ref_with_unit':
        'found element of type cellml:unit',
    '6.4.2.1.relationship_ref_with_units':
        'found element of type cellml:units',
    '6.4.2.1.relationship_ref_with_variable':
        'found element of type cellml:variable',
    '6.4.2.1.relationship_ref_with_variable_ref':
        'found element of type cellml:variable_ref',
    # 6.4.2.2 When not in a namespace, a relationship_ref's relationship must
    # be either containment or encapsulation.
    '6.4.2.2.relationship_ref_relationship_invalid':
        'Unknown relationship type',
    # 6.4.2.3 A relationship_ref name must be a cellml identifier
    '6.4.2.3.relationship_ref_name_invalid':
        'must be a valid CellML identifier',
    # 6.4.2.4 An encapsulation can not be named
    '6.4.2.4.relationship_ref_encapsulation_duplicate':
        'Encapsulation relationships may not define a name',
    '6.4.2.4.relationship_ref_encapsulation_named':
        'Encapsulation relationships may not define a name',
    # 6.4.2.5 name/relationship pairs must be unique
    '6.4.2.5.relationship_ref_duplicate_named':
        'must have a unique pair',
    '6.4.2.5.relationship_ref_duplicate_unnamed_1':
        'must have a unique pair',
    '6.4.2.5.relationship_ref_duplicate_unnamed_2':
        'must have a unique pair',
    # 6.4.3.1 A component_ref must define a component
    '6.4.3.1.component_ref_component_missing':
        'A component_ref must define a component attribute',
    # 6.4.3.1 A component_ref can only contain a component_ref
    '6.4.3.1.component_ref_with_component':
        'found element of type cellml:component',
    '6.4.3.1.component_ref_with_connection':
        'found element of type cellml:connection',
    '6.4.3.1.component_ref_with_group':
        'found element of type cellml:group',
    '6.4.3.1.component_ref_with_map_components':
        'found element of type cellml:map_components',
    '6.4.3.1.component_ref_with_map_variables':
        'found element of type cellml:map_variables',
    '6.4.3.1.component_ref_with_math':
        'found element of type mathml:math',
    '6.4.3.1.component_ref_with_model':
        'found element of type cellml:model',
    '6.4.3.1.component_ref_with_reaction':
        'found element of type cellml:reaction',
    '6.4.3.1.component_ref_with_relationship_ref':
        'found element of type cellml:relationship_ref',
    '6.4.3.1.component_ref_with_role':
        'found element of type cellml:role',
    '6.4.3.1.component_ref_with_unit':
        'found element of type cellml:unit',
    '6.4.3.1.component_ref_with_units':
        'found element of type cellml:units',
    '6.4.3.1.component_ref_with_variable':
        'found element of type cellml:variable',
    '6.4.3.1.component_ref_with_variable_ref':
        'found element of type cellml:variable_ref',
    # 6.4.3.2 The first component_ref in a containment must have children
    '6.4.3.2.component_ref_no_children_containment':
        'must have at least one child',
    # 6.4.3.2 The first component_ref in an encapsulation must have children
    '6.4.3.2.component_ref_no_children_encapsulation':
        'must have at least one child',
    '6.4.3.2.component_ref_cycle_5':
        'Encapsulation hierarchy cannot be circular',
    '6.4.3.2.component_ref_cycle_6':
        'Encapsulation hierarchy cannot be circular',
    '6.4.3.2.component_ref_cycle_7':
        'Encapsulation hierarchy cannot be circular',
    '6.4.3.2.component_ref_cycle_8':
        'Encapsulation hierarchy cannot be circular',
    # 6.4.3.2 A component cannot be named twice in a single hierarchy
    '6.4.3.2.component_ref_duplicate_child_3':
        'single encapsulation parent',
    '6.4.3.2.component_ref_duplicate_child_4':
        'single encapsulation parent',
    # 6.4.3.2 Encapsulation relationships cannot overlap
    '6.4.3.2.component_ref_overlapping_encapsulation':
        'can only have a single encapsulation parent',
    # 6.4.3.3 A component attribute must be an identifier
    '6.4.3.3.component_ref_component_invalid':
        'component attribute must reference a component in the same model',
    # 6.4.3.3 A component_ref must refer to an existing component
    '6.4.3.3.component_ref_component_nonexistent_1':
        'component attribute must reference a component in the same model',
    '6.4.3.3.component_ref_component_nonexistent_2':
        'component attribute must reference a component in the same model',
    # 8.4.1 cmeta:id attributes must have unique values
    '8.4.1.duplicate_cmeta_id_in_component':
        'Duplicate cmeta:id',
    '8.4.1.duplicate_cmeta_id_in_component_ref':
        'Duplicate cmeta:id',
    '8.4.1.duplicate_cmeta_id_in_connection':
        'Duplicate cmeta:id',
    '8.4.1.duplicate_cmeta_id_in_group':
        'Duplicate cmeta:id',
    '8.4.1.duplicate_cmeta_id_in_map_components':
        'Duplicate cmeta:id',
    '8.4.1.duplicate_cmeta_id_in_map_variables':
        'Duplicate cmeta:id',
    '8.4.1.duplicate_cmeta_id_in_model':
        'Duplicate cmeta:id',
    '8.4.1.duplicate_cmeta_id_in_relationship_ref':
        'Duplicate cmeta:id',
    '8.4.1.duplicate_cmeta_id_in_unit':
        'Duplicate cmeta:id',
    '8.4.1.duplicate_cmeta_id_in_units_1':
        'Duplicate cmeta:id',
    '8.4.1.duplicate_cmeta_id_in_units_2':
        'Duplicate cmeta:id',
    '8.4.1.duplicate_cmeta_id_in_variable':
        'Duplicate cmeta:id',
}


# Invalid models for which validation is not expected to pick up the (correct)
# error.
known_issues = {
    # Myokit accepts 'nan' and 'inf' as floats
    '0.1.real_number_invalid_7',
    '0.1.real_number_invalid_8',
    # Reactions are not supported
    # No reaction support
    '2.4.3.bad_cmeta_attribute_in_reaction',
    '2.4.3.bad_cmeta_attribute_in_role',
    '2.4.3.bad_cmeta_attribute_in_variable_ref',
    # No reaction support
    '2.4.3.bad_rdf_element_in_reaction',
    '2.4.3.bad_rdf_element_in_role',
    '2.4.3.bad_rdf_element_in_variable_ref',
    # No reaction support
    '2.4.3.cmeta_element_in_reaction',
    '2.4.3.cmeta_element_in_role',
    '2.4.3.cmeta_element_in_variable_ref',
    # No reaction support
    '2.4.3.mathml_attribute_in_reaction',
    '2.4.3.mathml_attribute_in_role',
    '2.4.3.mathml_attribute_in_variable_ref',
    # No reaction support
    '2.4.3.rdf_attribute_in_reaction',
    '2.4.3.rdf_attribute_in_role',
    '2.4.3.rdf_attribute_in_variable_ref',
    # Text in reactions is not detected
    '2.4.4.text_in_reaction',
    '2.4.4.text_in_role',
    '2.4.4.text_in_variable_ref',
    # Reactions
    '4.4.1.math_not_math_reaction',
    # DAEs
    '4.4.4.dae_public_in',
    # Myokit accepts both deca and deka
    '5.2.2.unit_deca',
    # New base units are not supported
    '5.4.1.1.units_base_units_with_children',
    # Myokit accepts integers in real notation
    '5.4.2.3.unit_prefix_real_int',
    '5.4.2.3.unit_prefix_e_notation_int',
    # Unit offsets are not supported
    '5.4.2.7.unit_offset_and_exponent',
    '5.4.2.7.unit_offset_and_siblings_1',
    '5.4.2.7.unit_offset_and_siblings_2',
    # Bad hierarchies are not detected for containment relationships
    '6.4.3.2.component_ref_cycle_1',
    '6.4.3.2.component_ref_cycle_2',
    '6.4.3.2.component_ref_cycle_3',
    '6.4.3.2.component_ref_cycle_4',
    '6.4.3.2.component_ref_duplicate_child_1',
    '6.4.3.2.component_ref_duplicate_child_2',
    # Myokit doesn't mind if relationships are spread over multiple groups
    '6.4.3.2.component_ref_children_declared_twice_1',
    '6.4.3.2.component_ref_children_declared_twice_2',
    '6.4.3.2.component_ref_children_declared_twice_3',
    # Reactions are not supported
    '7.4.1.1.reaction_variable_ref_missing',
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
    '7.4.1.2.reaction_reversible_invalid',
    '7.4.1.3.reaction_encapsulating_delta_variable',
    '7.4.2.1.variable_ref_role_missing',
    '7.4.2.1.variable_ref_variable_missing',
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
    '7.4.2.1.variable_ref_with_variable',
    '7.4.2.1.variable_ref_with_variable_ref',
    '7.4.2.2.variable_ref_variable_duplicate',
    '7.4.2.2.variable_ref_variable_hidden',
    '7.4.2.2.variable_ref_variable_nonexistent',
    '7.4.3.1.role_role_missing',
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
    '7.4.3.2.role_role_invalid',
    '7.4.3.3.reaction_multiple_rates',
    '7.4.3.3.role_rate_with_multiple_roles',
    '7.4.3.3.role_rate_with_delta_variable',
    '7.4.3.3.role_rate_with_stoichiometry',
    '7.4.3.4.role_direction_invalid',
    '7.4.3.5.role_direction_both_irreversible',
    '7.4.3.5.role_direction_reverse_irreversible',
    '7.4.3.5.role_direction_role_duplicate',
    '7.4.3.5.role_direction_both_rate',
    '7.4.3.5.role_direction_reverse_rate',
    '7.4.3.5.role_direction_both_reactant',
    '7.4.3.5.role_direction_reverse_reactant',
    '7.4.3.5.role_direction_both_product',
    '7.4.3.5.role_direction_reverse_product',
    '7.4.3.6.role_stoichiometry_invalid',
    '7.4.3.7.role_delta_variable_duplicate_1',
    '7.4.3.7.role_delta_variable_duplicate_2',
    '7.4.3.7.role_delta_variable_nonexistent_1',
    '7.4.3.7.role_delta_variable_nonexistent_2',
    '7.4.3.8.role_delta_variable_activator',
    '7.4.3.8.role_delta_variable_catalyst',
    '7.4.3.8.role_delta_variable_inhibitor',
    '7.4.3.8.role_delta_variable_modifier',
    '7.4.3.8.role_delta_variable_without_rate_or_math',
    '7.4.3.8.role_delta_variable_with_rate_and_math',
    '7.4.3.8.role_delta_variable_with_stoichiometry_no_rate',
    '7.4.3.9.role_math_not_relevant',
    # Reactions
    '8.4.1.duplicate_cmeta_id_in_reaction',
    '8.4.1.duplicate_cmeta_id_in_role',
    '8.4.1.duplicate_cmeta_id_in_variable_ref',
}


@pytest.fixture
def log():
    """ Returns a logger object. """
    return logging.getLogger(__name__)


class TestMyokit(object):
    """ Tests Myokit validation. """

    @classmethod
    def setup_class(cls):
        cls._report = Report('Myokit - CellML 1.0')

    @classmethod
    def teardown_class(cls):
        cls._report.render(
            os.path.join(check.REPORT_DIR, 'myokit_1_0.md'))

    @pytest.mark.skipif(not myokit.supported(), reason='Myokit not found')
    @pytest.mark.parametrize(('name', 'path'), shared.list_passes_1_0())
    def test_valid_model(self, name, path, log):

        # Validate model
        with warnings.catch_warnings() as w:
            warnings.filterwarnings('ignore', module='myokit')
            ok, msg = myokit.parse(path)

        # Report
        if ok:
            self._report.valid_passed(name, path, msg)
        else:
            self._report.valid_failed(name, path, msg)

        # Check returned status
        if name in false_negatives:
            if ok:
                # Expected fail, but passed
                log.error('Unexpected pass for ' + name)
                log.error(msg)
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

    @pytest.mark.skipif(not myokit.supported, reason='Myokit not found')
    @pytest.mark.parametrize(('name', 'path'), shared.list_fails_1_0())
    def test_invalid_model(self, name, path, log):

        # See if there's an expected error for this model
        expected_error = expected_messages.get(name, None)
        expected_issue = name in known_issues

        # Validate model
        ok, msg = myokit.parse(path)

        if ok:
            self._report.invalid_passed(name, path, expected_error, msg)

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
                self._report.invalid_failed_incorrectly(
                    name, path, 'Expected error not set', msg)

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
                    self._report.invalid_failed(
                        name, path, expected_error, msg)
                else:
                    # Expected error not found
                    self._report.invalid_failed_incorrectly(
                        name, path, expected_error, msg)

                    if expected_issue:
                        # But we knew this would happen?
                        pytest.xfail()
                    else:
                        log.error('Unexpected error in ' + name)
                        log.error(msg)
                        log.error('Expected error: ' + expected_error)
                        pytest.fail()


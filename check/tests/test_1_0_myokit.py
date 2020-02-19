#
# Tests CellML 1.0 validation with Myokit (CellML revamp)
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import logging
import os
import pytest

import check
from . import shared
from .report import Report_1_0 as Report

try:
    import myokit
    NO_MYOKIT = False
except ImportError:
    NO_MYOKIT = True

# Known instances where Myokit says a valid file is invalid
false_negatives = {
    # Myokit uses stricter rules for identifiers
    '2.4.1.valid_identifiers':
        'must be a valid CellML identifier',
    # No reaction support
    '2.4.3.reaction_with_extensions':
        'Reaction elements are not supported.',
    '2.4.3.role_with_extensions':
        'Reaction elements are not supported.',
    '2.4.3.variable_ref_with_extensions':
        'Reaction elements are not supported.',
    '3.4.2.1.component_child_order_1':
        'Reaction elements are not supported.',
    '3.4.2.1.component_child_order_2':
        'Reaction elements are not supported.',
    '3.4.2.1.component_with_one_reaction':
        'Reaction elements are not supported.',
    '3.4.2.1.component_with_reactions':
        'Reaction elements are not supported.',
    # Non-zero offsets are not supported
    '5.2.7.unit_conversion_dimensionless_offset':
        'non-zero offsets are not supported',
    '5.2.7.unit_conversion_offset':
        'non-zero offsets are not supported',
    # New base units are not supported
    '5.2.7.unit_conversion_new_base_units':
        'Defining new base units is not supported.',
    # New base units are not supported
    '5.4.1.1.units_base_units':
        'Defining new base units is not supported.',
    # Non-zero offsets are not supported
    '5.4.2.1.unit_offset_non_zero':
        'non-zero offsets are not supported',
    # Unit prefixes can't be too big for floats
    '5.4.2.1.unit_prefix_exponent_multiplier_huge':
        'Unit prefix too large',
    # Non-zero offsets are not supported
    '5.4.2.7.unit_offset_non_zero_and_exponent_one':
        'non-zero offsets are not supported.',
    # No reaction support
    '7.4.1.2.reaction_reversible_no':
        'Reaction elements are not supported.',
    '7.4.1.2.reaction_reversible_yes':
        'Reaction elements are not supported.',
    '7.4.3.reaction_all_roles_and_attributes':
        'Reaction elements are not supported.',
    '7.4.3.reaction_reversible_no':
        'Reaction elements are not supported.',
    '7.4.3.reaction_simple':
        'Reaction elements are not supported.',
    '8.4.1.cmeta_id_in_reaction':
        'Reaction elements are not supported.',
    '8.4.1.cmeta_id_in_role':
        'Reaction elements are not supported.',
    '8.4.1.cmeta_id_in_variable_ref':
        'Reaction elements are not supported.',
    '8.4.2.rdf_in_reaction':
        'Reaction elements are not supported.',
    '8.4.2.rdf_in_role':
        'Reaction elements are not supported.',
    '8.4.2.rdf_in_variable_ref':
        'Reaction elements are not supported.',
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
    '2.4.2.imaginary_elements':
        'found element of type cellml:fruit',
    # 2.4.3 Elements/attributes in extension namespaces
    '2.4.3.cellml_elements_inside_extensions':
        'CellML element cellml:component found inside extension element',
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
    ## 3.4.2.2 Component names must be unique
    '3.4.2.2.component_name_duplicate':
        'Component name must be unique',
    ## 3.4.2.2 A component name must be a valid identifier
    '3.4.2.2.component_name_invalid':
        'Component name must be a valid CellML identifier',
    ## 3.4.3.1 Variables can't contain any elements
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
        'found element of type cellml:math',
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
    #'3.4.6.2.map_variables_variable_1_nonexistent':
    #    'Variable_1 attribute doesn\'t refer to a valid variable',
    # 3.4.6.3 variable_2 must refer to an existing variable in component_2
    #'3.4.6.3.map_variables_variable_2_nonexistent':
    #    'Variable_2 attribute doesn\'t refer to a valid variable',
    # 3.4.6.4 Interfaces and encapsulation
    #'3.4.6.4.map_variables_child_multiple_out_1':
    #    'More than one connection to in interface of variable',
    #'3.4.6.4.map_variables_child_multiple_out_2':
    #    'More than one connection to in interface of variable',
    #'3.4.6.4.map_variables_child_out_to_out_1':
    #    'also has public interface of out',
    #'3.4.6.4.map_variables_child_out_to_out_2':
    #    'also has public interface of out',
    #'3.4.6.4.map_variables_child_private_in':
    #    'Mapping variable_2 which has public interface of none',
    #'3.4.6.4.map_variables_child_private_out':
    #    'Mapping variable_2 which has public interface of none',
    #'3.4.6.4.map_variables_hidden_aunt_1':
    #    'in the hidden set of each other',
    #'3.4.6.4.map_variables_hidden_aunt_2':
    #    'in the hidden set of each other',
    #'3.4.6.4.map_variables_hidden_cousins_1':
    #    'in the hidden set of each other',
    #'3.4.6.4.map_variables_hidden_cousins_2':
    #    'in the hidden set of each other',
    #'3.4.6.4.map_variables_hidden_cousins_3':
    #    'in the hidden set of each other',
    #'3.4.6.4.map_variables_hidden_cousins_4':
    #    'in the hidden set of each other',
    #'3.4.6.4.map_variables_hidden_grandchild_1':
    #    'in the hidden set of each other',
    #'3.4.6.4.map_variables_hidden_grandchild_2':
    #    'in the hidden set of each other',
    #'3.4.6.4.map_variables_hidden_grandparent_1':
    #    'in the hidden set of each other',
    #'3.4.6.4.map_variables_hidden_grandparent_2':
    #    'in the hidden set of each other',
    #'3.4.6.4.map_variables_hidden_niece_1':
    #    'in the hidden set of each other',
    #'3.4.6.4.map_variables_hidden_niece_2':
    #    'in the hidden set of each other',
    #'3.4.6.4.map_variables_nested_sibling_private_in':
    #    'public interface of none',
    #'3.4.6.4.map_variables_nested_sibling_private_in_and_out':
    #    'also has public interface of out',
    #'3.4.6.4.map_variables_nested_sibling_private_out':
    #    'public interface of none',
    #'3.4.6.4.map_variables_parent_in_to_in_1':
    #    'also has public interface of in',
    #'3.4.6.4.map_variables_parent_in_to_in_2':
    #    'also has public interface of in',
    #'3.4.6.4.map_variables_parent_multiple_out':
    #    'More than one connection to in interface of variable',
    #'3.4.6.4.map_variables_parent_out_to_out_1':
    #    'also has public interface of out',
    #'3.4.6.4.map_variables_parent_out_to_out_2':
    #    'also has public interface of out',
    #'3.4.6.4.map_variables_parent_public_in':
    #    'has private interface of none',
    #'3.4.6.4.map_variables_parent_public_out':
    #    'has private interface of none',
    #'3.4.6.4.map_variables_sibling_in_to_in':
    #    'also has public interface of in',
    #'3.4.6.4.map_variables_sibling_multiple_out_1':
    #    'More than one connection to in interface of variable',
    #'3.4.6.4.map_variables_sibling_multiple_out_2':
    #    'More than one connection to in interface of variable',
    #'3.4.6.4.map_variables_sibling_out_to_out':
    #    'also has public interface of out',
    #'3.4.6.4.map_variables_sibling_private_in_1':
    #    'public interface of none',
    #'3.4.6.4.map_variables_sibling_private_in_2':
    #    'also has public interface of out',
    #'3.4.6.4.map_variables_sibling_private_in_and_out':
    #    'public interface of none',
    #'3.4.6.4.map_variables_sibling_private_out_1':
    #    'public interface of none',
    #'3.4.6.4.map_variables_sibling_private_out_2':
    #    'also has public interface of in',
    # 4.4.1 Bad math
    #'4.4.1.math_not_math_component':
    #    'cake was not expected in this context',
    # 4.4.2 Ci can only refer to local variables
    #'4.4.2.ci_nonexistent':
    #    'ci element references variable which doesn\'t exist',
    #'4.4.2.ci_non_local_aunt':
    #    'ci element references variable which doesn\'t exist',
    #'4.4.2.ci_non_local_child':
    #    'ci element references variable which doesn\'t exist',
    #'4.4.2.ci_non_local_cousin':
    #    'ci element references variable which doesn\'t exist',
    #'4.4.2.ci_non_local_nested_sibling':
    #    'ci element references variable which doesn\'t exist',
    #'4.4.2.ci_non_local_niece':
    #    'ci element references variable which doesn\'t exist',
    #'4.4.2.ci_non_local_parent':
    #    'ci element references variable which doesn\'t exist',
    #'4.4.2.ci_non_local_sibling':
    #    'ci element references variable which doesn\'t exist',
    # 4.4.3.1 A cn must have a cellml:units
    #'4.4.3.1.cn_units_missing':
    #    'MathML cn elements must have CellML units attribute',
    # 4.4.3.2 A cn unit attribute must refer to a model, local component, or
    #         predefined unit
    #'4.4.3.2.cn_units_nonexistent_1':
    #    'MathML cn element has invalid units',
    #'4.4.3.2.cn_units_nonexistent_2':
    #    'MathML cn element has invalid units',
    #'4.4.3.2.cn_units_parent_component':
    #    'MathML cn element has invalid units',
    # 4.4.4 A mathml:math can only modify 'owned' variables
    #'4.4.4.modify_nonexistent':
    #    'ci element references variable which doesn\'t exist',
    # 5.4.1.1 Unitses must have a name
    '5.4.1.1.units_name_missing':
        'Units element must have a name attribute',
    # 5.4.1.1 A units can only contain unit elements
    '5.4.1.1.units_with_component':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_component_ref':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_connection':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_group':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_map_components':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_map_variables':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_math':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_model':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_reaction':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_relationship_ref':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_role':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_units':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_variable':
        'found element of type cellml:component_ref',
    '5.4.1.1.units_with_variable_ref':
        'found element of type cellml:component_ref',
    # 5.4.1.2 A units name must be a valid identifier
    '5.4.1.2.units_name_invalid':
        'Units name must be a valid CellML identifier',
    # 5.4.1.2 Units names must be unique (within model or local component)
    #'5.4.1.2.units_name_duplicate_1':
    #    'More than one units in the model named',
    #'5.4.1.2.units_name_duplicate_2':
    #    'More than one units in the component named',
    # 5.4.1.2 Units names cannot overlap with predefined ones
    #'5.4.1.2.units_name_predefined_ampere':
    #    'Units in the model uses reserved name ampere',
    #'5.4.1.2.units_name_predefined_becquerel':
    #    'Units in the model uses reserved name becquerel',
    #'5.4.1.2.units_name_predefined_candela':
    #    'Units in the model uses reserved name candela',
    #'5.4.1.2.units_name_predefined_celsius':
    #    'Units in the model uses reserved name celsius',
    #'5.4.1.2.units_name_predefined_coulomb':
    #    'Units in the model uses reserved name coulomb',
    #'5.4.1.2.units_name_predefined_dimensionless':
    #    'Units in the model uses reserved name dimensionless',
    #'5.4.1.2.units_name_predefined_farad':
    #    'Units in the model uses reserved name farad',
    #'5.4.1.2.units_name_predefined_gram':
    #    'Units in the model uses reserved name gram',
    #'5.4.1.2.units_name_predefined_gray':
    #    'Units in the model uses reserved name gray',
    #'5.4.1.2.units_name_predefined_henry':
    #    'Units in the model uses reserved name henry',
    #'5.4.1.2.units_name_predefined_hertz':
    #    'Units in the model uses reserved name hertz',
    #'5.4.1.2.units_name_predefined_joule':
    #    'Units in the model uses reserved name joule',
    #'5.4.1.2.units_name_predefined_katal':
    #    'Units in the model uses reserved name katal',
    #'5.4.1.2.units_name_predefined_kelvin':
    #    'Units in the model uses reserved name kelvin',
    #'5.4.1.2.units_name_predefined_kilogram':
    #    'Units in the model uses reserved name kilogram',
    #'5.4.1.2.units_name_predefined_liter':
    #    'Units in the model uses reserved name liter',
    #'5.4.1.2.units_name_predefined_litre':
    #    'Units in the model uses reserved name litre',
    #'5.4.1.2.units_name_predefined_lumen':
    #    'Units in the model uses reserved name lumen',
    #'5.4.1.2.units_name_predefined_lux':
    #    'Units in the model uses reserved name lux',
    #'5.4.1.2.units_name_predefined_meter':
    #    'Units in the model uses reserved name meter',
    #'5.4.1.2.units_name_predefined_metre':
    #    'Units in the model uses reserved name metre',
    #'5.4.1.2.units_name_predefined_mole':
    #    'Units in the model uses reserved name mole',
    #'5.4.1.2.units_name_predefined_newton':
    #    'Units in the model uses reserved name newton',
    #'5.4.1.2.units_name_predefined_ohm':
    #    'Units in the model uses reserved name ohm',
    #'5.4.1.2.units_name_predefined_pascal':
    #    'Units in the model uses reserved name pascal',
    #'5.4.1.2.units_name_predefined_radian':
    #    'Units in the model uses reserved name radian',
    #'5.4.1.2.units_name_predefined_second':
    #    'Units in the model uses reserved name second',
    #'5.4.1.2.units_name_predefined_siemens':
    #    'Units in the model uses reserved name siemens',
    #'5.4.1.2.units_name_predefined_sievert':
    #    'Units in the model uses reserved name sievert',
    #'5.4.1.2.units_name_predefined_steradian':
    #    'Units in the model uses reserved name steradian',
    #'5.4.1.2.units_name_predefined_tesla':
    #    'Units in the model uses reserved name tesla',
    #'5.4.1.2.units_name_predefined_volt':
    #    'Units in the model uses reserved name volt',
    #'5.4.1.2.units_name_predefined_watt':
    #    'Units in the model uses reserved name watt',
    #'5.4.1.2.units_name_predefined_weber':
    #    'Units in the model uses reserved name weber',
    # 5.4.1.2 Component units names cannot overlap with predefined ones
    #'5.4.1.2.units_name_predefined_component_ampere':
    #    'Units in the component uses reserved name ampere',
    # 5.4.1.3 Units base_units attribute can only be yes or no
    #'5.4.1.3.units_base_units_invalid':
    #    'the value of the base_units attribute MUST be',
    # 5.4.2.1 A unit must have a units attribute
    #'5.4.2.1.unit_units_missing':
    #    'MUST define a units attribute',
    # 5.4.2.1 A unit cannot have CellML children
    '5.4.2.1.unit_with_component':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_component_ref':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_connection':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_group':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_map_components':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_map_variables':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_math':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_model':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_reaction':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_relationship_ref':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_role':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_unit':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_units':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_variable':
        'found element of type cellml:component_ref',
    '5.4.2.1.unit_with_variable_ref':
        'found element of type cellml:component_ref',
    # 5.4.2.2 A unit must refer to an existing units
    #'5.4.2.2.unit_units_invalid':
    #    'units could not be found',
    # 5.4.2.2 A unit cannot refer to itself directly or indirectly
    #'5.4.2.2.unit_cycle_1':
    #    'Units are defined circularly',
    #'5.4.2.2.unit_cycle_2':
    #    'Units are defined circularly',
    #'5.4.2.2.unit_cycle_3':
    #    'Units are defined circularly',
    # 6.4.1.1 A group must have at least one component_ref
    #'6.4.1.1.group_component_ref_missing_1':
    #    'MUST contain at least one',
    #'6.4.1.1.group_component_ref_missing_2':
    #    'MUST contain at least one',
    # 6.4.1.1 A group must have at least one relationship_ref
    #'6.4.1.1.group_relationship_ref_missing_1':
    #    'MUST contain at least one',
    #'6.4.1.1.group_relationship_ref_missing_2':
    #    'MUST contain at least one',
    # 6.4.1.1 A group cannot be empty (extra test for missing comp_ref/rel_ref)
    #'6.4.1.1.group_empty':
    #    'MUST contain at least one',
    #'6.4.1.1.group_only_extensions':
    #    'MUST contain at least one',
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
    #'6.4.2.1.relationship_ref_relationship_missing':
    #    'Relationship attribute is mandatory',
    # 6.4.2.1 A relationship_ref cannot have any CellML children
    '6.4.2.1.relationship_ref_with_component':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_component_ref':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_connection':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_group':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_map_components':
       'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_map_variables':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_math':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_model':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_reaction':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_relationship_ref':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_role':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_unit':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_units':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_variable':
        'found element of type cellml:component_ref',
    '6.4.2.1.relationship_ref_with_variable_ref':
        'found element of type cellml:component_ref',
    # 6.4.2.2 When not in a namespace, a relationship_ref's relationship must
    # be either containment or encapsulation.
    #'6.4.2.2.relationship_ref_relationship_invalid':
    #    'The value of a relationship attribute in the CellML namespace',
    # 6.4.2.3 A relationship_ref name must be a cellml identifier
    #'6.4.2.3.relationship_ref_name_invalid':
    #    'A valid CellML identifier must contain at least one letter',
    # 6.4.2.4 An encapsulation can not be named
    #'6.4.2.4.relationship_ref_encapsulation_duplicate':
    #    'A name attribute must not be defined',
    #'6.4.2.4.relationship_ref_encapsulation_named':
    #    'A name attribute must not be defined',
    # 6.4.2.5 name/relationship pairs must be unique
    #'6.4.2.5.relationship_ref_duplicate_named':
    #    'Duplicate relationship_ref within group',
    #'6.4.2.5.relationship_ref_duplicate_unnamed_1':
    #    'Duplicate relationship_ref within group',
    #'6.4.2.5.relationship_ref_duplicate_unnamed_2':
    #    'Duplicate relationship_ref within group',
    # 6.4.3.1 A component_ref must define a component
    #'6.4.3.1.component_ref_component_missing':
    #    'must define a component attribute',
    # 6.4.3.1 A component_ref can only contain a component_ref
    '6.4.3.1.component_ref_with_component':
        'found element of type cellml:component_ref',
    '6.4.3.1.component_ref_with_connection':
        'found element of type cellml:component_ref',
    '6.4.3.1.component_ref_with_group':
        'found element of type cellml:component_ref',
    '6.4.3.1.component_ref_with_map_components':
        'found element of type cellml:component_ref',
    '6.4.3.1.component_ref_with_map_variables':
        'found element of type cellml:component_ref',
    '6.4.3.1.component_ref_with_math':
        'found element of type cellml:component_ref',
    '6.4.3.1.component_ref_with_model':
        'found element of type cellml:component_ref',
    '6.4.3.1.component_ref_with_reaction':
        'found element of type cellml:component_ref',
    '6.4.3.1.component_ref_with_relationship_ref':
        'found element of type cellml:component_ref',
    '6.4.3.1.component_ref_with_role':
        'found element of type cellml:component_ref',
    '6.4.3.1.component_ref_with_unit':
        'found element of type cellml:component_ref',
    '6.4.3.1.component_ref_with_units':
        'found element of type cellml:component_ref',
    '6.4.3.1.component_ref_with_variable':
        'found element of type cellml:component_ref',
    '6.4.3.1.component_ref_with_variable_ref':
        'found element of type cellml:component_ref',
    # 6.4.3.2 A component's children cannot be declared two places
    #'6.4.3.2.component_ref_children_declared_twice_1':
    #    'elements that reference a given component may contain further',
    #'6.4.3.2.component_ref_children_declared_twice_2':
    #    'elements that reference a given component may contain further',
    #'6.4.3.2.component_ref_children_declared_twice_3':
    #    'elements that reference a given component may contain further',
    # 6.4.3.2 The first component_ref in a containment must have children
    #'6.4.3.2.component_ref_no_children_containment':
    #    'does not have any child component_ref elements',
    # 6.4.3.2 The first component_ref in an encapsulation must have children
    #'6.4.3.2.component_ref_no_children_encapsulation':
    #    'does not have any child component_ref elements',
    # 6.4.3.3 A component attribute must be an identifier
    #'6.4.3.3.component_ref_component_invalid':
    #    'A valid CellML identifier must contain at least',
    # 6.4.3.3 A component_ref must refer to an existing component
    #'6.4.3.3.component_ref_component_nonexistent_1':
    #    'Component_ref element references component which does not exist',
    #'6.4.3.3.component_ref_component_nonexistent_2':
    #    'Component_ref element references component which does not exist',
    # 7.4.1.1 A reaction must contain at least one variable_ref
    #'7.4.1.1.reaction_variable_ref_missing':
    #    'must contain at least one',
    # 7.4.1.1 A reaction can only contain a variable_ref
    #'7.4.1.1.reaction_with_component':
    #'7.4.1.1.reaction_with_component_ref':
    #'7.4.1.1.reaction_with_connection':
    #'7.4.1.1.reaction_with_group':
    #'7.4.1.1.reaction_with_map_components':
    #'7.4.1.1.reaction_with_map_variables':
    #'7.4.1.1.reaction_with_math':
    #'7.4.1.1.reaction_with_model':
    #'7.4.1.1.reaction_with_reaction':
    #'7.4.1.1.reaction_with_relationship_ref':
    #'7.4.1.1.reaction_with_role':
    #'7.4.1.1.reaction_with_unit':
    #'7.4.1.1.reaction_with_units':
    #'7.4.1.1.reaction_with_variable':
    # 7.4.1.2 The reversible attribute can only be yes or no
    #'7.4.1.2.reaction_reversible_invalid':
    #    'the reversible attribute must have a value of "yes" or "no"',
    # 7.4.1.3 There's another rule about maths here that I don't understand
    # 7.4.2.1 A variable_ref must have at least one role
    #'7.4.2.1.variable_ref_role_missing':
    #    'must contain at least one',
    #'7.4.2.1.variable_ref_variable_missing':
    #    'must define a variable attribute',
    # 7.4.2.1 A variable_ref can only contain a role
    #'7.4.2.1.variable_ref_with_component_ref':
    #'7.4.2.1.variable_ref_with_component':
    #'7.4.2.1.variable_ref_with_connection':
    #'7.4.2.1.variable_ref_with_group':
    #'7.4.2.1.variable_ref_with_map_components':
    #'7.4.2.1.variable_ref_with_map_variables':
    #'7.4.2.1.variable_ref_with_math':
    #'7.4.2.1.variable_ref_with_model':
    #'7.4.2.1.variable_ref_with_reaction':
    #'7.4.2.1.variable_ref_with_relationship_ref':
    #'7.4.2.1.variable_ref_with_unit':
    #'7.4.2.1.variable_ref_with_units':
    #'7.4.2.1.variable_ref_with_variable':
    #'7.4.2.1.variable_ref_with_variable_ref':
    # 7.4.3.1 A role must define a role attribute
    #'7.4.3.1.role_role_missing':
    #    'must define a role attribute',
    # 7.4.3.1 A role cannot contain any CellML children (only math)
    #'7.4.3.1.role_with_component':
    #'7.4.3.1.role_with_component_ref':
    #'7.4.3.1.role_with_connection':
    #'7.4.3.1.role_with_group':
    #'7.4.3.1.role_with_map_components':
    #'7.4.3.1.role_with_map_variables':
    #'7.4.3.1.role_with_model':
    #'7.4.3.1.role_with_reaction':
    #'7.4.3.1.role_with_relationship_ref':
    #'7.4.3.1.role_with_role':
    #'7.4.3.1.role_with_unit':
    #'7.4.3.1.role_with_units':
    #'7.4.3.1.role_with_variable_ref':
    #'7.4.3.1.role_with_variable':
    # 7.4.3.2 A role must define a valid role attribute
    #'7.4.3.2.role_role_invalid':
    #    'must take one of the following seven values',
    # 7.4.3.4 A direction can only be forward, reverse, or both
    #'7.4.3.4.role_direction_invalid':
    #    'the direction attribute must take one of the following',
    # 7.4.3.6 Stoichiometry must be a real number
    #'7.4.3.6.role_stoichiometry_invalid':
    #    'Expected a real number',
}


# Invalid models for which validation is not expected to pick up the (correct)
# error.
known_issues = {
    # Attributes inside the CellML namespace are ignored
    '2.4.2.imaginary_attributes_2',
    # CellML namespace attributes inside extensions are not detected
    '2.4.3.cellml_attributes_inside_extensions',
    # Text in reactions is not detected
    '2.4.4.text_in_reaction',
    '2.4.4.text_in_role',
    '2.4.4.text_in_variable_ref',


}
'''
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
    # 6.4.3.2 A component cannot be named twice in a single hierarchy
    '6.4.3.2.component_ref_duplicate_child_1',
    '6.4.3.2.component_ref_duplicate_child_2',
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
    # 8.4.1 Cmeta id's are unique
    '8.4.1.cmeta_id_duplicate',
    # Bad messsage (there are no attributes in the CellML namespace):
    # The value of a relationship attribute in the CellML namespace must be
    # "containment" or "encapsulation" (section 6.4.2.2).
}
'''


@pytest.fixture
def log():
    """ Returns a logger object. """
    return logging.getLogger(__name__)


def parse(path):
    """ Parses the file at ``path``. """
    import myokit.formats.cellml.v1 as cellml
    p = cellml.CellMLParser()
    try:
        p.parse_file(path)
    except cellml.CellMLParsingError as e:
        return False, str(e)
    else:
        return True, 'OK'


class TestMyokit(object):
    """ Tests Myokit validation. """

    @classmethod
    def setup_class(cls):
        cls._report = Report('Myokit - CellML 1.0')

    @classmethod
    def teardown_class(cls):
        cls._report.render(
            os.path.join(check.REPORT_DIR, 'myokit_1_0.md'))

    @pytest.mark.skipif(NO_MYOKIT, reason='Myokit not found')
    @pytest.mark.parametrize(('name', 'path'), shared.list_passes_1_0(True))
    def test_valid_model(self, name, path, log):

        # Validate model
        ok, msg = parse(path)

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

    @pytest.mark.skipif(NO_MYOKIT, reason='Myokit not found')
    @pytest.mark.parametrize(('name', 'path'), shared.list_fails_1_0())
    def test_invalid_model(self, name, path, log):

        # See if there's an expected error for this model
        expected_error = expected_messages.get(name, None)
        expected_issue = name in known_issues

        # Validate model
        ok, msg = parse(path)

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


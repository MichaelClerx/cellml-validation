#
# Tests CellML 1.0 schema validation
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import logging
import os
import pytest
import re
from lxml import etree

import check


# Expected error messages and known fails
expected_errors = {
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
        "Element 'cellml:units', attribute 'name'",
    '2.4.1.identifier_only_underscore':
        "Element 'cellml:units', attribute 'name'",
    '2.4.1.identifier_unexpected_character':
        "Element 'cellml:units', attribute 'name'",
    '2.4.1.identifier_unexpected_character_2':
        "Element 'cellml:units', attribute 'name'",
    '2.4.1.identifier_unexpected_character_unicode':
        "Element 'cellml:units', attribute 'name'",
    # 2.4.2. Allowable CellML elements and attributes
    '2.4.2.imaginary_attributes_1':
        "The attribute 'fruit' is not allowed",
    '2.4.2.imaginary_attributes_2':
        "The attribute 'cellml:fruit' is not allowed",
    '2.4.2.imaginary_elements':
        "Element 'cellml:fruit': This element is not expected",
    # 2.4.3 Elements/attributes in extension namespaces
    '2.4.3.cellml_attributes_inside_extensions': None,
    '2.4.3.cellml_elements_inside_extensions': None,
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
        "Element 'cellml:model': The attribute 'name' is required",
    # 2.5.3 Extension namespaces again
    # 3.4.1.1 Models contain only units, component, group, connection
    '3.4.1.1.model_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    '3.4.1.1.model_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    '3.4.1.1.model_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    '3.4.1.1.model_with_math': None,
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
        "Element 'cellml:model', attribute 'name': '___' is not a valid value",
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
        "Element 'cellml:component': Not all fields of key",
    # 3.4.2.2 A component name must be a valid identifier
    '3.4.2.2.component_name_invalid':
        "Not all fields of key identity-constraint 'cellml:component_name'",
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
    '3.4.3.1.variable_with_math': None,
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
        "Not all fields of key identity-constraint 'cellml:variable_name'",
    # 3.4.3.1 Variables must have a units attribute
    '3.4.3.1.variable_units_missing':
        "Element 'cellml:variable': The attribute 'units' is required",
    # 3.4.3.2 A variable name must be an identifier
    '3.4.3.2.variable_name_invalid':
        "Not all fields of key identity-constraint 'cellml:variable_name'",
    # 3.4.3.2 A variable name must be unique with the component
    '3.4.3.2.variable_name_duplicate':
        "Element 'cellml:variable': Duplicate key-sequence",
    # 3.4.3.3 A variable must reference known units
    '3.4.3.3.variable_units_unknown': None,
    # 3.4.3.3 A variable cannot reference another component's units
    '3.4.3.3.variable_units_other_component': None,
    # 3.4.3.4 A public interface must be one of in/out/none
    '3.4.3.4.variable_interface_public_invalid':
        "is not a valid value of the atomic type 'cellml:interface'",
    # 3.4.3.5 A private interface must be one of in/out/none
    '3.4.3.5.variable_interface_private_invalid':
        "is not a valid value of the atomic type 'cellml:interface'",
    # 3.4.3.6 The private and public interface can't both be in
    '3.4.3.6.variable_interfaces_both_in': None,
    # 3.4.3.7 The initial value (if present) must be a real number
    '3.4.3.7.variable_initial_value_empty':
        "is not a valid value of the atomic type 'cellml:real_number'",
    '3.4.3.7.variable_initial_value_invalid':
        "is not a valid value of the atomic type 'cellml:real_number'",
    # 3.4.3.8 A variable can't have an initial value and an "in" interface
    '3.4.3.8.variable_interfaces_private_in_and_initial': None,
    '3.4.3.8.variable_interfaces_public_in_and_initial': None,

    # 3.4.4.1 A connection must contain exactly one map_components
    '3.4.4.1.connection_map_components_missing': None,
    '3.4.4.1.connection_map_components_multiple': None,
    # 3.4.4.1 A component must contain at least one map_variables
    '3.4.4.1.connection_map_variables_missing': None,
    # 3.4.4.1 A connection must have map_components and map_variables
    '3.4.4.1.connection_only_extensions': None,
    '3.4.4.1.connection_with_math': None,
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
    '3.4.5.1.map_components_with_math': None,
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
    # 3.4.5.4 component_1 cannot match component_2
    '3.4.5.4.map_components_component_1_equals_2': None,
    # 3.4.5.4 Each map_components in a model must be unique
    '3.4.5.4.map_components_duplicate_mirrored': None,
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
    '3.4.6.1.map_variables_with_math': None,
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
    # 3.4.6.2 variable_1 must refer to an existing variable in component_1
    '3.4.6.2.map_variables_variable_1_nonexistent': None,
    # 3.4.6.3 variable_2 must refer to an existing variable in component_2
    '3.4.6.3.map_variables_variable_2_nonexistent': None,
    # 3.4.6.4 Interfaces and encapsulation
    '3.4.6.4.map_variables_sibling_in_to_in': None,
    '3.4.6.4.map_variables_sibling_out_to_out': None,
    '3.4.6.4.map_variables_sibling_private_in_1': None,
    '3.4.6.4.map_variables_sibling_private_in_2': None,
    '3.4.6.4.map_variables_sibling_private_in_and_out': None,
    '3.4.6.4.map_variables_sibling_private_out_1': None,
    '3.4.6.4.map_variables_sibling_private_out_2': None,







    # Group elements
    'group_empty':
        "Element 'cellml:group': Missing child element(s).",
    'group_no_component_ref': None,
    'group_only_junk': None,
    'component_math_does_not_define_variable': None,

}


@pytest.fixture
def schema_parser():
    """ Returns a parser that can resolve schema locations. """
    parser = etree.XMLParser(no_network=True)
    parser.resolvers.add(check.SchemaResolver())
    return parser


@pytest.fixture
def schema(schema_parser):
    """ Returns a parsed schema object. """
    filename = check.cellml_1_0('cellml_1_0.xsd')
    assert os.path.isfile(filename)
    return etree.XMLSchema(etree.parse(filename, schema_parser))


def schema_1_0(filename):
    """
    Checks a file against the schema, outside of the test framework.
    """
    parser = schema_parser()
    assert_valid_with_schema(filename, schema(parser), parser)


def valid_models():
    """ Returns a list of filenames for models that should validate. """
    # Note: Returning file basename rather than path, so that the test output
    # is e.g. test_valid_models[empty-model] instead of something containing
    # containing the absolute path and extension.
    files = [os.path.splitext(x) for x in os.listdir(check.model_1_0('valid'))]
    return [x[0] for x in files if x[1] == '.cellml']


def invalid_models():
    """ Returns a list of filenames for models that should not validate. """
    files = []
    for f in os.listdir(check.model_1_0('invalid')):
        name, ext = os.path.splitext(f)
        if ext != '.cellml':
            continue
        if expected_errors.get(name, '') is None:
            files.append(pytest.param(name, marks=pytest.mark.xfail))
        else:
            files.append(name)
    return files


@pytest.mark.parametrize('filename', valid_models())
def test_valid_models(filename, schema, schema_parser):
    """
    Tests if all valid models validate.
    """
    # Parse CellML file
    filename = os.path.join('valid', filename + '.cellml')
    path = check.model_1_0(filename)
    assert os.path.isfile(path)
    xml = etree.parse(path, schema_parser)

    # Check if namespace is set correctly (for a nicer error message)
    tag = etree.QName(xml.getroot().tag)
    assert tag.namespace == check.CELLML_1_0_NS

    # Validate
    schema.assertValid(xml)


@pytest.mark.parametrize('filename', invalid_models())
def test_invalid_models(filename, schema, schema_parser):
    """
    Checks that no invalid models validate.
    """
    log = logging.getLogger(__name__)

    # Check file exists
    rel_path = os.path.join('invalid', filename + '.cellml')
    path = check.model_1_0(rel_path)
    assert os.path.isfile(path)

    # Parse and validate
    try:
        xml = etree.parse(path, schema_parser)
    except etree.XMLSyntaxError as e:

        # Log detected error
        error = str(e)
        log.info('Error during parsing: ' + error)
        assert True

    else:
        # Validate (known fails exit here)
        assert not schema.validate(xml)

        # Log detected error
        e = schema.error_log.last_error
        r = re.compile(re.escape('{' + check.CELLML_1_0_NS + '}'))
        error = r.sub('cellml:', e.message)
        log.info('Error on line ' + str(e.line) + ': ' + error)

    # Test correct error was raised
    expected = expected_errors.get(filename, '')
    print(expected)
    if expected == '':
        expected = 'No expected error set'
    log.info('Expected error: ' + expected)
    r = re.compile(re.escape(expected))
    if r.search(error) is None:
        log.error('Unexpected error in ' + filename)
        log.error('Expected: ' + expected)
        log.error('Returned: ' + error)
        pytest.fail()


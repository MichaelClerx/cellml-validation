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

from check import (
    CELLML_1_0_NS,
    cellml_1_0 as cellml,
    model_1_0 as model,
    SchemaResolver,
)



# Expected error messages, or known fails
expected_errors = {

    # 0 Root node
    '0.root_node_not_model':
        "No matching global declaration available for the validation root",
    '0.root_node_two_elements':
        "Extra content at the end of the document",
    '0.root_node_two_models':
        "Extra content at the end of the document",
    '0.root_node_namespace_wrong':
        "No matching global declaration available for the validation root",
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







    # Component element
    'component_name_duplicate':
        "Duplicate key-sequence ['c1']",
    'component_name_invalid':
        "Not all fields of key identity-constraint 'cellml:component_name'",
    'component_name_missing':
        "Element 'cellml:component': Not all fields of key",
    'component_with_component':
        "Element 'cellml:component': This element is not expected",
    'component_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    'component_with_connection':
        "Element 'cellml:connection': This element is not expected",
    'component_with_group':
        "Element 'cellml:group': This element is not expected",
    'component_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    'component_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    'component_with_model':
        "Element 'cellml:model': This element is not expected",
    'component_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    'component_with_role':
        "Element 'cellml:role': This element is not expected",
    'component_with_unit':
        "Element 'cellml:unit': This element is not expected",
    'component_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",

    'component_math_does_not_define_variable': None,

    # Connection elements
    'connection_empty':
        "Element 'cellml:connection': Missing child element(s).",
    'connection_with_component':
        "Element 'cellml:component': This element is not expected",
    'connection_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    'connection_with_connection':
        "Element 'cellml:connection': This element is not expected",
    'connection_with_group':
        "Element 'cellml:group': This element is not expected",
    'connection_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    'connection_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    'connection_with_model':
        "Element 'cellml:model': This element is not expected",
    'connection_with_name_attribute':
        "Element 'cellml:connection', attribute 'name'",
    'connection_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    'connection_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    'connection_with_role':
        "Element 'cellml:role': This element is not expected",
    'connection_with_unit':
        "Element 'cellml:unit': This element is not expected",
    'connection_with_units':
        "Element 'cellml:units': This element is not expected",
    'connection_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    'connection_with_variable':
        "Element 'cellml:variable': This element is not expected",

    'connection_map_components_missing': None,
    'connection_map_components_multiple': None,
    'connection_map_variables_missing': None,
    'connection_only_junk': None,
    'connection_with_math': None,


    # Group elements
    'group_empty':
        "Element 'cellml:group': Missing child element(s).",

    'group_no_component_ref': None,
    'group_only_junk': None,



    # Map_components elements
    'map_components_component_1_missing':
        "Element 'cellml:map_components': The attribute 'component_1' is req",
    'map_components_component_1_nonexistent':
        "Element 'cellml:map_components': No match found for key-sequence",
    'map_components_component_2_missing':
        "Element 'cellml:map_components': The attribute 'component_2' is req",
    'map_components_component_2_nonexistent':
        "Element 'cellml:map_components': No match found for key-sequence",
    'map_components_duplicate':
        "Element 'cellml:map_components': Duplicate key-sequence",
    'map_components_with_component':
        "Element 'cellml:component': This element is not expected",
    'map_components_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    'map_components_with_connection':
        "Element 'cellml:connection': This element is not expected",
    'map_components_with_group':
        "Element 'cellml:group': This element is not expected",
    'map_components_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    'map_components_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    'map_components_with_model':
        "Element 'cellml:model': This element is not expected",
    'map_components_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    'map_components_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    'map_components_with_role':
        "Element 'cellml:role': This element is not expected",
    'map_components_with_unit':
        "Element 'cellml:unit': This element is not expected",
    'map_components_with_units':
        "Element 'cellml:units': This element is not expected",
    'map_components_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    'map_components_with_variable':
        "Element 'cellml:variable': This element is not expected",

    'map_components_component_1_equals_2': None,
    'map_components_duplicate_mirrored': None,
    'map_components_with_math': None,


    # Map_variables elements
    'map_variables_variable_1_missing':
        "Element 'cellml:map_variables': The attribute 'variable_1' is req",
    'map_variables_variable_2_missing':
        "Element 'cellml:map_variables': The attribute 'variable_2' is req",
    'map_variables_with_component':
        "Element 'cellml:component': This element is not expected",
    'map_variables_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    'map_variables_with_connection':
        "Element 'cellml:connection': This element is not expected",
    'map_variables_with_group':
        "Element 'cellml:group': This element is not expected",
    'map_variables_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    'map_variables_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    'map_variables_with_model':
        "Element 'cellml:model': This element is not expected",
    'map_variables_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    'map_variables_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    'map_variables_with_role':
        "Element 'cellml:role': This element is not expected",
    'map_variables_with_unit':
        "Element 'cellml:unit': This element is not expected",
    'map_variables_with_units':
        "Element 'cellml:units': This element is not expected",
    'map_variables_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    'map_variables_with_variable':
        "Element 'cellml:variable': This element is not expected",

    'map_variables_with_math': None,
    'map_variables_variable_1_nonexistent': None,
    'map_variables_variable_2_nonexistent': None,
    # Model elements
    'model_name_invalid':
        "Element 'cellml:model', attribute 'name': '___' is not a valid value",
    'model_name_missing':
        "Element 'cellml:model': The attribute 'name' is required",
    'model_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    'model_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    'model_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    'model_with_model':
        "Element 'cellml:model': This element is not expected",
    'model_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    'model_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    'model_with_role':
        "Element 'cellml:role': This element is not expected",
    'model_with_unit':
        "Element 'cellml:unit': This element is not expected",
    'model_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    'model_with_variable':
        "Element 'cellml:variable': This element is not expected",

    'model_with_math': None,
    # Variable elements
    'variable_initial_value_invalid_1':
        "is not a valid value of the atomic type 'cellml:real_number'",
    'variable_initial_value_invalid_2':
        "is not a valid value of the atomic type 'cellml:real_number'",
    'variable_initial_value_invalid_3':
        "is not a valid value of the atomic type 'cellml:real_number'",
    'variable_initial_value_invalid_4':
        "is not a valid value of the atomic type 'cellml:real_number'",
    'variable_initial_value_invalid_5':
        "is not a valid value of the atomic type 'cellml:real_number'",
    'variable_initial_value_invalid_6':
        "is not a valid value of the atomic type 'cellml:real_number'",
    'variable_interfaces_private_invalid':
        "is not a valid value of the atomic type 'cellml:interface'",
    'variable_interfaces_public_invalid':
        "is not a valid value of the atomic type 'cellml:interface'",
    'variable_name_invalid':
        "Not all fields of key identity-constraint 'cellml:variable_name'",
    'variable_name_duplicate':
        "Element 'cellml:variable': Duplicate key-sequence",
    'variable_name_missing':
        "Not all fields of key identity-constraint 'cellml:variable_name'",
    'variable_units_missing':
        "Element 'cellml:variable': The attribute 'units' is required",
    'variable_with_component':
        "Element 'cellml:component': This element is not expected",
    'variable_with_component_ref':
        "Element 'cellml:component_ref': This element is not expected",
    'variable_with_connection':
        "Element 'cellml:connection': This element is not expected",
    'variable_with_group':
        "Element 'cellml:group': This element is not expected",
    'variable_with_map_components':
        "Element 'cellml:map_components': This element is not expected",
    'variable_with_map_variables':
        "Element 'cellml:map_variables': This element is not expected",
    'variable_with_model':
        "Element 'cellml:model': This element is not expected",
    'variable_with_reaction':
        "Element 'cellml:reaction': This element is not expected",
    'variable_with_relationship_ref':
        "Element 'cellml:relationship_ref': This element is not expected",
    'variable_with_role':
        "Element 'cellml:role': This element is not expected",
    'variable_with_unit':
        "Element 'cellml:unit': This element is not expected",
    'variable_with_units':
        "Element 'cellml:units': This element is not expected",
    'variable_with_variable_ref':
        "Element 'cellml:variable_ref': This element is not expected",
    'variable_with_variable':
        "Element 'cellml:variable': This element is not expected",


    'variable_interfaces_both_in': None,
    'variable_interfaces_private_in_and_initial': None,
    'variable_interfaces_public_in_and_initial': None,
    'variable_units_nonexistent': None,
    'variable_with_math': None,


}


@pytest.fixture
def schema_parser():
    """ Returns a parser that can resolve schema locations. """
    parser = etree.XMLParser(no_network=True)
    parser.resolvers.add(SchemaResolver())
    return parser


@pytest.fixture
def schema(schema_parser):
    """ Returns a parsed schema object. """
    filename = cellml('cellml_1_0.xsd')
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
    files = [os.path.splitext(x) for x in os.listdir(model('valid'))]
    return [x[0] for x in files if x[1] == '.cellml']


def invalid_models():
    """ Returns a list of filenames for models that should not validate. """
    files = []
    for f in os.listdir(model('invalid')):
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
    path = model(filename)
    assert os.path.isfile(path)
    xml = etree.parse(path, schema_parser)

    # Check if namespace is set correctly (for a nicer error message)
    tag = etree.QName(xml.getroot().tag)
    assert tag.namespace == CELLML_1_0_NS

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
    path = model(rel_path)
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
        r = re.compile(re.escape('{' + CELLML_1_0_NS + '}'))
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


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


known_fails = [
    'connection_no_map_components',
    'connection_no_map_variables',
    'connection_only_junk',
    'connection_two_map_components',
    'group_no_component_ref',
    'group_only_junk',
    'map_variables_bad_variable_1',
    'map_variables_bad_variable_2',
    'component_math_does_not_define_variable',
    'variable_with_math',
]

expected_errors = {
    'attribute_in_cellml_namespace':
        "Element 'cellml:model': The attribute 'name' is required",
    'component_as_root_node':
        "No matching global declaration available for the validation root",
    'component_invalid_name':
        "Not all fields of key identity-constraint 'cellml:component_name'",
    'component_with_same_name':
        "Duplicate key-sequence ['c1']",
    'component_no_name':
        "Element 'cellml:component': Not all fields of key",
    'component_with_component':
        "Element 'cellml:component': This element is not expected",
    'component_with_model':
        "Element 'cellml:model': This element is not expected",
    'component_with_text':
        "Element 'cellml:component': Character content other than white",
    'connection_empty':
        "Element 'cellml:connection': Missing child element(s).",
    'connection_with_a_name':
        "Element 'cellml:connection', attribute 'name'",
    'connection_with_text':
        "Element 'cellml:connection': Character content other than white",
    'group_empty':
        "Element 'cellml:group': Missing child element(s).",
    'identifier_empty_name':
        #"'name': '' is not a valid value",
        "Element 'cellml:units', attribute 'name'",
    'identifier_only_underscore':
        "Element 'cellml:units', attribute 'name'",
    'identifier_unexpected_character':
        "Element 'cellml:units', attribute 'name'",
    'identifier_unexpected_character_2':
        "Element 'cellml:units', attribute 'name'",
    'identifier_unexpected_character_unicode':
        "Element 'cellml:units', attribute 'name'",
    'map_components_with_text':
        "Element 'cellml:map_components': Character content other than white",
    'map_variables_with_text':
        "Element 'cellml:map_variables': Character content other than white",
    'model_invalid_name':
        "Element 'cellml:model', attribute 'name': '___' is not a valid value",
    'model_no_name':
        "Element 'cellml:model': The attribute 'name' is required",
    'model_with_text':
        "Element 'cellml:model': Character content other than white",
    'model_wrong_namespace':
        "No matching global declaration available for the validation root",
    'variable_with_text':
        "Element 'cellml:variable': Character content other than white",
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
    files = [os.path.splitext(x) for x in os.listdir(model('invalid'))]
    files = [x[0] for x in files if x[1] == '.cellml']
    return [
        pytest.param(x, marks=pytest.mark.xfail) if x in known_fails else x
        for x in files]


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

    # Parse CellML file
    rel_path = os.path.join('invalid', filename + '.cellml')
    path = model(rel_path)
    assert os.path.isfile(path)
    xml = etree.parse(path, schema_parser)

    # Validate
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


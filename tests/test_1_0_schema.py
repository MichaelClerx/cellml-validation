#
# Tests CellML 1.0 schema validation
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import logging
import os
import pytest
from lxml import etree

from .shared import (
    CELLML_1_0_NS,
    cellml_1_0 as cellml,
    model_1_0 as model,
    SchemaResolver,
)

known_fails = [
    'connection_only_junk',
    'connection_no_map_components',
    'connection_no_map_variables',
    'connection_two_map_components',
    'group_no_component_ref',
    'group_only_junk',
    'map_variables_bad_variable_1',
    'map_variables_bad_variable_2',
]


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
    return schema


def assert_valid_with_schema(filename, schema, schema_parser):
    """
    Parses a model and a schema, asserting the model is valid against the
    schema.
    """
    # Parse CellML file
    filename = model(filename + '.cellml')
    assert os.path.isfile(filename)
    xml = etree.parse(filename, schema_parser)

    # Check if namespace is set correctly (for a nicer error message)
    tag = etree.QName(xml.getroot().tag)
    assert tag.namespace == CELLML_1_0_NS

    # Validate
    schema.assertValid(xml)


def assert_invalid_with_schema(filename, schema, schema_parser):
    """
    Asserts that a model does not pass schema validation.
    """
    log = logging.getLogger(__name__)

    # Parse CellML file
    filename = model(filename + '.cellml')
    assert os.path.isfile(filename)
    xml = etree.parse(filename, schema_parser)

    # Check if namespace is set correctly (for a nicer error message)
    tag = etree.QName(xml.getroot().tag)
    if tag.namespace != CELLML_1_0_NS:
        log.info('Model in wrong namespace')
        return

    # Validate
    assert not schema.validate(xml)

    # Show detected error
    log.info(schema.error_log.last_error)


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
    """ Tests if all valid models validate. """
    filename = model('valid', filename)
    assert_valid_with_schema(filename, schema, schema_parser)


@pytest.mark.parametrize('filename', invalid_models())
def test_invalid_models(filename, schema, schema_parser):
    """ Checks that no invalid models validate. """
    filename = model('invalid', filename)
    assert_invalid_with_schema(filename, schema, schema_parser)


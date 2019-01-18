#
# Tests CellML 1.0 schema validation
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import os
import pytest
from lxml import etree

from .shared import (
    CELLML_1_0_NS,
    cellml_1_0 as cellml,
    model_1_0 as model,
    SchemaResolver,
)


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
    filename = model(filename)
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
    # Parse CellML file
    filename = model(filename)
    assert os.path.isfile(filename)
    xml = etree.parse(filename, schema_parser)

    # Check if namespace is set correctly (for a nicer error message)
    tag = etree.QName(xml.getroot().tag)
    assert tag.namespace == CELLML_1_0_NS

    # Validate
    assert not schema.validate(xml)


def valid_models():
    """ Returns a list of filenames for models that should validate. """
    models = []
    root = model('valid')
    for fname in os.listdir(root):
        fname = os.path.join(root, fname)
        if os.path.isfile(fname):
            if os.path.splitext(fname)[1] == '.cellml':
                models.append(fname)
    models.sort()
    return models


def valid_models():
    """ Returns a list of filenames for models that should validate. """
    # Note: Returning filename rather than path, so that the test output is
    # e.g. test_valid_models[empty-model.cellml] instead of something
    # containing the absolute path.
    return [
        x for x in os.listdir(model('valid'))
        if os.path.splitext(x)[1] == '.cellml']


def invalid_models():
    """ Returns a list of filenames for models that should not validate. """
    return [
        x for x in os.listdir(model('invalid'))
        if os.path.splitext(x)[1] == '.cellml']


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


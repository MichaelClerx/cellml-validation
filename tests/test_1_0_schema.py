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


def test_a_model(schema, schema_parser):
    assert_valid_with_schema(
        'aslanidi_atrial_model_2009_LindbladCa_corrected.cellml',
        schema,
        schema_parser
    )
    #f = cellml('beeler_reuter_1977.cellml')
    #f = cellml('espinosa_1998_hypertrophic.cellml')
    #f = cellml('vanderpol_vandermark_1928.cellml')
    #f = cellml('ohara_rudy_cipa_v1_2017.cellml')
    #f = cellml('noble_varghese_kohl_noble_1998_c.cellml')
    #f = cellml('test_simple_odes.cellml')


#
# Parses and validates "playground" files to let you experiment with
# validation.
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals


import os
from lxml import etree

from .shared import (
    cellml_1_0 as cellml,
    model_1_0 as model,
    SchemaResolver,
)


def test_schema_validation():
    # Create parser that can resolve URLs
    p = etree.XMLParser(no_network=True)
    p.resolvers.add(SchemaResolver())

    # Load schema
    f = cellml('playground.xsd')
    assert os.path.isfile(f)
    schema = etree.parse(f, p)
    schema = etree.XMLSchema(schema)

    # Parse CellML file
    f = model('playground.xml')
    assert os.path.isfile(f)
    x = etree.parse(f, p)

    # Validate
    schema.assertValid(x)


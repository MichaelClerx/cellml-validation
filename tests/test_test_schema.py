#
# Tests lxml schema validation
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals


import os
from lxml import etree

from .shared import (
    CELLML_1_0_NS as cellml_ns,
    file_1_0 as cellml,
    validation_1_0 as validation,
    SchemaResolver,
)


def test_a_model():
    # Create parser that can resolve URLs
    p = etree.XMLParser(no_network=True)
    p.resolvers.add(SchemaResolver())

    # Load schema
    f = validation('test_lxml.xsd')
    assert os.path.isfile(f)
    schema = etree.parse(f, p)
    schema = etree.XMLSchema(schema)

    # Parse CellML file
    f = cellml('test_lxml.xml')
    assert os.path.isfile(f)
    x = etree.parse(f, p)

    # Validate
    schema.assertValid(x)


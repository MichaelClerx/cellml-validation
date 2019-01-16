#
# Tests CellML 1.1 schema validation
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals


import os
from lxml import etree

from .shared import (
    CELLML_1_1_NS as cellml_ns,
    file_1_1 as cellml,
    validation_1_1 as validation,
    SchemaResolver,
)


'''
def test_a_model():
    # Create parser that can resolve URLs
    p = etree.XMLParser()
    p.resolvers.add(SchemaResolver())

    # Load schema
    f = validation('cellml_1_0.xsd')
    assert os.path.isfile(f)
    schema = etree.parse(f, p)
    schema = etree.XMLSchema(schema)

    # Parse CellML file
    f = cellml('???.cellml')
    assert os.path.isfile(f)
    x = etree.parse(f)

    # Check if namespace set
    tag = etree.QName(x.getroot().tag)
    assert tag.namespace == cellml_ns

    # Validate
    schema.assertValid(x)
'''

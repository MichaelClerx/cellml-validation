#
# Tests CellML 1.0 schema validation
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals


import os
from lxml import etree

from .shared import (
    CELLML_1_0_NS,
    cellml_1_0 as cellml,
    model_1_0 as model,
    SchemaResolver,
)


def test_a_model():
    # Create parser that can resolve URLs
    p = etree.XMLParser(no_network=True)
    p.resolvers.add(SchemaResolver())

    # Load schema
    f = cellml('cellml_1_0.xsd')
    assert os.path.isfile(f)
    schema = etree.parse(f, p)
    schema = etree.XMLSchema(schema)

    # Parse CellML file
    f = model('aslanidi_atrial_model_2009_LindbladCa_corrected.cellml')
    #f = cellml('beeler_reuter_1977.cellml')
    #f = cellml('espinosa_1998_hypertrophic.cellml')
    #f = cellml('vanderpol_vandermark_1928.cellml')
    #f = cellml('ohara_rudy_cipa_v1_2017.cellml')
    #f = cellml('noble_varghese_kohl_noble_1998_c.cellml')
    #f = cellml('test_simple_odes.cellml')
    assert os.path.isfile(f)
    x = etree.parse(f, p)

    # Check if namespace set
    tag = etree.QName(x.getroot().tag)
    assert tag.namespace == CELLML_1_0_NS

    # Validate
    schema.assertValid(x)


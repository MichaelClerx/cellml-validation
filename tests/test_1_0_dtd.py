#
# Tests CellML 1.0 DTD validation
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals


import os
from lxml import etree

from .shared import (
    CELLML_1_0_NS as cellml_ns,
    file_1_0 as cellml,
    validation_1_0 as validation,
)


'''
def test_a_model():
    # Load DTD
    f = validation('cellml_1_0.dtd')
    dtd = etree.DTD(f)

    # Parse CellML file
    #f = cellml('aslanidi_atrial_model_2009_LindbladCa_corrected.cellml')
    f = cellml('test_simple_odes.cellml')
    x = etree.parse(f)

    # Validate
    dtd.assertValid(x)
'''

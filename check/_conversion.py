#
# Conversion methods
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

from lxml import etree

import check


def xslt_1_to_2(path1, path2):
    """
    Uses an XSLT transform to Converts a CellML 1.0 or 1.1 file at ``path1`` to
    CellML 2.0, storing the result at ``path2``.
    """
    # Create lxml parser
    parser = etree.XMLParser(no_network=True)

    # Create xslt transform object
    xsl = etree.parse(check.cellml_2_0('cellml_1_to_2.xsl'), parser)
    transform = etree.XSLT(xsl)

    # Parse input document
    doc1 = etree.parse(path1, parser)

    # Transform
    doc2 = transform(doc1)

    # Write output
    doc2.write_output(path2)


def xslt_1_0_to_1_1(path1, path2):
    """
    Uses an XSLT transform to Converts a CellML 1.0 file at ``path1`` to
    CellML 1.1, storing the result at ``path2``.
    """
    # Create lxml parser
    parser = etree.XMLParser(no_network=True)

    # Create xslt transform object
    xsl = etree.parse(check.cellml_1_1('cellml_1_0_to_1_1.xsl'), parser)
    transform = etree.XSLT(xsl)

    # Parse input document
    doc1 = etree.parse(path1, parser)

    # Transform
    doc2 = transform(doc1)

    # Write output
    doc2.write_output(path2)


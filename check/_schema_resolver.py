#
# Defines a 'Resolver' that tells lxml how to deal with URL schema locations.
#
import os
import logging
from lxml import etree

import check


# Map common schemas to local copies
CATALOG_DIR = os.path.join(check.MODULE_DIR, '..', 'catalog', 'schema')
MATHML2_XSD = os.path.abspath(os.path.join(
    CATALOG_DIR, 'mathml2', 'mathml2.xsd'))
XLINK_HREF_XSD = os.path.abspath(os.path.join(
    CATALOG_DIR, 'xlink', 'xlink-href.xsd'))
CMETA_ID_XSD = os.path.abspath(os.path.join(
    CATALOG_DIR, 'cmeta', 'cmeta-id.xsd'))
catalog = {
    # MathML
    'http://www.w3.org/Math/XMLSchema/mathml2/mathml2.xsd': MATHML2_XSD,
    'http://www.cellml.org/tools/cellml_1_0_schema/mathml2.xsd': MATHML2_XSD,
    'http://www.cellml.org/tools/cellml_1_1_schema/mathml2.xsd': MATHML2_XSD,
    # XLink (href only)
    'http://cellml.org/specifications/xsd/xlink-href.xsd': XLINK_HREF_XSD,
    'http://www.cellml.org/tools/cellml_1_1_schema/common/xlink-href.xsd':
        XLINK_HREF_XSD,
    # CMeta (id only)
    'http://cellml.org/specifications/xsd/cmeta-id.xsd': CMETA_ID_XSD,
}


class SchemaResolver(etree.Resolver):
    """
    Redirects URL requests for known XML Schemas to the local catalog.
    """
    def resolve(self, url, id, context):
        log = logging.getLogger(__name__)
        filename = catalog.get(url, None)
        if filename is not None:
            log.debug('Resolving ' + url + ' to local file ' + filename)
            if not os.path.exists(filename) and os.path.isfile(filename):
                raise Exception('Catalog path does not exist: ' + filename)
            return self.resolve_filename(filename, context)
        return None


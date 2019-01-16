#
# Main module for CellML validation tests
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import os
import inspect
from lxml import etree


# Set namespaces
CELLML_1_0_NS = 'http://www.cellml.org/cellml/1.0#'
CELLML_1_1_NS = 'http://www.cellml.org/cellml/1.1#'
CELLML_2_0_NS = 'http://www.cellml.org/cellml/2.0#'


# Set paths
try:
    frame = inspect.currentframe()
    MODULE_DIR = os.path.dirname(inspect.getfile(frame))
finally:
    del(frame)

# CellML files
CELLML_FILES = os.path.abspath(os.path.join(MODULE_DIR, '..', 'cellml-files'))
CELLML_1_0_FILES = os.path.join(CELLML_FILES, 'cellml_1_0')
CELLML_1_1_FILES = os.path.join(CELLML_FILES, 'cellml_1_1')
CELLML_2_0_FILES = os.path.join(CELLML_FILES, 'cellml_2_0')

# Validation files
VALIDATION_FILES = os.path.abspath(os.path.join(MODULE_DIR, '..'))
VALIDATION_1_0_FILES = os.path.join(VALIDATION_FILES, 'cellml_1_0')
VALIDATION_1_1_FILES = os.path.join(VALIDATION_FILES, 'cellml_1_1')
VALIDATION_2_0_FILES = os.path.join(VALIDATION_FILES, 'cellml_2_0')


def file_1_0(filename):
    """
    Returns the path to a cellml 1.0 file.
    """
    return os.path.join(CELLML_1_0_FILES, filename)


def file_1_1(filename):
    """
    Returns the path to a cellml 1.1 file.
    """
    return os.path.join(CELLML_1_1_FILES, filename)


def file_2_0(filename):
    """
    Returns the path to a cellml 2.0 file.
    """
    return os.path.join(CELLML_2_0_FILES, filename)


def validation_1_0(filename):
    """
    Returns the path to a 1.0 validation file.
    """
    return os.path.join(VALIDATION_1_0_FILES, filename)


def validation_1_1(filename):
    """
    Returns the path to a 1.1 validation file.
    """
    return os.path.join(VALIDATION_1_1_FILES, filename)


def validation_2_0(filename):
    """
    Returns the path to a 2.0 validation file.
    """
    return os.path.join(VALIDATION_2_0_FILES, filename)


# Map common schemas to local copies
CATALOG_DIR = os.path.join(MODULE_DIR, '..', 'catalog')
catalog = {
    'http://www.cellml.org/tools/cellml_1_1_schema/mathml2.xsd':
        os.path.join(CATALOG_DIR, 'mathml2', 'mathml2.xsd'),
# <import namespace="http://www.w3.org/1999/xlink" schemaLocation="http://www.cellml.org/tools/cellml_1_1_schema/common/xlink-href.xsd
}


class SchemaResolver(etree.Resolver):
    """
    Redirects URL requests for known XML Schemas to the local catalog.
    """
    def resolve(self, url, id, context):
        filename = catalog.get(url, None)
        if filename is not None:
            filename = os.path.abspath(filename)
            if not os.path.exists(filename) and os.path.isfile(filename):
                raise Exception('Catalog path does not exist: ' + filename)
            return self.resolve_filename(filename, context)
        return None


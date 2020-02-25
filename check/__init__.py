#
# Main module for CellML validation tests
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals


#
# Namespaces
#
CELLML_1_0_NS = 'http://www.cellml.org/cellml/1.0#'
CELLML_1_1_NS = 'http://www.cellml.org/cellml/1.1#'
CELLML_2_0_NS = 'http://www.cellml.org/cellml/2.0#'


#
# Paths to validation and model files
#
import os, inspect   # noqa
try:
    frame = inspect.currentframe()
    MODULE_DIR = os.path.dirname(inspect.getfile(frame))
finally:
    del(frame)
del(inspect)

# Validation files
CELLML_ROOT = os.path.abspath(os.path.join(MODULE_DIR, '..'))
CELLML_1_0_DIR = os.path.join(CELLML_ROOT, 'cellml_1_0')
CELLML_1_1_DIR = os.path.join(CELLML_ROOT, 'cellml_1_1')
CELLML_2_0_DIR = os.path.join(CELLML_ROOT, 'cellml_2_0')

# Model files
MODEL_ROOT = os.path.abspath(os.path.join(MODULE_DIR, '..'))
MODELS_1_0_DIR = os.path.join(MODEL_ROOT, 'models_1_0')
MODELS_1_1_DIR = os.path.join(MODEL_ROOT, 'models_1_1')
MODELS_2_0_DIR = os.path.join(MODEL_ROOT, 'models_2_0')

# Reports
REPORT_DIR = os.path.abspath(os.path.join(MODULE_DIR, '..', 'reports'))

del(os)


#
# Import functions
#
from ._schema_resolver import SchemaResolver    # noqa
from ._loaders import (     # noqa
    cellml_1_0,
    cellml_1_1,
    cellml_2_0,
    model_1_0,
    model_1_1,
    model_2_0,
)
from ._validation import (  # noqa
    dtd_1_0,
    myokit,
    opencor,
    relaxng_1_0,
    schema_1_0,
)


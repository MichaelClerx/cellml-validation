#
# Main module for CellML validation tests
#

# Get paths
import os, inspect
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

def cellml_1_0(filename):
    """
    Returns the path to a cellml 1.0 file.
    """
    return os.path.join(CELLML_1_0_files, filename)

def cellml_1_1(filename):
    """
    Returns the path to a cellml 1.1 file.
    """
    return os.path.join(CELLML_1_1_files, filename)

def cellml_2_0(filename):
    """
    Returns the path to a cellml 2.0 file.
    """
    return os.path.join(CELLML_2_0_files, filename)

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


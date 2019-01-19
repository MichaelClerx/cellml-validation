#
# Methods for loading model and validation files
#
import os

import check


def cellml_1_0(filename):
    """
    Returns the path to a CellML 1.0 validation file.
    """
    return os.path.join(check.CELLML_1_0_DIR, filename)


def cellml_1_1(filename):
    """
    Returns the path to a CellML 1.1 validation file.
    """
    return os.path.join(check.CELLML_1_1_DIR, filename)


def cellml_2_0(filename):
    """
    Returns the path to a CellML 2.0 validation file.
    """
    return os.path.join(check.CELLML_2_0_DIR, filename)


def model_1_0(*filename):
    """
    Returns the path to a CellML 1.0 file.
    """
    return os.path.join(check.MODELS_1_0_DIR, *filename)


def model_1_1(*filename):
    """
    Returns the path to a CellML 1.1 file.
    """
    return os.path.join(check.MODELS_1_1_DIR, *filename)


def model_2_0(*filename):
    """
    Returns the path to a CellML 2.0 file.
    """
    return os.path.join(check.MODELS_2_0_DIR, *filename)


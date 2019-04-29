#
# Validate models with cellmlmanip
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

from cellmlmanip import load_model


def parse(path):
    """ Runs a CellML file through cellmlmanip. """

    try:
        model = load_model(path)
        assert len(model.check_dummy_metadata()[1]) == 0
        assert model.check_cmeta_id()
        assert model.check_dummy_assignment()
        for e in model.equations:
            model.check_left_right_units_equal(e)
    except Exception as e:
        return False, str(e)
    return True, 'ok'


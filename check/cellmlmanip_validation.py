#
# Validate models with cellmlmanip
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals


_CELLMLMANIP_FOUND = None


def supported():
    """
    Returns ``True`` iff cellmlmanip validation is supported in this
    installation.
    """
    global _CELLMLMANIP_FOUND

    if _CELLMLMANIP_FOUND is None:
        try:
            import cellmlmanip   # noqa
            _CELLMLMANIP_FOUND = True
        except ImportError:
            _CELLMLMANIP_FOUND = False

    return _CELLMLMANIP_FOUND


def parse(path):
    """ Runs a CellML file through cellmlmanip. """

    if not supported():
        raise RuntimeError(
            'No Myokit support detected (or outdated version of Myokit found).'
            ' Please install a recent version of Myokit into this Python'
            ' system.')

    from cellmlmanip import load_model
    try:
        model = load_model(path)
        # Do some manual checking
        for e in model.equations:
            model.check_left_right_units_equal(e)
    except Exception as e:
        return False, str(e)
    return True, 'ok'


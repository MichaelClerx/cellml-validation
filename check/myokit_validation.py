#
# Validate models with Myokit
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import logging

_MYOKIT_FOUND = None


def supported():
    """
    Returns ``True`` iff Myokit validation is supported in this installation.
    """
    global _MYOKIT_FOUND
    if _MYOKIT_FOUND is None:
        _MYOKIT_FOUND = False
        try:
            import myokit   # noqa
            major, minor, revision = myokit.__version_tuple__[:3]
            if major < 1 or minor < 30:
                log = logging.getLogger(__name__)
                log.info('Myokit must be at least version 1.30.0.')
            else:
                _MYOKIT_FOUND = True
        except ImportError:
            pass
    return _MYOKIT_FOUND


def parse(path):
    """
    Runs a CellML file through Myokit.

    Returns a tuple ``(valid, message)`` where ``valid`` is a boolean and
    ``message`` is a string.
    """

    if not supported():
        raise RuntimeError(
            'No Myokit support detected (or outdated version of Myokit found).'
            ' Please install a recent version of Myokit into this Python'
            ' system.')

    import myokit.formats.cellml.v1 as cellml
    p = cellml.CellMLParser()
    try:
        p.parse_file(path)
    except cellml.CellMLParsingError as e:
        return False, str(e)
    else:
        return True, 'OK'


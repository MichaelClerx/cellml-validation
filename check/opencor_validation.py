#
# Validate models with OpenCOR
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import os
import subprocess


# Location of OpenCOR binary
OPENCOR = '/home/michael/dev/ext/opencor/OpenCOR-2021-10-05-Linux/bin/OpenCOR'


def supported():
    """
    Returns ``True`` iff OpenCOR validation is supported in this installation.
    """
    return os.path.isfile(OPENCOR)


def parse(path):
    """
    Runs a CellML file through OpenCOR.

    Returns a tuple ``(return_code, stdout, stderr)`` where ``return_code`` is
    the return code from calling the OpenCOR process, while ``stdout`` and
    ``stderr`` and the processes standard output and error output respectively.
    """

    if not supported():
        raise RuntimeError(
            'No OpenCOR support detected. Please update opencor_validation.py'
            ' with the correct location of an OpenCOR executable. Currently'
            ' pointed at ' + OPENCOR)

    cmd = [OPENCOR] + [
        '-c',
        'CellMLTools::validate',
        path,
    ]

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        stdout, stderr = p.communicate()
        ret = p.returncode
    except KeyboardInterrupt:
        try:
            p.terminate()
        except OSError:
            pass
        p.communicate()
        raise

    return ret, stdout.decode(), stderr.decode()


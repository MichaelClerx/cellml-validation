#
# Validate models with OpenCOR
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import os
import subprocess


# Location of OpenCOR binary
OPENCOR = '/home/michael/dev/ext/opencor/OpenCOR-2019-02-01-Linux/bin/OpenCOR'

if not os.path.isfile(OPENCOR):
    raise Exception(
        'Please update opencor_validation.py with the correct locaiton of the'
        ' OpenCOR binary.')


def parse(path):
    """ Runs a CellML file through OpenCOR. """

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


#
# Validation methods
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import re
import sys
from lxml import etree

import check

from . import cellmlmanip_validation
from . import myokit_validation
from . import opencor_validation


def colored(color, text):
    colors = {
        'normal': '\033[0m',
        'warning': '\033[93m',
        'fail': '\033[91m',
        'bold': '\033[1m',
        'underline': '\033[4m',
    }
    return colors[color] + str(text) + colors['normal']


def cellmlmanip(filename):
    """
    Validates ``filename`` in cellmlmanip, prints the result and then exits.
    """
    ok, msg = cellmlmanip_validation.parse(filename)

    if ok:
        print(
            colored('warning', '[pass]')
            + ' This file validates in cellmlmanip.')
        sys.exit(0)
    else:
        print(colored('fail', '[fail]'))
        print(msg)
        sys.exit(1)


def dtd_1_0(filename):
    """
    Validates ``filename`` against the CellML 1.0 DTD, prints the result and
    then exits.
    """
    # Create lxml parser
    parser = etree.XMLParser(no_network=True)

    # Create xml object
    xml = etree.parse(filename, parser)

    # Create DTD object
    dtd = etree.DTD(check.cellml_1_0('cellml_1_0.dtd'))

    # Validate
    if dtd.validate(xml):
        print(
            colored('warning', '[pass]')
            + ' This file validates against the CellML 1.0 DTD.')
        sys.exit(0)
    else:
        for e in dtd.error_log:
            r = re.compile(re.escape('{' + check.CELLML_1_0_NS + '}'))
            print(colored('fail', '[fail]') + ' Error on line ' + str(e.line))
            print(r.sub('cellml:', e.message))
        print()
        sys.exit(1)


def myokit(filename):
    """
    Validates ``filename`` using Myokit, prints the result, and then exits.
    """
    ok, msg = myokit_validation.parse(filename)
    if ok:
        print(colored('warning', '[pass]') + ' This file validates in Myokit.')
        sys.exit(0)
    else:
        print(colored('fail', '[fail]'))
        print(msg)
        sys.exit(1)


def opencor(filename):
    """
    Validates ``filename`` against the CellML API by running it through
    OpenCOR, prints the result and then exits.
    """
    ret, out, err = opencor_validation.parse(filename)
    if ret == 0:
        print(
            colored('warning', '[pass]')
            + ' This file validates against OpenCOR.')
        sys.exit(0)
    else:
        print(colored('fail', '[fail]'))
        for line in out.splitlines() + err.splitlines():
            print(line)
        sys.exit(1)


def relaxng_1_0(filename):
    """
    Validates ``filename`` against the CellML 1.0 RELAX NG schema, prints the
    result and then exits.
    """
    # Create lxml parser
    parser = etree.XMLParser(no_network=True)

    # Create xml object
    xml = etree.parse(filename, parser)

    # Create RelaxNG object
    rnc = etree.RelaxNG(
        etree.parse(check.cellml_1_0('cellml_1_0.rng'), parser))

    # Validate
    if rnc.validate(xml):
        print(
            colored('warning', '[pass]')
            + ' This file validates against the CellML 1.0 RELAX NG schema.')
        sys.exit(0)
    else:
        for e in rnc.error_log:
            r = re.compile(re.escape('{' + check.CELLML_1_0_NS + '}'))
            print(colored('fail', '[fail]') + ' Error on line ' + str(e.line))
            print(r.sub('cellml:', e.message))
        print()
        sys.exit(1)


def schema_1_0(filename):
    """
    Validates ``filename`` against the CellML 1.0 schema, prints the result and
    then exits.
    """
    # Create lxml parser
    parser = etree.XMLParser(no_network=True)
    parser.resolvers.add(check.SchemaResolver())

    # Create xml object
    xml = etree.parse(filename, parser)

    # Create schema object
    schema = etree.XMLSchema(
        etree.parse(check.cellml_1_0('cellml_1_0.xsd'), parser))

    # Validate
    if schema.validate(xml):
        print(
            colored('warning', '[pass]')
            + ' This file validates against the CellML 1.0 schema.')
        sys.exit(0)
    else:
        for e in schema.error_log:
            r = re.compile(re.escape('{' + check.CELLML_1_0_NS + '}'))
            print(colored('fail', '[fail]') + ' Error on line ' + str(e.line))
            print(r.sub('cellml:', e.message))
        print()
        sys.exit(1)


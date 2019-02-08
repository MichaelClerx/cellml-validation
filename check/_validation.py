#
# Validation methods
#
import re
import sys
from lxml import etree

import check


def colored(color, text):
    colors = {
        'normal': '\033[0m',
        'warning': '\033[93m',
        'fail': '\033[91m',
        'bold': '\033[1m',
        'underline': '\033[4m',
    }
    return colors[color] + str(text) + colors['normal']


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
        e = dtd.error_log.last_error
        r = re.compile(re.escape('{' + check.CELLML_1_0_NS + '}'))
        print(colored('fail', '[fail]') + ' Error on line ' + str(e.line))
        print(r.sub('cellml:', e.message))
        print()
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
        e = rnc.error_log.last_error
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
        e = schema.error_log.last_error
        r = re.compile(re.escape('{' + check.CELLML_1_0_NS + '}'))
        print(colored('fail', '[fail]') + ' Error on line ' + str(e.line))
        print(r.sub('cellml:', e.message))
        print()
        sys.exit(1)


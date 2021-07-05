#
# Command line tools for CellML validation
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals


def main():
    """
    Parses command line arguments
    """
    import sys

    # Create parser
    import argparse
    parser = argparse.ArgumentParser(
        usage='python check',
        description='Command line validation tools.',
    )
    subparsers = parser.add_subparsers(
        description='Select one of the available commands from the list below',
        title='Commands',
    )

    # Load tool dependent validation modules
    from . import (
        cellmlmanip_validation,
        myokit_validation,
        opencor_validation,
    )

    # Add subparsers, in alphabetical order
    if cellmlmanip_validation.supported():
        add_cellmlmanip_parser(subparsers)
    add_dtd_1_0_parser(subparsers)
    if myokit_validation.supported():
        add_myokit_parser(subparsers)
    if opencor_validation.supported():
        add_opencor_parser(subparsers)
    add_relaxng_1_0_parser(subparsers)
    add_schema_1_0_parser(subparsers)
    add_xslt_1_0_to_1_1_parser(subparsers)
    add_xslt_1_to_2_parser(subparsers)

    # Parse!
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()

        # Get the args' objects attributes as a dictionary
        args = vars(args)

        # Split into function and arguments
        func = args['func']
        del(args['func'])

        # Call the selected function with the parsed arguments
        func(**args)


def add_cellmlmanip_parser(subparsers):
    """
    Adds a subcommand parser for ``cellmlmanip``.
    """
    parser = subparsers.add_parser(
        'cellmlmanip',
        description='Validates a CellML file using cellmlmanip.',
        help='Validates a CellML file using cellmlmanip.',
    )
    parser.add_argument(
        'filename',
        metavar='filename',
        help='The CellML file to validate.',
    )
    parser.set_defaults(func=cellmlmanip)


def add_dtd_1_0_parser(subparsers):
    """
    Adds a subcommand parser for ``dtd_1_0``.
    """
    parser = subparsers.add_parser(
        'dtd_1_0',
        description='Validates a CellML file against the 1.0 DTD.',
        help='Validates a CellML file against the 1.0 DTD.',
    )
    parser.add_argument(
        'filename',
        metavar='filename',
        help='The CellML file to validate.',
    )
    parser.set_defaults(func=dtd_1_0)


def add_myokit_parser(subparsers):
    """
    Adds a subcommand parser for ``myokit``.
    """
    parser = subparsers.add_parser(
        'myokit',
        description='Validates a CellML file using Myokit.',
        help='Validates a CellML file using Myokit.',
    )
    parser.add_argument(
        'filename',
        metavar='filename',
        help='The CellML file to validate.',
    )
    parser.set_defaults(func=myokit)


def add_opencor_parser(subparsers):
    """
    Adds a subcommand parser for ``opencor``.
    """
    parser = subparsers.add_parser(
        'opencor',
        description='Validates a CellML file using OpenCOR.',
        help='Validates a CellML file against the CellML API, via OpenCOR.',
    )
    parser.add_argument(
        'filename',
        metavar='filename',
        help='The CellML file to validate.',
    )
    parser.set_defaults(func=opencor)


def add_relaxng_1_0_parser(subparsers):
    """
    Adds a subcommand parser for ``relaxng_1_0``.
    """
    parser = subparsers.add_parser(
        'relaxng_1_0',
        description='Validates a CellML file against the 1.0 RELAX NG schema.',
        help='Validates a CellML file against the 1.0 RELAX NG schema.',
    )
    parser.add_argument(
        'filename',
        metavar='filename',
        help='The CellML file to validate.',
    )
    parser.set_defaults(func=relaxng_1_0)


def add_schema_1_0_parser(subparsers):
    """
    Adds a subcommand parser for ``schema_1_0``.
    """
    parser = subparsers.add_parser(
        'schema_1_0',
        description='Validates a CellML file against the 1.0 schema.',
        help='Validates a CellML file against the 1.0 schema.',
    )
    parser.add_argument(
        'filename',
        metavar='filename',
        help='The CellML file to validate.',
    )
    #parser.add_argument(
    #    '--hello',
    #    action='store_true',
    #    help='Do a special thing.',
    #)
    parser.set_defaults(func=schema_1_0)


def add_xslt_1_0_to_1_1_parser(subparsers):
    """
    Adds a subcommand parser for `xslt_1_0_to_1_1`.
    """
    parser = subparsers.add_parser(
        'xslt_1_0_to_1_1',
        description='Converts from 1.0 to 1.1, using XSLT.',
        help='Converts from 1.0 to 1.1, using XSLT.',
    )
    parser.add_argument(
        'path1',
        metavar='path1',
        help='The CellML 1.0 file to convert.',
    )
    parser.add_argument(
        'path2',
        metavar='path2',
        help='The path to write a CellML 1.1 file to.',
    )
    parser.set_defaults(func=xslt_1_0_to_1_1)


def add_xslt_1_to_2_parser(subparsers):
    """
    Adds a subcommand parser for `xslt_1_to_2`.
    """
    parser = subparsers.add_parser(
        'xslt_1_to_2',
        description='Converts from 1.0 or 1.1 to 2.0, using XSLT.',
        help='Converts from 1.0 or 1.1 to 2.0, using XSLT.',
    )
    parser.add_argument(
        'path1',
        metavar='path1',
        help='The CellML 1.0 or 1.1 file to convert.',
    )
    parser.add_argument(
        'path2',
        metavar='path2',
        help='The path to write a CellML 2.0 file to.',
    )
    parser.set_defaults(func=xslt_1_to_2)


def cellmlmanip(filename):
    """
    Validates a cellml file using cellmlmanip.
    """
    filename = str(filename)

    import os
    import sys
    if not os.path.exists(filename):
        print('File not found: ' + filename)
        sys.exit(1)
    if not os.path.isfile(filename):
        print('Not a file: ' + filename)
        sys.exit(1)

    import check
    check.cellmlmanip(filename)


def dtd_1_0(filename):
    """
    Validates a cellml file against the 1.0 DTD.
    """
    filename = str(filename)

    import os
    import sys
    if not os.path.exists(filename):
        print('File not found: ' + filename)
        sys.exit(1)
    if not os.path.isfile(filename):
        print('Not a file: ' + filename)
        sys.exit(1)

    import check
    check.dtd_1_0(filename)


def myokit(filename):
    """
    Validates a cellml file using Myokit.
    """
    filename = str(filename)

    import os
    import sys
    if not os.path.exists(filename):
        print('File not found: ' + filename)
        sys.exit(1)
    if not os.path.isfile(filename):
        print('Not a file: ' + filename)
        sys.exit(1)

    import check
    check.myokit(filename)


def opencor(filename):
    """
    Validates a cellml file using OpenCOR.
    """
    filename = str(filename)

    import os
    import sys
    if not os.path.exists(filename):
        print('File not found: ' + filename)
        sys.exit(1)
    if not os.path.isfile(filename):
        print('Not a file: ' + filename)
        sys.exit(1)

    import check
    check.opencor(filename)


def relaxng_1_0(filename):
    """
    Validates a cellml file against the 1.0 RELAX NG schema.
    """
    filename = str(filename)

    import os
    import sys
    if not os.path.exists(filename):
        print('File not found: ' + filename)
        sys.exit(1)
    if not os.path.isfile(filename):
        print('Not a file: ' + filename)
        sys.exit(1)

    import check
    check.relaxng_1_0(filename)


def schema_1_0(filename):
    """
    Validates a cellml file against the 1.0 schema.
    """
    filename = str(filename)

    import os
    import sys
    if not os.path.exists(filename):
        print('File not found: ' + filename)
        sys.exit(1)
    if not os.path.isfile(filename):
        print('Not a file: ' + filename)
        sys.exit(1)

    import check
    check.schema_1_0(filename)


def xslt_1_0_to_1_1(path1, path2):
    """
    Converts a CellML 1.0 file to CellML 1.1 using XSLT.
    """
    path1 = str(path1)
    path2 = str(path2)

    import os
    import sys
    if not os.path.exists(path1):
        print('File not found: ' + path1)
        sys.exit(1)
    if not os.path.isfile(path1):
        print('Not a file: ' + path1)
        sys.exit(1)
    print('Looking for CellML 1.0 file at: ' + path1)

    if os.path.exists(path2):
        if not os.path.isfile(path2):
            print('Cannot write to: ' + path2)
            sys.exit(1)
        else:
            print('Overwriting file at: ' + path2)

    import check
    check.xslt_1_0_to_1_1(path1, path2)
    print('CellML 1.1 written to: ' + path2)


def xslt_1_to_2(path1, path2):
    """
    Converts a CellML 1 file to CellML 2 using XSLT.
    """
    path1 = str(path1)
    path2 = str(path2)

    import os
    import sys
    if not os.path.exists(path1):
        print('File not found: ' + path1)
        sys.exit(1)
    if not os.path.isfile(path1):
        print('Not a file: ' + path1)
        sys.exit(1)
    print('Looking for CellML 1.0 or 1.1 file at: ' + path1)

    if os.path.exists(path2):
        if not os.path.isfile(path2):
            print('Cannot write to: ' + path2)
            sys.exit(1)
        else:
            print('Overwriting file at: ' + path2)

    import check
    check.xslt_1_to_2(path1, path2)
    print('CellML 2.0 written to: ' + path2)


if __name__ == '__main__':
    main()

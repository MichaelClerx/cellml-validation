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

    # Add subparsers
    add_schema_1_0_parser(subparsers)

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


def schema_1_0(filename):
    """
    Validates a cellml file against the 1.0 schema
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


def add_schema_1_0_parser(subparsers):
    """
    Adds a subcommand parser for `schema_1_0`.
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


if __name__ == '__main__':
    main()

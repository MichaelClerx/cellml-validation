#!/usr/bin/env python3
#
# Compares the 1.0 and 1.1 model test sets.
#
# Call with:
#  python diff_10_11.py
# to show all unexpected changes.
#
# To show all changes, even the known ones, use
#  python diff_10_11.py --force
#
# To write the output to a file, use
#  python diff_10_11.py filename.txt
#
import argparse
import difflib
import os
import re
import sys


# Write to file or print
printing = True
_handle = None

# Show all or hide known
hide_known = True
known_only_0 = (
    # Xlink is an "extension namespace" in 1.0
    'valid/2.4.3.xlink_href_in_component.cellml',
    'valid/2.4.3.xlink_href_in_component_ref.cellml',
    'valid/2.4.3.xlink_href_in_connection.cellml',
    'valid/2.4.3.xlink_href_in_group.cellml',
    'valid/2.4.3.xlink_href_in_map_components.cellml',
    'valid/2.4.3.xlink_href_in_map_variables.cellml',
    'valid/2.4.3.xlink_href_in_model.cellml',
    'valid/2.4.3.xlink_href_in_reaction.cellml',
    'valid/2.4.3.xlink_href_in_relationship_ref.cellml',
    'valid/2.4.3.xlink_href_in_role.cellml',
    'valid/2.4.3.xlink_href_in_unit.cellml',
    'valid/2.4.3.xlink_href_in_units_1.cellml',
    'valid/2.4.3.xlink_href_in_units_2.cellml',
    'valid/2.4.3.xlink_href_in_variable.cellml',
    'valid/2.4.3.xlink_href_in_variable_ref.cellml',

    # Initial values can not be variables in 1.0
    'invalid/3.4.3.7.variable_with_initial_value_variable.cellml',
)
known_only_1 = (
    # Xlink is no longer an "extension namespace" in 1.1
    'invalid/2.4.3.xlink_href_in_component.cellml',
    'invalid/2.4.3.xlink_href_in_component_ref.cellml',
    'invalid/2.4.3.xlink_href_in_connection.cellml',
    'invalid/2.4.3.xlink_href_in_group.cellml',
    'invalid/2.4.3.xlink_href_in_map_components.cellml',
    'invalid/2.4.3.xlink_href_in_map_variables.cellml',
    'invalid/2.4.3.xlink_href_in_model.cellml',
    'invalid/2.4.3.xlink_href_in_reaction.cellml',
    'invalid/2.4.3.xlink_href_in_relationship_ref.cellml',
    'invalid/2.4.3.xlink_href_in_role.cellml',
    'invalid/2.4.3.xlink_href_in_unit.cellml',
    'invalid/2.4.3.xlink_href_in_units_1.cellml',
    'invalid/2.4.3.xlink_href_in_units_2.cellml',
    'invalid/2.4.3.xlink_href_in_variable.cellml',
    'invalid/2.4.3.xlink_href_in_variable_ref.cellml',

    # Initial values can be variables in 1.1
    'valid/3.4.3.7.variable_with_initial_value_child_var.cellml',
    'valid/3.4.3.7.variable_with_initial_value_parent_var.cellml',
    'valid/3.4.3.7.variable_with_initial_value_sibling_var.cellml',
    'valid/3.4.3.7.variable_with_initial_value_variable.cellml',
    'valid/3.4.3.7.variable_with_initial_value_variable_math_1.cellml',
    'valid/3.4.3.7.variable_with_initial_value_variable_math_2.cellml',
    'valid/3.4.3.7.variable_with_initial_value_variable_math_3.cellml',
    'invalid/3.4.3.7.variable_with_initial_value_nonexistent_variable_1.cellml',    # noqa
    'invalid/3.4.3.7.variable_with_initial_value_nonexistent_variable_2.cellml',    # noqa

    # 1.1 has new rules for identifiers
    'invalid/2.4.1.identifier_no_letter.cellml',
    'invalid/2.4.1.identifier_starting_with_number.cellml',
)
known_diff = (
    # 1.1 has new rules for identifiers
    'valid/2.4.1.valid_identifiers.cellml',
)
skipped = 0

# https://stackoverflow.com/questions/4842424
bold = 1
red = 31
cyan = 32
yellow = 33
blue = 34
Cyan = 92
Yellow = 93
Blue = 94

# Regex to strip html comments
_comment = re.compile('<!--.+?-->', flags=re.DOTALL)

# Differ
_d = difflib.Differ()


def s(code, text):
    """ Returns styled text. """
    if printing:
        return f'\033[{code}m{text}\033[0m'
    return text


def w(text=''):
    """ Print text or write to file. """
    if printing:
        print(text)
    else:
        _handle.write(text + '\n')


def print_diff(lines):
    for line in lines:
        line = line.rstrip()
        if line == '':
            continue

        char = line[:1]
        if char == '?':
            continue
        elif char == '-':
            w(s(red, line))
        elif char == '+':
            w(s(cyan, line))
        else:
            w(line)


def diff(path1, name1, path2, name2):
    """
    Compare a CellML 1.0 and a CellML 1.1 file.
    """
    if hide_known and name1.lstrip('models_1_0/') in known_diff:
        global skipped
        skipped += 1
        return

    # Read full contents
    with open(path1) as f:
        a = a0 = f.read()
    with open(path2) as f:
        b = b0 = f.read()

    # Replace CellML namespaces with placeholders
    a = a.replace('http://www.cellml.org/cellml/1.0#', 'correct-ns')
    a = a.replace('http://www.cellml.org/cellml/1.1#', 'wrong-ns')
    b = b.replace('http://www.cellml.org/cellml/1.1#', 'correct-ns')
    b = b.replace('http://www.cellml.org/cellml/1.0#', 'wrong-ns')

    # Remove comments
    a = _comment.sub('', a)
    b = _comment.sub('', b)

    if a == b:
        return

    # Show difference
    w('=' * 90)
    w(s(bold, s(Blue, name2)))
    w()
    w(s(blue, 'meld ' + name1 + ' ' + name2))
    w('- ' * 45)

    x = _d.compare(a.splitlines(keepends=True), b.splitlines(keepends=True))
    print_diff(x)

    w('-' * 90)


def only_0(r):
    """ Show file that exists only in 1.0. """
    if hide_known and r.lstrip('models_1_0/') in known_only_0:
        global skipped
        skipped += 1
    else:
        w(s(yellow, '- ' + r))


def only_1(r):
    """ Show file that exists only in 1.1. """
    if hide_known and r.lstrip('models_1_1/') in known_only_1:
        global skipped
        skipped += 1
    else:
        w(s(Yellow, '+ ' + r))


def diff_dir(path1, path2, root):
    """
    Compare ``path1`` to ``path2`` (both given as absolute path names).

    When showing filenames to user, make them relative to ``root``.
    """

    paths1, paths2 = os.listdir(path1), os.listdir(path2)
    paths1.sort()
    paths2.sort()
    paths1, paths2 = iter(paths1), iter(paths2)

    def nxt(path, piter, subst=False):
        """ Return path, absolute path, path relative to root. """

        # Get next filename
        p = next(piter)
        while p.endswith('.md') or p.startswith('.'):
            p = next(piter)

        # Get absolute path, path relative to root
        q = os.path.join(path, p)
        r = os.path.relpath(q, root)

        # Make change to filename used in comparison, if needed
        if subst:
            p = p.replace('5.4.3', '5.4.2')

        return p, q, r

    try:
        p1, q1, r1 = nxt(path1, paths1)
        p2, q2, r2 = nxt(path2, paths2, True)

        while True:
            if p1 == p2:
                if os.path.isdir(q1) and os.path.isdir(q2):
                    diff_dir(q1, q2, root)
                elif os.path.isfile(q1) and os.path.isfile(q2):
                    diff(q1, r1, q2, r2)
                else:
                    w(s(red, 'File/directory mismatch: ') + r1)
                    w(p1, os.path.isdir(q1), os.path.isdir(q2))

                p1, q1, r1 = nxt(path1, paths1)
                p2, q2, r2 = nxt(path2, paths2, True)

            elif p1 < p2:
                while p1 < p2:
                    only_0(r1)
                    p1, q1, r1 = nxt(path1, paths1)
            else:
                while p2 < p1:
                    only_1(r2)
                    p2, q2, r2 = nxt(path2, paths2, True)

    except StopIteration:
        pass

    # Handle remaining files (if any)
    for p1 in paths1:
        q1 = os.path.join(path1, p1)
        r1 = os.path.relpath(q1, root)
        only_0(r1)

    for p2 in paths2:
        q2 = os.path.join(path2, p2)
        r2 = os.path.relpath(q2, root)
        only_1(r2)


if __name__ == '__main__':

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        usage='diff_10_11.py',
        description='Compares the 1.0 and 1.1 tests.',
    )
    parser.add_argument(
        'filename',
        default=None,
        nargs='?',
        metavar='filename',
        help='An optional filename to write the diff report to.',
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Show known changes.',
    )
    args = parser.parse_args()
    hide_known = not args.force
    filename = args.filename
    printing = filename is None
    del(args, parser)

    # Get absolute paths to model dirs
    path1 = os.path.abspath('models_1_0')
    path2 = os.path.abspath('models_1_1')
    root = os.path.abspath('')

    # Go!
    try:
        if not printing:
            _handle = open(sys.argv[1], 'w')
        diff_dir(path1, path2, root)
        if hide_known and skipped:
            w(f'Skipped {skipped} known changes (use --force to see all).')

    finally:
        if not printing:
            _handle.close()


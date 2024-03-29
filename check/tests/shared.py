#
# Shared methods for tests
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import os
import pytest
import re
from lxml import etree

import check


# Regex to find the CellML 1.0 namespace
r1_0 = re.compile(re.escape('{' + check.CELLML_1_0_NS + '}'))


def list_models_1_0(subdir):
    """
    Scans a path (without recursing into subdirectories) and returns a list of
    tuples ``(name, path)`` representing each file.
    """
    files = []
    subdir = check.model_1_0(subdir)
    for filename in os.listdir(subdir):
        name, ext = os.path.splitext(filename)
        if ext == '.cellml':
            files.append(pytest.param(
                name, os.path.join(subdir, filename), id=name))

    files.sort(key=lambda x: x[0])
    return files


def list_passes_1_0(debug=False):
    """
    Returns a list of ``pytest.param`` objects for CellML 1.0 models that
    should pass validation.

    If ``debug=False`` is set, only a single model is returned.
    """
    # Valid models
    files = list_models_1_0('valid')

    # There are no strict rules about bools (in the spec), so these should pass
    files += list_models_1_0('booleans')

    # Models are allowed to be overdefined
    files += list_models_1_0('overdefined')

    # Numbers are all valid MathML2, so should pass schema validation
    files += list_models_1_0('numbers')

    # Units do not affect validity, so these should all pass
    files += list_models_1_0('unit_checking_consistent')
    files += list_models_1_0('unit_checking_inconsistent')
    files += list_models_1_0('unit_conversion_convertible')
    files += list_models_1_0('unit_conversion_inconvertible')

    if debug:
        return files[:1]
    return files


def list_fails_1_0(debug=False):
    """
    Returns a list of ``pytest.param`` objects for CellML 1.0 models that
    should fail validation.

    If ``debug=False`` is set, only a single model is returned.
    """
    files = list_models_1_0('invalid')

    # Duplicate connections should probably be disallowed
    files += list_models_1_0('duplicate_connections')

    # Deca- is an official prefix, but CellML prefers deka-
    files += list_models_1_0('unit_deca')

    # Units elements with base_units="no" should not be empty
    files += list_models_1_0('units_empty')

    if debug:
        return files[:1]
    return files


def assert_valid(report, name, path, parser, validator, false_negatives, log):
    """
    Tries validating a valid file, and tests if the results are expected.

    - If the validator agrees the model is valid, the test passes.
    - If the validator agrees the model is valid, but this was not expected,
      the test result is a ``fail``.
    - If the validator does not pass the file, but this was expected, the test
      result is an ``xfail``.
    - If the validator does not pass the file, in an unexpected way, the test
      result is a ``fail``.

    Arguments:

    ``name``
        A string identifying the model
    ``path``
        The path to the model file
    ``parser``
        An XML parser
    ``validator``
        An lxml validator (e.g. a schema, dtd, relaxng etc.)
    ``false_negatives``
        A dict mapping model names to expected error messages.
    ``log``
        A logging object for error messages.

    """
    # See if there's an expected false negative for this model
    expected_error = false_negatives.get(name, None)

    # Parse and validate
    xml = etree.parse(path, parser)
    valid = validator.validate(xml)

    if valid:
        # Report valid passed
        report.valid_passed(name, path)

        # Let the user know if a listed false negative is actually handled
        # correctly
        if expected_error is not None:
            log.error('Unexpected pass for ' + name)
            log.error('Expected error: ' + expected)
            log.error('But model passed validation.')
            pytest.xpass()

    else:
        # Report valid failed
        lmsg = []
        for e in validator.error_log:
            msg = r1_0.sub('cellml:', e.message)
            lmsg.append('Error on line ' + str(e.line) + ': ' + msg)
        lmsg = '\n'.join(lmsg)
        report.valid_failed(name, path, lmsg)

        # Check for unexpected fails
        if expected_error is None:
            log.error('Unexpected error in ' + name)
            for e in validator.error_log:
                msg = r1_0.sub('cellml:', e.message)
                log.error('Error on line ' + str(e.line) + ': ' + msg)
            pytest.fail()

        else:
            # Scan logged errors for expected error
            expected_found = False
            for e in validator.error_log:
                msg = r1_0.sub('cellml:', e.message)
                if expected_error in msg:
                    expected_found = True
                    break

            if expected_found:
                pytest.xfail()
            else:
                log.error('Unexpected error in ' + name)
                log.error('Expected: ' + expected_error)
                for e in validator.error_log:
                    msg = r1_0.sub('cellml:', e.message)
                    log.error('Error on line ' + str(e.line) + ': ' + msg)
                pytest.fail()


def assert_invalid(
        report, name, path, parser, validator, expected_messages, known_issues,
        log):
    """
    Tries validating an invalid file, and tests if the results are expected.

    - If the validator agrees the model is invalid, and returns the expected
      error message, the test result is a ``pass``.
    - If the validator agrees the model is invalid, but returns an unexpected
      error message, the test result is a ``fail``.
    - If the validator fails to detect the correct error, and this is listed as
      a known issue, the test result is an ``xfail``.

    Arguments:

    ``name``
        A string identifying the model
    ``path``
        The path to the model file
    ``parser``
        An XML parser
    ``validator``
        An lxml validator (e.g. a schema, dtd, relaxng etc.)
    ``expected_messages``
        A dict mapping model names to expected error messages.
    ``known_issues``
        A set of model names that are known to validate even though they should
        not.
    ``log``
        A logging object for error messages.

    """
    # See if there's an expected error for this model
    expected_error = expected_messages.get(name, None)
    expected_issue = name in known_issues

    # Parse model
    try:
        xml = etree.parse(path, parser)
    except etree.XMLSyntaxError as e:

        # Check if we expected this parsing problem (pass!)
        msg = str(e)
        if (expected_error is not None) and expected_error in msg:
            report.invalid_failed(name, path, expected_error, msg)
            return

        # Report unexpected parsing problem
        report.invalid_failed_incorrectly(name, path, expected_error, msg)
        log.error('Unexpected parse error in ' + name)
        log.error(msg)
        pytest.fail()
        return

    # Validate model
    valid = validator.validate(xml)

    if valid:
        report.invalid_passed(name, path, expected_error)

        # Check if this was expected
        if expected_issue:
            pytest.xfail()
        else:
            # Unexpected pass
            log.error('Unexpected pass in ' + name)
            if expected_error is not None:
                log.error('Expected error: ' + expected_error)
            else:
                log.error('No expected error set')
            pytest.fail()

    else:

        # Check if expected error set
        if expected_error is None:

            # Expected error not set: Test designer needs to update tests.
            # Don't report: don't know what the outcome should be!
            log.error('Unknown error in invalid file: ' + name)
            log.error('Found this error:')
            for e in validator.error_log:
                msg = r1_0.sub('cellml:', e.message)
                log.error('Error on line ' + str(e.line) + ': ' + msg)
            log.error('But no expected error set, please update test file.')
            pytest.fail()

        else:

            # Scan logged errors for expected one
            expected_found = False
            for e in validator.error_log:
                msg = r1_0.sub('cellml:', e.message)
                if expected_error in msg:
                    expected_found = True
                    break

            # Compose multi-line error message
            lmsg = []
            for e in validator.error_log:
                msg = r1_0.sub('cellml:', e.message)
                lmsg.append('Error on line ' + str(e.line) + ': ' + msg)
            lmsg = '\n'.join(lmsg)

            # Check if test OK
            if expected_found:
                report.invalid_failed(name, path, expected_error, lmsg)
            else:
                report.invalid_failed_incorrectly(
                    name, path, expected_error, lmsg)

                if expected_issue:
                    pytest.xfail()
                else:
                    log.error('Unexpected error in ' + name)
                    for e in validator.error_log:
                        msg = r1_0.sub('cellml:', e.message)
                        log.error('Error on line ' + str(e.line) + ': ' + msg)
                    log.error('Expected error: ' + expected_error)
                    pytest.fail()


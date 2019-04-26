#
# Generates a report about the performance of a validation method.
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import os

from . import shared


class Report(object):
    """
    Gathers test results and generates reports about the performance of a
    validation method.
    """
    def __init__(self, name):
        self._name = str(name) or 'No title'
        self._results = {}
        self._all_tests = self._list_all_tests()

    def _list_all_tests(self):
        raise NotImplementedError()

    def valid_passed(self, name, path):
        """ Report that a valid file passed validation. """
        name = str(name)
        if name in self._results:
            raise Exception('Duplicate test result for: ' + name)
        self._results[name] = ValidPassed(name, path)

    def valid_failed(self, name, path, message):
        """ Report that a valid file failed to pass validation. """
        name = str(name)
        if name in self._results:
            raise Exception('Duplicate test result for: ' + name)
        self._results[name] = ValidFailed(name, path, message)

    def invalid_passed(self, name, path, expected):
        """ Report that an invalid file passed validation. """
        name = str(name)
        if name in self._results:
            raise Exception('Duplicate test result for: ' + name)
        self._results[name] = InvalidPassed(name, path, expected)

    def invalid_failed(self, name, path, expected, message):
        """ Report that the error in an invalid file was detected. """
        name = str(name)
        if name in self._results:
            raise Exception('Duplicate test result for: ' + name)
        self._results[name] = InvalidFailed(name, path, message, expected)

    def invalid_failed_incorrectly(self, name, path, expected, message):
        """
        Report that an invalid file failed validation, but for the wrong
        reasons.
        """
        name = str(name)
        if name in self._results:
            raise Exception('Duplicate test result for: ' + name)
        self._results[name] = InvalidFailedIncorrectly(
            name, path, message, expected)

    def render(self, path):
        """
        Renders this report, storing the result as a markdown file in the given
        ``path``.
        """
        # Header and body
        h = []
        b = []

        # Add title to header
        e = ''
        h.append('# ' + self._name)
        h.append(e)

        # Count
        valid_passed = 0
        valid_failed = 0
        invalid_passed = 0
        invalid_failed = 0
        invalid_failed_incorrectly = 0
        not_run = 0
        extra = 0

        # Create body
        efail = '❌ '
        ebad1 = '❗ '
        ebad2 = '❗❗❗ '
        pre1 = '* '
        pre2 = '  * '

        # Loop over known tests, show results
        last = [-1, -1, -1, -1]
        level = 0
        for test in self._all_tests:

            # Split index part from textual test name
            code = []
            for x in test.split('.'):
                if not x.isdigit():
                    break
                code.append(int(x))
            next = code + [0] * (4 - len(code))

            # Determine heading level
            if last == next:
                header = 6
            else:
                header = 2
                for i in range(4):
                    if next[i] > last[i]:
                        break
                    header += 1
                last = next

            # Write header
            if header < 6:
                b.append(e)
                b.append('#' * header + ' ' + '.'.join([str(x) for x in code]))
                b.append(e)

            # Get path to test file
            r = self._results.get(test, None)
            if r:
                rpath = os.path.relpath(r.path, os.path.basename(path))
                name = '[' + test + '](' + rpath + ')'
            else:
                name = '`' + test + '`'
            name += ': '

            # Show result
            if isinstance(r, ValidPassed):
                valid_passed += 1
                b.append(name + 'Valid file passed OK')
            elif isinstance(r, ValidFailed):
                valid_failed += 1
                b.append(efail + name + 'Valid file failed validation')
                b.append(pre1 + 'Returned: ')
                for line in r.message.splitlines():
                    b.append(pre2 + line)
            elif isinstance(r, InvalidPassed):
                invalid_passed += 1
                b.append(efail + name + 'Invalid file passed validation')
                if r.expected:
                    b.append(pre1 + 'Expected: ' + r.expected)
            elif isinstance(r, InvalidFailed):
                invalid_failed += 1
                b.append(name + 'Error in invalid file detected')
                #b.append(pre1 + 'Expected: ' + r.expected)
                #b.append(pre1 + 'Returned: ')
                #for line in r.message.splitlines():
                #    b.append(pre2 + line)
            elif isinstance(r, InvalidFailedIncorrectly):
                invalid_failed_incorrectly += 1
                b.append(ebad1 + name +
                         'Invalid file failed validation for wrong reason')
                if r.expected:
                    b.append(pre1 + 'Expected: ' + r.expected)
                b.append(pre1 + 'Returned: ')
                for line in r.message.splitlines():
                    b.append(pre2 + line)
            else:
                not_run += 1
                b.append(ebad2 + name + 'Test not run')
            b.append(e)

        # Show unknown tests
        extra = set(self._results.keys()) - set(self._all_tests)
        if extra:
            b.append('# Unknown tests found')
            for test in sorted(extra):
                b.append(ebad2 + '`' + name + '`')

        # Calculate scores
        valid_total = valid_passed + valid_failed
        invalid_total = (
            invalid_passed + invalid_failed + invalid_failed_incorrectly)
        total = valid_total + invalid_total
        correct = valid_passed + invalid_failed
        percent_correct = int(100 * correct / total) if total else 0

        # Update header
        h.append('Performance:')
        h.append(
            '* ' + str(percent_correct) + '% according to spec ('
            + str(correct) + ' out of ' + str(total) + ')')
        h.append(
            '* ' + str(valid_passed) + ' out of ' + str(valid_total)
            + ' valid files passed')
        h.append(
            '* ' + str(invalid_failed) + ' out of ' + str(invalid_total)
            + ' invalid files detected')
        h.append(e)
        h.append('Issues:')
        h.append(
            '* ' + str(valid_failed) + ' valid files failed to parse')
        h.append(
            '* ' + str(invalid_passed) + ' invalid files passed validation')
        h.append(
            '* ' + str(invalid_failed_incorrectly)
            + ' invalid files failed validation for the wrong reason')
        if not_run or extra:
            h.append(e)
            h.append('Test implementation issues')
            if extra:
                h.append('* ' + str(unknown) + ' unknown tests run')
            else:
                h.append('* ' + str(not_run) + ' tests not run')

        # Write tests to file
        with open(path, 'w') as f:
            f.write('\n'.join(h))
            f.write('\n')
            f.write('\n'.join(b))


class Report_1_0(Report):
    """
    CellML 1.0 Validation report. See :class:`Report`.
    """
    def __init__(self, name):
        super(Report_1_0, self).__init__(name)

    def _list_all_tests(self):
        tests = shared.list_passes_1_0() + shared.list_fails_1_0()
        tests = [t.values[0] for t in tests]
        print(tests[0])

        tests.sort()
        return tests


class Result(object):
    def __init__(self, name, path):
        self.name = str(name)
        self.path = str(path)


class ValidPassed(Result):
    def __init__(self, name, path):
        super(ValidPassed, self).__init__(name, path)


class ValidFailed(Result):
    def __init__(self, name, path, message):
        super(ValidFailed, self).__init__(name, path)
        self.message = str(message)


class InvalidPassed(Result):
    def __init__(self, name, path, expected):
        super(InvalidPassed, self).__init__(name, path)
        self.expected = str(expected) if expected else None


class InvalidFailed(Result):
    def __init__(self, name, path, message, expected):
        super(InvalidFailed, self).__init__(name, path)
        self.message = str(message)
        self.expected = str(expected)


class InvalidFailedIncorrectly(Result):
    def __init__(self, name, path, message, expected):
        super(InvalidFailedIncorrectly, self).__init__(name, path)
        self.message = str(message)
        self.expected = str(expected)

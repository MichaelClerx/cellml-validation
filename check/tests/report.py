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

    def valid_passed(self, name, path, output=''):
        """ Report that a valid file passed validation. """
        name = str(name)
        if name in self._results:
            raise Exception('Duplicate test result for: ' + name)
        self._results[name] = ValidPassed(name, path, output)

    def valid_failed(self, name, path, output=''):
        """ Report that a valid file failed to pass validation. """
        name = str(name)
        if name in self._results:
            raise Exception('Duplicate test result for: ' + name)
        self._results[name] = ValidFailed(name, path, output)

    def invalid_passed(self, name, path, expected, output=''):
        """ Report that an invalid file passed validation. """
        name = str(name)
        if name in self._results:
            raise Exception('Duplicate test result for: ' + name)
        self._results[name] = InvalidPassed(name, path, expected, output)

    def invalid_failed(self, name, path, expected, output=''):
        """ Report that the error in an invalid file was detected. """
        name = str(name)
        if name in self._results:
            raise Exception('Duplicate test result for: ' + name)
        self._results[name] = InvalidFailed(name, path, expected, output)

    def invalid_failed_incorrectly(self, name, path, expected, output=''):
        """
        Report that an invalid file failed validation, but for the wrong
        reason(s).
        """
        name = str(name)
        if name in self._results:
            raise Exception('Duplicate test result for: ' + name)
        self._results[name] = InvalidFailedIncorrectly(
            name, path, expected, output)

    def count(self, category=None):
        """
        Counts and returns the different test results.
        """
        valid_passed = 0
        valid_failed = 0
        invalid_passed = 0
        invalid_failed = 0
        invalid_failed_incorrectly = 0
        not_run = 0

        for test in self._all_tests:
            try:
                r = self._results[test]
            except KeyError:
                not_run += 1
                continue
            if category is not None:
                if r.category != category:
                    continue

            if isinstance(r, ValidPassed):
                valid_passed += 1
            elif isinstance(r, ValidFailed):
                valid_failed += 1
            elif isinstance(r, InvalidPassed):
                invalid_passed += 1
            elif isinstance(r, InvalidFailed):
                invalid_failed += 1
            elif isinstance(r, InvalidFailedIncorrectly):
                invalid_failed_incorrectly += 1
            else:
                raise NotImplementedError(
                    'Unknown test result class: ' + str(type(r)))

        output = [
            valid_passed,
            valid_failed,
            invalid_passed,
            invalid_failed,
            invalid_failed_incorrectly,
        ]
        if category is None:
            return output + [not_run]
        return output

    def render(self, path):
        """
        Renders this report, storing the result as a markdown file in the given
        ``path``.
        """
        # Header and body
        h = []
        b = []

        # Add title to header
        h.append('# ' + self._name)
        h.append('')

        # Create body
        e_valid_failed = '🔴'
        e_invalid_passed = '🔵'
        e_invalid_failed_bad = '🔶'
        e_not_run = '❗'
        e_unknown_test = '❗❗'

        # Loop over known tests, show results
        next = last = (-1, -1, -1, -1)
        level = 0
        for test in self._all_tests:

            # Get result
            r = self._results.get(test, None)

            # Write header
            if r is not None:
                next = r.index
            if last != next:
                b.append('')
                b.append('---')
                b.append('')
                if last[0] != next[0]:
                    b.append('## ' + self._categories[next[0]])
                    b.append('')
                if r.level > 1:
                    b.append('#' * (1 + r.level) + ' ' + r.pretty_index)
                    b.append('')
                last = next

            # Get path to test file
            if r:
                rpath = os.path.relpath(r.path, os.path.basename(path))
                name = '[' + test + '](' + rpath + ')'
            else:
                name = '`' + test + '`'
            name += ': '

            # Show expected/returned
            def expret(expected=None, returned=None):
                if expected:
                    b.append('* Expected: ```' + expected + '```')
                if returned:
                    returned = returned.splitlines()
                    if len(returned) == 1:
                        b.append('* Output: ```' + returned[0] + '```')
                    else:
                        b.append('* Output:')
                        for line in returned:
                            b.append('  * ```' + line + '```')

            # Show results
            if isinstance(r, ValidPassed):
                b.append(name + 'Valid file passed validation.')
            elif isinstance(r, ValidFailed):
                b.append(e_valid_failed + ' ' + name +
                         '**Valid file failed validation.**')
                expret(None, r.output)
            elif isinstance(r, InvalidPassed):
                b.append(e_invalid_passed + ' ' + name
                         + '**Error not detected.**')
                expret(r.expected, r.output)
            elif isinstance(r, InvalidFailed):
                b.append(name + 'Error detected correctly.')
                expret(r.expected, r.output)
            elif isinstance(r, InvalidFailedIncorrectly):
                b.append(e_invalid_failed_bad + ' ' + name +
                         '**Invalid file failed for unexpected reason.**')
                expret(r.expected, r.output)
            else:
                b.append(e_not_run + name + '**Test not run**')
            b.append('')

        # Show unknown tests
        extra = set(self._results.keys()) - set(self._all_tests)
        if extra:
            b.append('# Unknown tests found')
            for test in sorted(extra):
                b.append(e_unknown_test + '`' + name + '`')

        # Calculate scores
        vpass, vfail, ipass, ifail, ibad, not_run = self.count()
        vtotal = vpass + vfail
        itotal = ipass + ifail + ibad
        total = vtotal + itotal
        correct = vpass + ifail
        pcorrect = int(100 * correct / total) if total else 0

        # Add scores to header
        h.append('Performance:')
        h.append(
            '* ' + str(pcorrect) + '% according to spec (' + str(correct)
            + ' out of ' + str(total) + ')')
        h.append(
            '* ' + str(vpass) + ' out of ' + str(vtotal)
            + ' valid files passed')
        h.append(
            '* ' + str(ifail) + ' out of ' + str(itotal)
            + ' invalid files detected')
        h.append('')
        h.append('Issues:')
        h.append(
            '* ' + str(vfail) + ' valid files failed validation')
        h.append(
            '* ' + str(ipass) + ' invalid files passed validation')
        h.append(
            '* ' + str(ibad)
            + ' invalid files failed validation for the wrong reason')
        if not_run or extra:
            h.append('')
            h.append('Test implementation issues')
            if extra:
                h.append('* **' + str(unknown) + ' unknown tests run**')
            else:
                h.append('* **' + str(not_run) + ' tests not run**')
        h.append('')

        # Add table of scores to header
        h.append('Results per category')
        h.append('')
        h.append('(Valid passed, invalid failed, valid failed, invalid passed'
                 ', invalid failed for wrong reason'
                 ', percent classified correctly according to spec)')
        h.append('')
        h.append('|Category|V Pass|I Fail|'
                 + e_valid_failed + ' V Fail|'
                 + e_invalid_passed + ' I Pass|'
                 + e_invalid_failed_bad + ' I Bad|'
                 + 'Score|')
        h.append('|-|-|-|-|-|-|-|')

        for key, label in self._categories.items():
            # Category, with link
            a = '[' + label + '](#' + self._anchors[key]  + ')'

            # Body
            c = self.count(key)
            vpass, vfail, ipass, ifail, ibad = c
            if sum(c):
                score = int(100 * (vpass + ifail) / sum(c))
            else:
                score = 0
            line = [a, vpass, ifail, vfail, ipass, ibad, str(score) + '%']
            h.append('|' + '|'.join([str(x) for x in line]) + '|')

        h.append('')

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

        self._categories = {
            0: '0. Not mentioned in spec',
            2: '2. Fundamentals',
            3: '3. Model structure',
            4: '4. Mathematics',
            5: '5. Units',
            6: '6. Grouping',
            7: '7. Reactions',
            8: '8. Metadata framework',
            103: 'C. Advanced units functionality',
        }
        self._anchors = {}
        for k, v in self._categories.items():
            a = v.lower()
            a = a.replace('.', '')
            a = a.replace(' ', '-')
            self._anchors[k] = a

    def _list_all_tests(self):
        tests = shared.list_passes_1_0() + shared.list_fails_1_0()
        tests = [t.values[0] for t in tests]

        tests.sort()
        return tests


class Result(object):
    def __init__(self, name, path, output):
        self.name = str(name)
        self.path = str(path)
        self.output = str(output) if output else ''

        # Get index from test name
        index = []
        for x in self.name.split('.'):
            # Allow only numbers or single letters (appendix)
            if x.isdigit():
                index.append(int(x))
            elif len(x) == 1:
                index.append(ord(x) + 36)
            else:
                break
        assert len(index) <= 4

        # String index
        self.pretty_index = '.'.join([str(x) for x in index])

        # Number of entries in index
        self.level = len(index)
        index += [0] * (4 - len(index))

        # Index, appended with zeros
        self.index = tuple(index)

        # First index
        self.category = index[0]


class ValidPassed(Result):
    def __init__(self, name, path, output):
        super(ValidPassed, self).__init__(name, path, output)


class ValidFailed(Result):
    def __init__(self, name, path, output):
        super(ValidFailed, self).__init__(name, path, output)


class InvalidPassed(Result):
    def __init__(self, name, path, expected, output):
        super(InvalidPassed, self).__init__(name, path, output)
        self.expected = str(expected) if expected else ''


class InvalidFailed(Result):
    def __init__(self, name, path, expected, output):
        super(InvalidFailed, self).__init__(name, path, output)
        self.expected = str(expected) if expected else ''


class InvalidFailedIncorrectly(Result):
    def __init__(self, name, path, expected, output):
        super(InvalidFailedIncorrectly, self).__init__(name, path, output)
        self.expected = str(expected) if expected else ''


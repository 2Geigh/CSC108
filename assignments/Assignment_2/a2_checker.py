"""A simple checker for types of functions in mm_functions.py."""

from typing import Any, Dict, Union
import pytest
import checker_generic
import compatibility_calculator

FILENAME = 'compatibility_calculator.py'
PYTA_CONFIG = 'a2_pythonta.json'
TARGET_LEN = 79
SEP = '='

CONSTANTS = {'HIGH_COMPATIBILITY': 100,
             'MID_COMPATIBILITY': 60,
             'LOW_COMPATIBILITY': 20
             }


class TestChecker:
    """Sanity checker for assignment functions."""

    def test_count_common_occurrences(self) -> None:
        """Function count_common_occurrences"""
        self._check(compatibility_calculator.count_common_occurrences,
                    ['BOB Y', 'bobbette z'], int)

    def test_get_name_compatibility(self) -> None:
        """Function get_name_compatibility"""
        self._check(compatibility_calculator.get_name_compatibility,
                    ['BOB Y', 'bobbette z'], float)

    def test_extract_year(self) -> None:
        """Function extract_year"""
        self._check(compatibility_calculator.extract_year,
                    ['1991/08/02'], int)

    def test_extract_month(self) -> None:
        """Function extract_month"""
        self._check(compatibility_calculator.extract_month,
                    ['1991/08/02'], int)

    def test_extract_day(self) -> None:
        """Function extract_day"""
        self._check(compatibility_calculator.extract_day,
                    ['1991/08/02'], int)

    def test_get_numerological_root(self) -> None:
        """Function get_numerological_root"""
        self._check(compatibility_calculator.get_numerological_root,
                    [1989], int)

    def test_build_numerology_list(self) -> None:
        """Function build_numerology_list"""
        self._check(compatibility_calculator.build_numerology_list,
                    [['1,2,YES', '1,1,YES', '1,4,NO']], list
                    )

    def test_get_numerology_compatibility(self) -> None:
        """Function get_numerology_compatibility"""
        self._check(compatibility_calculator.get_numerology_compatibility,
                    [9, 11, [[9, [3, 6], [4]], [3, [3, 6, 9], []]]], int
                    )

    def test_find_astrological_sign(self) -> None:
        """Function find_astrological_sign"""
        self._check(compatibility_calculator.find_astrological_sign,
                    [[['VIR', 2, (8, 23), (9, 22)],
                      ['CAP', 2, (12, 22), (1, 20)]], 8, 23], str)

    def test_get_sign_group(self) -> None:
        """Function get_sign_group"""
        self._check(compatibility_calculator.get_sign_group,
                    [[['VIR', 2, (8, 23), (9, 22)],
                      ['ARI', 1, (3, 21), (4, 19)]],
                     'VIR'], int)

    def test_find_astrological_compatibility(self) -> None:
        """Function find_astrological_compatibility"""
        self._check(compatibility_calculator.find_astrological_compatibility,
                    [1, 1], int)

    def test_build_sign_data_list(self) -> None:
        """Function build_sign_data_list"""
        self._check(compatibility_calculator.build_sign_data_list,
                    [['str1,0,1,2,3,4', 'str2,5,6,7,8,9']], list)

    def _check(self, func: callable, args: list, ret_type: Union[type, tuple]) -> None:
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.
        """
        print('\nChecking {}...'.format(func.__name__))
        result = checker_generic.type_check_simple(func, args, ret_type)
        assert result[0] is True, result[1]
        print('  check complete')

    def _check_constants(self, name2value: Dict[str, object], mod: Any) -> None:
        """Check that, for each (name, value) pair in name2value, the value of
        a variable named name in module mod is value.
        """

        for name, expected in name2value.items():
            actual = getattr(mod, name)
            msg = 'The value of constant {} should be {} but is {}.'.format(
                name, expected, actual)
            assert expected == actual, msg


print(''.center(TARGET_LEN, SEP))
print(' Start: checking coding style with PythonTA '.center(TARGET_LEN, SEP))
checker_generic.run_pyta(FILENAME, PYTA_CONFIG)
print(' End checking coding style with PythonTA '.center(TARGET_LEN, SEP))

print(' Start: checking type contracts '.center(TARGET_LEN, SEP))
pytest.main(['--show-capture', 'no', '--disable-warnings', '--tb=short',
             'a2_checker.py'])
print(' End checking type contracts '.center(TARGET_LEN, SEP))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style with Python TA')
print('  - checking type contract\n')

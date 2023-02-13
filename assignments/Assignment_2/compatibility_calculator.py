"""CSC108/CSCA08: Winter 2023 -- Assignment 1: Question Bot

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2023 Paul Gries, Sophia Huynh, and Sadia
Sharmin.

====

Assignment 2: Bob's Compatibility Calculator

Bob wants to write a program to calculate compatibility between two people
based on their names, birthdays, and astrological signs.

Help Bob complete the code below. He's managed to at least create most of the
function headers, but needs your help with how to write the function bodies.

He's hired a bunch of professors to add helpful TODO notes throughout.
"""

from compatibility_data import SIGN_DATA, NUM_COMPATIBILITY_DATA

# The compatibility measures.
HIGH_COMPATIBILITY = 100
MID_COMPATIBILITY = 60
LOW_COMPATIBILITY = 20

# Whether to run doctests. See the bottom of this file to see it in action.
# Switch it to False to run it in interactive mode. (Bob says to try it to
# see what it does!)
DOCTEST_MODE = True


###################################################################
#  TASK 1: NAME COMPATIBILITY CALCULATOR
###################################################################

def count_common_occurrences(word1: str, word2: str) -> int:
    """
    Return how many alphabetical characters in word1 also occur in word2, case
    insensitive (that is 'A' and 'a' should count as common).
    Spaces and punctuation do NOT count as a common character.

    In this example, the B O and B all appear in lowercase form in the second
    argument. Notice that we count both B's in the first argument:
    >>> count_common_occurrences('BOB Y', 'bobbette z')
    3

    Here, b, o, b, and b appear in uppercase form in the second argument.
    We count all 3 occurrences of the letter b in the first argument:
    >>> count_common_occurrences('bobbette z', 'BOB Y')
    4
    """

    # TODO: design and write the function body


def get_name_compatibility(name1: str, name2: str) -> float:
    """
    Return the name compatibility between `name1` and `name2`, which is the
    number of letters from `name1` that appear in `name2` plus the number
    of letters from `name2` that appear in `name1`, divided by the total
    number of letters in both names together, all multiplied by 100.

    >>> get_name_compatibility('BOB Y', 'BOBBETTE ZE')
    50.0

    >>> get_name_compatibility('BOB Y123', 'bob y!')
    100.0

    >>> get_name_compatibility('Alice', 'Alyssa')
    45.45454545454545
    """

    # TODO: design and write the function body
    # Note from Bob: maybe you can call helper function
    # count_common_occurrences twice to do the bulk of the work?


###################################################################
#  TASK 2: BIRTHDAY COMPATIBILITY CALCULATOR
##################################################################

############
# TASK 2.1 #
############

def extract_year(bday: str) -> int:
    """
    Return the year within bday that is in the format YYYY/MM/DD.

    >>> extract_year('1991/08/02')
    1991

    >>> extract_year('1995/12/22')
    1995
    """

    # TODO: design and write the function body


def extract_month(bday: str) -> int:
    """
    Return the month within bday that is in the format YYYY/MM/DD.

    >>> extract_month('1991/08/02')
    8

    >>> extract_month('1995/12/22')

    """
    # TODO: fill in the expected value for the second docstring example above

    # TODO: design and write the function body


def extract_day(bday: str) -> int:
    """

    >>> extract_day('1991/08/02')

    >>> extract_day('1995/12/22')

    """
    # TODO: write the docstring function description above
    # TODO: fill in the expected values for the docstring examples above

    # TODO: design and write the function body


############
# TASK 2.2 #
############

def get_numerological_root(num: int) -> int:
    """
    Return the root number of num, found by repeatedly adding the digits in
    the number together until you are left with a single digit or the Special
    Numbers 11 or 22.

    >>> get_numerological_root(1989)
    9

    >>> get_numerological_root(11)
    11

    >>> get_numerological_root(1993)
    22

    >>> get_numerological_root(2002)

    """
    # TODO: fill in the expected value for the last docstring example above

    # TODO: design and write the function body


# Note: Bob managed to get this function working.
# He's asked you not to change it.
def get_bday_numerology_num(bday: str) -> int:
    """
    Return the root number of the given bday formatted as YYYY/MM/DD.

    Refer to handout for details.

    >>> get_bday_numerology_num('1998/08/18')
    8

    >>> get_bday_numerology_num('2002/03/22')
    11
    """

    num = (get_numerological_root(extract_year(bday))
           + get_numerological_root(extract_month(bday))
           + get_numerological_root(extract_day(bday)))

    return get_numerological_root(num)


############
# TASK 2.3 #
############

# Note from Bob: Wow this bends my brain! Think it through before starting
# to program!
def build_numerology_list(compatibility_data: list[str]) -> list:
    """
    Given `compatibility_data`, formatted as in NUM_COMPATIBILITY_DATA, return
    a list of lists with the following structure:

        [
            [n1, [all compatible nums for n1], [all incompatible nums for n1]],
            [n2, [all compatible nums for n2], [all incompatible nums for n2]],
            :
        ]

    Each inner compatibility list will be sorted in increasing order, and
    the overall list should be sorted by the n's.

    >>> test_list = ['1,2,YES', '1,1,YES', '1,4,NO']
    >>> build_numerology_list(test_list)
    [[1, [1, 2], [4]]]

    >>> test_list = ['3,1,NO', '1,3,YES']
    >>> build_numerology_list(test_list)
    [[1, [3], []], [3, [], [1]]]

    >>> test_list = ['1,1,YES', '1,2,YES', '2,3,YES', '3,1,YES','3,2,NO']
    >>> build_numerology_list(test_list)

    """
    # TODO: fill in the expected value for the last docstring example above

    # TODO: design and write the function body


def get_numerology_compatibility(bday_num1: int, bday_num2: int,
                                 num_compatibility_table: list) -> int:
    """
    Return the compatibility percentage (one of `HIGH_COMPATIBILITY`,
    `LOW_COMPATIBILITY`, and `MID_COMPATIBILITY`) for `bday_num1` and
    `bday_num2`, which are the numerology numbers of two birthdays,
    according to the numerological compatibility data in
    `num_compatibility_table`.

    If `bday_num2` is in the high compatibility list of `bday_num1`,
    return `HIGH_COMPATIBILITY`.

    If `bday_num2` is in the low compatibility list of `bday_num1`,
    return `LOW_COMPATIBILITY`.

    Otherwise, the second number is mildly compatible with the first number,
    so return MID_COMPATIBILITY. Note that if the first number is not in
    `num_compatibility_table` this rule applies.

    >>> sample_compatibility = [[9, [3, 6], [4]], [3, [3, 6, 9], []]]
    >>> get_numerology_compatibility(9, 11, sample_compatibility)
    60

    >>> get_numerology_compatibility(3, 6, sample_compatibility)
    100

    >>>

    """
    # TODO: add a docstring example above for a LOW_COMPATIBILITY result

    # TODO: design and write the function body


# NOTE FROM BOB: I'm proud of this function. Don't modify it, I'm pretty sure
# it's correct. I had the professors check it. Well, really, I mostly had them
# solve it.
def get_bday_numerology_compatibility(num_compatibility_table: list,
                                      bday1: str, bday2: str) -> int:
    """
    Figure out the numerology number of bday1 and bday2 and return
    the numerological compatibility of the two birthdates.

    >>> get_bday_numerology_compatibility([[5, [7], []]], '2001/01/01',
    ...                                   '2003/01/01')
    100

    >>> get_bday_numerology_compatibility([[5, [], [7]]], '2001/01/01',
    ...                                   '2003/01/01')
    20
    """

    bday_num1 = get_bday_numerology_num(bday1)
    bday_num2 = get_bday_numerology_num(bday2)

    return get_numerology_compatibility(bday_num1, bday_num2,
                                        num_compatibility_table)


###################################################################
#  TASK 3: ASTROLOGICAL COMPATIBILITY CALCULATOR
##################################################################

############
# TASK 3.1 #
############

def build_sign_data_list(data_lst: list[str]) -> list:
    """
    Given a list of strings each in the following format (this is the same
    format as for `SIGN_DATA`):
        [
            'str1,int0,int1,int2,int3,int4',
            'str2,int5,int6,int7,int8,int9',
            :
        ]
    Return a nested list containing this data in the following format:
        [
            [str1, int0, (int1, int2), (int3, int4)],
            [str2, int5, (int6, int7), (int8, int9)],
            :
        ]

    >>> s = ['str1,0,1,2,3,4', 'str2,5,6,7,8,9']
    >>> build_sign_data_list(s)
    [['str1', 0, (1, 2), (3, 4)], ['str2', 5, (6, 7), (8, 9)]]

    >>> L = build_sign_data_list(SIGN_DATA)
    >>> L == [['ARI', 1, (3, 21), (4, 19)], ['TAU', 2, (4, 20), (5, 20)],\
            ['GEM', 3, (5, 21), (6, 21)], ['CAN', 4, (6, 22), (7, 22)],\
            ['LEO', 1, (7, 23), (8, 22)], ['VIR', 2, (8, 23), (9, 22)],\
            ['LIB', 3, (9, 23), (10, 23)], ['SCO', 4, (10, 24), (11, 20)],\
            ['SAG', 1, (11, 21), (12, 21)], ['CAP', 2, (12, 22), (1, 20)],\
            ['AQU', 3, (1, 21), (2, 21)], ['PIS', 4, (2, 22), (3, 20)],\
            ]
    True
    """

    # TODO: design and write the function body


def find_astrological_sign(sign_data: list, month: int, date: int) -> str:
    """
    Return the sign of a person born on the month and date based on the data
    in `sign_data`.

    `sign_data` is a list of sublists, one sublist for each sign. Each sublist
    is structured like this:

    [sign_name, sign_group, (start_month, start_date), (end_month, end_date)]

    All dates are inclusive.

    Return the associated sign_name from sign_data for the given birthday.

    Precondition: `month` and `date` are covered by the date ranges in
    `sign_data`.

    In this example, Virgo spans from the 23rd of August (8, 23) to the 22nd of
    September (9, 22) and the 24th of August (8, 24) falls into this period:
    >>> data = [['VIR', 2, (8, 23), (9, 22)], ['CAP', 2, (12, 22), (1, 20)]]
    >>> find_astrological_sign(data, 8, 24)
    'VIR'

    >>> find_astrological_sign(data, 1, 15)

    """
    # TODO: fill in the expected value for the last docstring example above

    # TODO: design and write the function body


def get_sign_group(sign_data: list, sign: str) -> int:
    """
    Return the group number of the `sign` using `sign_data`.

    `sign_data` is a list of sublists, one sublist for each sign. Each sublist
    is structured like this:

    [sign_name, sign_group, (start_month, start_date), (end_month, end_date)]

    Precondition: `sign` exists as a sign_name in `sign_data`

    >>> data = [['VIR', 2, (8, 23), (9, 22)], ['ARI', 1, (3, 21), (4, 19)]]
    >>> get_sign_group(data, 'VIR')
    2
    >>> get_sign_group(data, 'ARI')
    1

    >>> data = [['FAKE_SIGN', 9000, (1, 2), (3, 4)]]
    >>> get_sign_group(data, 'FAKE_SIGN')

    """
    # TODO: fill in the expected value for the last docstring example above

    # TODO: design and write the function body


############
# TASK 3.2 #
############

def find_astrological_compatibility(sign_gp1: int, sign_gp2: int) -> int:
    """
    Return an int representing how compatible sign groups `sign_gp1` and
    `sign_gp2` are.

    The compatibility between signs is calculated based on the sign groups
    they belong in, as follows:
    - return `HIGH_COMPATIBILITY` if the signs groups are the same
    - return `MID_COMPATIBILITY` if both sign groups are odd-numbered
      groups (i.e. 1 and 3) or if both are even-numbered groups (i.e.
      2 and 4)
    - return `LOW_COMPATIBILITY` in all other cases

    >>> find_astrological_compatibility(1, 1)
    100

    >>> find_astrological_compatibility(2, 2)
    100

    >>> find_astrological_compatibility(4, 2)
    60

    >>> find_astrological_compatibility(1, 3)
    60

    >>> find_astrological_compatibility(1, 2)
    20

    >>> find_astrological_compatibility(2, 3)
    20
    """

    # TODO: complete this helper function


# NOTE FROM BOB: I'm proud of this function. Don't modify it, I'm pretty sure
# it's correct. I had the professors check it. Well, really, I mostly had them
# solve it.
def get_bday_sign_compatibility(sign_data: list, bday1: str, bday2: str) -> int:
    """
    Figure out what star signs bday1 and bday2 belong to and return
    the astrological compatibility of the two signs.

    >>> sign_data = [['ARI', 1, (3, 21), (4, 19)], \
    ['LEO', 1, (7, 23), (8, 22)], ['VIR', 2, (8, 23), (9, 22)], \
    ['AQU', 3, (1, 21), (2, 21)], ['PIS', 4, (2, 22), (3, 20)]]

    >>> get_bday_sign_compatibility(sign_data, '1998/08/30', '1998/03/10')
    60

    >>> get_bday_sign_compatibility(sign_data, '1998/08/10', '1995/04/01')
    100
    """

    sign1 = find_astrological_sign(sign_data, extract_month(bday1),
                                   extract_day(bday1))
    sign2 = find_astrological_sign(sign_data, extract_month(bday2),
                                   extract_day(bday2))

    sign_group1 = get_sign_group(sign_data, sign1)
    sign_group2 = get_sign_group(sign_data, sign2)

    return find_astrological_compatibility(sign_group1, sign_group2)


# =====================================================================
# NOTE FROM BOB:
# Do NOT change the following function.
# I already did it (although it won't work until you complete the three
# `extract_` functions.)
# =====================================================================
def is_valid_date(bday: str) -> bool:
    """
    Return True iff bday is a valid date in the calender and
    in the format YYYY/MM/DD.

    >>> is_valid_date('1903/02/03')
    True

    >>> is_valid_date('1999/20/01')
    False

    >>> is_valid_date('3123/310/31')
    False

    >>> is_valid_date('2003/02/31')
    False
    """

    digit_check = (bday[:4].isdigit() and bday[5:7].isdigit()
                   and bday[8:].isdigit())

    if len(bday) == 10 and digit_check and bday[4] == '/' and bday[7] == '/':

        year = extract_year(bday)
        month = extract_month(bday)
        date = extract_day(bday)

        if 1 <= month <= 12 and 1 <= date <= 31 and year <= 2022:
            if (month == 2 and date > 29) or (
                    month == 2 and date == 29 and year % 4 != 0):
                return False

            if month in [4, 6, 9, 11] and date > 30:
                return False

            return True

    return False


###################################################################
#  TASK 4: PUTTING IT ALL TOGETHER
##################################################################

def calculate_love_score(name1: str, name2: str, bday1: str,
                         bday2: str) -> float:
    """
    `name1` and `name2` are two names and `bday1` and `bday2` are their
    respective birthdays in the format YYYY/MM/DD.

    Return the average of:
    1) the name compatibility between `name1` and `name2`
        (hint: use get_name_compatibility as a helper)
    2) the numerology compatibility between `bday1` and `bday2`
        (hint: use get_bday_numerology_compatibility), and
    3) the sign compatibility of the two birthdays
        (hint: use get_bday_sign_compatibility)
    rounded down to the nearest whole number (use // to divide instead of /).

    Note: Relevant calculations are based on the values in `SIGN_DATA` and
    `NUM_COMPATIBILITY_DATA`. Use those to build data lists as appropriate,
    to pass in to the helper functions mentioned in the hints above.
    (Hint: Use build_sign_data_list and build_numerology_list)

    >>> calculate_love_score('Bob', 'Alice', '1997/12/04', '1996/01/23')
    40.0

    >>> calculate_love_score('Pocoyo', 'Tomoyo', '2019/10/29', '2019/09/21')
    75.0
    """

    # TODO: complete this function body


if __name__ == "__main__":

    if DOCTEST_MODE:
        import doctest
        doctest.testmod()
    else:
        name_1 = input("Give me your first and last name: ")
        bday_1 = input("Give me your birthdate in the format YYYY/MM/DD: ")
        while not is_valid_date(bday_1):
            bday_1 = input(
                "Invalid input. "
                + "Give me your birthdate in the format YYYY/MM/DD: ")

        print("=====")
        name_2 = input("Give me your crush's first and last name: ")
        bday_2 = \
            input("Give me your crush's birthdate in the format YYYY/MM/DD: ")
        while not is_valid_date(bday_2):
            bday_2 = input(
                "Invalid input. "
                + "Give me your birthdate in the format YYYY/MM/DD: ")

        print("You are " + str(
            calculate_love_score(name_1.lower(), name_2.lower(), bday_1,
                                 bday_2)) + "% compatible in love!")

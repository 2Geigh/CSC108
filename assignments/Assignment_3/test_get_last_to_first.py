"""A3. Test cases for function get_last_to_first from club_functions
"""

from club_functions import get_last_to_first


def test_empty() -> None:
    """Test get_last_to_first with empty dictionary."""

    assert get_last_to_first({}) == {}


def test_one_person_one_friend_same_last() -> None:
    """Test get_last_to_first with one person who has one friend that shares
    the same last name as them."""

    param = {'Clare Dunphy': ['Phil Dunphy']}
    actual = get_last_to_first(param)
    expected = {'Dunphy': ['Clare', 'Phil']}
    assert get_last_to_first(param) == expected

def test_no_one_same_last_name() -> None:
    """Test get_last_to_first with two people
    who don't share a last name"""

    param = {'John Adams': ['George Washington']}
    actual = get_last_to_first(param)
    expected = {'Adams': ['John'], 'Washington': ['George']}

def test_no_friends() -> None:
    """Test get_last_to_first with someone
    who has no friends to compare surnames with"""

    param = {'John Adams': []}
    actual = get_last_to_first(param)
    expected = {'Adams': ['John']}

def test_two_lonely_soles() -> None:
    """Test get_last_to_first with two people
    who have no friends to compare surnames with"""

    param = {'John Adams': [], 'Alexander Hamilton': []}
    actual = get_last_to_first(param)
    expected = {'Adams': ['John'], 'Hamilton': ['Alexander']}

def test_everyone_same_surname() -> None:
    """Test get_last_to_first with a group
    of immediate relatives"""

    param = {'Papa Smurf': ['Billy Smurf',
                            'Joey Smurf',
                            'Grumpy Smurf,'
                            'Bartholomeux Smurf']}
    actual = get_last_to_first(param)
    expected = {'Smurf': ['Papa', 'Joey', 'Grumpy', 'Bartholomeux']}

def test_everyone_same_given_name() -> None:
    """Test get_last_to_first with a group
    of picky friends who all share the same
    given name"""

    param = {'Michael Jackson': ['Michael Jordan',
                                 'Michael Cera',
                                 'Michael Stevens'],
             'Elizabeth May': ['Elizabeth Windsor',
                               'Elizabeth Taylor']}
    actual = get_last_to_first(param)
    expected = {'Cera': ['Michael'],
                'Jackson': ['Michael'],
                'Jordan': ['Michael'],
                'Stevens': ['Michael'],
                'Taylor': ['Elizabeth'],
                'Windsor': ['Elizabeth']}

if __name__ == '__main__':
    import pytest
    pytest.main(['test_get_last_to_first.py'])

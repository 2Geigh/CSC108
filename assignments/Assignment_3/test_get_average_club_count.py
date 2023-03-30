"""A3. Test cases for function get_average_club_count from club_functions
"""

from club_functions import get_average_club_count


def test_empty() -> None:
    """Test get_average_club_count with empty dict"""

    assert get_average_club_count({}) == 0


def test_one_person_one_club() -> None:
    """Test get_average_club_count with one person who is in one club."""

    param = {'Claire Dunphy': ['Parent Teacher Association']}
    actual = get_average_club_count(param)
    expected = 1

    assert actual == expected

def test_10_people_one_club() -> None:
    """Test get_average_club_count with ten people
    who are in one club."""

    param = {'Claire Dunphy': ['Parent Teacher Association'],
             'Timmy Turner': ['Dimsdale Elementary'],
             'Danny Phantom': ['Casper High School'],
             'Spongebob Squarepants': ['Krusty Krab'],
             'Squidward Tentacles': ['Krusty Krab'],
             'Eugene Krabs': ['Krusty Krab'],
             'Patrick Star': ['Krusty Krab'],
             'Sheldon J Plankton': ['Chum Bucket'],
             'Karen Computer-Wife': ['Chum Bucket'],
             'Larry Lobster': ["Gold's Gym"],
             'Sandy Cheeks': ['Goo Lagoon']}
    actual = get_average_club_count(param)
    expected = 1

    assert actual == expected

def test_10_people__but_only_one_in_a_club() -> None:
    """Test get_average_club_count with ten people
    but only one is in a club."""

    param = {'Claire Dunphy': ['Parent Teacher Association'],
             'Timmy Turner': [],
             'Danny Phantom': [],
             'Spongebob Squarepants': [],
             'Squidward Tentacles': [],
             'Eugene Krabs': [],
             'Patrick Star': [],
             'Sheldon J Plankton': [],
             'Karen Computer-Wife': [],
             'Larry Lobster': [],
             'Sandy Cheeks': []}
    actual = get_average_club_count(param)
    expected = 0

    assert actual == expected

def test_one_clubber_one_nonclubber() -> None:
    """Test get_average_club_count with two people,
    one who is in a club and one who isnt."""

    param = {'Claire Dunphy': ['Parent Teacher Association'],
             'Timmy Turner': []}
    actual = get_average_club_count(param)
    expected = 0

    assert actual == expected


if __name__ == '__main__':
    import pytest
    pytest.main(['test_get_average_club_count.py'])

""" CSC108 Assignment 3: Club Recommendations - Starter code."""
from typing import TextIO
import io

# Sample Data (Used by Docstring examples)
# What a Profile File might look like.
EXAMPLE_PROFILE_DATA = '''Katsopolis, Jesse
Parent Council
Rock N Rollers
Tanner, Danny R
Donaldson-Katsopolis, Rebecca
Gladstone, Joey

Donaldson-Katsopolis, Rebecca
Gibbler, Kimmy

Tanner, Stephanie J
Tanner, Michelle
Gibbler, Kimmy

Tanner, Danny R
Parent Council
Tanner-Fuller, DJ
Gladstone, Joey
Katsopolis, Jesse

Gibbler, Kimmy
Smash Club
Rock N Rollers

Gladstone, Joey
Comics R Us
Parent Council

Tanner, Michelle
Comet Club
'''

EXAMPLE_PROFILE_DATA_2 = '''Squarepants, Spongebob
Goofy Goober's
Goo Lagoon
Star, Patrick
Krabs, Eugene
Cheeks, Sandy

Plankton, Sheldon J
Chum Bucket

Cheeks, Sandy
Squarepants, Spongebob
Star, Patrick
'''

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Kimmy Gibbler', 'Michelle Tanner'],
       'Danny R Tanner': ['DJ Tanner-Fuller', 'Jesse Katsopolis',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}

P2F_2 = {'Spongebob Squarepants': ['Eugene Krabs', 'Patrick Star', 'Sandy Cheeks'],
         'Sandy Cheeks': ['Patrick Star', 'Spongebob Squarepants']}

P2C_2 = {'Spongebob Squarepants': ['Goo Lagoon', "Goofy Goober's", ],
         'Sheldon J Plankton': ['Chum Bucket']}


# Helper functions

def update_dict(key: str, value: str,
                key_to_values: dict[str, list[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []

    if value not in key_to_values[key]:
        key_to_values[key].append(value)


# Required functions

def load_profiles(profiles_file: TextIO) -> tuple[dict[str, list[str]],
                                                  dict[str, list[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from
    profiles_file. The values in the two dictionaries are sorted in
    alphabetical order.

    >>> data = io.StringIO(EXAMPLE_PROFILE_DATA) # this treats a str as a file
    >>> result = load_profiles(data)
    >>> result == (P2F, P2C)
    True
    
    >>> data_2 = io.StringIO(EXAMPLE_PROFILE_DATA_2)
    >>> result_2 = load_profiles(data_2)
    >>> result_2 == (P2F_2, P2C_2)
    True
    """

    line = profiles_file.readline()
    person_to_clubs = {}
    person_to_friends = {}

    while line != '':
        clubs = []
        friends = []

        if ',' in line:
            person_surname = line[:line.index(',')].strip()
            person_given_name = line[line.index(',') + 1:].strip()
            person = person_given_name + ' ' + person_surname
        
        line = profiles_file.readline()
        while ',' not in line and line.strip() != '':
            clubs.append(line[:].strip())
            line = profiles_file.readline()
        
        while ',' in line:
            friend_surname = line[:line.index(',')].strip()
            friend_given_name = line[line.index(',') + 1:].strip()
            friend = friend_given_name + ' ' + friend_surname
            friends.append(friend)
            line = profiles_file.readline()
        
        line = profiles_file.readline()

        clubs.sort()
        friends.sort()

        if len(friends) > 0:
            person_to_friends[person] = friends
        if len(clubs) > 0:
            person_to_clubs[person] = clubs
        
    return (person_to_friends, person_to_clubs)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    """
    for person in load_profiles(io.StringIO(EXAMPLE_PROFILE_DATA_2))[0]:
        print(person,': ',load_profiles(io.StringIO(EXAMPLE_PROFILE_DATA_2))[0][person])
    print('\n')

    for person in load_profiles(io.StringIO(EXAMPLE_PROFILE_DATA))[0]:
        print(person,': ',load_profiles(io.StringIO(EXAMPLE_PROFILE_DATA))[0][person])
    """
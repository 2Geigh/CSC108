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

P2F_2 = {'Spongebob Squarepants': ['Eugene Krabs', 'Patrick Star',
                                   'Sandy Cheeks'],
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
        
        
def sort_dictionary_lists(dictionary: dict[list]) -> dict:
    """Sorts all of the list values in a dictionary.
    
    >>> A = sort_dictionary_lists({'first': [2, 1], 'second': ['c', 'a']})
    >>> A == {'first': [1, 2], 'second': ['a', 'c']}
    True
    """
    
    return_dictionary = dictionary
    
    for key in return_dictionary:
        if type(return_dictionary[key]) == list:
            return_dictionary[key].sort()
        
    return return_dictionary


def collect_dict_data(key_to_value: dict) -> list[list[list], list, list]:
    """ Returns a list containing nested lists. The first nested list is a
    nested list containing lists of keys and their corresponding values from
    key_to_value. The second nested list is a list of the keys in key_to_value.
    The third nested list is a list of the values of keys in key_to_value.
    
    >>> collect_dict_data({1: 2, 3: 4, 5: 6})
    [[[1, 2], [3, 4], [5, 6]], [1, 3, 5], [2, 4, 6]]
    
    >>> collect_dict_data({'k1': 'v1', 'k2': 'v2'})
    [[['k1', 'v1'], ['k2', 'v2']], ['k1', 'k2'], ['v1', 'v2']]
    
    """
    
    keys_and_values = []
    for key in key_to_value:
        keys_and_values.append([key, key_to_value[key]])
    keys = []
    for pair in keys_and_values:
        keys.append(pair[0])
    values = []
    for pair in keys_and_values:
        values.append(pair[1])
    return [keys_and_values, keys, values]


def remove_degenerates(lst: list) -> list:
    """Removes duplicated items in a list until every element is unique
    
    >>> remove_degenerates([1, 2, 2])
    [1, 2]
    >>> remove_degenerates([1, 2, 3, 4, 5, 1])
    [1, 2, 3, 4, 5]
    """

    reverse = lst[::-1]
    for item in reverse:
        if reverse.count(item) > 1:
            reverse.remove(item)

    to_return = reverse[::-1]

    return to_return


def recommend_clubs_condition_1(clubs_friends_are_in: list[str],
                                friends: list[str],
                                person_to_clubs: dict[str, list[str]],
                                recomend_club_to_score: dict[str, int]) -> None:
    """
    This function modifies recommend_clubs_to_score to add points to
    each club basedo on condition 1 in the assignment for recommending clubs.

    Condition 1 goes as follows:
        "Add 1 point to the potential club's score
        for each of the person's friends who is a member of the potential club"
    """

    # CONDITION 1
    for potential_club in clubs_friends_are_in:  # for club the person's not in
        condition1 = 0  # update per friend is a member of the potential club.
        condition2 = 0  # update per member who's in one of person's clubs.

        if potential_club in clubs_friends_are_in:
            for friend in friends:
                if (friend in person_to_clubs) and \
                   (potential_club in person_to_clubs[friend]):  # condition 1
                    condition1 += 1
                    
        if condition1 > 0:
            recomend_club_to_score[potential_club] = (condition1
                                                      + condition2)


def recommend_clubs_condition_2(all_clubs: list, 
                                person_to_clubs: dict[str, list[str]],
                                clubs_person_is_in: list[str],
                                recomend_club_to_score: dict[str, int]) -> None:
    """
    This function modifies recommend_clubs_to_score to add points to
    each club basedo on condition 1 in the assignment for recommending clubs.

    Condition 1 goes as follows:
        Add 1 point for every member of the potential club,
        who is in at least one different club with the person.
    """
    # CONDITION 2
    for potential_club in all_clubs:
        clubs_to_person = invert_and_sort(person_to_clubs)
        
        potential_clubs_members = clubs_to_person.get(potential_club, [])
        
        for member in potential_clubs_members:
            clubs_member_is_in = []
            if member in person_to_clubs:
                clubs_member_is_in = person_to_clubs[member]

            trigger = False
            for club_member_is_in in clubs_member_is_in:
                if club_member_is_in in clubs_person_is_in:
                    trigger = True
            if trigger:
                if potential_club in recomend_club_to_score:
                    recomend_club_to_score[potential_club] += 1
                else:
                    recomend_club_to_score[potential_club] = 1
                trigger = False                


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

        if len(friends) > 0:
            friends.sort()
            person_to_friends[person] = friends
        if len(clubs) > 0:
            clubs.sort()
            person_to_clubs[person] = clubs
        
    return (person_to_friends, person_to_clubs)


def get_average_club_count(person_to_clubs: dict[str, list[str]]) -> int:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to, rounded down to the nearest integer (i.e. use // instead of /).

    >>> get_average_club_count(P2C)
    1

    >>> get_average_club_count({'Henrey': ['Da Klub', 'The Drunken Sailor'], \
    'Jenny': ['Weenie Hut Jrs', 'Super Weenie Hut Jrs']})
    2
    """

    every_persons_club_count = []
    
    for person in person_to_clubs:
        every_persons_club_count.append(len(person_to_clubs[person]))

    sum_counter = 0
    for number in every_persons_club_count:
        sum_counter += number
    
    if len(person_to_clubs) > 0:
        return sum_counter // len(person_to_clubs)
    return 0


def get_last_to_first(
        person_to_friends: dict[str, list[str]]) -> dict[str, list[str]]:
    """Return a "last name to first name(s)" dictionary with the people from the
    "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True

    >>> get_last_to_first({'Dorothy Jenner': ['Rebecca Jenner', 'Liuqi Wu']}) \
    == { 'Jenner': ['Dorothy', 'Rebecca'], 'Wu': ['Liuqi']}
    True
    """

    last_to_first = {}

    # Create a list of names of everyone in the input dict
    list_of_full_names = []
    for person in person_to_friends:
        list_of_full_names.append(person)
        for friend in person_to_friends[person]:
            list_of_full_names.append(friend)
    
    # remove name redundancies
    list_of_full_names_copy = list_of_full_names[:]
    for name in list_of_full_names_copy:
        while list_of_full_names.count(name) > 1:
            list_of_full_names.remove(name)

    # split names in list
    for i in range(len(list_of_full_names)):
        list_of_full_names[i] = list_of_full_names[i].split()
    # join every name component but surnames
    formatted_givenname_surnames = []
    for name_components in list_of_full_names:
        if len(name_components) > 2:
            surname = name_components[-1]
            given_names = ''
            for component in name_components[:-1]:
                given_names = given_names + component + ' '
            formatted_givenname_surnames.append([given_names.strip(),
                                                 surname.strip()])
        else:
            formatted_givenname_surnames.append(name_components)

    # create dictionary surname index and corresponding given names as values
    for full_name in formatted_givenname_surnames:
        last_to_first[full_name[1]] = []
    for full_name in formatted_givenname_surnames:
        if full_name[1] in last_to_first:
            last_to_first[full_name[1]].append(full_name[0])

    return sort_dictionary_lists(last_to_first)


def invert_and_sort(key_to_value: dict[object, object]) -> dict[object, list]:
    """Return key_to_value inverted so that each key in the returned dict
    is a value from the original dict (for non-list values) or each item from a
    value (for list values), and each value in the returned dict
    is a list of the corresponding keys from the original key_to_value.
    The value lists in the returned dict are sorted.

    if comet club in michelle tanner
    if new key in old_dict[old key]

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True

    >>> club_to_score = {'Parent Council': 3, 'Smash Club': 2, 'Orchestra': 2}
    >>> invert_and_sort(club_to_score) == {
    ...  3: ['Parent Council'], 2: ['Orchestra', 'Smash Club']}
    True

    >>> dict = {1: 2, 3: [4, 5]}
    >>> invert_and_sort(dict) == {2: [1], 4: [3], 5: [3]}
    True
    """

    # collect data
    keys = collect_dict_data(key_to_value)[1]
    values = collect_dict_data(key_to_value)[2]

    value_to_keys = {}
    # initialising dictionary-to-return with new keys
    for value in values:
        if type(value) == tuple or type(value) == list:
            for element in value:
                value_to_keys[element] = []
        else:
            value_to_keys[value] = []

    for old_key in keys:
        if type(key_to_value[old_key]) == list:
            for new_key in value_to_keys:
                if new_key in key_to_value[old_key]:
                    value_to_keys[new_key].append(old_key)
        else:
            for new_key in value_to_keys:
                if new_key == key_to_value[old_key]:
                    value_to_keys[new_key].append(old_key)

    return sort_dictionary_lists(value_to_keys)


def get_clubs_of_friends(person_to_friends: dict[str, list[str]],
                         person_to_clubs: dict[str, list[str]],
                         person: str) -> list[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']

    >>> person_to_clubs = {'Charlie': ['Harvard', 'Yale'], 'Bob': ['Princeton', 'Yale'], 'Bartholomeux': ['Princeton', 'UBC']}
    >>> person_to_friends = {'Bartholomeux': ['Bob', 'Charlie']}
    >>> get_clubs_of_friends(person_to_friends, person_to_clubs, 'Bartholomeux')
    ['Harvard', 'Yale']
    """

    clubs_of_friends = []

    # get list of clubs
    if person in person_to_friends:
        friends = person_to_friends[person]
    else:
        friends = []

    for friend in friends:
        if friend in person_to_clubs:
            for club in person_to_clubs[friend]:
                clubs_of_friends.append(club)
    
    clubs_of_friends_copy = clubs_of_friends[:]
    for club in clubs_of_friends_copy:
        if person in person_to_clubs:
            if club in person_to_clubs[person]:
                clubs_of_friends.remove(club)

    # remove redundant values
    clubs_of_friends = remove_degenerates(clubs_of_friends)
    clubs_of_friends.sort()

    return clubs_of_friends


def recommend_clubs(
        person_to_friends: dict[str, list[str]],
        person_to_clubs: dict[str, list[str]],
        person: str) -> list[tuple[str, int]]:
    
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Jesse Katsopolis')
    [('Comics R Us', 2), ('Smash Club', 1)]

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner')
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]
    """
    recommended_clubs_to_score = {}
    clubs_person_is_in = person_to_clubs.get(person, [])
    friends = []
    clubs_friends_are_in = get_clubs_of_friends(person_to_friends,
                                                person_to_clubs,
                                                person)
    all_clubs = []
    for club in invert_and_sort(person_to_clubs):
        all_clubs.append(club)
        friends = person_to_friends.get(person, [])

    recommend_clubs_condition_1(clubs_friends_are_in, friends,
                                person_to_clubs,
                                recommended_clubs_to_score)
    recommend_clubs_condition_2(all_clubs, person_to_clubs,
                                clubs_person_is_in,
                                recommended_clubs_to_score)

    # putting it all together    
    recommended_clubs = []
    for recommended_clubs_key in recommended_clubs_to_score:
        if recommended_clubs_key not in clubs_person_is_in:
            recommended_clubs.append((recommended_clubs_key,
                                      recommended_clubs_to_score
                                      [recommended_clubs_key]))

    return recommended_clubs


if __name__ == '__main__':
    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    import doctest
    doctest.testmod()

from typing import TextIO

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}

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

    #collect data
    keys_and_values = []
    for key in key_to_value:
        keys_and_values.append([key, key_to_value[key]])
    keys = []
    for pair in keys_and_values:
        keys.append(pair[0])
    values = []
    for pair in keys_and_values:
        values.append(pair[1])

    value_to_keys = {}
    #initialising dictionary-to-return with new keys
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

    for key in value_to_keys:
        if type(value_to_keys[key]) == list:
            value_to_keys[key].sort()

    return value_to_keys

if __name__ == '__main__':
    print(invert_and_sort(P2C))
    print(invert_and_sort(P2C) == {'Comet Club': ['Michelle Tanner'], 'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis', 'Joey Gladstone'], 'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'], 'Comics R Us': ['Joey Gladstone'], 'Smash Club': ['Kimmy Gibbler']})
    print('\n')
    print(invert_and_sort({'Parent Council': 3, 'Smash Club': 2, 'Orchestra': 2}))
    print(invert_and_sort({'Parent Council': 3, 'Smash Club': 2, 'Orchestra': 2}) == { 3: ['Parent Council'], 2: ['Orchestra', 'Smash Club']})
    print("\n")
    print(invert_and_sort({1: 2, 3: [4, 5]}))
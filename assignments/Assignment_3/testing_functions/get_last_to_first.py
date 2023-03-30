P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Kimmy Gibbler', 'Michelle Tanner'],
       'Danny R Tanner': ['DJ Tanner-Fuller', 'Jesse Katsopolis',
                          'Joey Gladstone']}

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

    >>> get_last_to_first({'Dorothy Jenner': ['Rebecca Jenner', 'Liuqi Wu']}) == {
    ...                                            'Jenner': ['Dorothy', 'Rebecca'],
    ...                                                'Wu': ['Liuqi']}
    True
    """

    #Create a list of names of everyone in the input dict
    list_of_full_names = []
    for person in person_to_friends:
        list_of_full_names.append(person)
        for friend in person_to_friends[person]:
            list_of_full_names.append(friend)
    
    #remove name redundancies
    for name in list_of_full_names:
        while list_of_full_names.count(name) > 1:
            list_of_full_names.remove(name)

    #split names in list
    for i in range(len(list_of_full_names)):
        list_of_full_names[i] = list_of_full_names[i].split()
    #join every name component but surnames
    formatted_givenname_surnames = []
    for name_components in list_of_full_names:
        if len(name_components) > 2:
            surname = name_components[-1]
            given_names = ''
            for component in name_components[:-1]:
                given_names = given_names + component + ' '
            formatted_givenname_surnames.append([given_names.strip(), surname.strip()])
        else:
            formatted_givenname_surnames.append(name_components)

    #create dictionary with surnames as index and corresponding given names as values
    last_to_first = {}
    for full_name in formatted_givenname_surnames:
        last_to_first[full_name[1]] = []
    for full_name in formatted_givenname_surnames:
        if full_name[1] in last_to_first:
            last_to_first[full_name[1]].append(full_name[0])
    
    #sort each key's list
    for surname in last_to_first:
        last_to_first[surname].sort()



    return last_to_first



print(get_last_to_first(P2F))
print(get_last_to_first(P2F) == {'Katsopolis': ['Jesse'], 'Tanner': ['Danny R', 'Michelle', 'Stephanie J'], 'Gladstone': ['Joey'], 'Donaldson-Katsopolis': ['Rebecca'], 'Gibbler': ['Kimmy'], 'Tanner-Fuller': ['DJ']})
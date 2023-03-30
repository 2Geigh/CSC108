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

    #get list of clubs
    friends = person_to_friends[person]

    for friend in friends:
        if friend in person_to_clubs:
            for club in person_to_clubs[friend]:
                clubs_of_friends.append(club)
    
    for club in clubs_of_friends: #checking if the person is in the club
        if person in person_to_clubs:
            if club in person_to_clubs[person]:
                clubs_of_friends.remove(club)

    for item in clubs_of_friends:
        while clubs_of_friends.count(item) > 1:
            clubs_of_friends.remove(item)

    clubs_of_friends.sort()
    
    return clubs_of_friends

if __name__ == '__main__':
    import doctest
    doctest.testmod()
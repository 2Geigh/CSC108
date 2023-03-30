from get_clubs_of_friends import get_clubs_of_friends
from invert_and_sort import invert_and_sort

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

    if person in person_to_clubs:
        clubs_person_is_in = person_to_clubs[person]
    else:
        clubs_person_is_in = []

    clubs_friends_are_in = get_clubs_of_friends(person_to_friends, person_to_clubs, person)
    clubs_person_and_friends_are_in = (clubs_person_is_in + clubs_friends_are_in).sort()

    all_clubs = []
    for club in invert_and_sort(person_to_clubs):
        all_clubs.append(club)

    if person in person_to_friends:
        friends = person_to_friends[person]
    else:
        friends = []

    # CONDITION 1
    for potential_club in clubs_friends_are_in: #for each club that the person is not in
        score = 0
        condition1 = 0 # update for each friend is a member of the potential club.
        condition2 = 0 # update for each member who's in one of person's clubs.

        if potential_club in clubs_friends_are_in:
            for friend in friends:
                if friend in person_to_clubs: #checking condition 1
                    if potential_club in person_to_clubs[friend]:
                        condition1 += 1

        score = condition1 + condition2
        if score > 0:
            recommended_clubs_to_score[potential_club] = score
    
    # CONDITION 2
    for potential_club in all_clubs:
        clubs_to_person = invert_and_sort(person_to_clubs)
        if potential_club in clubs_to_person:
            potential_clubs_members = clubs_to_person[potential_club]
        else:
            potential_clubs_members = []
        
        for member in potential_clubs_members:
            clubs_member_is_in = []
            if member in person_to_clubs:
                clubs_member_is_in = person_to_clubs[member] # GOOD UP UNTIL HERE

            trigger = False
            for club_member_is_in in clubs_member_is_in:
                if club_member_is_in in clubs_person_is_in:
                    trigger = True
            if trigger:
                if potential_club in recommended_clubs_to_score:
                    recommended_clubs_to_score[potential_club] += 1
                else:
                    recommended_clubs_to_score[potential_club] = 1
                trigger = False                
        
    recommended_clubs = []
    for recommended_clubs_key in recommended_clubs_to_score:
        if recommended_clubs_key not in clubs_person_is_in:
            recommended_clubs.append((recommended_clubs_key, recommended_clubs_to_score[recommended_clubs_key]))

    return recommended_clubs

if __name__ == '__main__':
    import doctest
    doctest.testmod()
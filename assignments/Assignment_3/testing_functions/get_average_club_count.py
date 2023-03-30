P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}

def get_average_club_count(person_to_clubs: dict[str, list[str]]) -> int:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to, rounded down to the nearest integer (i.e. use // instead of /).

    >>> get_average_club_count(P2C)
    1
    """

    every_persons_club_count = []
    
    for person in person_to_clubs:
        clubs_this_person_is_in = 0
        for club in person_to_clubs[person]:
            clubs_this_person_is_in += 1
        every_persons_club_count.append(clubs_this_person_is_in)

    sum = 0
    for number in every_persons_club_count:
        sum += number
    
    return sum // len(every_persons_club_count)

print(get_average_club_count(P2C))
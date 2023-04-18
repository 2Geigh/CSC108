# Question 1
## A
def is_eligible_for_award(gpa, major, req_gpa, req_major):
    """
    Do the thing
    >>> is_eligible_for_award(4.0, 'CS', 3.5, 'CS')
    True
    >>> is_eligible_for_award(4.0, 'Econ', 3.5, 'CS')
    False
    >>> is_eligible_for_award(3.3, 'CS', 3.5, 'CS')
    False
    """

    return gpa >= req_gpa and major == req_major
## B

def get_award_winners(applicants: list[tuple[float, str, str]], req_gpa: float,
req_major: str) -> list[tuple[float, str]]:
    """Return a new list of students from applicants who are eligible for an
    award, based on req_gpa and req_major. Each student in applicants is of
    the form (gpa, name, major).
    In the new list, award winning students should be of the form (gpa, name)
    and should appear in the same order as they appear in the original list.
    >>> get_award_winners([(3.6, 'JC', 'CS'), (4.0, 'MB', 'CS'), (3.7, 'JW', 'Econ')], 3.2, 'CS')
    [(3.6, 'JC'), (4.0, 'MB')]
    >>> get_award_winners([(3.6, 'JC', 'Bio'), (4.0, 'MB', 'Bio'),(3.7, 'JW', 'Econ')], 3.7, 'Bio')
    [(4.0, 'MB')]
    """

    to_return = []
    
    for student in applicants:
        if student[0] >= req_gpa and student[2] == req_major:
            to_return.append((student[0], student[1]))

    return to_return



















if __name__ == "__main__":
    import doctest
    doctest.testmod()

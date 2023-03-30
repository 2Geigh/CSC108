def build_grades_dict(lst1: list[str], lst2: list[int], lst3: list[int])\
    -> dict[str, tuple[int]]:
    """Given three parallel lists where lst1 has student names, lst2
    has each student's grade for A1, and lst3 has each student's grade
    for A2, return a dictionary where the keys are student names and the
    values are a tuple

    Precondition:
    - len(lst1) == len(lst2) == len(lst3)
    
    >>> d = build_grades_dict(['Sadia', 'Bumbly', 'Mia'], [50, 60, 70], \
        [60, 70, 80])
    >>> d == {'Sadia': (50, 60), 'Bumbly': (60, 70), 'Mia': (70, 80)}
    True
    """

    # TODO: YOUR CODE HERE


    
def organize_scores(scores: list[list], points_required: int) -> dict[str, tuple[int]]:
    """Given a list of lists where each sublist is in the format:
    [str, int, int, int ...]
    with the first element being a string name and the rest of the
    elements (can be 0 or more) being int scores that the person earned,
    organize the scores into a dictionary where the keys are the
    person's names and each value is that person's score as a tuple
    of two elements.

    The first element in the tuple is a list containing
    all their losing scores (sorted in non-descending order) and the
    second element in the tuple is a list of all their winning scores
    (also sorted in non-descending order). Scores greater than or
    equal to the given points_required are considered winning scores,
    and anything less than points_required is considered a losing score.

    Precondition: Assume each sublist in scores has a unique name
                    as the first element

    >>> lst = [['Sadia', 20, 60, 50], ['Fernando', 30, 55, 63], \
    ['Paul', 90, 80, 200]]
    >>> organize_scores(lst, 50) == {
    ...  'Sadia': ([20], [50, 60]),
    ...  'Fernando': ([30], [55, 63]), 'Paul': ([], [80, 90, 200])}
    True
    """

    # TODO: YOUR CODE HERE










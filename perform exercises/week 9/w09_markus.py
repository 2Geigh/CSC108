"""Week 9 Perform - Part 2"""

# file name: w09_markus.py
#
# Complete the following steps:
# (1) In addition to this file, download and open 
#     fluffy_functions.py in Wing101.
# (2) Review the test cases you chose for the all_fluffy function as part of 
#     the Choosing Test Cases exercise in the Week 9 Rehearse/lecture.
# (3) Implement the test cases you chose as test functions below.
#     Make sure you save your file regularly.
# (4) Run your tests on the correct version of all_fluffy from the 
#     fluffy_functions.py file, where it is named all_fluffy_v0. We have
#     provided an import statement below to help you do that. Make sure your
#     tests all run and pass when the correct code is provided.
# (5) Run your tests on the buggy versions of all_fluffy from the 
#     fluffy_functions.py file. The simplest way to do that is to make the
#     first import statement that we have provided into a comment, and then
#     uncomment one of the import statements that follow.  To test a different
#     buggy version of all_fluffy, uncomment a different import statement.
# (6) When convinced that your tests are complete, submit your modified
#     w09_markus.py file to MarkUs. You can find instructions on submitting a
#     file to MarkUs in the Week *2* Perform -> Accessing Part 2 of the
#     Week 2 Perform (For Credit) on PCRS.
# (7) Verify you have submit the right file to MarkUs by downloading it again
#     and checking it is the one you meant to submit.
# (8) We have also provided a checker test for you to run in MarkUs. This week
#     the checker runs your tests on a correct version of the all_fluffy
#     function.  We will not be marking your style on this exercise, so there
#     will be no PyTA check. We will run additional tests with different
#     versions of buggy code when we mark your submission.

import pytest

# Uncomment ONE of the following statements, depending on which version
# of all_fluffy you wish to test.  Only add/delete the comment (#) symbol.
from fluffy_functions import all_fluffy_v0 as all_fluffy
# from fluffy_functions import all_fluffy_v1 as all_fluffy
# from fluffy_functions import all_fluffy_v2 as all_fluffy


def test_empty_string() -> None:
    """Test that the empty string is fluffy."""
    expected = True
    actual = all_fluffy('')
    msg = "Expected {}, but returned {}".format(expected, actual)
    assert actual is expected, msg
    
def test_single_lowercase_fluffy() -> None:
    """Test that a single lowercase fluffly letter is fluffy."""
    expected = True
    actual = all_fluffy('f')
    msg = "Expected {}, but returned {}".format(expected, actual)
    assert actual is expected, msg

def test_single_lowercase_nonfluffy() -> None:
    """Test that a single lowercase non-fluffly letter is fluffy."""
    expected = False
    actual = all_fluffy('o')
    msg = "Expected {}, but returned {}".format(expected, actual)
    assert actual is expected, msg  

def test_start_with_fluffy() -> None:
    """Test that a fluffy-non-fluffy letter pair, starting with fluffy, is fluffy."""
    expected = False
    actual = all_fluffy('fo')
    msg = "Expected {}, but returned {}".format(expected, actual)
    assert actual is expected, msg 
    
def test_end_with_fluffy() -> None:
    """Test that a fluffy-non-fluffy letter pair, ending with fluffy, is fluffy."""
    expected = False
    actual = all_fluffy('of')
    msg = "Expected {}, but returned {}".format(expected, actual)
    assert actual is expected, msg
    
def test_all_fluffy_with_space() -> None:
    """Test that two fluffy letters with a space inbetween them is fluffy."""
    expected = False
    actual = all_fluffy('f f')
    msg = "Expected {}, but returned {}".format(expected, actual)
    assert actual is expected, msg 
    
def test_single_uppercase_fluffy() -> None:
    """Test if a single uppercase fluffly letter is fluffy."""
    expected = False
    actual = all_fluffy('F')
    msg = "Expected {}, but returned {}".format(expected, actual)
    assert actual is expected, msg 
    
def test_uppercase_lowercase_fluffy_pair() -> None:
    """Test if a pair of a fluffy lowercase letter and its uppercase equivalent
    is fluffy."""
    expected = False
    actual = all_fluffy('Ff')
    msg = "Expected {}, but returned {}".format(expected, actual)
    assert actual is expected, msg
    
def test_fluffy_number_fluffy() -> None:
    """Test if a number sandwhiched between two fluffy letters is fluffy."""
    expected = False
    actual = all_fluffy('f2f')
    msg = "Expected {}, but returned {}".format(expected, actual)
    assert actual is expected, msg 

# Add your other test methods here


if __name__ == '__main__':
    pytest.main(['w09_markus.py'])

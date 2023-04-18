"""Week 10 Perform - Part 2"""

# file name: w10_markus.py
#
# Complete the following steps:
#  (1) Below is a bubble_up function that takes 3 parameters: the list, a left
#      index, and a right index, and bubbles the items in that interval.
#      We have started a function called bubble_down that takes the same 3
#      parameters but it is to bubble in the opposite direction.
#      Complete function bubble_down.
#  (2) Save your file after you make changes, and then run the file by
#      clicking on the green Run button in Wing101. This will let you call your
#      modified function in the shell. An asterisk * on the Wing101
#      w10_markus.py tab indicates that modifications have NOT been saved.
#  (3) Test your function in the Wing101 shell by evaluating the examples from
#      the docstring and confirming that the correct result is displayed.
#  (4) Test your function using different function arguments.
#  (5) When convinced that your function is correct, submit your modified
#      file to MarkUs. You can find instructions on submitting a file
#      to MarkUs in Week *2* Perform -> Accessing Part 2 of the
#       Week 2 Perform (For Credit) on PCRS.
#  (6) Verify you have submit the right file to MarkUs by downloading it again
#      and checking it is the one you meant to submit.
#  (7) We have also provided a checker test for you to run on MarkUs. Click on
#      the Automated Testing tab and then Run tests to make sure your code
#      passes our simple test case. Go back to step (1) if errors were reported
#      and modify your work.  You may need to click on some arrows to see all
#      of the error report. Note that we will run additional tests when we mark
#      your submission.


# This function is complete and provided for reference only.
# This function will not be marked.
def bubble_up(values: list, left: int, right: int) -> None:
    """Bubble up through values[left: right+1], swapping items that are out of
    order. Note that use of this slicing notation means that items
    values[left], values[left + 1], values[left + 2], ..., values[right] could
    be modified.

    Precondition: left and right are valid indexes in values.

    >>> list_example_1 = [4, 3, 2, 1, 0]
    >>> bubble_up(list_example_1, 0, 3)
    >>> list_example_1
    [3, 2, 1, 4, 0]
    >>> list_example_2 = [4, 3, 2, 1, 0]
    >>> bubble_up(list_example_2, 2, 4)
    >>> list_example_2
    [4, 3, 1, 0, 2]
    """

    for i in range(left, right):
        if values[i] > values[i + 1]:
            temp = values[i]
            values[i] = values[i + 1]
            values[i + 1] = temp


# Use the bubble_up function as a starting point to help you complete the
# bubble_down function.
def bubble_down(values: list, left: int, right: int) -> None:
    """Bubble down through values[left: right+1], swapping items that are out
    of order. Note that use of this slicing notation means that items
    values[left], values[left + 1], values[left + 2], ..., values[right] could
    be modified.

    Precondition: left and right are valid indexes in values.

    >>> list_example_1 = [4, 3, 2, 1, 0]
    >>> bubble_down(list_example_1, 1, 3)
    >>> list_example_1
    [4, 1, 3, 2, 0]
    >>> list_example_2 = [4, 3, 2, 1, 0]
    >>> bubble_down(list_example_2, 0, 4)
    >>> list_example_2
    [0, 4, 3, 2, 1]
    """

    # get reverse list of indexes to iterate over
    indexes = []
    for i in range(left, right + 1):
        indexes.append(i)
    indexes.reverse()

    for index in indexes:
        if index != indexes[-1]:
            if values[index] < values[index - 1]:
                temp = values[index - 1]
                values[index - 1] = values[index]
                values[index] = temp


if __name__ == '__main__':
    import doctest
    doctest.testmod()

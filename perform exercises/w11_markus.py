"""Week 11 Perform - Part 2"""

# file name: w11_markus.py
#
# Complete the following steps:
#
#  (1) Add an __init__ method to the Widget class below. Each object of type
#      Widget should have an instance variable called name and an instance
#      variable called cost that represents a cost in dollars; those values are
#      passed in when an object of type Widget is initialized.
#  (2) Add a method to class Widget called is_cheap that returns True if the
#      cost is less than $10, and False otherwise.
#  (3) Add proper doctrings along with two examples for each method. You may
#      use the Sample Usage code given below in your work.
#  (4) Test your methods in the Wing101 shell by evaluating the examples from
#      the docstrings and confirming that the results are correct. For a
#      quicker way to test with your examples, you may uncomment the
#      doctest.testmod() call on the last line of this module so that the
#      docstring examples are run when this module is run.
#  (5) When you are convinced that your methods are correct, submit your
#      modified file to MarkUs. You can find instructions on submitting a file
#      to MarkUs in Week *2* Perform -> Accessing Part 2 of the
#      Week 2 Perform (For Credit) on PCRS.
#  (6) Verify you have submitted the right file to MarkUs by downloading it
#      and checking that the downloaded file is the one you meant to submit.
#  (7) We have also provided a checker test for you to run on MarkUs. Click on
#      the Automated Testing tab and then Run tests to make sure your code
#      passes our simple test case. Go back to step (1) if errors were reported
#      and modify your work.  You may need to click on some arrows to see all
#      of the error report. Note that we will run additional tests when we mark
#      your submission.


class Widget:
    """A class representing a simple Widget

    === Instance Attributes (the attributes of this class and their types) ===
    name: the name of this Widget (str)
    cost: the cost of this Widget (int); cost >= 0

    === Sample Usage (to help you understand how this class would be used) ===
    >>> my_widget = Widget('Puzzle', 15)
    >>> my_widget.name
    'Puzzle'
    >>> my_widget.cost
    15
    >>> my_widget.is_cheap()
    False
    >>> your_widget = Widget("Rubik's Cube", 6)
    >>> your_widget.name
    "Rubik's Cube"
    >>> your_widget.cost
    6
    >>> your_widget.is_cheap()
    True
    """
    
    def __init__(self, name: str, cost: float) -> None:
        """
        Initiaises an instance of an object of this class with values name
        and cost based on the inputted values.
        
        >>> your_widget = Widget("Rubik's Cube", 6)
        >>> your_widget.name
        "Rubik's Cube"
        >>> your_widget.cost
        6
        
        >>> my_widget = Widget('Puzzle', 15)
        >>> my_widget.name
        'Puzzle'
        >>> my_widget.cost
        15
        """
        
        self.name = name
        self.cost = cost
    
    def is_cheap(self) -> bool:
        """
        Returns true if an instance of this class' cost is less than 10.
        False otherwise
        
        >>> my_widget = Widget('Puzzle', 15)
        >>> my_widget.is_cheap()
        False
        
        >>> your_widget = Widget("Rubik's Cube", 6)
        >>> your_widget.is_cheap()
        True
        """
        return self.cost < 10


if __name__ == '__main__':
    import doctest
    # Uncomment the line below if you prefer to test your examples with doctest
    doctest.testmod()

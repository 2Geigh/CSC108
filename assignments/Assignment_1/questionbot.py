"""CSC108/CSCA08: Winter 2023 -- Assignment 1: Question Bot

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2023 Paul Gries, Sophia Huynh, Kaveh Mahdaviani, and Sadia Sharmin

====

This module has the code for a simple chatbot that rephrases questions
as statements and statements as questions.

Load the program into the Python shell by clicking the green triangle
in Wing101. Then you can chat as follows at the Python shell.

>>> chat('The dog ate my homework!')
'Homework is a meme.'
"""

# This tells Python to give us access to the functions in chat_utilities.py.
from chat_utilities import *

import numpy as np

# Whether to run doctests. See the bottom of this file to see it in action.
DOCTEST_MODE = True

# Punctuation.
SEPARATOR = '|'
SPACE = ' '
PERIOD = '.'
QUESTION_SYMBOL = '?'
EXCLAMATION_SYMBOL = '!'

# Key terms.
HOMEWORK_KEYWORD = 'homework'

# A list of helping verbs.
HELPING_VERBS = '|have|has|had|should|would|could|might|may|will|' + \
                'is|am|are|was|be|do|does|did|'

# Special Canadian words.
CANADIAN_WORD_1 = 'snow'
CANADIAN_WORD_2 = 'ice'
CANADIAN_WORD_3 = 'hockey'

# Question words that start a sentence.
QUESTION_KEYWORD_1 = 'Will'
QUESTION_KEYWORD_2 = 'Can'

# Response fragments.
HOMEWORK_RESPONSE = 'Homework is a meme.'

EXCLAMATION_RESPONSE = ' ate my homework.'

CANADIAN_RESPONSE = ', eh?'

QUESTION_RESPONSE_0A = 'Is '
QUESTION_RESPONSE_0B = ' the homework topic?'

QUESTION_RESPONSE_1 = 'The future is opaque.'

QUESTION_RESPONSE_2A = ' is as '
QUESTION_RESPONSE_2B = ' does.'

QUESTION_RESPONSE_3A = 'Why do you say "'
QUESTION_RESPONSE_3B = '" and "'
QUESTION_RESPONSE_3C = '"?'


####################################
# TASK 1.1: Homework-related Inputs
# Complete the docstring examples below.
# You do not have to write any code for this task, but rather, read
# the code we have provided, understand it, and pay attention to our
# use of constants. You are expected to use constants accordingly, when
# appropriate, for the rest of the tasks.
####################################

def contains_homework(sentence: str) -> bool:
    """
    Return whether `sentence` contains the word 'homework', regardless of case.

    >>> contains_homework('The dog has eaten my Homework!')

    >>> contains_homework('The dog has eaten my lunch!')

    >>> contains_homework('The dog has eaten my hoMewOrK.')

    """

    # Below, we are using the constant HOMEWORK_KEYWORD defined at the beginning
    # of this file, and the function get_lowercase_version which
    # we imported from chat_utilities.py
    return HOMEWORK_KEYWORD in get_lowercase_version(sentence)


def do_homework() -> str:
    """
    Return 'Homework is a meme.'

    >>> do_homework()

    """

    return HOMEWORK_RESPONSE


####################################
# TASK 2: Exclamations
####################################

def is_exclamation(input: str) -> bool:
    """
    This function returns a true or false boolean if the inputted string does or does not end with an "!", respectively.

    >>> is_exclamation("doo?")
    False

    >>> is_exclamation("boo!")
    True

    >>> is_exclamation("!")
    True
    """

    if input[-1] == "!":
        return True

    return False


def do_exclamation(sentence: str) -> str:
    """
    Using a full sentence as input, this function returns the last word of the input, capitalized, with ' ate my homework' concatenated on the end.
    
    >>> do_exclamation("I play with my dog!")
    'Dog ate my homework.'

    >>> do_exclamation('ding dong!')
    'Dong ate my homework.'

    >>> do_exclamation('dong!')
    'Input must be a complete, exclamatory sentence.'
    """

    if (count_words(sentence) >= 2) and (is_exclamation(sentence) is True):
        return get_capitalized_word(get_last_word(sentence)) + "ate my homework."

    return 'Input must be a complete, exclamatory sentence.'


####################################
# TASK 3: Helping Verbs
####################################

# The following helper function is already completed for you
# Do not add or change anything in this function
def is_helping_verb(word: str) -> bool:
    """
    Return whether word is a lowercase helping verb in HELPING_VERBS.
    Every word in HELPING_VERBS is surrounded by SEPARATOR characters,
    for example '|will|'.

    >>> is_helping_verb('do')
    True
    >>> is_helping_verb('i')
    False
    """

    return (SEPARATOR + word + SEPARATOR) in HELPING_VERBS


def contains_helping_verb(sentence: str) -> bool:
    """
    This function returns True if the inputted sentence argument ends with a period and contains a lowercase helping verb as its third word, and False otherwise.

    >>> contains_helping_verb('The dog has eaten my notes.')
    True

    >>> contains_helping_verb('The big dog has eaten my notes.')
    False
    """
    if sentence[-1] != ".":
        return False

    #checking if the third word is lowercase
    if not (get_word(sentence, 2) == get_lowercase_version(get_word(sentence, 2))):
        return False

    #checking if said third word is a helping verb
    if not (is_helping_verb(get_word(sentence, 2))):
        return False
    
    return True


def do_helping_verb(statement: str) -> bool:
    """
    This function takes the argument, a statement (ends with a .) whose third word is a helping verb, and returns a question generated by moving the helping verb to the front.
    
    >>> do_helping_verb('The dog has eaten my notes.')
    'Has the dog eaten my notes?'

    >>> do_helping_verb('Poor Clara had slept through her test.')
    'Had poor Clara slept through her test?'

    >>> do_helping_verb("boo.")
    "Sentence is either not a statement, or a statement which does not contain a helping verb as its third word."

    >>> do_helping_verb("bee")
    "Sentence is either not a statement, or a statement which does not contain a helping verb as its third word."
    """

    if not contains_helping_verb(statement):
        return "Sentence is either not a statement, or a statement which does not contain a helping verb as its third word."

    helping_verb = get_word(statement, 2)
    remainder = " "

    for i in np.arange(3, count_words(statement) - 1):
        remainder = remainder + " " + get_word(statement, i)

    return helping_verb + remainder

    

####################################
# TASK 4: Canadian
####################################

# TODO: write functions is_canadian_question and do_canadian_question.
def is_canadian_question(question: str) -> bool:
    """
    Returns True if an inputted string is a question (if it has a ? at the end) which contains some form of a Canadian word in the sentence ('snow', 'ice', 'hockey').
    Returns False otherwise.
    
    >>> is_canadian_question("Do you like icecream?")
    True

    >>> is_canadian_question("Icecream?")
    False

    >>> is_canadian_question("dookey?")
    False

    >>> is_canadian_question("snow")
    False
    """
    if question[-1] != "?":
        return False

    for CANADIAN_WORD in [CANADIAN_WORD_1, CANADIAN_WORD_2, CANADIAN_WORD_3]:
        if CANADIAN_WORD in question:
            return True

def do_canadian_question(canadian_question: str) -> str:
    """
    Takes a question, returns it with ', eh?' on the end instead of just ? if it's Canadian as per is_canadian_question().
    
    >>> do_canadian_question('Am I Canadian?')
    'That doesn't sound very Canadian to me, eh.'

    >>> do_canadian_question('iceream?')
    'icecream, eh?'

    >>> do_canadian_question('iceream')
    'That doesn't sound very Canadian to me, eh.'
    """


    if is_canadian_question(canadian_question) is True:
        return canadian_question[0,len(canadian_question) - 2] + ", eh?"

    return "That doesn't sound very Canadian to me, eh."
    


####################################
# TASK 5: Questions
####################################

# TODO: write functions is_question and do_question.


####################################
# TASK 6: Question Exclamations
####################################

# TODO: write functions is_question_exclamation and do_question_exclamation.


####################################
# TASK 8: None of the above
####################################

# TODO: write function do_unmatched.


####################################
# Chat Functionality
####################################

# TASK 7: Make sure the chat function has the correct order for all checks
def chat(sentence: str) -> str:
    """Return a question if `sentence` is a statement or exclamation, and
    return a statement if `sentence` is a question.

    >>> chat('The dog ate my homework!')
    'Homework is a meme.'
    >>> chat('The thing is due tomorrow!')
    'Tomorrow ate my homework.'
    >>> chat('The dog has eaten my shoe.')
    'Has the dog eaten my shoe?'
    >>> chat('You watching the hockey game?')
    'You watching the hockey game, eh?'
    >>> chat('How much wood could a woodchuck chuck?')
    'Why do you say "much" and "chuck"?'
    >>> chat("Yes! Don't you think the pictures are awesome?")
    'Why do you say "Don\\'t" and "awesome"?'
    """

    if contains_homework(sentence):
        return do_homework()
    # TODO: write more here to handle other kinds of sentences.


if __name__ == '__main__':

    if DOCTEST_MODE:
        import doctest
        doctest.testmod()

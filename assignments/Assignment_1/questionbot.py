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

UNMATCHED_RESPONSE = 'What do you mean?'


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
    Return whether the inputed sentence contains the word 'homework',
    regardless of case.

    >>> contains_homework('The dog has eaten my Homework!')
    True

    >>> contains_homework('The dog has eaten my lunch!')
    False

    >>> contains_homework('The dog has eaten my hoMewOrK.')
    True

    """

    # Below, we are using the constant HOMEWORK_KEYWORD defined at the beginning
    # of this file, and the function get_lowercase_version which
    # we imported from chat_utilities.py
    return HOMEWORK_KEYWORD in get_lowercase_version(sentence)


def do_homework() -> str:
    """
    Return 'Homework is a meme.'

    >>> do_homework()
    'Homework is a meme.'
    """

    return HOMEWORK_RESPONSE


####################################
# TASK 2: Exclamations
####################################

def is_exclamation(input_string: str) -> bool:
    """
    Returns a true or false boolean if the inputted string does or
    does not end with an "!", respectively.

    >>> is_exclamation("doo?")
    False

    >>> is_exclamation("boo!")
    True

    >>> is_exclamation("!")
    True
    """

    return input_string[-1] == EXCLAMATION_SYMBOL


def do_exclamation(sentence: str) -> str:
    """
    Returns the last word of the input, capitalized,
    with ' ate my homework' concatenated on the end.
    
    Precondition: sentence must be exclamatory as per is_exclamation
                  and longer than one word.
    
    >>> do_exclamation("I play with my dog!")
    'Dog ate my homework.'

    >>> do_exclamation('ding dong!')
    'Dong ate my homework.'

    >>> do_exclamation('dong!')
    'Input must be a complete, multi-word, exclamatory sentence.'
    """

    if (count_words(sentence) >= 2) and (is_exclamation(sentence)):
        return get_capitalized_word(get_last_word(sentence)) + \
            EXCLAMATION_RESPONSE

    return 'Input must be a complete, multi-word, exclamatory sentence.'


####################################
# TASK 3: Helping Verbs
####################################

# The following helper function is already completed for you
# Do not add or change anything in this function
def is_helping_verb(word: str) -> bool:
    """
    Return whether word is a lowercase helping verb in HELPING_VERBS..

    >>> is_helping_verb('do')
    True
    
    >>> is_helping_verb('Do')
    False
    
    >>> is_helping_verb('i')
    False
    """

    return (SEPARATOR + word + SEPARATOR) in HELPING_VERBS


def contains_helping_verb(sentence: str) -> bool:
    """
    Returns True if sentence input ends with a period and contains a lowercase
    helping verb as its third word. False otherwise.
    
    Precondition: sentence is a properly-formed English sentence with at least
                  three words.

    >>> contains_helping_verb('The dog has eaten my notes.')
    True

    >>> contains_helping_verb('The big dog has eaten my notes.')
    False
    """
    if sentence[-1] != PERIOD:
        return False

    # checking if the third word is lowercase
    if get_word(sentence, 2) != get_lowercase_version(get_word(sentence, 2)):
        return False

    # checking if said third word is a helping verb
    if not (is_helping_verb(get_word(sentence, 2))):
        return False
    
    return True


def do_helping_verb(statement: str) -> bool:
    """
    Takes input statement and returns a question generated by moving its
    helping verb to the front.
    
    Precondition: sentence is a properly-formed English sentence at least three 
                  words long with punctuation.
    
    >>> do_helping_verb('The dog has eaten my notes.')
    'Has the dog eaten my notes?'

    >>> do_helping_verb('Poor Clara had slept through her test.')
    'Had poor Clara slept through her test?'

    >>> do_helping_verb("boo.")
    'Is there anything I can do to help with, say, your verbs?'

    >>> do_helping_verb("a bee has")
    'Is there anything I can do to help with, say, your verbs?'
    """

    if not contains_helping_verb(statement):
        return "Is there anything I can do to help with, say, your verbs?"

    # organizing the first three words of the sentence, now with the helping
    # verb repositioned as the first word
    remainder = get_capitalized_word(get_word(statement, 2)) + SPACE +\
        get_lowercase_version(get_word(statement, 0)) + SPACE + \
        get_word(statement, 1)
    
    # rebuilding statemnt with the words after the first three in the same order
    i = 4
    while i <= count_words(statement):
        if i == count_words(statement):
            remainder = remainder + SPACE + get_word(statement, i - 1)[:-1] +\
                QUESTION_SYMBOL
        else:
            remainder = remainder + SPACE + get_word(statement, i - 1)
        i = i + 1

    return remainder


####################################
# TASK 4: Canadian
####################################

def is_canadian_question(question: str) -> bool:
    """
    Returns True if an inputted string is a question (if it has a ? at the end)
    which contains some form of a lowercase Canadian word in the sentence
    ('snow', 'ice', 'hockey'). False otherwise.
    
    >>> is_canadian_question("Do you like icecream?")
    True

    >>> is_canadian_question("Icecream?")
    False

    >>> is_canadian_question("dookey?")
    False

    >>> is_canadian_question("snow")
    False
    """
    if question[-1] != QUESTION_SYMBOL:
        return False
        
    canadian_words = [CANADIAN_WORD_1, CANADIAN_WORD_2, CANADIAN_WORD_3]
    
    for CANADIAN_WORD in canadian_words:
        if CANADIAN_WORD in question:
            return True
        
    return False


def do_canadian_question(canadian_question: str) -> str:
    """
    Takes a question, returns it with ', eh?' on the end instead of just ? if
    it's Canadian as per is_canadian_question().

    Precondition: sentence is a properly-formed punctuated English sentence
    
    >>> do_canadian_question('icecream?')
    'icecream, eh?'
    
    >>> do_canadian_question('icecream.')
    'How should I know, I am too busy playing in the snow.'
    """
    
    if is_canadian_question(canadian_question):
        return canadian_question[0:-1] + CANADIAN_RESPONSE
    
    return 'How should I know, I am too busy playing in the snow.'


####################################
# TASK 5: Questions
####################################

def is_question(string: str) -> bool:
    """
    Returns True if the inputed stringends with a question mark ('?'). False 
    otherwise.
    
    >>> is_question("e")
    False

    >>> is_question("e?")
    True
    """

    return string[-1] == QUESTION_SYMBOL


def do_question(question: str) -> str:
    """
    Answers input question, whether with a statement or another question.
    
    Precondition: input must be a properly formed question (ending in ?)
    
    >>> do_question("Yes! Do you think the pictures are awesome?")
    'Why do you say "Do" and "awesome"?'
    
    >>> do_question("Hungry?")
    'Is hungry the homework topic?'
    
    >>> do_question("Will you help me with the cleaning?")
    'The future is opaque.'
    
    >>> do_question("Can a dog go to the gym?")
    'Gym is as gym does.'
    """
    
    # scenario 0
    if count_words(question) == 1:
        return QUESTION_RESPONSE_0A + get_lowercase_version(question)[0:-1]\
            + QUESTION_RESPONSE_0B
    
    # scenario 1
    if get_first_word(question) == QUESTION_KEYWORD_1:
        return QUESTION_RESPONSE_1
    
    # scenario 2
    elif get_first_word(question) == QUESTION_KEYWORD_2:
        return get_capitalized_word(get_last_word(question)) + \
            QUESTION_RESPONSE_2A + get_last_word(question) + \
            QUESTION_RESPONSE_2B

    else:
        # scenario 3
        if get_lowercase_version(get_first_word(question)) ==\
           get_lowercase_version(get_last_word(question)):
            return QUESTION_RESPONSE_3A + get_word(question, 1) + \
                QUESTION_SYMBOL

        # scenario 4
        else:
            return QUESTION_RESPONSE_3A + get_word(question, 1) + \
                QUESTION_RESPONSE_3B + get_last_word(question) + \
                QUESTION_RESPONSE_3C
        
    return 'Could you please rephrase the question?'


####################################
# TASK 6: Question Exclamations
####################################

def is_question_exclamation(input_string: str) -> bool:
    """ 
    Returns True if the given string ends with '?!'. False otherwise.

    >>> is_question_exclamation("Eh?!")
    True

    >>> is_question_exclamation("Eh!?")
    False
    """

    return input_string[-1] == EXCLAMATION_SYMBOL and input_string[-2] ==\
        QUESTION_SYMBOL


def do_question_exclamation(question_exclamation: str) -> str:
    """
    Takes an input question-exclamation string and passes it through 
    do_question() as though it ended with "?".
    
    Precondition: input string must end with a "?!"
    
    >>> do_question_exclamation("Yes! Do you think the pictures are awesome?!")
    'Why do you say "Do" and "awesome"?'
    
    >>> do_question_exclamation("Hungry?!")
    'Is hungry the homework topic?'
    
    >>> do_question_exclamation("Will you help me with the cleaning?!")
    'The future is opaque.'
    
    >>> do_question_exclamation("Can a dog go to the gym?!")
    'Gym is as gym does.'
    
    """
    if not is_question_exclamation(question_exclamation):
        return 'Could you please speak in a different tone?'
    
    return do_question(question_exclamation[:-1])


####################################
# TASK 8: None of the above
####################################

def do_unmatched() -> str:
    """
    Returns 'What do you mean?', the unmatched response.
    """

    return UNMATCHED_RESPONSE

    
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

    if type(sentence) != str:
        return 'Unfortunately, I am only good at basic conversation.'
    
    if len(sentence) == 0:
        return 'Wonderful weather we\'re having, eh?'

    if contains_homework(sentence):
        return do_homework()

    if is_question_exclamation(sentence):
        return do_question_exclamation(sentence)

    if is_exclamation(sentence):
        return do_exclamation(sentence)

    if contains_helping_verb(sentence):
        return do_helping_verb(sentence)

    if is_canadian_question(sentence):
        return do_canadian_question(sentence)
    
    if is_question(sentence):
        return do_question(sentence)

    return do_unmatched()    


if __name__ == '__main__':

    if DOCTEST_MODE:
        import doctest
        doctest.testmod()

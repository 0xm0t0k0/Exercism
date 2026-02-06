"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(time_spent):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    minutes_needed = EXPECTED_BAKE_TIME - time_spent
    return minutes_needed

def preparation_time_in_minutes(layers):
    '''The amount of layers multiplied by the time it takes to prepare them'''
    time = layers * PREPARATION_TIME
    return time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''The total time u have spent cooking'''
    layers_time = preparation_time_in_minutes(number_of_layers)
    total = layers_time + elapsed_bake_time
    return total

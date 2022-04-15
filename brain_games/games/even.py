#!/usr/bin/env python

from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
FIRST_NUMBER = 2
LAST_NUMBER = 100


def is_it_even(number):
    return number % 2 == 0


def get_game_round():
    number = randint(FIRST_NUMBER, LAST_NUMBER)
    correct_answer = 'yes' if is_it_even(number) else 'no'
    return number, correct_answer

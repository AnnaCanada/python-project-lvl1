#!/usr/bin/env python

from random import randint

TASK_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_round():
    number = randint(2, 100)
    return number, 'yes' if number % 2 == 0 else 'no'

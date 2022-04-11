#!/usr/bin/env python

from random import randint

TASK_DESCRIPTION = 'Answer "yes" if given the number is prime. Otherwise answer "no".'


def get_game_round():
    number = randint(1, 100)
    for index in range(2, number):
        if (number % index) == 0:
            return number, 'no'
    return number, 'yes'

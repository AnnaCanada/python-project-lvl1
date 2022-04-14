#!/usr/bin/env python

from random import randint

TASK = 'Answer "yes" if given the number is prime. Otherwise answer "no".'
FIRST_NUMBER = 2
LAST_NUMBER = 100


def is_it_prime(number):
    for index in range(2, number):
        if (number % index) == 0:
            return 'no'
    return 'yes'


def get_game_round():
    number = randint(FIRST_NUMBER, LAST_NUMBER)
    return number, is_it_prime(number)

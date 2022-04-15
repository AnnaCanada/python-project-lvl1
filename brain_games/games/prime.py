#!/usr/bin/env python

from random import randint

TASK = 'Answer "yes" if given the number is prime. Otherwise answer "no".'
FIRST_NUMBER = 2
LAST_NUMBER = 100


def is_it_prime(number):
    for index in range(2, number):
        if (number % index) == 0:
            return False
    return True


def get_game_round():
    number = randint(FIRST_NUMBER, LAST_NUMBER)
    correct_answer = 'yes' if is_it_prime(number) else 'no'
    return number, correct_answer

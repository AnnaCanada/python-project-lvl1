#!/usr/bin/env python

from math import gcd
from random import randint

TASK = 'Find the greatest common divisor of given numbers.'
FIRST_NUMBER = 1
LAST_NUMBER = 100


def get_game_round():
    num1 = randint(FIRST_NUMBER, LAST_NUMBER)
    num2 = randint(FIRST_NUMBER, LAST_NUMBER)
    correct_answer = gcd(num1, num2)
    return ('{} {}'.format(num1, num2)), correct_answer

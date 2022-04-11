#!/usr/bin/env python

from math import gcd
from random import randint

TASK = 'Find the greatest common divisor of given numbers.'


def get_game_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    correct_answer = gcd(num1, num2)
    return ('{} {}'.format(num1, num2)), correct_answer

#!/usr/bin/env python

import random

TASK = 'What is the result of the expression?'
FIRST_NUMBER = 1
LAST_NUMBER = 10


def get_game_round():
    num1 = random.randint(FIRST_NUMBER, LAST_NUMBER)
    num2 = random.randint(FIRST_NUMBER, LAST_NUMBER)
    ops = ['+', '-', '*']
    operation = random.choice(ops)
    question = ('{} {} {}'.format(num1, operation, num2))
    return question, eval(question)

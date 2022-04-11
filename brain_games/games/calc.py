#!/usr/bin/env python

import random

TASK_DESCRIPTION = 'What is the result of the expression?'


def get_game_round():
    ops = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(ops)
    question = ('{} {} {}'.format(num1, operation, num2))
    return question, eval(question)

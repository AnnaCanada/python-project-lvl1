#!/usr/bin/env python

from random import randint

TASK_DESCRIPTION = 'What number is missing in the progression?'

count = randint(5, 10)


def build_the_progression():
    start = randint(1, 10)
    step = randint(1, 10)
    progression = [start]
    index = 0
    while index < (count - 1):
        index = index + 1
        start += step
        progression.append(start)
    return progression


def get_game_round():
    new_progression = build_the_progression()
    question = []
    hiden_number = randint(0, count - 2)
    for index in range(count):
        question.append(str(new_progression[index]))
    question[hiden_number] = '..'
    return ' '.join(question), new_progression[hiden_number]

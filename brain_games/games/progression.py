#!/usr/bin/env python

from random import randint

TASK = 'What number is missing in the progression?'
FIRST_NUMBER = 1
LAST_NUMBER = 10
MIN_LENGTH = 5
MAX_LENGTH = 10
FIRST_INDEX = 0


def build_progression(initial_term, common_diff, progression_len):
    progression = [initial_term]
    index = 0
    while index < (progression_len - 1):
        index = index + 1
        initial_term += common_diff
        progression.append(initial_term)
    return progression


def get_string(progression_len, hiden_index, answer):
    question = []
    for index in range(progression_len):
        question.append(str(answer[index]))
    question[hiden_index] = '..'
    return ' '.join(question)


def get_game_round():
    initial_term = randint(FIRST_NUMBER, LAST_NUMBER)
    common_diff = randint(FIRST_NUMBER, LAST_NUMBER)
    progression_len = randint(MIN_LENGTH, MAX_LENGTH)
    hiden_index = randint(FIRST_INDEX, progression_len - 2)
    answer = build_progression(initial_term, common_diff, progression_len)
    return get_string(progression_len, hiden_index, answer), answer[hiden_index]

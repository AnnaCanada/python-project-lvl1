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


def get_question(progression, hidden_element_index):
    question = []
    for element in progression:
        question.append(str(element))
    question[hidden_element_index] = '..'
    return ' '.join(question)


def get_game_round():
    initial_term = randint(FIRST_NUMBER, LAST_NUMBER)
    common_diff = randint(FIRST_NUMBER, LAST_NUMBER)
    progression_len = randint(MIN_LENGTH, MAX_LENGTH)
    hidden_element_index = randint(FIRST_INDEX, progression_len - 2)
    answer = build_progression(initial_term, common_diff, progression_len)
    return (
        get_question(answer, hidden_element_index),
        answer[hidden_element_index],
    )

#!/usr/bin/env python

from random import randint

TASK = 'What number is missing in the progression?'
COUNT = randint(5, 10)


def build_progression(initial_term, common_difference):
    progression = [initial_term]
    index = 0
    while index < (COUNT - 1):
        index = index + 1
        initial_term += common_difference
        progression.append(initial_term)
    return progression


def ask_the_question():
    new_progression = build_progression(
        initial_term=randint(1, 10),
        common_difference=randint(1, 10),
    )
    question = []
    random_index = randint(0, COUNT - 2)
    for index in range(COUNT):
        question.append(str(new_progression[index]))
    question[random_index] = '..'
    return ' '.join(question), new_progression[random_index]


def get_game_round():
    return ask_the_question()

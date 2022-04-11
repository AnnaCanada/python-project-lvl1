#!/usr/bin/env python

import prompt

COUNT_ROUNDS = 3


def welcome_user():
    print('Welcome to the Brain Games!')


def get_user_name():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def play_game(game):
    welcome_user()
    name = get_user_name()
    print(game.TASK)
    index = 1
    while index <= COUNT_ROUNDS:
        index = index + 1
        question, correct_answer = game.get_game_round()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            continue
        print(
            f"'{answer}' is wrong answer ;(. ",
            f"Correct answer was '{correct_answer}'\n",
            f"Let's try again, {name}!",
        )
        return

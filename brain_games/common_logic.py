#!/usr/bin/env python

import prompt

count_rounds = 3


def welcome_user():
    print('Welcome to the Brain Games!')


def get_user_name():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def play_game(game):
    welcome_user()
    name = get_user_name()
    print(game.TASK_DESCRIPTION)
    index = 1
    while index <= 3:
        index = index + 1
        question, correct_answer = game.get_game_round()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            continue
        print('{} is wrong answer ;( Correct answer was {}.'.format(answer, correct_answer))
        return print("Let's try again, {}!".format(name))
    return print('Congratulations, {}!'.format(name))

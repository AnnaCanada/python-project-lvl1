

import prompt

print('Welcome to the Brain Games!')

name = prompt.string('May I have your name? ')


def welcome_user():
    if name:
        print('Hello, {}!'.format(name))

#!/usr/bin/env python


from random import randint

import prompt

from brain_games import cli


def main():
    cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 1
    while index <= 3:
        index = index + 1
        number = randint(2, 100)
        print('Question: {}'.format(number))

        def correct_answer():
            return 'yes' if number % 2 == 0 else 'no'
        correct_answer()
        answer = prompt.string('Your answer: ')
        if answer == correct_answer():
            print('Correct!')
            continue
        else:
            print("{} is wrong answer ;( Correct answer was {}.\nLet's try again, {}".format(answer, correct_answer(), cli.name))
            break
    else:
        return print('Congratulations, {}!'.format(cli.name))


if __name__ == '__main__':
    main()

#!/usr/bin/env python


from random import randint

import prompt

from brain_games import cli


def main():
    cli.welcome_user()
    print('Answer "yes" if given the number is prime. Otherwise answer "no".')
    cycle = 1
    while cycle <= 3:
        cycle = cycle + 1
        number = randint(1, 100)
        print('Question: {}'.format(number))

        def correct_answer():
            for index in range(2, number):
                if (number % index) == 0:
                    return 'no'
            else:
                return 'yes'
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

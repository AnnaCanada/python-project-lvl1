#!/usr/bin/env python


import random

import prompt

from brain_games import cli


def main():
    cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    index = 1
    while index <= 3:
        index = index + 1
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print('Question: {} {}'.format(num1, num2))

        def correct_answer():
            num1a = num1
            num2a = num2
            while num1a != 0 and num2a != 0:
                if num1a >= num2a:
                    num1a = num1a % num2a
                else:
                    num2a = num2a % num1a
            return str(num1a + num2a)
        correct_answer()
        answer = prompt.string('Your answer: ')
        if answer == correct_answer():
            print('Correct!')
            continue
        else:
            print("{} is wrong answer ;( Correct answer was {}.\nLet's try again, {}".format(answer, correct_answer(), cli.name))
            break
    else:
        print('Congratulations, {}!'.format(cli.name))


if __name__ == '__main__':
    main()

#!/usr/bin/env python


import random

import prompt

from brain_games import cli


def main():
    cli.welcome_user()
    print('What is the result of the expression?')
    index = 1
    while index <= 3:
        index = index + 1
        ops = ['+', '-', '*']
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(ops)
        print('Question: {} {} {}'.format(num1, operation, num2))
        correct_answer = eval(str(num1) + operation + str(num2))
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            continue
        return print("{} is wrong answer ;( Correct answer was {}.\nLet's try again, {}".format(answer, correct_answer, cli.name))
    else:
        print('Congratulations, {}!'.format(cli.name))


if __name__ == '__main__':
    main()

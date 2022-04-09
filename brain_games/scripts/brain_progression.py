#!/usr/bin/env python


from random import randint

import prompt

from brain_games import cli


def main():
    cli.welcome_user()
    print('What number is missing in the progression?')
    cycle = 0
    while cycle < 3:
        cycle = cycle + 1
        count = randint(5, 10)
        start = randint(1, 10)
        step = randint(1, 10)
        def build_the_progression(start, step):
            progression = [start]
            index = 0
            while index < (count - 1):
                index = index + 1
                start = start + step
                progression.append(start)
            return progression
        new_progression = build_the_progression(start, step)
        hiden_number = randint(0, count - 2)
        def ask_question():
            question = []
            for index in range(count):
                question.append(str(new_progression[index]))
            question[hiden_number] = ".."
            return " ".join(question)
        print('Question: {}'.format(ask_question()))
        correct_answer = new_progression[hiden_number]
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            continue
        else:
            print("{} is wrong answer ;( Correct answer was {}.\nLet's try again, {}".format(answer, correct_answer, cli.name))
            break
    else:
        return print('Congratulations, {}!'.format(cli.name))


if __name__ == '__main__':
    main()

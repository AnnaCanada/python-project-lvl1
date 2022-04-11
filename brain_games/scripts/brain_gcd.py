#!/usr/bin/env python


from brain_games import common_logic
from brain_games.games import gcd


def main():
    common_logic.play_game(gcd)


if __name__ == '__main__':
    main()

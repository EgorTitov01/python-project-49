#!/usr/bin/env python3

from brain_games.games.brain_gcd_logic import brain_gcd
from brain_games.games_logic import start_game


def main():
    start_game(brain_gcd)


if __name__ == '__main__':
    main()

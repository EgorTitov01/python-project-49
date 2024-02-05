#!/usr/bin/env python3

from brain_games.logic.calc import brain_calc
from brain_games.common_games_logic import start_game


def main():
    start_game(brain_calc)


if __name__ == '__main__':
    main()

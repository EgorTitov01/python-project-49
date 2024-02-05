#!/usr/bin/env python3

from brain_games.logic.prime import brain_prime
from brain_games.common_games_logic import start_game


def main():
    start_game(brain_prime)


if __name__ == '__main__':
    main()

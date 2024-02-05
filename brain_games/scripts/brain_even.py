#!/usr/bin/env python3


from brain_games.logic.even import brain_even
from brain_games.common_games_logic import start_game


def main():
    start_game(brain_even)


if __name__ == '__main__':
    main()

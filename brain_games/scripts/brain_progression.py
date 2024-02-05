#!/usr/bin/env python3


from brain_games.logic.progression import brain_progression
from brain_games.common_games_logic import start_game


def main():
    start_game(brain_progression)


if __name__ == '__main__':
    main()

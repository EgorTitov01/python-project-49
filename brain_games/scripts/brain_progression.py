#!/usr/bin/env python3

from random import randint
import prompt
from brain_games.games.brain_progression_logic import brain_progression
from brain_games.games_logic import start_game

def main():
    start_game(brain_progression)

if __name__ == '__main__':
    main()
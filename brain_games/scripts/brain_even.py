#!/usr/bin/env python3

from random import randint
import prompt
from brain_games.scripts.brain_games import greet

def welcome_user():
    global name
    name = prompt.string('May I have your name?\n')
    print(f'Hello, {name}!')


def brain_even():
    count_ = 0
    while count_ < 3 :
        print('Answer "yes" if the number is even, otherwise answer "no".')
        number = randint(1,99)

        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'

        answer = prompt.string(f'Question: {number}\nYour answer: ')

        if answer == right_answer:
            print('Correct!')
            count_ += 1
        else:
            count_ = 4
            break

    if count_ == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}. Let's try again, {name}")

def main():
    greet()
    welcome_user()
    brain_even()

if __name__ == '__main__':
    main()
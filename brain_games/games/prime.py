from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():

    number = randint(2, 100)
    right_answer = 'yes'
    question = f'Question: {number}'

    for i in range(2, round(number ** (1 / 2)) + 1):
        if number % i == 0:
            right_answer = 'no'
            break

    return question, right_answer

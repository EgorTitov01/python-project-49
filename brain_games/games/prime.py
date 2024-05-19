from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, round(number ** (1 / 2)) + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer():

    number = randint(2, 100)
    question = f'{number}'
    if is_prime(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return question, right_answer

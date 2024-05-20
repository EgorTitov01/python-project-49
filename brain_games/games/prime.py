from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, round(number ** (1 / 2)) + 1):
        if number % i == 0:
            return False

    return True


def get_question_and_answer():

    number = randint(1, 100)
    question = f'{number}'
    right_answer = ('yes' if is_prime(number) else 'no')

    return question, right_answer

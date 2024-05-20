from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():

    number = randint(1, 99)
    right_answer = ('yes' if number % 2 == 0 else 'no')
    question = f'{number}'

    return question, right_answer

from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'

def get_question_and_answer():

    number = randint(1, 99)

    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    question = f'Question: {number}'

    return question, right_answer

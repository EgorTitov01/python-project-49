from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():

    a = randint(1, 100)
    b = randint(1, 100)
    question = f'{a} {b}'

    while b != 0:
        t = b
        b = a % b
        a = t

    right_answer = str(a)

    return question, right_answer

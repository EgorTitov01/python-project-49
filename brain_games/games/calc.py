from random import randint, choice
from operator import add, mul, sub


TASK = 'What is the result of the expression?'


def get_question_and_answer():

    operations = [('+', add), ('*', mul), ('-', sub)]
    operator = choice(operations)
    number1 = randint(1, 20)
    number2 = randint(1, 20)

    right_answer = str(operator[1](number1, number2))

    question = (f'{(number1)} '
                f'{operator[0]} {(number2)}')

    return question, right_answer

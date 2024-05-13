from random import randint
from operator import add, mul, sub


TASK = 'What is the result of the expression?'


def get_question_and_answer():

    operators = ['+', '*', '-']
    operations = [add, mul, sub]
    oper_number = randint(0, 2)
    number1 = randint(1, 20)
    number2 = randint(1, 20)

    right_answer = str(operations[oper_number](number1, number2))

    question = (f'Question: {str(number1)} '
                f'{operators[oper_number]} {str(number2)}')

    return question, right_answer

from random import randint
from operator import add, mul, sub


TASK = 'What is the result of the expression?'


def return_args_wrapper():
    def brain_calc():

        operators = ['+', '*', '-']
        operations = [add, mul, sub]
        oper_number = randint(0, 2)
        number1 = randint(1, 20)
        number2 = randint(1, 20)

        right_answer = str(operations[oper_number](number1, number2))

        question = (f'Question: {str(number1)} '
                    f'{operators[oper_number]} {str(number2)}\nYour answer: ')

        return question, right_answer
    return brain_calc
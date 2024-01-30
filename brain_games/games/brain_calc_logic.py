from random import randint


def brain_calc():

    print('What is the result of the expression?')

    operators = ['+', '-', '*']
    oper = randint(0, 2)
    number1 = randint(1, 20)
    number2 = randint(1, 20)

    right_answer = str(eval(f'{str(number1)}'
                            f'{operators[oper]}{str(number2)}'))
    question = (f'Question: {str(number1)} '
                f'{operators[oper]} {str(number2)}\nYour answer: ')

    return question, right_answer

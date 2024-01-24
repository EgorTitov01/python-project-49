from random import randint

def brain_calc():

    operators = ['+', '-', '*']
    oper = randint(0, 2)
    number1 = randint(1, 20)
    number2 = randint(1, 20)

    right_answer = str(eval(f'{str(number1)}{operators[oper]}{str(number2)}'))
    question = (f'What is the result of the expression?\n'
                f'Question: {str(number1)}{operators[oper]}{str(number2)}\n')

    return question, right_answer
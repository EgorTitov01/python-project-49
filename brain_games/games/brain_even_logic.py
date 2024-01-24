from random import randint

def brain_even():

    print('Answer "yes" if the number is even, otherwise answer "no".')

    number = randint(1,99)

    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    question = f'Question: {number}\nYour answer: '

    return question, right_answer
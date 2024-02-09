from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def return_args_wrapper():
    def brain_even():

        number = randint(1, 99)

        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'

        question = f'Question: {number}\nYour answer: '

        return question, right_answer
    return brain_even

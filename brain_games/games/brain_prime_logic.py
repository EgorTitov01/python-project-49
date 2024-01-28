from random import randint


def brain_prime():

    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    number = randint(1, 100)
    right_answer = 'yes'
    question = f'Question: {number}\nYour answer: '

    for i in range(2, round(number ** (1/2)) + 1):
        if number % i == 0:
            right_answer = 'no'
            break

    return question, right_answer

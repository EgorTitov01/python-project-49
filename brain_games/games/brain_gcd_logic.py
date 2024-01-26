from random import randint
def brain_gcd():

    print('Find the greatest common divisor of given numbers.')

    a = randint(1,100)
    b = randint(1,100)
    question = f'Question: {a} {b}\nYour answer: '

    while b != 0:
        t = b
        b = a % b
        a = t

    right_answer = str(a)


    return question, right_answer
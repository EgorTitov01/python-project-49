from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def return_args_wrapper():
    def brain_gcd():

        a = randint(1, 100)
        b = randint(1, 100)
        question = f'Question: {a} {b}\nYour answer: '

        while b != 0:
            t = b
            b = a % b
            a = t

        right_answer = str(a)

        return question, right_answer
    return brain_gcd

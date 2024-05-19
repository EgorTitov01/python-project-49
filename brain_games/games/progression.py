from random import randint


TASK = 'What number is missing in the progression?'


def get_question_and_answer():

    first_number = randint(1, 20)
    added_number = randint(1, 10)
    sequence = list(range(first_number, first_number + added_number * 10,
                          added_number))
    sequence = list(map(str, sequence))
    missing_index = randint(0, 9)
    right_answer = sequence[missing_index]
    sequence[missing_index] = '..'
    question = f"{' '.join(sequence)}"

    return question, right_answer

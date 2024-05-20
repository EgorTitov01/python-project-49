from random import randint


TASK = 'What number is missing in the progression?'


def get_question_and_answer():

    prog_start = randint(1, 20)
    prog_step = randint(1, 10)
    prog_elements = 10
    prog_stop = prog_start + prog_step * prog_elements
    sequence = list(range(prog_start, prog_stop,
                          prog_step))
    sequence = list(map(str, sequence))
    missing_index = randint(0, 9)
    right_answer = sequence[missing_index]
    sequence[missing_index] = '..'
    question = f"{' '.join(sequence)}"

    return question, right_answer

from random import randint

def brain_progression():

    print('What number is missing in the progression?')

    first_number = randint(1,20)
    added_number = randint(1,10)
    sequence = []

    for i in range(0,10):
        sequence.append(str(first_number + added_number * i))

    missing_index = randint(0,9)
    right_answer = sequence[missing_index]
    sequence[missing_index] = '..'
    question = f"Question: {' '.join(sequence)}\nYour answer: "

    return question, right_answer



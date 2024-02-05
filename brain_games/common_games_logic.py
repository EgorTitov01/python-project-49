import prompt


def start_game(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    number_of_questions = 3

    for i in range(number_of_questions):

        question, right_answer = game()
        answer = prompt.string(question)

        if right_answer == str(answer):
            print('Correct!')
        else:
            break
    else:
        print(f'Congratulations, {name}!')
        return

    print(f"{answer} is wrong answer ;(. Correct answer was"
          f" {right_answer}. Let's try again, {name}!")

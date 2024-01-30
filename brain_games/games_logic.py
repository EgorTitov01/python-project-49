import prompt


def start_game(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    all_questions = 3

    for i in range(1, all_questions + 1):

        question, right_answer = game()
        answer = prompt.string(question)

        if right_answer == str(answer):
            print('Correct!')
        else:
            i = all_questions - 1
            break

    if i == all_questions:
        print(f'Congratulations, {name}!')
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was"
              f" {right_answer}. Let's try again, {name}!")

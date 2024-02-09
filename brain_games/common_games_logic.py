import prompt


def start_game(game):

    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name?\n')
    print(f'Hello, {user_name}!')
    print(game.TASK)

    questions_count = 3

    for _ in range(questions_count):

        question, right_answer = game.return_args_wrapper()()
        user_answer = prompt.string(question)

        if right_answer != str(user_answer):
            print(f"{user_answer} is wrong answer ;(. Correct answer was"
                  f" {right_answer}. Let's try again, {user_name}!")
            break

        print('Correct!')

    else:
        print(f'Congratulations, {user_name}!')
        return



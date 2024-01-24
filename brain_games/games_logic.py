import prompt

def start_game(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    count = 0

    while count < 3:

        question, right_answer = game()
        answer = prompt.string(question)

        if right_answer == str(answer):
            print('Correct!')
            count += 1
        else:
            count = 4
            break

    if count == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}. Let's try again, {name}")
import quiz_brain

question = quiz_brain.results

question_number = len(question)
index = 0
score = 0


def quiz():
    global index, score
    while index < question_number:
        answer = input(f"Q.{index + 1}: {question[index].question} (True/False)?: ").lower()
        if answer == question[index].answer.lower():
            score += 1
            print('You got that right!')
            print(f"The correct answer was {question[index].answer}!")
            print(f'Your score is {score} / {index + 1}!')

        else:
            print('You got that wrong!')
            print(f"The correct answer was {question[index].answer}!")
            print(f'Your score is {score} / {index + 1}!')
        index += 1

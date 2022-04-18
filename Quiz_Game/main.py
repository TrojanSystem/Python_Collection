from question import questions
from logic import GameLogic

gameLogic = GameLogic
x = 0
rightAnswer = 0
while x < len(questions):
    for i in range(len(questions)):
        print(f" Q.{i + 1}: {questions[i]['question']} (True/False)?: ")
        answer = input('').title()

        rightAnswer = gameLogic.questionfunction(current_question=questions[i]['question'],
                                                 current_answer=questions[i]['answer'], input_answer=answer,
                                                 current_right_answer=rightAnswer, current_index=i)

        x = x + 1

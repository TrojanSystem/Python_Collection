class GameLogic:
    def __init__(self, current_question, current_answer, current_right_answer, current_index, input_answer):
        self.question = current_question,
        self.answer = current_answer,
        self.rightAnswer = current_right_answer,
        self.index = current_index,
        self.input = input_answer

    def questionfunction(current_question, current_answer, current_right_answer, current_index, input_answer):
        if input_answer == str(current_answer):
            current_right_answer = current_right_answer + 1
            print('You got it right!')
            print(f"The correct answer was: {current_answer}")
            print(f"Your current score is: {current_right_answer} / {current_index + 1}")
        else:
            print('That\'s Wrong!')
            print(f"The correct answer was: {current_answer}")
            print(f"Your current score is: {current_right_answer} / {current_index + 1}")
        return current_right_answer;

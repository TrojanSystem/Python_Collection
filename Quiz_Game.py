questions = [
    {
        'question': 'A slug\'s blood is green.',
        'answer': True,
    },
    {
        'question': 'The loudest animal is the African Elephant.',
        'answer': False,
    },
    {
        'question': 'Approximately one quarter of the human bone are in the feet.',
        'answer': True,
    },
    {
        'question': 'The total surface area of a human lung is the size of a football pitch.',
        'answer': True,
    }
]

x = 0
rightAnswer = 0
while x < len(questions):
    for i in range(len(questions)):
        print(f" Q.{i+1}: {questions[i]['question']} (True/False)?: ")
        answer = input('').title()

        if answer == str(questions[i]['answer']):
            rightAnswer = rightAnswer + 1
            print('You got it right!')
            print(f"The correct answer was: {questions[i]['answer']}")
            print(f"Your current score is: {rightAnswer} / {i+1}")
        else:
            print('That\'s Wrong!')
            print(f"The correct answer was: {questions[i]['answer']}")
            print(f"Your current score is: {rightAnswer} / {i+1}")
        x = x + 1

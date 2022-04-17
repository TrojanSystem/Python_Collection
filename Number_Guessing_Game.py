import random

print('Welcome to the number guessing game!')
print('I\'m thinking of a number b/n 1 and 100')
attemptsEasy = 10
attemptsHard = 5
randomNumber = random.randint(0, 101)
difficulty = input('Choose difficulty, Type "easy" or "hard": ')


if difficulty == 'easy':
    print(f'You have {attemptsEasy} remaining to guess the number!')
    while attemptsEasy > 0:

        guessedNumber = input('Make a guess: ')

        if int(guessedNumber) > randomNumber:
            print('Too High')

        elif int(guessedNumber) < randomNumber:
            print('Too Low')

        elif int(guessedNumber) == randomNumber:
            print('Correct')
            break
        else:
            print('Invalid')

        attemptsEasy = attemptsEasy - 1
        if attemptsHard == 0:
            print('You Lose!')
        print(f'You have {attemptsEasy} remaining to guess the number!')


elif difficulty == 'hard':
    print(f'You have {attemptsHard} remaining to guess the number!')
    while attemptsHard > 0:

        guessedNumber = input('Make a guess: ')
        if int(guessedNumber) > randomNumber:
            print('Too High')

        elif int(guessedNumber) < randomNumber:
            print('Too Low')

        elif int(guessedNumber) == randomNumber:
            print('Correct')
            break
        else:
            print('Invalid')
        attemptsHard = attemptsHard - 1
        if attemptsHard == 0:
            print('You Lose!')
        print(f'You have {attemptsHard} remaining to guess the number!')

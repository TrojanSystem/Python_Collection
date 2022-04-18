from hangman_string import *
import random

selectedWord = ' '
listOfWords = ['Mouse', 'Cat', 'Dog', 'BeeKeeper', 'Python', 'Java', 'StackOverFlow', 'GitHub']
dashedList = []
hangman = [ss, nn, aa, m, g, n, a, h]

randomNumbers = random.randint(0, len(listOfWords) - 1)
end = False
selectedWord = listOfWords[randomNumbers]
x = 7
print(selectedWord)
for x in range(len(selectedWord)):
    dashedList += "_"
print(dashedList)
while not end:
    guess = input('Guess a letter: ')

    for i in range(0, len(selectedWord)):
        print("\n")
        letter = selectedWord[i]
        if letter == guess:
            dashedList[i] = guess
    if guess not in selectedWord:
        x = x - 1
        if x == 0:
            print("You Lose!")
            end = True
        print(hangman[x])
    print(dashedList)
    if "_" not in dashedList:
        end = True
        print('You Win!')

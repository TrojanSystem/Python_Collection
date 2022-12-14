import random

hangman_list = [
    ''' ---------------|
                   |
                   |
                   |
                   |
                   |
                   |
          ============''',

    ''' --------|------|
                    |      |
                    0      |
                           |
                           |
                           |
                           |
                   ============''',
    ''' --------|------|
                    |      |
                    0      |
                   /|\     |
                    |      |
                           |
                           |
                   ============''',
    ''' --------|------|
                    |      |
                    0      |
                   /|\     |
                    |      |
                   /       |
                           |
                   ============''',
    ''' --------|------|
                    |      |
                    0      |
                   /|\     |
                    |      |
                   / \     |
                           |
                  ============''']


class Hangman:

    @staticmethod
    def hangman_game():
        world_list = ['Beekeeper', 'fly', 'aardvark', 'hornet', 'cow', 'ox', 'sheep']
        choosed_word = random.choice(world_list)
        guessedWord = []
        last_index = 0
        for dashedSpell in choosed_word:
            guessedWord += '_'
        print(guessedWord)
        print('\n')

        x = 0
        print(choosed_word)
        game_over = False
        while not game_over:
            guess = input('Guess a word please input letter: ')
            for position in range(len(choosed_word)):
                spell = choosed_word[position]
                if spell == guess:
                    guessedWord[position] = spell
                    # current_index = choosed_word.index(guess, last_index)
                    # last_index = current_index + 1
                    # numList = [current_index]
                    #
                    # for add in numList:
                    #     guessedWord.insert(add, guess)
                    # print(f'You are correct letter "{spell}" is in the chosen word')
                    # if x == len(choosed_word):
                    #     break
            if guess not in choosed_word:

                if x == 5:
                    game_over = True
                print(hangman_list[x])
                x += 1
            print(guessedWord)
            if '_' not in guessedWord:
                game_over = True
                print('You Win!')
        print(guessedWord)
# last_index = 0
# while last_index < len(pickedCountry):
#     current_index = pickedCountry.index('e', last_index)
#     print(current_index)
#     last_index = current_index + 1

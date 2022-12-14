import random

import day_8
import hangman


class UptoDay8:
    @staticmethod
    def project_day_8():
        totalEven = 0
        totalOdd = 0
        print('Which Program U want to Run')
        which = input('Type "EvenOdd", "FizzBuzz","Password","Hangman","Calculator","PrimeChecker" program: ')
        if which == 'EvenOdd':
            for evens in range(1, 101):
                if evens % 2 == 0:
                    totalEven += evens

                else:

                    totalOdd += evens
            print(f"Total Even {totalEven} : Total Odd {totalOdd}")
        elif which == 'FizzBuzz':
            for evens in range(1, 101):
                if evens % 3 == 0 and evens % 5 == 0:
                    print('FizzBuzz')
                elif evens % 5 == 0:
                    print('Buzz')
                elif evens % 3 == 0:
                    print('Fizz')
                else:
                    print(evens)
        elif which == 'Password':
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
            passNumber = int(input('How many numbers in your Numbers: '))
            passLetters = int(input('How many numbers in your Letters: '))
            passSymbols = int(input('How many numbers in your Symbols: '))
            password = []

            for number in range(0, passNumber):
                password.append(random.choice(numbers))
            for number in range(0, passLetters):
                password.append(random.choice(letters))
            for number in range(0, passSymbols):
                password.append(random.choice(symbols))
            random.shuffle(password)
            generatedPassword = ""
            for passw in password:
                generatedPassword += passw

            print(f'Password Generated: {generatedPassword}')
        elif which == 'Hangman':
            hangman.Hangman.hangman_game()
        elif which == 'Calculator':
            day_8.calculator()
        elif which == "PrimeChecker":
            day_8.prime_checker()

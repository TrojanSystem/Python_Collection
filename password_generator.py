import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '<', '>', '#', '$', '^',
           '&', '*', '(', '|', ')', '_', '-', '+', '=']
password = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
passwordLength = input('Enter length of the password: ')
lengthNumber = input('Enter number of symbols numbers: ')
lengthsymbol = input('Enter number of symbols characters: ')
choosedNumbers = ''
choosedLetter = ''
choosedSymbol = ''
finalPassowrd = '';
totLength = 0
totLength = int(passwordLength) - (int(lengthNumber) + int(lengthsymbol));
for i in range(0, totLength):

    rand = random.randint(0, totLength)
    choosedLetter += letters[rand]
    password += choosedLetter
for i in range(0, int(lengthNumber)):

    rand = random.randint(0, int(lengthNumber))
    choosedNumbers += numbers[rand]
    password += choosedNumbers
for i in range(0, int(lengthsymbol)):

    rand = random.randint(0, int(lengthsymbol))
    choosedSymbol += symbols[rand]
    password += choosedSymbol
   
random.shuffle(password)
for char in password:
    finalPassowrd += char
print(f"Your password is: {finalPassowrd}")
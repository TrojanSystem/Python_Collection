runAgain = True


def addOperation(firstNumber, secondNumber):
    sum = int(firstNumber) + int(secondNumber)
    print(f"{int(firstNumber)} + {int(secondNumber)} is {sum}")

    return sum


def minusOperation(firstNumber, secondNumber):
    sum = int(firstNumber) - int(secondNumber)
    print(f"{int(firstNumber)} - {int(secondNumber)} is {sum}")

    return sum


while runAgain == True:
    firstNumber = input('What is the first number: ')
    operation = input("Pick an operation \n + \n  - \n  * \n  \ \n")
    secondNumber = input('What is the second number: ')

    sum = 0

    if operation == '+':
        addOperation(firstNumber=firstNumber, secondNumber=secondNumber)
        run = input('Do you want to run the calculator again? (y/n): ')
        if run == 'y':
            runAgain = True
        else:
            runAgain = False
    elif operation == '-':
        minusOperation(firstNumber=firstNumber, secondNumber=secondNumber)
        run = input('Do you want to run the calculator again? (y/n): ')
        if run == 'y':
            runAgain = True
        else:
            runAgain = False
    elif operation == '*':
        sum = int(firstNumber) * int(secondNumber)
        print(f"{int(firstNumber)} * {int(secondNumber)} is {sum}")
        run = input('Do you want to run the calculator again? (y/n): ')
        if run == 'y':
            runAgain = True
        else:
            runAgain = False
    elif operation == '/':
        sum = int(firstNumber) / int(secondNumber)
        print(f"{int(firstNumber)} / {int(secondNumber)} is {sum}")
        run = input('Do you want to run the calculator again? (y/n): ')
        if run == 'y':
            runAgain = True
        else:
            runAgain = False
    else:
        print('Unknown operation')
        run = input('Do you want to run the calculator again? (y/n): ')
        if run == 'y':
            runAgain = True
        else:
            runAgain = False

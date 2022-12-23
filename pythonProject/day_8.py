


def prime_checker():
    length = 0
    for x in range(1, 101):
        for y in range(1, 101):
            if x % y == 0:
                length += 1
        if length > 2:
            print(f'{x} Not Prime')
            length = 0
        elif length <= 2:
            print(f'{x} Prime')
            length = 0


PI = 3.14




def calculation(first, second, operation):
    """Enter the number first then pick an operator finally enter the second number"""

    if operation == '+':

        return first + second

    elif operation == '-':
        return first - second

    elif operation == '*':
        return first * second

    elif operation == '/':
        return first / second

    else:
        print('Invalid Operator!')


def encryption():
    def operation():
        function = input('Do you want "encrypt" or "decrypt": ')
        if function == "encrypt":
            codedWord = input('Type your message: ').lower()
            shift = int(input('Type your shift key: '))

            encrypted_word = ''

            for spell in codedWord:
                index = letters.index(spell)

                encrypted_word += letters[index + shift]

            print(f"The encrypted message is: {encrypted_word}")
        elif function == 'decrypt':
            codedWord = input('Type your message: ')
            shift = int(input('Type your shift key: '))
            decrypted_word = ''

            for spell in codedWord:
                index = letters.index(spell)
                decrypted_word += letters[index - shift]
            print(f'The decrypted message is: {decrypted_word}')

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's',

               't', 'u', 'v', 'w', 'x', 'y', 'z']
    operation()
    loop = True
    while loop:

        runAgain = input('Do you want to run again y | n : ')
        if runAgain == 'y':
            operation()
        else:
            loop = False
            exit()


def calculator():
    loop = 0
    if loop == 0:
        num_1 = float(input('Enter your first number: '))
        print(' + \n - \n * \n / ')
        operator = input('Pick an operation: ')
        num_2 = float(input('Enter your second number: '))

        result = calculation(num_1, num_2, operator)
        print(f'{num_1} {operator} {num_2} =  {result}')
        loop += 1
        while loop > 0:
            answer = input('Do you want to continue with existing value y | n ')
            if answer == 'y':
                num_1 = float(input('Enter your next number: '))
                print(' + \n - \n * \n / ')
                operator = input('Pick an operation: ')

                result = calculation(num_1, result, operator)
                print(f'{num_1} {operator} {num_2} =  {result}')
            elif answer == 'n':
                newCalculator = input('Do you want to continue with new value y | n ')
                if newCalculator == 'y':
                    num_1 = float(input('Enter your first number: '))
                    print(' + \n - \n * \n / ')
                    operator = input('Pick an operation: ')
                    num_2 = float(input('Enter your second number: '))

                    result = calculation(num_1, num_2, operator)
                    print(f'{num_1} {operator} {num_2} =  {result}')
                else:
                    exit()

    else:
        exit()

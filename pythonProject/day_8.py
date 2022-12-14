# import math
#
# print('Welcome to Area calculator')
#
#
# def area(radius):
#     circle_area = math.pi * radius ** 2
#     return print(f'Area of circle is {round(circle_area, 2)}')
#
#
# radi = float(input('Enter circle radius: '))
# area(radius=radi)
#
#
# def bmi_index(height, weight):
#     bmi = weight / height ** 2
#     return round(bmi, 2)
#
#
# print(f"BMI value {bmi_index(1.65, 85)}")
#
# def prime_checker():
#     x=1
#     for x in range(0,101):
#         if x


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

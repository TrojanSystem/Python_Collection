import random


class UptoDay4:
    @staticmethod
    def projects():
        print('Which Program U want to Run')
        which = input('Type "Tip", "Digit", "Age", "BMI","Leap","WhoPays" program: ')

        if which == "Tip":
            # TIP CALCULATOR
            # TIP CALCULATOR
            # TIP CALCULATOR
            # TIP CALCULATOR
            # TIP CALCULATOR
            # TIP CALCULATOR
            # TIP CALCULATOR
            # TIP CALCULATOR
            totalBill = input('What is the total bill? $')
            numberOfPeople = input('How many people to split the Bill? ')
            percentTip = input('What percentage tip would you like to give ? 10,12 or 15? ')

            splitedBill = (float(totalBill) / int(numberOfPeople))

            tip = float(splitedBill) * (int(percentTip) / 100)
            totalTobePayed = tip + splitedBill
            print('Each person should pay: $' + str((round(totalTobePayed, 2))))
        elif which == "Digit":

            # TWO-DIGIT NUMBER
            # TWO-DIGIT NUMBER
            # TWO-DIGIT NUMBER
            # TWO-DIGIT NUMBER
            # TWO-DIGIT NUMBER
            # TWO-DIGIT NUMBER
            # TWO-DIGIT NUMBER
            print('Calculator')
            totalBill = input('Enter Two digit number? ')

            sum1 = int(totalBill[0])
            sum2 = int(totalBill[1])

            converted = sum1 + sum2
            print(f'The sum is {converted}')
        elif which == "Age":
            # AGE CALCULATOR
            # AGE CALCULATOR
            # AGE CALCULATOR
            # AGE CALCULATOR
            # AGE CALCULATOR
            # AGE CALCULATOR
            print('Welcome to remaining Life calculator!')
            age = input('Enter your age? ')
            remain = 90 - int(age)

            month = remain * 12

            week = remain * 52
            day = remain * 365

            print(f'You got {round(month)} months {round(week)} weeks {round(day)} days before reaching 90!')
        elif which == "BMI":
            print('Welcome to BMI Calculator')
            weight = input('Enter your weight in kg: ')
            height = input('Enter your height in m: ')
            bmi = float(weight) / (float(height) ** 2)
            if bmi < 18.5:
                print(f'BMI:{round(bmi, 2)}  Under-Weight')
            elif 18.5 <= bmi < 25:
                print(f'BMI:{round(bmi, 2)}  Normal-Weight')
            elif 25 <= bmi < 30:
                print(f'BMI:{round(bmi, 2)}  Over-Weight')
            elif 30 <= bmi < 35:
                print(f'BMI:{round(bmi, 2)}  Obese')
            elif bmi >= 35:
                print(f'BMI:{round(bmi, 2)}  Clinical Obese')
            else:
                print('Unknown')

        elif which == "Leap":
            print('Welcome to leap year calculator')
            year = input('Enter year: ')
            if float(year) % 4 == 0:
                if float(year) % 100 == 0:
                    if float(year) % 400 == 0:
                        print('Leap Year')
                    else:
                        print('Not Leap Year')
                else:
                    print('Leap Year')
            else:
                print('Not Leap Year')
        elif which == "WhoPays":
            print('Welcome to Who pays ')
            who = input('Give me everybody\'s name? comma separated: ')
            whoPays = who.split(',')
            randomPay = random.randint(0, len(whoPays)-1)
            print(f'{whoPays[randomPay]} card pulled out!!')
        else:
            exit()

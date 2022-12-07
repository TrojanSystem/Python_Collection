print('Welcome to Tip Calculator!')
totalBill = input('What is the total bill? $')
numberOfPeople = input('How many people to split the Bill? ')
percentTip = input('What percentage tip would you like to give ? 10,12 or 15? ')

splitedBill = (float(totalBill) / int(numberOfPeople))

tip = float(splitedBill) * (int(percentTip) / 100)
totalTobePayed = tip + splitedBill
print('Each person should pay: $' + str(totalTobePayed))

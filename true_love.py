love = ['L', 'O', 'V', 'E']
true = ['T', 'R', 'U', 'E']
hisName = input('Enter his name in Capital letters: ')
herName = input('Enter her name in Capital letters: ')

couple = hisName + herName
loveCounter = 0
trueCounter = 0

for i in range(len(couple)):
    if couple[i] in true:
        trueCounter += 1

    if couple[i] in love:
        loveCounter += 1


print('Your love bond is ' + str(trueCounter) + str(loveCounter)+' %')

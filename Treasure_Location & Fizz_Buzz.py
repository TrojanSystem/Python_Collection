
row1 = ['1', '2', '3']
row2 = ['4', '5', '6']
row3 = ['7', '8', '9']
mix = [row1, row2, row3]

treasure = input('Where you want to put your treasure: ')

mix[int(treasure[0])][int(treasure[1])] = 'X'
print(f"{row1}\n{row2}\n{row3}")
print()


sum = 0
for x in range(1, 101):
    if (x % 3 == 0) and (x % 5 == 0):
        print('fizz buzz')
    elif x % 3 == 0:
        print('fizz')

    elif x % 5 == 0:
        print('buzz')

    else:
        print(x)

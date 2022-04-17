# identifier = input('Enter a number ');
# if int(identifier) % 2 == 0:
#     print( 'The number is EVEN')
# else :
#     print ('The number is ODD');


weight = input('Enter your weight in kg ')
height = input('Enter your height in m ')

bmi = (float(weight) / float(height) ** 2)
bmi_int = int(bmi)

print('Your BMI Index is ' + str(bmi_int))
if (float(bmi) < 18.5):
    print('UNDER-WEIGHT')
elif ((float(bmi) > 18.5) & (float(bmi) < 25.0)):
    print('NORMAL-WEIGHT')
elif (float(bmi) > 35.0):
    print('OBESE')

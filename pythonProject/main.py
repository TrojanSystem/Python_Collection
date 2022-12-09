from upto_day_4 import UptoDay4

projects = UptoDay4()

x = 0

if x == 0:
    projects.projects()
    x += 1

while x > 0:

    answer = input('Do u want to run again! y or n : ')

    if x > 0 and answer == 'y':
        projects.projects()
    else:
        exit()

# print('Welcome to Tip Calculator!')


# print(converted)

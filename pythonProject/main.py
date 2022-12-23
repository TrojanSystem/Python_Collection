import day_18
from upto_day_4 import UptoDay4
from upto_day_8 import UptoDay8

projects_till_day_4 = UptoDay4()
projects_till_day_8 = UptoDay8()

x = 0
if x == 0:
    whichDay = input('Till which day project would like to run ? Type 4, 8, 18:  ')
    if whichDay == '4':
        if x == 0:
            projects_till_day_4.projects()
            x += 1

        while x > 0:

            answer = input('Do u want to run again! y or n : ')

            if x > 0 and answer == 'y':
                projects_till_day_4.projects()
            else:
                exit()
    elif whichDay == '8':
        projects_till_day_8.project_day_8()
    elif whichDay == '18':
        choice = input('Which one: Colors | Spirograph: ')
        if choice.lower() == 'colors':
            day_18.color_generator()
        elif choice.lower() == 'spirograph':
            day_18.spirograph()
    else:
        print('Project day does\'t Exist!')
    x += 1
    while x > 0:

        answer = input('Do u want to run again! y or n : ')

        if x > 0 and answer == 'y':
            whichDay = input('Till which day project would like to run ? Type 4, 8, 18:  ')
            if whichDay == '4':
                projects_till_day_4.projects()
            elif whichDay == '8':
                projects_till_day_8.project_day_8()
            elif whichDay == '18':
                choice = input('Which one: Colors | Spirograph')
                if choice.lower() == 'colors':
                    day_18.color_generator()
                elif choice.lower() == 'spirograph':
                    day_18.spirograph()
        else:
            exit()
# print('Welcome to Tip Calculator!')


# print(converted)

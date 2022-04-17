studentScore = {
    'Surafel': 81,
    'Henok': 78,
    'Sala': 99,
    'Alazar': 74,
    'Yordi': 62
}
travelLog = [
    {
        'country': 'France',
        'visits': 12,
        'cities': ['Paris', 'Lille', 'Dijon'],
    },
    {
        'country': 'Germany',
        'visits': 5,
        'cities': ['Berlin', 'Hamburg', 'Stuttgart'],
    },
]


def grade(studentScore):
    for key in studentScore:
        score = studentScore[key]
        if (score > 90) and (score <= 100):
            print(f'Outstanding {key} you got {score}')
        elif (score > 80) and (score <= 90):
            print(f'Exceeds Expectation {key} you got {score}')
        elif (score > 70) and (score <= 80):
            print(f'Acceptable {key} you got {score}')
        elif (score <= 70):
            print(f'Fail {key} you got {score}')
        else:
            print('Unknown Grade')
def nestedDeictionaries(country, cities, visits):
    newCountry = {}
    newCountry['country'] = country,
    newCountry['visits'] = int(visits),
    newCountry['cities'] = cities.split()
    travelLog.append(newCountry)
    print(travelLog)
grade(studentScore)


country = input('What country do you visits: ')
visits = input('What how many times do you visit: ')
cities = input('What cities do you visits: ')



nestedDeictionaries(country=country, cities=cities, visits=int(visits))



#import pandas as pd
from pandas import read_json
from datetime import datetime

tamriel_heroes = read_json('tamriel1.json', encoding='UTF-8')
print('tamriel_heroes_json')
print(tamriel_heroes)

print(tamriel_heroes.columns)

print(tamriel_heroes['motos'])
print(tamriel_heroes['birthday'])

print(tamriel_heroes['birthday'])
bday = tamriel_heroes.loc[0, 'birthday']


# Considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(bday, "%d.%m.%Y")
print("dt_object1 =", dt_object1)


print(tamriel_heroes.dtypes)
#print(tamriel_heroes.convert_dtypes().dtypes)

print(tamriel_heroes['strength'].dtype)

print(tamriel_heroes['strength'].astype(int).dtype)

print(tamriel_heroes['strength'].values.astype(int))


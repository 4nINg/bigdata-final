import csv
import pandas as pd

csvfile = open('./data/processed_data.csv', newline='')
reader = csv.DictReader(csvfile)

Fnc = {'Fnc':set()}
Ibase = {'Ibase':set()}
for idx, dic in enumerate(reader):

    MAIN_FNCTN = list(dic['MAIN_FNCTN'].split('\n'))
    List = list(dic['BASE_STANDARD'].split('\n'))

    for fnc in MAIN_FNCTN:
        Fnc['Fnc'].add(fnc)

    for l in List:
        LList = list(l.split(':'))
        Ibase['Ibase'].add(LList[0])

Fnc['Fnc'] = list(Fnc['Fnc'])
Ibase['Ibase'] = list(Ibase['Ibase'])

Fn = pd.DataFrame(Fnc)
Fn.to_csv("./data/function_data.csv", index = True, encoding='cp949')

Ib = pd.DataFrame(Ibase)
Ib.to_csv("./data/ingredient_data.csv", index = True, encoding='cp949')
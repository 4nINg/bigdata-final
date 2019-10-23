import csv

csvfile = open('Final_Data.csv', newline='')
reader = csv.DictReader(csvfile)

Dic = {'items':[]}
for dic in reader:
    product = {}
    product['PRDUCT'] = dic['PRDCUT']
    # MAIN_FNCTN = list(dic['MAIN_FNCTN'].split('\n'))
    # STTEMNT_NO = list(dic['STTEMNT_NO'].split('\n'))
    # INTAKE_HINT1 = list(dic['INTAKE_HINT1'].split('\n'))
    # List = list(dic['BASE_STANDARD'].split('\n'))
    # for l in List:
    #     LList = list(l.split(':'))
    #     LList[0] = LList[0].replace('(mg/kg)','')q
    # #     dic[LList[0]] = LList[1]
    # # print(dic)
    Dic['items'].append(product)
print(Dic)
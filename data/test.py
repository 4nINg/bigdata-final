import csv

csvfile = open('Final_Data.csv', newline='')
reader = csv.DictReader(csvfile)
for dic in reader:
    List = list(dic['MAIN_FNCTN'].split('\n'))
    print(List)
    # List = list(dic['STTEMNT_NO'].split('\n'))
    # List = list(dic['BASE_STANDARD'].split('\n'))
    # Dic = {}
    # for l in List:
    #     LList = list(l.split(':'))
    #     Dic[LList[0]] = LList[1]
    # print(Dic)
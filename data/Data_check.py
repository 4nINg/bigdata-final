import csv
with open('entire_list.csv') as f:
    txt_data = f.readlines()[1:]
    rdr = csv.reader(txt_data)
n=1
Dic = {}
for lst in rdr:
    if not lst[6] in Dic:
        Dic[lst[6]] = []
    Dic[lst[6]].append(lst[3])
print(Dic['헬스프랜드 프리미엄'])
# print('총 종류: ',len(Dic))
# cnt = 0
# for key, value in Dic.items():
#     print(key, ': ', value)
    # if len(value)>1:
    #     cnt+=1
        # print(key, value)
# print('회사 2개이상:' ,cnt)

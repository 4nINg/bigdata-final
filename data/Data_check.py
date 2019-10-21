# import csv
# with open('entire_list.csv') as f:
#     txt_data = f.readlines()[1:]
#     rdr = csv.reader(txt_data)
# n=1
# Dic = {}
# for lst in rdr:
#     if not lst[6] in Dic:
#         Dic[lst[6]] = []
#     Dic[lst[6]].append(lst[3])
# print(Dic)
# # print('총 종류: ',len(Dic))
# # cnt = 0
# # for key, value in Dic.items():
# #     print(key, ': ', value)
# #     if len(value)>1:
# #         cnt+=1
# #         print(key, value)
# # print('회사 2개이상:' ,cnt)



# import csv
# with open('entire_list.csv','r') as entire, open('Data.csv', 'r') as url, open('new_data', 'w') as fout:
#     Entire_data = entire.readlines()
#     Entire_List= csv.reader(Entire_data)
#     URL_data = url.readlines()[1:]
#     URL_List = csv.reader(URL_data)

# URL = []
# for url in URL_List:
#     for entire in Entire_List:
#         if url[0] == entire[0]:
#             URL.append(url[5])
#             break
# print(len(URL))




import csv
with open('entire_list.csv','r') as entire, open('Add_Data.csv', 'r') as url, open('new_data.csv', 'a', newline='') as fout:
    Entire_data = entire.readlines()
    Entire_List= csv.reader(Entire_data)
    URL_data = url.readlines()[1:]
    URL_List = csv.reader(URL_data)
    # writer = csv.writer(fout)
    fieldnames = ['register_date','product_name','preservation_desc','main_function','sungsang','intake_hint','srv_use','register_num','distribute','full_desc','standard_stnd','company_name','image_url']
    writer = csv.DictWriter(fout, fieldnames=fieldnames)

    cnt = 0
    for url in URL_List:
        for entire in Entire_List:
            if url[0] == entire[0]:
                print(url)
                # writer = csv.writer(fout)
                cnt += 1
                # writer.writerow({'register_date':entire[8], 'product_name':entire[6], 'preservation_desc':entire[7], 'main_function':entire[5], 'sungsang':entire[1], 'intake_hint':entire[4], 'srv_use':entire[9], 'register_num':entire[11], 'distribute':entire[2], 'full_desc':entire[0], 'standard_stnd':entire[10], 'company_name':url[3], 'image_url':url[5]})
                break
    print(cnt)
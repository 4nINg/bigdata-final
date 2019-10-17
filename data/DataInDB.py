# import requests
# import json
# import xmltodict
# import csv

# ServiceKey = 'hZ5wN1oxmwnrr1aSfsKpi1XM8AhX3DGSYBkahybytwVOCZfDpDgfvrQmZkxHvEGfNd%2BgFEsDzQdl4BhjG%2BbU3Q%3D%3D'
# URL = 'http://apis.data.go.kr/1470000/HtfsTrgetInfoService/getHtfsInfoList?ServiceKey='+ ServiceKey

# Add_Imform = {}

# for num in range(1, 10):
#     parameters = {
#         'numOfRows': 100,
#         'pageNo': num,
#         }

#     res = requests.get(URL, params=parameters)
#     response = res.text
#     response = xmltodict.parse(response)
#     response = json.dumps(response)
#     response = json.loads(response)

#     items = response['response']['body']['items']['item']

#     for Product_Num in items:
#         # print(Product_Num['GU_PRDLST_MNF_MANAGE_NO'])
#         # print(Product_Num['STDR_STND'])
#         Add_Imform[Product_Num['GU_PRDLST_MNF_MANAGE_NO']] = Product_Num['STDR_STND']
#         # print('--------------------------------------------------------------------')
#         # print()

# print(Add_Imform)

# # with open('full_lst.csv', 'r') as f:
# #     txt_data = f.readlines()[1:]
# #     rdr = list(csv.reader(txt_data))
# #     with open('full_list.csv', 'w') as w:
# #         n = 0
# #         for idx, line in enumerate(rdr):
# #             try:
# #                 data = Add_Imform[line[11]]
# #                 w.write(data)
# #                 n += 1
# #                 print(n)

# #             except Exception as e:
# #                 continue
            
# # print(rdr[0][10])



import xmltodict
import json
import requests
import pandas as pd

# 'http://apis.data.go.kr/1470000/HtfsInfoService/' 건강기능 식품 정보 서비스
# 'http://apis.data.go.kr/1470000/HtfsTrgetInfoService' 건강기능 대상별 정보(DB) 서비스


ServiceKey_for_add_info = 'hZ5wN1oxmwnrr1aSfsKpi1XM8AhX3DGSYBkahybytwVOCZfDpDgfvrQmZkxHvEGfNd%2BgFEsDzQdl4BhjG%2BbU3Q%3D%3D'
URL_for_add_info = 'http://apis.data.go.kr/1470000/HtfsTrgetInfoService/getHtfsInfoList?ServiceKey='+ ServiceKey_for_add_info

add_info = {}

for num in range(1, 272):
    parameters = {
        'numOfRows': 100,
        'pageNo': num,
        }

    res = requests.get(URL_for_add_info, params=parameters)
    response = res.text
    response = xmltodict.parse(response)
    response = json.dumps(response)
    response = json.loads(response)

    items = response['response']['body']['items']['item']

    for Product_Num in items:
        add_info[Product_Num['GU_PRDLST_MNF_MANAGE_NO']] = Product_Num['STDR_STND']
    
    print(num)
print(add_info)
with open('add')

for key, value in add_info.items():
    print(key+' : '+value)


print('-----------------------------------')


ServiceKey = "hZ5wN1oxmwnrr1aSfsKpi1XM8AhX3DGSYBkahybytwVOCZfDpDgfvrQmZkxHvEGfNd%2BgFEsDzQdl4BhjG%2BbU3Q%3D%3D"
url = 'http://apis.data.go.kr/1470000/HtfsInfoService/getHtfsItem?ServiceKey=' + ServiceKey

entire_list = {}
index = []
register_date = []
product_name = []
preservation_desc = []
main_function = []
sungsang = []
intake_hint = []
srv_use = []
register_num = []
distribute = []
full_desc = []
company_name = []
standard_stnd = []


cnt = 1
for page in range(1,3):
    params = {
        'numOfRows': 100,
        'pageNo':page,
    }

    res = requests.get(url, params=params)
    response = res.text
    response = xmltodict.parse(response) # xml을 orderDict로 변환
    response = json.dumps(response) # orderDict를 Json(유니코드)로 변환
    response = json.loads(response) # Json(유니코드) -> utf-8으로 변경

    try:
        response = response['response']['body']['items']['item'] #100개씩 리스트 형태로 들어있음
        print('현재 페이지', page, '페이지 내 데이터 갯수', len(response))
        for i in range(len(response)):
            index.append(cnt)
            register_date.append(response[i]['REGIST_DT'])
            product_name.append(response[i]['PRDUCT'])
            preservation_desc.append(response[i]['PRSRV_PD'])
            main_function.append(response[i]['MAIN_FNCTN'])
            sungsang.append(response[i]['SUNGSANG'])
            intake_hint.append(response[i]['INTAKE_HINT1'])
            srv_use.append(response[i]['SRV_USE'])
            register_num.append(response[i]['STTEMNT_NO'])
            distribute.append(response[i]['DISTB_PD'])
            full_desc.append(response[i]['BASE_STANDARD'])
            company_name.append(response[i]['ENTRPS'])
            cnt += 1
            try:
                standard_stnd.append(add_info['STTEMNT_NO'])
            except Exception as e:
                standard_stnd.append('')
                print(e,"추가정보 값 없음")       
            
    except Exception as e:
            print(e,"에러발생")   

entire_list['index'] = index
entire_list['REGIST_DT'] = register_date
entire_list['PRDUCT'] = product_name
entire_list['PRSRV_PD'] = preservation_desc
entire_list['MAIN_FNCTN'] = main_function
entire_list['SUNGSANG'] = sungsang
entire_list['INTAKE_HINT1'] = intake_hint
entire_list['SRV_USE'] = srv_use
entire_list['STTEMNT_NO'] = register_num
entire_list['DISTB_PD'] = distribute
entire_list['BASE_STANDARD'] = full_desc
entire_list['ENTRPS'] = company_name
entire_list['STDR_STND'] = standard_stnd


df = pd.DataFrame(entire_list)
df.to_csv("full_lst_trial_1.csv", encoding='cp949')
print('완료')
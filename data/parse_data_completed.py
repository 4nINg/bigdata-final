import xmltodict
import json
import requests
import pandas as pd

with open('secret.json') as f:
    secrets = json.loads(f.read())

# 'http://apis.data.go.kr/1470000/HtfsInfoService/' 건강기능 식품 정보 서비스
# 'http://apis.data.go.kr/1470000/HtfsTrgetInfoService' 건강기능 대상별 정보(DB) 서비스


# 건강기능 대상별 정보(DB) 파싱
ServiceKey_for_add_info = secrets['key']
URL_for_add_info = 'http://apis.data.go.kr/1470000/HtfsTrgetInfoService/getHtfsInfoList?ServiceKey='+ ServiceKey_for_add_info

#기준 및 규격 정보 저장용, 딕셔너리 변수 선언
add_info = {}

# 데이터 갯수 약 27,000개, 1페이지 당 100개의 데이터 파싱 가능
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
    
    # print(num)

print('-----------------------------------')



# 건강기능 식품 정보 서비스 정보 파싱
ServiceKey = secrets['key']
url = 'http://apis.data.go.kr/1470000/HtfsInfoService/getHtfsItem?ServiceKey=' + ServiceKey

entire_list = {}
index = []
register_date = [] #등록일자
product_name = [] #제품명
preservation_desc = [] #보존 및 유통기준
main_function = [] #주된 기능
sungsang = [] #성상
intake_hint = [] #섭취시 주의사항
srv_use = [] #용도용법 섭취량, 섭취방법
register_num = [] #품목제조관리번호
distribute = [] #보존 및 유통기한
full_desc = [] #기본 전체 정보
company_name = [] #회사명
standard_stnd = [] #기준 및 규격


cnt = 1
for page in range(1,272):
    params = {
        'numOfRows': 100,
        'pageNo':page,
    }

    res = requests.get(url, params=params)
    response = res.text
    response = xmltodict.parse(response) # xml을 orderDict로 변환
    response = json.dumps(response) # orderDict를 Json(유니코드)로 변환
    response = json.loads(response) # Json(유니코드) -> utf-8으로 변경

    #데이터를 다 받아온 경우, response값 에러발생 막기 위해 try & except 사용
    try:
        response = response['response']['body']['items']['item'] #100개씩 리스트 형태로 들어있음
        print('현재 페이지', page, '페이지 내 데이터 갯수', len(response))
        for i in range(len(response)):
            index.append(cnt)
            register_date.append(response[i]['REGIST_DT']) #등록일자
            product_name.append(response[i]['PRDUCT']) #제품명
            preservation_desc.append(response[i]['PRSRV_PD']) #보존 및 유통기준
            main_function.append(response[i]['MAIN_FNCTN']) #주된 기능
            sungsang.append(response[i]['SUNGSANG']) #성상
            intake_hint.append(response[i]['INTAKE_HINT1']) #섭취시 주의사항
            srv_use.append(response[i]['SRV_USE']) #용도용법 섭취량, 섭취방법
            register_num.append(response[i]['STTEMNT_NO']) #품목제조관리번호
            distribute.append(response[i]['DISTB_PD']) #보존 및 유통기한
            full_desc.append(response[i]['BASE_STANDARD']) #기본 전체 정보
            company_name.append(response[i]['ENTRPS']) #회사명
            cnt += 1

            #기준 및 규격 정보가 없을 경우, 에러발생 막기 위해 try & except 사용
            try:
                standard_stnd.append(add_info[response[i]['STTEMNT_NO']]) #기준 및 규격
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


df = pd.DataFrame(entire_list) #pandas Dataframe 형태로 변형
df.to_csv("full_lst_trial_1.csv", encoding='cp949') #csv 파일로 저장
print('완료')

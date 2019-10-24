import urllib
import xmltodict
import json

# ServiceKey = "hZ5wN1oxmwnrr1aSfsKpi1XM8AhX3DGSYBkahybytwVOCZfDpDgfvrQmZkxHvEGfNd%2BgFEsDzQdl4BhjG%2BbU3Q%3D%3D"
# url = 'http://apis.data.go.kr/1470000/HtfsInfoService/getHtfsItem' #상세정보조회
# # url = 'http://apis.data.go.kr/1470000/HtfsInfoService/getHtfsList' #목록조회
# queryParams = '?' + 'serviceKey=' + ServiceKey

# request = urllib.request.Request(url+queryParams)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
# #     print(response_body.decode('utf-8')) 
#     XML_dict = xmltodict.parse(response_body)
#     change_json = json.dumps(XML_dict)
#     json_dict = json.loads(change_json)
#     print(change_json)
# else:
#     print("Error Code:" + rescode)



import requests

ServiceKey = 'hZ5wN1oxmwnrr1aSfsKpi1XM8AhX3DGSYBkahybytwVOCZfDpDgfvrQmZkxHvEGfNd%2BgFEsDzQdl4BhjG%2BbU3Q%3D%3D'
URL = 'http://apis.data.go.kr/1470000/HtfsInfoService/getHtfsItem?ServiceKey='+ ServiceKey
parameters = {
    # 'numOfRows': 10,
    # 'pageNo': 1,
    'Prduct': "나우푸드",
    }

res = requests.get(URL, params=parameters)
response = res.text
response = xmltodict.parse(response) #xml 딕셔너리 형식
response = json.dumps(response) #json으로 변환
# response = json.loads(response) #json 딕셔너리 형식
print(response)

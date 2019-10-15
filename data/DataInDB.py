import requests
import json
import xmltodict

ServiceKey = 'hZ5wN1oxmwnrr1aSfsKpi1XM8AhX3DGSYBkahybytwVOCZfDpDgfvrQmZkxHvEGfNd%2BgFEsDzQdl4BhjG%2BbU3Q%3D%3D'
URL = 'http://apis.data.go.kr/1470000/HtfsTrgetInfoService/getHtfsInfoList?ServiceKey='+ ServiceKey
parameters = {
    'numOfRows': 1,
    'pageNo': 1,
    'prdlst_nm': '6년근 고려홍삼정골드 플러스',
    }

res = requests.get(URL, params=parameters)
response = res.text
response = xmltodict.parse(response)
response = json.dumps(response)
response = json.loads(response)
items = response['response']['body']['items']
print(items)


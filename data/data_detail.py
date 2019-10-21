
import xmltodict
import json
import requests
import pandas as pd

ServiceKey = 'hZ5wN1oxmwnrr1aSfsKpi1XM8AhX3DGSYBkahybytwVOCZfDpDgfvrQmZkxHvEGfNd%2BgFEsDzQdl4BhjG%2BbU3Q%3D%3D'
URL = 'http://apis.data.go.kr/1470000/HtfsTrgetInfoService/getHtfsInfoList?ServiceKey='+ ServiceKey

add_info = {}

for num in range(1, 100):
    parameters = {
        'numOfRows': 100,
        'pageNo': num,
        }

    res = requests.get(URL, params=parameters)
    response = res.text
    response = xmltodict.parse(response)
    response = json.dumps(response)
    response = json.loads(response)

    items = response['response']['body']['items']['item']

    for Product_Num in items:
        add_info[Product_Num['GU_PRDLST_MNF_MANAGE_NO']] = Product_Num['STDR_STND']

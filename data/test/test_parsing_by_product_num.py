import urllib
import xmltodict
import json
import requests

# 'http://apis.data.go.kr/1470000/HtfsInfoService/' 건강기능 식품 정보 서비스
# 'http://apis.data.go.kr/1470000/HtfsTrgetInfoService' 건강기능 대상별 정보(DB) 서비스



ServiceKey = "hZ5wN1oxmwnrr1aSfsKpi1XM8AhX3DGSYBkahybytwVOCZfDpDgfvrQmZkxHvEGfNd%2BgFEsDzQdl4BhjG%2BbU3Q%3D%3D"
url = 'http://apis.data.go.kr/1470000/HtfsInfoService/getHtfsItem?ServiceKey=' + ServiceKey
# url = 'http://apis.data.go.kr/1470000/HtfsInfoService/getHtfsList?ServiceKey=' + ServiceKey

params = {
    # 'numOfRows': 1,
    # 'pageNo':3,
    'STTEMNT_NO':'201100200015'

}

res = requests.get(url, params=params)
response = res.text
response = xmltodict.parse(response)
response = json.dumps(response)
# response = json.loads(response)
print(response)

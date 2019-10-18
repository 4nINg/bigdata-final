import urllib
import xmltodict
import json

ServiceKey = "hZ5wN1oxmwnrr1aSfsKpi1XM8AhX3DGSYBkahybytwVOCZfDpDgfvrQmZkxHvEGfNd%2BgFEsDzQdl4BhjG%2BbU3Q%3D%3D"
url = 'http://apis.data.go.kr/1470000/HtfsInfoService/getHtfsItem'
# 'http://apis.data.go.kr/1470000/HtfsInfoService/' 건강기능 식품 정보 서비스
# 'http://apis.data.go.kr/1470000/HtfsTrgetInfoService' 건강기능 대상별 정보(DB) 서비스

queryParams = '?' + 'serviceKey=' + ServiceKey

request = urllib.request.Request(url+queryParams)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    rD = xmltodict.parse(response_body)
    rDJ = json.dumps(rD)
    rDD = json.loads(rDJ)
    print(rDD)
else:
    print("Error Code:" + rescode)

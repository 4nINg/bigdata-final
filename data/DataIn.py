import urllib
import xmltodict
import json
from pprint import pprint

ServiceKey = "hZ5wN1oxmwnrr1aSfsKpi1XM8AhX3DGSYBkahybytwVOCZfDpDgfvrQmZkxHvEGfNd%2BgFEsDzQdl4BhjG%2BbU3Q%3D%3D"
# url = 'http://apis.data.go.kr/1470000/HtfsInfoService/getHtfsItem'
url = 'http://apis.data.go.kr/1470000/HtfsInfoService/getHtfsList

queryParams = '?' + 'serviceKey=' + ServiceKey

request = urllib.request.Request(url+queryParams)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
#     print(response_body.decode('utf-8')) 
    rD = xmltodict.parse(response_body)
    rDJ = json.dumps(rD)
    rDD = json.loads(rDJ)
    print(rDD)
else:
    print("Error Code:" + rescode)
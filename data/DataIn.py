import urllib
import xmltodict
import json

ServiceKey = "hZ5wN1oxmwnrr1aSfsKpi1XM8AhX3DGSYBkahybytwVOCZfDpDgfvrQmZkxHvEGfNd%2BgFEsDzQdl4BhjG%2BbU3Q%3D%3D"
url = 'http://apis.data.go.kr/1470000/HtfsInfoService/getHtfsItem' #상세정보조회
# url = 'http://apis.data.go.kr/1470000/HtfsInfoService/getHtfsList' #목록조회
queryParams = '?' + 'serviceKey=' + ServiceKey

request = urllib.request.Request(url+queryParams)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
#     print(response_body.decode('utf-8')) 
    XML_dict = xmltodict.parse(response_body)
    change_json = json.dumps(XML_dict)
    json_dict = json.loads(change_json)
    print(json_dict)
else:
    print("Error Code:" + rescode)
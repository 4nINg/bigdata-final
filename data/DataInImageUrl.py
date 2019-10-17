import os
import sys
import urllib.request
import json

client_id = "vIfAnKuEGVn8pdpNJHU5"
client_secret = "ICj95OKn_H"
encText = urllib.parse.quote("박보영")
url = "https://openapi.naver.com/v1/search/image?query=" + encText # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_body = response_body.decode('utf-8')
#     print(response_dict)
    response_dict = json.loads(response_body)
    print(response_dict['items'])
    print('-'*30 + '데이터 구성' + '-'*30)
    print(response_dict['items'][0])
else:
    print("Error Code:" + rescode)
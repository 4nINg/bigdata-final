import urllib.request
import json

response = urllib.request.urlopen('http://apis.data.go.kr/1470000/HtfsTrgetInfoService/getHtfsInfoList?serviceKey=%2BzCak%2FfLP4v3W6mGff2%2Bhsj%2BJvQ9pOQBEevpvH8hjZswIEmK7vOkvqq12nX2AGqLD7VBRqqODGHoLQBorV5OaQ%3D%3D')
byte_data = response.read()
text_data = byte_data.decode('utf-8')
flag = False
flag2 = False
for line in text_data.split("\n"):
    if "<items>" in line:
        flag = True
    if flag:
        if "<item>" in line:
            flag2 = True
        if flag2:
            print(line)
        if "</item>" in line:
            flag2 = False
    if "</items>" in line:
        flag = False
    

# print(type(text_data))
# print(text_data)
import requests
import json
import xmltodict

# List = ['홍삼파워멀티비타민앤미네랄', '홍삼프리미엄유산균', '황작 황작고', '힘내', "'간'편함을 누리다 밀크씨슬 간 肝", '(fine)파인실엠I', '(구) 눈에좋은 루테인+오메가3', '(구) 무르핀', '(구) 팻다운 톡',]

# List = ["6년근 고려홍삼정 PREMIUM", "Brain Factor-7 Silk Fibroin Peptide(BF-7)(전량 수출용)", "CosmeHeal HEALTHY WHITE EfferGlow(수출용)？(코스메힐 헬씨 화이트, 에퍼글로우？)", "엽산400"]
List = ["엽산400"]

for name in List:
    ServiceKey = 'hZ5wN1oxmwnrr1aSfsKpi1XM8AhX3DGSYBkahybytwVOCZfDpDgfvrQmZkxHvEGfNd%2BgFEsDzQdl4BhjG%2BbU3Q%3D%3D'
    URL = 'http://apis.data.go.kr/1470000/HtfsTrgetInfoService/getHtfsInfoList?ServiceKey='+ ServiceKey
    parameters = {
        'numOfRows': 1,
        'pageNo': 1,
        'prdlst_nm': name,
        }


    res = requests.get(URL, params=parameters)
    response = res.text
    response = xmltodict.parse(response)
    response = json.dumps(response)
    # json_dict = json.loads(change_json)
    # items = response['response']['body']['items']
    print(response)

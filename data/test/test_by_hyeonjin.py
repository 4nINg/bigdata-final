import requests
import json
import csv

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def create_products():
    csvfile = open('./data/processed_data.csv', newline='')
    product_data = csv.DictReader(csvfile)

    request_data = {'items': []}
    for idx, product in enumerate(product_data):
        dic = {}
        dic['PRDUCT'] = product['PRDUCT']
        dic['COMPANY_NM'] = product['COMPANY_NM']
        dic['PRSRV_PD'] = list(product['PRSRV_PD'].split('\n'))
        dic['IMAGE_URL'] = product['IMAGE_URL']
        dic['MAIN_FNCTN'] = list(product['MAIN_FNCTN'].split('\n'))
        dic['SUNGSANG'] = product['SUNGSANG']
        dic['INTAKE_HINT1'] = list(product['INTAKE_HINT1'].split('\n'))
        dic['SRV_USE'] = product['SRV_USE']

        # 성분
        base_standard = {}
        base_detail = []
        base_std_list = list(product['BASE_STANDARD'].split('\n'))
        for base in base_std_list:
            base_list = list(base.split(':'))
            base_standard[base_list[0]] = base_list[1]
            base_detail.append(base_list[0])

        dic['BASE_STANDARD'] = base_standard
        dic['BASE'] = base_detail

        # 첨가물
        heavy_metal = {}
        heavy_metal_list = list(product['STTEMNT_NO'].split('\n'))
        for metal in heavy_metal_list:
            metal_list = list(metal.split('(mg/kg):'))
            heavy_metal[metal_list[0]] = metal_list[1]

        dic['HEAVY_METAL'] = heavy_metal
        dic['DISTB_PD'] = product['DISTB_PD']

        request_data['items'].append(dic)

    print(request_data)


    # response = requests.post(API_URL + 'movies/', data=json.dumps(request_data), headers=headers)
    # print(response.text)


if __name__ == '__main__':
    create_products()

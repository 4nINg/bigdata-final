import requests, csv, json, sys, io
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ISO-8859-1')

API_URL = 'http://192.168.100.69:8000/api/'
headers = {'content-type': 'application/json'}

# 효능 리스트 파싱 함수
def create_function(): 
    function_data = open('./data/function_data.csv', 'r')
    request_data = {'function': []}
    for line in function_data.readlines()[1:]:
        [idx, function] = line.split(',')
        function = function[:-1]

        request_data['function'].append({
            'name': function,
        })

    response = requests.post(API_URL + 'data/functions/', data=json.dumps(request_data), headers=headers)

# 성분 리스트 파싱 함수
def create_ingredient():
    ingredient_data = open('./data/ingredient_data.csv', 'r')
    request_data = {'ingredient': []}
    for line in ingredient_data.readlines()[1:]:
        [idx, ingredient] = line.split(',')
        ingredient = ingredient[:-1]

        request_data['ingredient'].append({
            'name': ingredient,
        })
    
    response = requests.post(API_URL + 'data/ingredients/', data=json.dumps(request_data), headers=headers)

# 제품 리스트 파싱 함수
def create_products():
    product_data = open('./data/processed_data.csv', newline='')
    product_data = csv.DictReader(product_data)

    request_data = {'product': []}
    for idx, product in enumerate(product_data):
        dic = {}
        dic['name'] = product['PRDUCT'] # 제품명
        dic['company_name'] = product['COMPANY_NM'] #회사명
        dic['product_to_function'] = list(product['MAIN_FNCTN'].split('\n')) #효능 M:N
        dic['sungsang'] = product['SUNGSANG'] #성상
        dic['intake_hint'] = list(product['INTAKE_HINT1'].split('\n')) # 섭취힌트
        dic['intake_method'] = product['SRV_USE'] # 섭취방법
        dic['preservation'] = list(product['PRSRV_PD'].split('\n')) # 보존방법
        dic['image_url'] = product['IMAGE_URL'] # 이미지 url

        # 성분
        base_standard = {}
        base_detail = []
        base_std_list = list(product['BASE_STANDARD'].split('\n'))
        for base in base_std_list:
            base_list = list(base.split(':'))
            base_standard[base_list[0]] = base_list[1]
            base_detail.append(base_list[0])

        dic['ingredient_list'] = base_standard # 주성분 전체리스트(json)
        dic['product_to_ingredient'] = base_detail # 성분 M:N

        # 첨가물
        heavy_metal = {} 
        heavy_metal_list = list(product['STTEMNT_NO'].split('\n'))
        for metal in heavy_metal_list:
            metal_list = list(metal.split('(mg/kg):'))
            heavy_metal[metal_list[0]] = metal_list[1]

        dic['heavy_metal'] = heavy_metal # 중금속 전체리스트(json)

        request_data['product'].append(dic)

    response = requests.post(API_URL + 'data/products/', data=json.dumps(request_data), headers=headers)



if __name__ == '__main__':
    # create_function()
    # create_ingredient()
    create_products()
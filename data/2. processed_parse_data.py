import csv
import pandas as pd

with open('./data/entire_data_from_api.csv') as f:
    txt_data = f.readlines()[1:]
    Entire_List= csv.reader(txt_data)

with open('./data/Add_Data.csv') as f:
    txt_data = f.readlines()[1:]
    URL_List = csv.reader(txt_data)

entire_list = {}
index = []
register_date = []
product_name = []
preservation_desc = []
main_function = []
sungsang = []
intake_hint = []
srv_use = []
register_num = []
distribute = []
full_desc = []
company_name = []
standard_stnd = []
image_url = []

for url in URL_List:
    for entire in Entire_List:
        if url[0] == entire[0]:
            register_date.append(entire[8])
            product_name.append(entire[6])
            preservation_desc.append(entire[7])
            main_function.append(entire[5])
            sungsang.append(entire[12])
            intake_hint.append(entire[4])
            srv_use.append(entire[9])
            register_num.append(entire[11])
            distribute.append(entire[2])
            full_desc.append(entire[1])
            company_name.append(url[3])
            image_url.append(url[5])
            standard_stnd.append(entire[10])
            break
entire_list['REGIST_DT'] = register_date
entire_list['PRDUCT'] = product_name
entire_list['PRSRV_PD'] = preservation_desc
entire_list['MAIN_FNCTN'] = main_function
entire_list['SUNGSANG'] = sungsang
entire_list['INTAKE_HINT1'] = intake_hint
entire_list['SRV_USE'] = srv_use
entire_list['STTEMNT_NO'] = register_num
entire_list['DISTB_PD'] = distribute
entire_list['BASE_STANDARD'] = full_desc
entire_list['COMPANY_NM'] = company_name
entire_list['STDR_STND'] = standard_stnd
entire_list['IMAGE_URL'] = image_url
print(entire_list)

# df = pd.DataFrame(entire_list)
# df.to_csv("./data/processed_data.csv", mode = 'a',index = False, header = False, encoding='cp949')
import requests
import csv
# import json

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ISO-8859-1')

API_URL = 'http://localhost:8000/api/'
# headers = {'content-type': 'application/json'}

def create_fnc():
    csv_data = open('./Fnc.csv', 'r', encoding='ISO-8859-1')
    # request_data = csv.reader(csv_data)
    read_data = csv_data.readlines()[1:]
    fnc_data = csv.reader(read_data)
    request_data = {'function': []}
    for data in fnc_data:
        [idx, fnc] = data
        request_data['function'].append({
            'idx': idx,
            'fnc': fnc,
        })
    print(request_data)

    # response = requests.post(API_URL + 'fnc/', data=json.dumps(request_data), headers=headers)
    response = requests.post(API_URL + 'fnc/', data=request_data)
    print(response.text)

create_fnc()











# API_URL = 'http://localhost:8000/api/'
# headers = {'content-type': 'application/json'}

# def create_users(num_users):
#     user_data = open('./users.dat', 'r', encoding='ISO-8859-1')
#     request_data = {'profiles': []}
#     occupation_map = {
#         0: "other", 1: "academic/educator", 2: "artist", 3: "clerical/admin", 4: "college/grad student",
#         5: "customer service", 6: "doctor/health care", 7: "executive/managerial", 8: "farmer", 9: "homemaker",
#         10: "K-12 student", 11: "lawyer", 12: "programmer", 13: "retired", 14: "sales/marketing",
#         15: "scientist", 16:  "self-employed", 17: "technician/engineer", 18: "tradesman/craftsman",
#         19: "unemployed", 20: "writer"
#     }

#     for line in user_data.readlines():
#         [userid, gender, age, occupation, zipcode] = line.split('::')
#         username = 'user' + userid
#         age = int(age)
#         occupation = occupation_map[int(occupation)]

#         request_data['profiles'].append({
#             'username': username,
#             'password': username,
#             'age': age,
#             'gender': gender,
#             'occupation': occupation
#         })

#         if len(request_data['profiles']) >= num_users:
#             break

#     response = requests.post(API_URL + 'auth/signup-many/', data=json.dumps(request_data), headers=headers)
#     print(response.text)


# def create_health_food():
#     health_food_data = open('./new_data.csv', 'r', encoding='ISO-8859-1')
#     request_data = csv.reader(health_food_data)
#     # request_data = {'health_food': []}
#     # for data in reader:
#     #     [id, title, genres] = data[]
#     #     genres = genres[:-1].split('|')
#     #     request_data['health_food'].append({
#     #         'id': id,
#     #         'title': title,
#     #         'genres': genres
#     #     })

#     response = requests.post(API_URL + 'health_food/', data=json.dumps(request_data), headers=headers)
#     print(response.text)


# def create_ratings(num_users):
#     pass


# if __name__ == '__main__':
#     num_users = 15
#     create_movies()
#     create_users(num_users)
#     create_ratings(num_users)

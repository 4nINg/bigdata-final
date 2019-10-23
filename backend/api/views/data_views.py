from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Ingredient, Function

# import requests
# import pandas as pd
# import csv

@api_view(['POST'])
def create_fnc_data():
    if request.method == 'POST':
        functions = request.data.get('function', None)
        print(function)
        for function in functions:
            idx = function.get('idx', None)
            fnc = function.get('fnc', None)
            print(idx)
            print(fnc)
    return 'yo!'

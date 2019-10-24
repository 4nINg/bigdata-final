from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Ingredient, Function, Product
from api.serializers import HeavyMetalSerializer

# 테스트 코드
# from django.http import JsonResponse
# def test(request):
#     product = Product.objects.last()
#     serializer = HeavyMetalSerializer(product)
#     data = serializer.data
#     print(data)

#     # return Response(data=data, status=status.HTTP_200_OK)
#     return JsonResponse({'error': 'Some error'}, status=401)


@api_view(['POST'])
def functions(request):
    if request.method == 'POST':
        functions = request.data.get('function', None)

        for function in functions:
            name = function.get('name', None)
            Function(name=name).save()

        return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def ingredients(request):
    if request.method == 'POST':
        ingredients = request.data.get('ingredient', None)

        for function in ingredients:
            name = function.get('name', None)
            Ingredient(name=name).save()

        return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def products(request):
    if request.method == 'POST':
        products = request.data.get('product', None)
        
        for product in products:
            name = product.get('name', None)
            company_name = product.get('company_name', None)
            ingredient_list = product.get('ingredient_list', None)
            product_to_ingredient = product.get('product_to_ingredient', None)
            product_to_function = product.get('product_to_function', None)
            heavy_metal = product.get('heavy_metal', None)
            sungsang = product.get('sungsang', None)
            intake_hint = product.get('intake_hint', None)
            intake_method = product.get('intake_method', None)
            preservation = product.get('preservation', None)
            image_url = product.get('image_url', None)

            product = Product(name=name, company_name=company_name, ingredient_list=ingredient_list, 
                              heavy_metal=heavy_metal, sungsang=sungsang, intake_hint=intake_hint, 
                              intake_method=intake_method, preservation=preservation, image_url=image_url)
            
            product.save()

            for my_ingredient in product_to_ingredient:
                ingredient = Ingredient.objects.get(name=my_ingredient)
                product.product_to_ingredient.add(ingredient)
            
            for my_function in product_to_function:
                function = Function.objects.get(name=my_function)
                product.product_to_function.add(function)

            break
            
        return Response(status=status.HTTP_201_CREATED)

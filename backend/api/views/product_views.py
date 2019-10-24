from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Ingredient, Function, Product
from api.serializers import ProductSerializer, FunctionSerializer, IngredientSerializer

@api_view(['POST', 'GET'])
def product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        data = serializer.data

        return Response(data=data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        keyword = request.data.get('keyword', None)
        products_by_name = Product.objects.filter(name__icontains=keyword)
        products_by_ingredient = Product.objects.filter(ingredient_list__icontains=keyword)
        products = products_by_name | products_by_ingredient

        serializer = ProductSerializer(products, many=True)
        data = serializer.data

        return Response(data=data, status=status.HTTP_200_OK)
        

@api_view(['POST', 'GET'])
def function(request):
    if request.method == 'GET':
        functions = Function.objects.all()
        serializer = FunctionSerializer(functions, many=True)
        data = serializer.data

        return Response(data=data, status=status.HTTP_200_OK)

@api_view(['POST', 'GET'])
def ingredient(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        data = serializer.data

        return Response(data=data, status=status.HTTP_200_OK)
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
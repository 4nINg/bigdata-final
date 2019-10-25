from .models import Profile, Product, Ingredient, Function
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField('get_ingredients')
    heavy_metals = serializers.SerializerMethodField('get_heavy_metals')
    functions = serializers.SerializerMethodField('get_functions')

    class Meta:
        model = Product
        fields = ('id', 'name', 'company_name', 'functions', 'ingredients', 'ingredient_list',  'heavy_metals', 'heavy_metal_list',  'sungsang', 'intake_hint', 'intake_method', 'preservation', 'image_url')

    def get_ingredients(self, obj): # 성분이름만 출력
        ingredient_list = obj.ingredient_list
        ingredients = [key for key in ingredient_list]
        return ingredients
    
    def get_heavy_metals(self, obj): # 중금속이름만 출력
        heavy_metal_list = obj.heavy_metal_list
        heavy_metals = [key for key in heavy_metal_list]
        return heavy_metals
    
    def get_functions(self, obj): # 효능이름만 출력
        function_list = obj.product_to_function.all()
        functions = [function.name for function in function_list]
        return functions

class FunctionSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField('get_product_name')

    class Meta:
        model = Function
        fields = ('name', 'products')
    
    def get_product_name(self, obj): # 제품 이름 출력(제품테이블PK, 이름)
        product_list = obj.function_to_product.all()
        products = [(product.id, product.name) for product in product_list]
        return products


class IngredientSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField('get_product_name')

    class Meta:
        model = Ingredient
        fields = ('name', 'products')
    
    def get_product_name(self, obj): # 제품 이름 출력(제품테이블PK, 이름)
        product_list = obj.ingredient_to_product.all()
        products = [(product.id, product.name) for product in product_list]
        return products


class ProfileSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Profile
        fields = ('id', 'email', 'nickname', 'age', 'gender')



# class ProfileSerializer(serializers.ModelSerializer):
#     email = serializers.SerializerMethodField('get_email')
#     token = serializers.SerializerMethodField('get_token')
#     is_authenticated = serializers.SerializerMethodField('get_is_authenticated')
#     nickname = serializers.SerializerMethodField('get_nickname')
   
#     class Meta:
#         model = Profile
#         fields = ('email', 'token', 'is_authenticated', 'nickname')

#     def get_email(self, obj):
#         return str(obj['username'])

#     def get_token(self, obj):
#         return str(obj['token'])
    
#     def get_is_authenticated(self, obj):
#         return obj['is_authenticated']

#     def get_nickname(self, obj):
#         return str(obj['nickname'])


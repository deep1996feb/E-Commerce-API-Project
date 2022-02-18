from rest_framework import serializers
from .models import Cart, Category, ShoppingMart, Product, Cart, User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class ShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingMart
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    shopping = serializers.PrimaryKeyRelatedField(many=True, queryset=ShoppingMart.objects.all())
    product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ('__all__')


class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class CartSerializer(serializers.ModelSerializer):
    cart_id = CartUserSerializer(read_only=True, many=False)
    shopping = ShoppingSerializer(read_only = True, many=True)
    products = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ('__all__')
from django.shortcuts import render
from rest_framework import generics
from .models import Category, Product, ShoppingMart, User, Cart
from .serializers import CartSerializer, CategorySerializer, ProductSerializer, ShoppingSerializer, UserSerializer
from rest_framework import permissions
# Create your views here.

class ListCategory(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListShopping(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ShoppingMart.objects.all()
    serializer_class = ShoppingSerializer

class DetailShopping(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ShoppingMart.objects.all()
    serializer_class = ShoppingSerializer

class ListProduct(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListUser(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListCart(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

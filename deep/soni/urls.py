from django.urls import path
from .views import ListCategory, DetailCategory,ListShopping,DetailShopping,ListProduct,DetailProduct,ListUser,DetailUser,ListCart,DetailCart

urlpatterns = [
    path('categories',ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/',DetailCategory.as_view(), name='single category'),
    path('shopping', ListShopping.as_view(), name='shopping'),
    path('shopping/<int:pk>/', DetailShopping.as_view(), name='singleshopping'),
    path('product', ListProduct.as_view(), name='product'),
    path('product/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),
    path('users',ListUser.as_view(), name='users'),
    path('users/<int:pk>/',DetailUser.as_view(), name='singleuser'),
    path('carts', ListCart.as_view(), name='allcart'),
    path('carts/<int:pk>/',DetailCart.as_view(), name='detailcart'),
]

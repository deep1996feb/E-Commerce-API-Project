from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title


class ShoppingMart(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    image = models.ImageField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    dateadd = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['category']
    def __str__(self):
        return self.title


class Product(models.Model):
    product_tag = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    dateadd = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['category']
    def __str__(self):
        return '{}'.format(self.product_tag, self.name)


class Cart(models.Model):
    cart_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    shopping = models.ManyToManyField(ShoppingMart)
    products = models.ManyToManyField(Product)

    class meta:
        ordering = ['cart_id']
    def __str__(self):
        return str(self.cart_id)

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} * {self.product.name}'


class ClientProfile(models.Model):
    client_name = models.CharField(max_length=200)
    client_bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    dat_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

    def edit(self, client_name, client_bio, profile_image):
        self.client_name = client_name
        self.client_bio = client_bio
        self.profile_image = profile_image
        self.save()

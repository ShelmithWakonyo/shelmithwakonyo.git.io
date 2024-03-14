from django.contrib import admin

from pets.models import Product, CartItem, ClientProfile

# Register your models here.
admin.site.register(Product)
admin.site.register(CartItem)

admin.site.register(ClientProfile)

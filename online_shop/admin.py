from django.contrib import admin
from .models import Category, Product, Comment, Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Order)


from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('categories/', views.categories, name='categories'),
    path('product_detail/<int:product_id>/', views.detail, name='product_detail')
]


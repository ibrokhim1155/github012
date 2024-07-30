
from django.urls import path
from . import views
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('catagories/',views.catagories,name ='catagories'),
    path('product_detail/<int:product_id/>',views.detail,name='product_detail')

]

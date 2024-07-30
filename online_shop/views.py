from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from online_shop.models import Category, Product

def categories(request):
    category_list = Category.objects.all()
    context = {
        'categories': category_list
    }
    return render(request, 'online_shop/home.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'online_shop/home.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = product.comments.filter(is_visible=True)
    context = {
        'product': product,
        'comments': comments
    }
    return render(request, 'online_shop/detail.html', context)

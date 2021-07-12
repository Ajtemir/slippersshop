from django.shortcuts import render

from shops.models import Product


def index(request):
    return render(request, 'index.html')

def home(request):
    products = Product.objects.filter(availability=True).all()
    print(products)
    return render(request, 'shops/home.html', {'products': products})

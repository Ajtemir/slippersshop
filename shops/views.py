from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from cart.forms import CartAddProductForm
from shops.forms import ContactForm
from shops.models import Product


def index(request):
    return render(request, 'index.html')

def home(request):
    products = Product.objects.filter(availability=True).all()
    return render(request, 'shops/home.html', {'products': products})

def optom(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            number = form.cleaned_data['phone']
            try:
                send_mail(f"{name},{number},", 'defog', 'u_iskenderov@mail.ru', ['aytush2001@gmail.com'],
                          fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return HttpResponse('Приняли! Спасибо за вашу заявку.')
    else:
        return HttpResponse('Неверный запрос.')
    # return render(request, "index.html", {'form': form})
    return render(request, 'shops/optom.html', {'form': form})

def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')




        # EMAIL_HOST = 'aytush2001@gmail.com'
    # EMAIL_HOST_USER = 'aytush2001@gmail.com'
    # EMAIL_HOST_PASSWORD = 'archabeshik'
    # EMAIL_PORT = 587
    # EMAIL_USE_TLS = True
    # if request.method == 'POST':
    #     # Форма была отправлена
    #     form = EmailPostForm(request.POST)
    #     if form.is_valid():
    #     # Поля формы прошли проверку
    #     cd = form.cleaned_data
    #     post_url = request.build_absolute_uri(post.get_absolute_url())
    #     subject = '{} ({}) recommends you reading " {}"'.format(cd['name'], cd['email'], post.title)
    #     message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
    #     send_mail(subject, message, 'admin@myblog.com', [cd['to']])
    #     sent = True
    #     else:
    #     form = EmailPostForm()

def product_detail(request, id):
    product = get_object_or_404(Product, id=id, availability=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shops/detail.html', {'product': product,
                                                 'cart_product_form': cart_product_form})

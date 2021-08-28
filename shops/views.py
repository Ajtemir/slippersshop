from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError

from cart.cart import Cart
from cart.forms import CartAddProductForm
from main.settings.production import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from shops.forms import ContactForm, OrderForm, SearchForm
from shops.models import Product
from django.contrib import messages


def index(request):
    return redirect('shop:home')


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
                send_mail('Оптом', f"Имя: {name},\nНомер: {number}", DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL,
                          fail_silently=False)
                messages.success(request, 'Ожидайте наш звонок!!!')
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            # return HttpResponse('Приняли! Спасибо за вашу заявку.')
            return redirect('shop:optom')
    else:
        return HttpResponse('Неверный запрос.')
    # return render(request, "index.html", {'form': form})
    return render(request, 'shops/optom.html', {'form': form})


def order(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    text = str()
    for item in cart:
        text += f"Название:{item['product']} => Количество:{item['quantity']}\n"
    text += f'Общая сумма:{Cart.get_total_price(self=Cart(request))} сом'

    form = OrderForm(initial={'text': text})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            subject = 'Заказ'
            message = f'\n{text}\nИмя:{name}\nАдрес:{address}\nНомер:{phone}'
            send_mail(f"{subject}", message, 'u_iskenderov@mail.ru', ['aytush2001@gmail.com'], fail_silently=False)
        return redirect('cart:cart_detail')
    return render(request, 'shops/order.html', {'form': form})

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

def search(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            products = Product.objects.filter(name__icontains=name)
            return render(request, 'shops/search.html',{'form':form,
                                                'products':products})
    products = Product.objects.filter(availability=True).all()

    return render(request, 'shops/search.html',{'form':form,
                                                'products':products})

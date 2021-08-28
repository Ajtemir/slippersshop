from django.urls import path
from shops import views

urlpatterns = [
    path('', views.home, name='home'),
    path('optom/', views.optom, name='optom'),
    path('<int:id>/', views.product_detail,
         name='detail'),
    path('order/', views.order, name='order'),
    path('search/', views.search, name='search'),


]
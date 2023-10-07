from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fuel-delivery.html', views.fuelDelivery, name='fuelDelivery'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('service-1.html', views.services, name='services'),
    path('engin-oil-service.html', views.enginOil, name='enginOil'),
    path('car-wash.html', views.carWash, name='carWash'),
    path('battery-serivce.html', views.battery, name='battery'),
    path('tyre-service.html', views.tyre, name='tyre'),
    path('tow-truck-service.html', views.towTruck, name='towTruck'),
    path('register/',views.register , name='register'),
    path('login_user',views.login_user , name='login_user'),
    path('logout_user',views.logout_user , name='logout_user'),
    path('reservation_form',views.reservation_form , name='reservation_form'),
    path('payment',views.visa , name='visa'),
    path('dashboard',views.dashboard , name='dashboard'),
    path('profile',views.profile , name='profile'),
    path('orders_history',views.orders_history , name='orders_history'),
]
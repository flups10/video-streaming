from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.premium_offers, name="premium"),
    path('checkout', views.checkout, name="checkout"),
]

from django.contrib import admin
from django.urls import path
from .views import AboutUsView, ProductListView, HomeView


app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/', HomeView.as_view(), name='product-list'),
    path('product/<int:pk>/', HomeView.as_view(), name='product-list'),
    path('about-us/', HomeView.as_view(), name='about-us'),
]

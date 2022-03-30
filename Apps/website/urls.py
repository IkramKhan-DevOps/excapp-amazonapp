from django.contrib import admin
from django.urls import path
from .views import AboutUsView, ProductListView, HomeView, ProductDetailView


app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('about-us/', HomeView.as_view(), name='about-us'),
]

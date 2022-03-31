import django_filters
from django.forms import TextInput
from Apps.website.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'name'}), lookup_expr='icontains')

    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'brand': ['exact'],
        }
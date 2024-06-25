from django_filters.rest_framework import FilterSet
from .models import Product

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'rudder': ['exact'],
            'drive_unit': ['exact'],
            'car_year': ['exact'],
            'type_of_fuel': ['exact'],
            'checkpoint': ['exact'],
            'price': ['gt', 'lt']

        }
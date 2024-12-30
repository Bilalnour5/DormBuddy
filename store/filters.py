from django_filters.rest_framework import FilterSet
from .models import Properties

class PropertyFilter(FilterSet):
    class Meta:
        model = Properties
        fields = {
            'city' : ['exact'],
            'rent' : ['gt', 'lt']
        }

from rest_framework import serializers
from .models import Properties

class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = [
            'externalid',
            'areasqm',
            'city',
            'postalcode',
            'coverimageurl',
            'propertytype',
            'title',
            'descriptiontranslated',
            'rentdetail',
            'rent',
            'deposit',
            'furnish'
        ]

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = [
            'externalid',
            'city',
            'coverimageurl',
            'title',
            'rent',
        ]
        

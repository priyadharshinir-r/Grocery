from rest_framework import serializers
from .models import Grocery


# Response Serializer (Full Model)
class GroceryResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        fields = '__all__'


# Request Serializer (For Input Validation)
class GroceryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        fields = ['name', 'price', 'rating']

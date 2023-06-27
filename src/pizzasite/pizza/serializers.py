from rest_framework import serializers
from .models import Pizza, Deal

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'pizza_name', 'image', 'price', 'deal')
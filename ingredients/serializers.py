from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ingredients.models import Bread, Topping, Cheese, Sauce


class BreadSerializer(ModelSerializer):
    def create(self, validated_data):
        bread = Bread.objects.create(**validated_data)
        return bread

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.in_stock += validated_data.get('name', 0)
        instance.price = validated_data.get('price', instance.price)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    class Meta:
        model = Bread
        fields = "__all__"

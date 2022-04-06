from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ingredients.models import Bread, Topping, Cheese, Sauce


class BreadSerializer(ModelSerializer):
    def create(self, validated_data):
        bread = Bread.objects.create(**validated_data)
        return bread

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.in_stock = validated_data.get('in_stock', instance.in_stock)
        instance.price = validated_data.get('price', instance.price)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    class Meta:
        model = Bread
        fields = '__all__'


class ToppingSerializer(ModelSerializer):
    def create(self, validated_data):
        topping = Topping.objects.create(**validated_data)
        return topping

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.in_stock = validated_data.get('in_stock', instance.in_stock)
        instance.price = validated_data.get('price', instance.price)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    class Meta:
        model = Topping
        fields = '__all__'


class CheeseSerializer(ModelSerializer):
    def create(self, validated_data):
        cheese = Cheese.objects.create(**validated_data)
        return cheese

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.in_stock = validated_data.get('in_stock', instance.in_stock)
        instance.price = validated_data.get('price', instance.price)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    class Meta:
        model = Cheese
        fields = '__all__'


class SauceSerializer(ModelSerializer):
    def create(self, validated_data):
        sauce = Sauce.objects.create(**validated_data)
        return sauce

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.in_stock = validated_data.get('in_stock', instance.in_stock)
        instance.price = validated_data.get('price', instance.price)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    class Meta:
        model = Sauce
        fields = '__all__'


class BreadShortSerializer(ModelSerializer):

    class Meta:
        model = Bread
        fields = ['id', 'name']


class CheeseShortSerializer(ModelSerializer):

    class Meta:
        model = Cheese
        fields = ['id', 'name']


class ToppingShortSerializer(ModelSerializer):

    class Meta:
        model = Bread
        fields = ['id', 'name']


class SauceShortSerializer(ModelSerializer):

    class Meta:
        model = Bread
        fields = ['id', 'name']

from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from sandwiches.models import Sandwich
from ingredients.serializers import (
    BreadSerializer,
    CheeseSerializer,
    ToppingSerializer,
    SauceSerializer,)


class SandwichSerializer(ModelSerializer):
    price = serializers.SerializerMethodField()

    def get_price(self, instance) -> int:
        bread = instance.bread.price
        cheese = instance.cheese.price
        toppings = sum([obj.price for obj in instance.toppings.all()])
        sauces = sum([obj.price for obj in instance.sauces.all()])

        price = bread + cheese + toppings + sauces
        return price

    @transaction.atomic()
    def create(self, validated_data):
        bread = validated_data.get('bread')
        cheese = validated_data.get('cheese')
        toppings = validated_data.pop('toppings')
        sauces = validated_data.pop('sauces')

        if bread.in_stock == 0:
            raise serializers.ValidationError(
                f"bread id {bread.id} is out of stock")
        if cheese.in_stock == 0:
            raise serializers.ValidationError(
                f"cheese id {cheese.id} is out of stock")

        bread.in_stock -= 1
        bread.save()
        cheese.in_stock -= 1
        cheese.save()
        sandwich = Sandwich.objects.create(**validated_data)

        if len(toppings) > 2 or len(sauces) > 2:
            raise serializers.ValidationError(
                "can not select more than 2 choices in topping & sauce")

        for topping in toppings:
            if topping.in_stock == 0:
                raise serializers.ValidationError(
                    f"topping id {topping.id} is out of stock")
            topping.in_stock -= 1
            topping.save()
            sandwich.toppings.add(topping)

        for sauce in sauces:
            if sauce.in_stock == 0:
                raise serializers.ValidationError(
                    f"sauce id {sauce.id} is out of stock")
            sauce.in_stock -= 1
            sauce.save()
            sandwich.sauces.add(sauce)

        return sandwich

    @transaction.atomic()
    def update(self, instance, validated_data):
        instance.status = validated_data.get("status", instance.status)

        bread = instance.bread
        cheese = instance.cheese
        toppings = instance.toppings.all()
        sauces = instance.sauces.all()

        bread.in_stock += 1
        bread.save()
        cheese.in_stock += 1
        cheese.save()

        for topping in toppings:
            topping.in_stock += 1
            topping.save()

        for sauce in sauces:
            sauce.in_stock += 1
            sauce.save()

        instance.save()

        return instance

    class Meta:
        model = Sandwich
        fields = ["name", "price", "status",
                  "bread", "cheese", "toppings", "sauces"]


class SandwichDetailSerializer(ModelSerializer):
    bread = BreadSerializer()
    cheese = CheeseSerializer()
    toppings = ToppingSerializer(many=True)
    sauces = SauceSerializer(many=True)
    price = serializers.SerializerMethodField()

    def get_price(self, instance) -> int:
        bread = instance.bread.price
        cheese = instance.cheese.price
        toppings = sum([obj.price for obj in instance.toppings.all()])
        sauces = sum([obj.price for obj in instance.sauces.all()])

        price = bread + cheese + toppings + sauces
        return price

    class Meta:
        model = Sandwich
        fields = '__all__'


class QuerySearchSerializer(serializers.Serializer):
    bread = serializers.IntegerField(
        help_text='bread id(max_1)', required=False)
    topping = serializers.IntegerField(
        help_text='topping id(max_2)', required=False)
    cheese = serializers.IntegerField(
        help_text='cheese id(max_1)', required=False)
    sauce = serializers.IntegerField(
        help_text='topping id(max_2)', required=False)
    offset = serializers.IntegerField(help_text='page offset', default=0)
    limit = serializers.IntegerField(help_text='page limit', default=10)
    price = serializers.IntegerField(
        help_text='positive number = greater than,\
            negative number = less than', default=0)

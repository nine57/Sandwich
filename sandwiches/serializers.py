from django.db import transaction
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from sandwiches.models import Sandwich
from ingredients.models import Topping, Sauce


class SandwichSerializer(ModelSerializer):
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

        sandwich = Sandwich.objects.create(**validated_data)

        for topping in toppings:
            if Topping.in_stock == 0:
                raise serializers.ValidationError(
                    f"topping id {topping.id} is out of stock")
            sandwich.toppings.add(topping)

        for sauce in sauces:
            if Sauce.in_stock == 0:
                raise serializers.ValidationError(
                    f"sauce id {sauce.id} is out of stock")
            sandwich.sauces.add(sauce)

        return sandwich

    class Meta:
        model = Sandwich
        fields = "__all__"

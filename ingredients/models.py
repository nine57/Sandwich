from django.db import models


class Bread(models.Model):
    name = models.CharField(max_length=100)
    in_stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "breads"


class Topping(models.Model):
    name = models.CharField(max_length=100)
    in_stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "toppings"


class Cheese(models.Model):
    name = models.CharField(max_length=100)
    in_stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "cheeses"


class Sauce(models.Model):
    name = models.CharField(max_length=100)
    in_stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "Sauces"

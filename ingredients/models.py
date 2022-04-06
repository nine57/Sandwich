from django.db import models

STATUS_TYPES = [
    ("in_use", "in_use"),
    ("deleted", "deleted")
]


class Bread(models.Model):
    name = models.CharField(max_length=255)
    in_stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    status = models.CharField(
        max_length=50, choices=STATUS_TYPES, default="in_use")

    class Meta:
        db_table = "breads"


class Topping(models.Model):
    name = models.CharField(max_length=255)
    in_stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    status = models.CharField(
        max_length=50, choices=STATUS_TYPES, default="in_use")

    class Meta:
        db_table = "toppings"


class Cheese(models.Model):
    name = models.CharField(max_length=255)
    in_stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    status = models.CharField(
        max_length=50, choices=STATUS_TYPES, default="in_use")

    class Meta:
        db_table = "cheeses"


class Sauce(models.Model):
    name = models.CharField(max_length=255)
    in_stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    status = models.CharField(
        max_length=50, choices=STATUS_TYPES, default="in_use")

    class Meta:
        db_table = "sauces"

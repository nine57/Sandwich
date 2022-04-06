from django.db import models

STATUS_TYPES = [
    ("in_use", "in_use"),
    ("deleted", "deleted")
]


class Sandwich(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=50, choices=STATUS_TYPES, default="in_use")
    bread = models.ForeignKey('ingredients.Bread', on_delete=models.PROTECT)
    cheese = models.ForeignKey('ingredients.Cheese', on_delete=models.PROTECT)
    toppings = models.ManyToManyField(
        'ingredients.Topping', related_name='sandwiches')
    sauces = models.ManyToManyField(
        'ingredients.Sauce', related_name='sandwiches')

    class Meta:
        db_table = "sandwiches"

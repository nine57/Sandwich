from django.urls import path

from ingredients.views import (
    BreadView,
    BreadListView,
    ToppingView,
    ToppingListView,
    CheeseView,
    CheeseListView,
    SauceView,
    SauceListView)

urlpatterns = [
    path('/breads', BreadListView.as_view()),
    path('/bread/<int:bread_id>', BreadView.as_view()),
    path('/toppings', ToppingListView.as_view()),
    path('/topping/<int:topping_id>', ToppingView.as_view()),
    path('/cheeses', CheeseListView.as_view()),
    path('/cheese/<int:cheese_id>', CheeseView.as_view()),
    path('/sauces', SauceListView.as_view()),
    path('/sauce/<int:sauce_id>', SauceView.as_view()),
]

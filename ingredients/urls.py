from django.urls import path

from ingredients.views import BreadView, BreadListView

urlpatterns = [
    path('/breads', BreadListView.as_view()),
    path('/bread/<int:bread_id>', BreadView.as_view()),
]

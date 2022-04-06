from django.urls import path

from sandwiches.views import SandwichListView, SandwichView

urlpatterns = [
    path('', SandwichListView.as_view()),
    path('/<int:sandwich_id>', SandwichView.as_view()),
]

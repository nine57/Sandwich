from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ingredients', include('ingredients.urls')),
    path('admin/', admin.site.urls),
]

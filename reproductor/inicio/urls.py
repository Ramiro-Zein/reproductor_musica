from django.urls import path
from . import views

# Las '' indican la ruta principal

urlpatterns = [
    path('', views.inicio),
]

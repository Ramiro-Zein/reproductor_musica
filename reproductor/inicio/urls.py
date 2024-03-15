from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cancion/<int:id_cancion>/', views.cancion, name='cancion'),
    path('playlist/', views.playlist, name='playlist')
]

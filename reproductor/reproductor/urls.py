from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from . import views

# Variable que detecta las rutas a las cuales se van a acceder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('inicio.urls')),
    path('', RedirectView.as_view(url='/inicio/', permanent=True))
]

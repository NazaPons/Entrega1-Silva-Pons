from django.urls import path
from ProyectoDesblog.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('remeras/', remeras, name="Remeras"),
    path('buzos', buzos, name="Buzos"),
    path('pantalones', pantalones, name="Pantalones"),
    path('api_usuarios/', api_usuarios),
    path('buscar_usuario/', buscar_usuario),
]
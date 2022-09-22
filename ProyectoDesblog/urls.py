from django.urls import path
from ProyectoDesblog.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('remeras/', remeras, name="Remeras"),
    path('buzos/', buzos, name="Buzos"),
    path('pantalones/', pantalones, name="Pantalones"),
    path('api_usuarios/', api_usuarios),
    path('api_buzos/', api_buzos),
    path('api_remeras/', api_remeras),
    path('api_pantalones/', api_pantalones),
    path('buscar_usuario/', buscar_usuario),
    path('buscar_pantalon/', buscar_pantalon),
    path('buscar_remera/', buscar_remera),
    path('buscar_buzo/', buscar_buzo),


]
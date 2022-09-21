from django.urls import path
from ProyectoDesblog.views import *

urlpatterns = [
    path('', inicio),
    path('remeras/', remeras),
    path('buzos', buzos),
    path('pantalones', pantalones),
]
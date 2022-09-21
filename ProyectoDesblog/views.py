from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return render(request, "inicio.html")

def remeras(request):
    return render(request, "remeras.html")

def buzos(request):
    return render(request, "buzos.html")

def pantalones(request):
    return render(request, "pantalones.html")
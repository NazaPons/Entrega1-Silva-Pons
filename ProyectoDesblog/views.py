from django.shortcuts import render
from django.http import HttpResponse
from ProyectoDesblog.models import Buzo, Pantalon, Remera, Usuario
from ProyectoDesblog.forms import form_buzos, form_pantalones, form_remeras, form_usuarios
# Create your views here.


def inicio(request):
    if request.method == "POST":
        usuario = Usuario(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
        usuario.save()
    return render(request, "inicio.html")

def remeras(request):
    if request.method == "POST":
        remera = Remera(color = request.POST['color'], talle = request.POST['talle'], marca = request.POST['marca'])
        remera.save()
    return render(request, "remeras.html")

def buzos(request):
    if request.method == "POST":
        buzo = Buzo(color = request.POST['color'], talle = request.POST['talle'], marca = request.POST['marca'])
        buzo.save()
    return render(request, "buzos.html")

def pantalones(request):
    if request.method == "POST":
        pantalon = Pantalon(color = request.POST['color'], talle = request.POST['talle'], marca = request.POST['marca'])
        pantalon.save()
    return render(request, "pantalones.html")

def api_usuarios(request):
    if request.method == "POST":
        formulario = form_usuarios(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = Usuario(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])
            usuario.save()
            return render(request, "api_usuarios.html")
    else:
            formulario = form_usuarios()
    return render(request, "api_usuarios.html", {"formulario": formulario})

def api_buzos(request):
    if request.method == "POST":
        formulario = form_buzos(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            buzo = Buzo(color = informacion['color'], talle = informacion['talle'], marca = informacion['marca'])
            buzo.save()
            return render(request, "api_buzos.html")
    else:
            formulario = form_buzos()
    return render(request, "api_buzos.html", {"formulario": formulario})

def api_pantalones(request):
    if request.method == "POST":
        formulario = form_pantalones(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            pantalon = Pantalon(color = informacion['color'], talle = informacion['talle'], marca = informacion['marca'])
            pantalon.save()
            return render(request, "api_pantalones.html")
    else:
            formulario = form_pantalones()
    return render(request, "api_pantalones.html", {"formulario": formulario})

def api_remeras(request):
    if request.method == "POST":
        formulario = form_remeras(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            remera = Remera(color = informacion['color'], talle = informacion['talle'], marca = informacion['marca'])
            remera.save()
            return render(request, "api_remeras.html")
    else:
            formulario = form_remeras()
    return render(request, "api_remeras.html", {"formulario": formulario})


def buscar_usuario(request):
    if request.GET["email"]:
        email = request.GET["email"]
        usuarios = Usuario.objects.filter(email__icontains = email)
        return render(request, "inicio.html", {"usuarios" : usuarios})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def buscar_buzo(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        buzos = Buzo.objects.filter(marca__icontains = marca)
        return render(request, "buzos.html", {"buzos" : buzos})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def buscar_pantalon(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        pantalones = Pantalon.objects.filter(marca__icontains = marca)
        return render(request, "pantalones.html", {"pantalones" : pantalones})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def buscar_remera(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        remeras = Remera.objects.filter(marca__icontains = marca)
        return render(request, "remeras.html", {"remeras" : remeras})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)



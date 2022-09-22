from django.shortcuts import render
from django.http import HttpResponse
from ProyectoDesblog.models import Usuario
from ProyectoDesblog.forms import form_usuarios
# Create your views here.


def inicio(request):
    if request.method == "POST":
        usuario = Usuario(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
        usuario.save()
    return render(request, "inicio.html")

def remeras(request):
    return render(request, "remeras.html")

def buzos(request):
    return render(request, "buzos.html")

def pantalones(request):
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

def buscar_usuario(request):
    if request.GET["email"]:
        email = request.GET["email"]
        usuarios = Usuario.objects.filter(email__icontains = email)
        return render(request, "inicio.html", {"usuarios" : usuarios})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

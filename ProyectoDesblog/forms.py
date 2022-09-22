from django import forms

class form_usuarios(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class form_remeras(forms.Form):
    color: forms.CharField(max_length=40)
    talle: forms.CharField(max_length=40)
    marca: forms.CharField(max_length=40)

class form_pantalones(forms.Form):
    color: forms.CharField(max_length=40)
    talle: forms.CharField(max_length=40)
    marca: forms.CharField(max_length=40)

class form_buzos(forms.Form):
    color: forms.CharField(max_length=40)
    talle: forms.CharField(max_length=40)
    marca: forms.CharField(max_length=40)
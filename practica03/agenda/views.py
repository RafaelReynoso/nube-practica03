from django.shortcuts import render, redirect
from .models import *

def home(request):
    contactoListado = Contacto.objects.all()
    
    return render(request, "gestionContacto.html", {"contacto": contactoListado})

def registrarContacto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellidos = request.POST['txtApellido']
    email = request.POST['txtEmail']
    fecha_nacimiento = request.POST['txtFecha_nacimiento']
    
    foto = request.FILES.get('foto')
    
    contacto = Contacto.objects.create(
            codigo=codigo,
            nombre=nombre,
            apellidos=apellidos,
            fecha_nacimiento=fecha_nacimiento,
            email=email,
            foto=foto
        )

    return redirect('/')

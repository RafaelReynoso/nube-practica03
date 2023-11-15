from django.db import models

class Contacto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/')

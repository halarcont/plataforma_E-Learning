from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

class MaterialDeEstudio(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200) # Ej: 'video', 'pdf', etc.
    url = models.URLField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Examen(models.Model):
    nombre = models.CharField(max_length=200)
    preguntas = models.TextField() # Esto podría ser un campo JSON
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class RespuestaDelEstudiante(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    respuestas = models.TextField()  # Esto podría ser un campo JSON

    



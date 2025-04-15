import datetime

from django.db import models
from django.utils import timezone

class Encuesta(models.Model):
    texto_encuesta = models.CharField(max_length=200)
    fecha_publ = models.DateTimeField("fecha de publicacion")
    def __str__(self):
        return self.texto_encuesta
    def fue_publicado_recientemente(self):
        return self.fecha_publ >= timezone.now() - datetime.timedelta(days=1)

class Respuesta(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    texto_respuesta = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.texto_respuesta

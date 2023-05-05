from django.db import models


# Create your models here.
class Prompt(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre_contexto = models.CharField(max_length=50, null=True, unique=True)
    tipo = models.CharField(max_length=50, null=False, unique=True)
    contenido = models.CharField(max_length=550, null=False, unique=True)

    def __str__(self):
        return self.nombre_contexto

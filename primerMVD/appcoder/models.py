from django.db import models

# Create your models here.


class familiares(models.Model):
    nombre = models.CharField(max_length=30)
    suerte = models.IntegerField()
    nacimiento = models.DateField()


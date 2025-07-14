from django.db import models
from datetime import date

# Create your models here.


class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name="Nombre")
    description = models.TextField(max_length=300, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    date = models.DateField(default=date.today, verbose_name="Fecha")
    photo = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="Foto")

    
    def __str__(self):
        return self.name

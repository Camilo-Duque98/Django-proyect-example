from django.db import models
from django.utils import timezone

# Create your models here.
class CategoriaBooks(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.nombre

class ProductoBooks(models.Model):
    nombre = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    categoria = models.ForeignKey(
        CategoriaBooks,
        on_delete=models.CASCADE
    )
    creado_en = models.DateTimeField(default = timezone.now)
    
    def __str__(self) -> str:
        return self.nombre
    
    def __str__(self) -> str:
        return self.autor
    
from django.db import models
from django.utils import timezone

# Create your models here.  

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # ALTERNATIVAS PARA CUANDO SE ELIMINA UN PRODUCTO, on_delete ->
    # Es un metodo estatico de la clase models 
    # CASCADE: eliminar el producto
    # PROTECT: lanza un error, no deja eliminar la categoría
    # RESTRICT: no deja eliminar la categoría, al menos que se hayan eliminado todos los productos
    # SET_NULL: mapea un valor nulo dentro de la categoria
    # SET_DEFAULT: asigna valor por defecto
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.nombre
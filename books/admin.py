from django.contrib import admin
from .models import CategoriaBooks, ProductoBooks

# Register your models here.
class CategoriaBooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    
class ProductoBooksAdmin(admin.ModelAdmin):
    exclude = ('creado_en',)
    list_display = ('id', 'nombre', 'autor', 'stock', 'puntaje', 'categoria','creado_en')
    
admin.site.register(CategoriaBooks, CategoriaBooksAdmin)
admin.site.register(ProductoBooks, ProductoBooksAdmin)
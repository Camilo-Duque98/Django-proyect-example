from . import models
from django.forms import ModelForm

class ProductoBooksForm(ModelForm):
    class Meta:
        model = models.ProductoBooks
        fields = ["nombre","autor","stock","puntaje","categoria"]
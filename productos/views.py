from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Producto
from .forms import ProductoForm
# Create your views here.
# /productos
def index(request):
    # productos = Producto.objects.all().values()
    productos = Producto.objects.all()
    # productos = Producto.objects.filter(puntaje=3)
    # productos = Producto.objects.get(pk=1)
    return render(
        request = request,
        template_name = 'index.html',
        context={'productos':productos}  
    )
    # return HttpResponse(list(productos))
    
def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    # producto = Producto.objects.get(id=producto_id)
    return render(
        request, 
        'detalle.html', 
        context={'producto': producto}
        )
    
def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()
    
    return render(
        request,
        'producto_form.html',
        {'form': form}    
    )
        
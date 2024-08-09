from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import ProductoBooks
from .forms import ProductoBooksForm
# Create your views here.
def index(request):
    books = ProductoBooks.objects.all()
    print(books)
    return render(
        request=request,
        template_name='index2.html',
        context={'books':books}
    )
    
def formulario_books(request):
    if request.method == 'POST':
        form = ProductoBooksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books')
    else:
        form = ProductoBooksForm()
    return render(
        request,
        'books_form.html',
        {'form':form}
    )        
        
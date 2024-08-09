from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('',views.index, name='index'),
    path('formulario', views.formulario_books, name='formulario')
]

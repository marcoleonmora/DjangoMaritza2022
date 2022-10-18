from django.shortcuts import render
from .models import *

# Create your views here.
def listarProductos(request):
    #consultar los productos
    listaProductos = Producto.objects.all().values('nombreProd', 'icono')
    #crear el context
    context = {
        'tituloPag': 'Productos',
        'tituloPlantilla': 'Listado de Productos',
        'productos':  listaProductos,      
    }
    #renderizar
    return render(request, 'listaProductos.html', context)

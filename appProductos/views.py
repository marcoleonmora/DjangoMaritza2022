from asyncio.windows_events import NULL
from django.shortcuts import render
from django.db.models import Count
from .models import *

# Create your views here.
def listarCategorias(request):
    #listaCateg = Categoria.objects.all()
    listaCateg = Producto.objects.select_related('categoria').values('categoria__pk', 'categoria__nombreCat').annotate(cantidad=Count('id'))

    #crear context
    context = {
        'titulo': 'Lista de Categorias',
        'categorias': listaCateg,
    }
    #renderizar
    print('----------------')
    print(context)
    return render(request, 'categorias.html', context)


def listarProductos(request):
    #consultar los productos
    listaProductos = Producto.objects.all()
    #crear el context
    context = {
        'tituloPag': 'Productos',
        'tituloPlantilla': 'Listado de Productos',
        'productos':  listaProductos,      
    }
    #renderizar

    return render(request, 'listaProductos.html', context)



def listarProductosCategoria(request, idCateg):
    #consultar los productos
    regCateg = Categoria.objects.get(id=idCateg)
    listaProductos = Producto.objects.filter(categoria = regCateg)
    #crear el contextidCateg
    context = {
        'tituloPag': 'Productos',
        'tituloPlantilla': 'Listado de Productos de ' + regCateg.nombreCat,
        'productos':  listaProductos,      
    }

    return render(request, 'listaProductos.html', context)

#*******************************************************************
def verProducto(request, idProd):
    #Consultar producto en BD
    regProducto = Producto.objects.get(id=idProd)

    #crear context
    context = {
        'titulo': 'Detalle del Producto',
        'producto': regProducto,
    }
    #renderizar
    return render(request, 'producto.html', context)

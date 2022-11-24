from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.db.models import Count
from .models import *

from django.contrib import auth
from django.contrib.auth.decorators import login_required


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


#******** CONTROL DE INGRESO DE USUARIOS  ***********************************************************
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print('---------------')
        print(email, '--', password)
        user = auth.authenticate(username= email, password = password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'login.html', {'alarma': 'Correo o password no valido!'})

    else:
        return render(request, 'login.html')    

#********* DESACTIVACION DEL USUARIO **********************************************************
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
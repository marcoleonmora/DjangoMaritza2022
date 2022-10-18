from django.shortcuts import render


"""
    Funcion para renderizar la página de inicio
"""
def home(request):
    context = {
        'tituloPag': 'SuperMarket',
    }
    return render(request, 'home.html', context)

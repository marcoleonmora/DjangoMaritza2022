from django.shortcuts import render


"""
    Funcion para renderizar la página de inicio
"""
def home(request):
    return render(request, 'home.html')

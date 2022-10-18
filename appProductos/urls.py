
from django.urls import path, include
from . import views


urlpatterns = [
    path('productos/', views.listarProductos, name='productos'),
 
]
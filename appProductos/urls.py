
from django.urls import path, include
from . import views


urlpatterns = [
    path('productos/', views.listarProductos, name='productos'),
    path('producto/<int:idProd>', views.verProducto, name='unproducto'),
    path('categorias/', views.listarCategorias, name='categorias'),
    path('productos_categ/<int:idCateg>', views.listarProductosCategoria, name='productos_categ'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]


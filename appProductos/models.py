from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombreCat= models.CharField(max_length=100, null= False)

    def __str__(self):
        return self.nombreCat

class Producto(models.Model):
    nombreProd = models.CharField(max_length=100, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    descripProd = models.CharField(max_length=300, null=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    unidad = models.CharField(max_length=10, null=False)
    imagen = models.ImageField(upload_to='productos', null=True)
    icono = models.ImageField(upload_to='iconos', null=True)

    def __str__(self):
        return self.nombreProd


from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="imgprod",blank=False, null=True)

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    SKU = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to="imgprod",blank=False, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.nombre}, de SKU {self.SKU}, de valor {self.precio}, con stock {self.stock}' 


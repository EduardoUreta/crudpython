from django.db import models

from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from api.models import Productos

class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendedor")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=18)

    def __str__(self):
        return f'Vendedor - Nombre: {self.nombre}\nApellido: {self.apellido}'

class Comprador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="comprador")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=18)

    def __str__(self):
        return f'Comprador - Nombre: {self.nombre}\nApellido: {self.apellido}'

class Venta(models.Model):
    idventa = models.IntegerField(primary_key=True)
    comprador = models.ForeignKey(Comprador, related_name='comprador', on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, related_name='vendedor', on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.DO_NOTHING)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)
    cantidad = models.PositiveIntegerField()
    precio_total = models.PositiveIntegerField(editable=False)

    def __str__(self):
        return f'El {self.producto.nombre} del dueño {self.vendedor} fue vendido a {self.comprador} por ${self.producto.precio}'
    
    class Meta:
        ordering = ("-fecha_venta",)
    
    def clean(self) -> None:
        if self.cantidad > self.producto.stock:
            raise ValidationError("La cantidad solicitada es mayor al stock disponible")
        
    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)



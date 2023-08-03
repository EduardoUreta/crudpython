from django.contrib import admin
from .models import Comprador, Vendedor, Venta

admin.site.register(Comprador)
admin.site.register(Vendedor)
admin.site.register(Venta)
from django.contrib import admin
from .models import Productos, Categoria

admin.site.register(Productos)
admin.site.register(Categoria)

admin.site.site_header = "Panel Administrativo | La Vecindad"
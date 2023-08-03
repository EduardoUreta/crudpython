from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import Productos, Categoria


class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
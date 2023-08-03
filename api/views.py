from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from api.models import Productos, Categoria
from api.serializers import ProductosSerializer, CategoriaSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]
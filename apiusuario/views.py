from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from apiusuario.models import Comprador, Vendedor, Venta
from apiusuario.serializers import CompradorSerializer, VendedorSerializer, VentaSerializer

class CompradorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Comprador.objects.all()
    serializer_class = CompradorSerializer
    permission_classes = [permissions.IsAuthenticated]

class VendedorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    permission_classes = [permissions.IsAuthenticated]

class VentaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [permissions.IsAuthenticated]
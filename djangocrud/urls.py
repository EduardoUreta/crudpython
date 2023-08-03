from django.contrib import admin
from django.urls import path

from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'productos', views.ProductosViewSet)
router.register(r'categoria', views.CategoriaViewSet)

from apiusuario import views
router.register(r'comprador', views.CompradorViewSet)
router.register(r'vendedor', views.VendedorViewSet)
router.register(r'venta', views.VentaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

from django.conf import settings
from django.conf.urls.static import static

# Añadir esta línea al final para servir las imágenes en desarrollo.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

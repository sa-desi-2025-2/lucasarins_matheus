
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from maintence.views import AlertasViewSet ,AtivosViewSet, CategoriaativosViewSet, UsuariosViewSet

router = DefaultRouter()
router.register(r'alertas', AlertasViewSet)
router.register(r'ativos', AtivosViewSet)
router.register(r'categoriaativos', CategoriaativosViewSet)
router.register(r'usuarios', UsuariosViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

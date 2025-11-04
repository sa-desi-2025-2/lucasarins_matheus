from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from maintence.views import (
    AlertasViewSet,
    AtivosViewSet,
    CategoriaativosViewSet,
    FornecedoresViewSet,
    LogAuditoriasViewSet,
    UsuariosViewSet,
    cadastro,  
)

router = DefaultRouter()
router.register(r'alertas', AlertasViewSet)
router.register(r'ativos', AtivosViewSet)
router.register(r'categoriaativos', CategoriaativosViewSet)
router.register(r'fornecedores', FornecedoresViewSet)
router.register(r'logauditorias', LogAuditoriasViewSet)
router.register(r'usuarios', UsuariosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cadastro/', cadastro, name='cadastro'),  
]

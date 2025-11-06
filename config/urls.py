from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from maintence.views import (
    AlertasViewSet,
    AtivosViewSet,
    CategoriaativosViewSet,
    FornecedoresViewSet,
    ItensViewSet,
    ItensReparoViewSet,
    LogAuditoriasViewSet,
    ReparosViewSet,
    UsuariosViewSet,
    cadastro,  
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'alertas', AlertasViewSet)
router.register(r'ativos', AtivosViewSet)
router.register(r'categoriaativos', CategoriaativosViewSet)
router.register(r'fornecedores', FornecedoresViewSet)
router.register(r'itens', ItensViewSet)
router.register(r'logauditorias', LogAuditoriasViewSet)
router.register(r'reparos', ReparosViewSet)
router.register(r'usuarios', UsuariosViewSet)
router.register(r'itensreparo', ItensReparoViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cadastro/', cadastro, name='cadastro'),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

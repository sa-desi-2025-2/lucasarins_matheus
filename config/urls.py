from django.contrib import admin
from django.urls import path, include
from maintence.views import (
    AlertasViewSet,
    AtivosViewSet,
    CategoriaativosViewSet,
    FornecedoresViewSet,
    LogAuditoriasViewSet,
    ReparosViewSet,
    UsuariosViewSet,
    ItensReparoViewSet,
    cadastro,
    ReparosCSVExportView,
)
from maintence.views.ativos import dashboard  

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter
from maintence.views.reparos import exportar_reparos_pdf


router = DefaultRouter()
router.register(r'alertas', AlertasViewSet)
router.register(r'ativos', AtivosViewSet)
router.register(r'categoriasativos', CategoriaativosViewSet)
router.register(r'fornecedores', FornecedoresViewSet)
router.register(r'logauditorias', LogAuditoriasViewSet)
router.register(r'reparos', ReparosViewSet)
router.register(r'usuarios', UsuariosViewSet)
router.register(r'itensreparo', ItensReparoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cadastro/', cadastro, name='cadastro'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('dashboard/', dashboard, name='dashboard'),
    path('exportar/csv/reparos/', ReparosCSVExportView.as_view()),
    path('exportar/pdf/reparos/', exportar_reparos_pdf),


]
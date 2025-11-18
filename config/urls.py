from django.contrib import admin
from django.urls import path, include
from maintence.views import (


    # ViewSets da API (já existentes)
    AlertasViewSet, AtivosViewSet, CategoriaativosViewSet,
    FornecedoresViewSet, LogAuditoriasViewSet, ReparosViewSet,
    UsuariosViewSet, ItensReparoViewSet,
    
    # Views de Páginas Web (novas)
    login_view, logout_view, dashboard_view, ativos_view, ativos_criar,
    manutencao_view, reparos_criar, analise_roi_view, alertas_view, alertas_criar,
    cadastro_view, # Sua view de cadastro adaptada
)  


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

   
 
    path('exportar/csv/reparos/', ReparosCSVExportView.as_view()),
    path('exportar/pdf/reparos/', exportar_reparos_pdf),




    
    # 1. ROTAS DAS PÁGINAS WEB (DEVE VIR PRIMEIRO)
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('', dashboard_view, name='dashboard'), # <--- AGORA É A PRIMEIRA A SER VERIFICADA PARA '/'
    path('ativos/', ativos_view, name='ativos'),
    path('ativos/criar/', ativos_criar, name='ativos_criar'),
    path('manutencao/', manutencao_view, name='manutencao'),
    path('reparos/criar/', reparos_criar, name='reparos_criar'),
    path('analise-roi/', analise_roi_view, name='analise_roi'),
    path('alertas/', alertas_view, name='alertas_view'),
    path('alertas/criar/', alertas_criar, name='alertas_criar'),
    
    # 2. ROTAS DA API (DEVE VIR DEPOIS)
    path('api/', include(router.urls)), # <--- MUDANÇA: ADICIONE UM PREFIXO '/api/'
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


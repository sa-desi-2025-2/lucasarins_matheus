from django.contrib import admin
from django.urls import path, include
from maintence.views import (


    # ViewSets da API (já existentes)
    AlertasViewSet, AtivosViewSet, CategoriaativosViewSet,
    FornecedoresViewSet, LogAuditoriasViewSet, ReparosViewSet,
    UsuariosViewSet, ItensReparoViewSet,
    
    # Views de Páginas Web (novas)
    login_view, logout_view, dashboard_view, ativos_view, ativos_criar, ativos_excluir, ativos_editar, ativos_atualizar,
    manutencao_view, reparos_criar, analise_roi_view, alertas_view, alertas_criar,
    cadastro_view, # Sua view de cadastro adaptada
    alertas_editar, alertas_atualizar,
)  


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter
from maintence.views.reparos import exportar_reparos_pdf
from maintence.views.reparos import ReparosCSVExportView
from maintence.views.reparos import reparos_editar, reparos_atualizar, reparos_criar, reparos_listar
from maintence.views import reparos as reparos_views



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
    path('', dashboard_view, name='dashboard'), 
    path('ativos/', ativos_view, name='ativos'),
    path('ativos/criar/', ativos_criar, name='ativos_criar'),
    path('ativos/<int:id_ativo>/editar/', ativos_editar, name='ativos_editar'),
    path('ativos/<int:id_ativo>/atualizar/', ativos_atualizar, name='ativos_atualizar'),
    path('ativos/<int:id_ativo>/excluir/', ativos_excluir, name='ativos_excluir'),
    path('manutencao/', manutencao_view, name='manutencao'),
    path('analise-roi/', analise_roi_view, name='analise_roi'),
    path('alertas/', alertas_view, name='alertas_view'),
    path('alertas/criar/', alertas_criar, name='alertas_criar'),
    path('alertas/<int:id_alerta>/editar/', alertas_editar, name='alertas_editar'),
    path('alertas/<int:id_alerta>/atualizar/', alertas_atualizar, name='alertas_atualizar'),
    
    # 2. ROTAS DA API (DEVE VIR DEPOIS)
    path('api/', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('reparos/<int:id_reparo>/editar/', reparos_views.reparos_editar, name='reparos_editar'),
    path('reparos/<int:id_reparo>/atualizar/', reparos_views.reparos_atualizar, name='reparos_atualizar'),
    path('reparos/criar/', reparos_views.reparos_criar, name='reparos_criar'),
    path('reparos/', reparos_views.reparos_listar, name='reparos_listar'),
    path('reparos/<int:id_reparo>/excluir/', reparos_views.reparos_excluir, name='reparos_excluir')
]
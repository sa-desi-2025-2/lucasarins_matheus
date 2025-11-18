# /maintence/urls_web.py (novo)

from django.urls import path
from .views import auth, dashboard, ativos, manutencao, analise_roi, alertas_view, cadastro

urlpatterns = [
    # Autenticação
    path('login/', auth.login_view, name='login'),
    path('logout/', auth.logout_view, name='logout'),
    path('cadastro/', cadastro.cadastro_view, name='cadastro'), # Atualizar view existente

    # Páginas
    path('', dashboard.dashboard_view, name='dashboard'),
    path('ativos/', ativos.ativos_view, name='ativos'),
    path('ativos/criar/', ativos.ativos_criar, name='ativos_criar'),
    path('manutencao/', manutencao.manutencao_view, name='manutencao'),
    path('reparos/criar/', manutencao.reparos_criar, name='reparos_criar'),
    path('analise-roi/', analise_roi.analise_roi_view, name='analise_roi'),
    path('alertas/', alertas_view.alertas_view, name='alertas_view'),
    path('alertas/criar/', alertas_view.alertas_criar, name='alertas_criar'),
]
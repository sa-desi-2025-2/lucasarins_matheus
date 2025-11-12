# ... (imports de models e serializers existentes) ...

from maintence.views.alertas import AlertasViewSet
from maintence.views.ativos import AtivosViewSet
# ... (outros ViewSets existentes) ...
from maintence.views.usuarios import UsuariosViewSet

# NOVAS IMPORTAÇÕES DE VIEWS DE PÁGINA
from maintence.views.cadastro import cadastro as cadastro_view
from maintence.views.auth import login_view, logout_view
from maintence.views.dashboard import dashboard_view
from maintence.views.ativos import ativos_view, ativos_criar
from maintence.views.reparos import manutencao_view, reparos_criar
from maintence.views.alertas import alertas_view, alertas_criar
from maintence.views.analise_roi import analise_roi_view

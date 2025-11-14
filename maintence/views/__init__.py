from maintence.models import Alertas, Ativos, Categoriaativos, Fornecedores, Itens, ItensReparo, LogAuditorias, Reparos, Usuarios
from maintence.serializers import (
    AlertasSerializer,
    AtivosSerializer,
    CategoriaativosSerializer,
    FornecedoresSerializer,
    ItensSerializer,
    ItensReparoSerializer,
    LogAuditoriasSerializer,
    ReparosSerializer,
    UsuariosSerializer,
)
from maintence.views.alertas import AlertasViewSet
from maintence.views.ativos import AtivosViewSet
from maintence.views.categoriaativos import CategoriaativosViewSet
from maintence.views.fornecedores import FornecedoresViewSet
from maintence.views.itens import ItensViewSet
from maintence.views.itensreparo import ItensReparoViewSet
from maintence.views.logauditorias import LogAuditoriasViewSet
from maintence.views.reparos import ReparosViewSet
from maintence.views.usuarios import UsuariosViewSet
from maintence.views.cadastro import cadastro
from maintence.views.reparos import ReparosCSVExportView

from rest_framework.viewsets import ModelViewSet
from maintence.models import Alertas, Ativos, Categoriaativos, Usuarios
from maintence.serializers import AlertasSerializer, AtivosSerializer, CategoriaativosSerializer, UsuariosSerializer

class AlertasViewSet(ModelViewSet):
    queryset = Alertas.objects.all()
    serializer_class = AlertasSerializer

class AtivosViewSet(ModelViewSet):
    queryset = Ativos.objects.all()
    serializer_class = AtivosSerializer
class CategoriaativosViewSet(ModelViewSet):
    queryset = Categoriaativos.objects.all()
    serializer_class = CategoriaativosSerializer

class UsuariosViewSet(ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

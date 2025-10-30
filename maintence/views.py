from rest_framework.viewsets import ModelViewSet
from maintence.models import Alertas, Ativos, Categoriaativos
from maintence.serializers import AlertasSerializer, AtivosSerializer, CategoriaativosSerializer

class AtivosViewSet(ModelViewSet):
    queryset = Ativos.objects.all()
    serializer_class = AtivosSerializer
class CategoriaativosViewSet(ModelViewSet):
    queryset = Categoriaativos.objects.all()
    serializer_class = CategoriaativosSerializer


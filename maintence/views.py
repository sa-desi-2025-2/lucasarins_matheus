from rest_framework.viewsets import ModelViewSet
from maintence.models import Ativos, Categoriaativos
from maintence.serializers import AtivosSerializer, CategoriaativosSerializer

class AtivosViewSet(ModelViewSet):
    queryset = Ativos.objects.all()
    serializer_class = AtivosSerializer
class CategoriaativosViewSet(ModelViewSet):
    queryset = Categoriaativos.objects.all()
    serializer_class = CategoriaativosSerializer


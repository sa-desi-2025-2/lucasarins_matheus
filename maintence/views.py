from rest_framework.viewsets import ModelViewSet
from maintence.models import Categoriaativos
from maintence.serializers import CategoriaativosSerializer

class CategoriaativosViewSet(ModelViewSet):
    queryset = Categoriaativos.objects.all()
    serializer_class = CategoriaativosSerializer
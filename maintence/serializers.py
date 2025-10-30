from rest_framework.serializers import ModelSerializer
from maintence.models import Categoriaativos

class CategoriaativosSerializer(ModelSerializer):
    class Meta:
        model = Categoriaativos
        fields = '__all__'

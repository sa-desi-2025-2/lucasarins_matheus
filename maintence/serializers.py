from rest_framework.serializers import ModelSerializer
from maintence.models import Alertas, Ativos, Categoriaativos


class AlertasSerializer(ModelSerializer):
    class Meta:
        model = Alertas
        fields = '__all__'

class AtivosSerializer(ModelSerializer):
    class Meta:
        model = Ativos
        fields = '__all__'
class CategoriaativosSerializer(ModelSerializer):
    class Meta:
        model = Categoriaativos
        fields = '__all__'

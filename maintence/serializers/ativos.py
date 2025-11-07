from rest_framework.serializers import ModelSerializer
from maintence.models.ativos import Ativos

class AtivosSerializer(ModelSerializer):
    class Meta:
        model = Ativos
        fields = '__all__'
from rest_framework.serializers import ModelSerializer
from maintence.models.ativos import Ativos
from maintence.serializers.reparos import ReparosSerializer 

class AtivosSerializer(ModelSerializer):
    reparos = ReparosSerializer(many=True, read_only=True)

    class Meta:
        model = Ativos
        fields = '__all__'
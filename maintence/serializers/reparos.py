from rest_framework.serializers import ModelSerializer
from maintence.models.reparos import Reparos

class ReparosSerializer(ModelSerializer):
    class Meta:
        model = Reparos
        fields = '__all__'

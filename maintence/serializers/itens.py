from rest_framework.serializers import ModelSerializer
from maintence.models.itens import Itens

class ItensSerializer(ModelSerializer):
    class Meta:
        model = Itens
        fields = '__all__'

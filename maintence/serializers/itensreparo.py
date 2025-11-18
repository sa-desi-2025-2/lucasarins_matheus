from rest_framework.serializers import ModelSerializer
from maintence.models.itensreparo import ItensReparo

class ItensReparoSerializer(ModelSerializer):
    class Meta:
        model = ItensReparo
        fields = '__all__'

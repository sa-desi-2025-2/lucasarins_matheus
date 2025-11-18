from rest_framework.serializers import ModelSerializer
from maintence.models.fornecedores import Fornecedores

class FornecedoresSerializer(ModelSerializer):
    class Meta:
        model = Fornecedores
        fields = '__all__'

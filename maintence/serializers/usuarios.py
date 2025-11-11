from rest_framework.serializers import ModelSerializer
from maintence.models.usuarios import Usuarios

class UsuariosSerializer(ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
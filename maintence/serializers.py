from rest_framework.serializers import ModelSerializer
from maintence.models import Alertas, Ativos, Categoriaativos, Fornecedores, Itens, LogAuditorias, Reparos, Usuarios


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

class FornecedoresSerializer(ModelSerializer):
    class Meta:
        model = Fornecedores
        fields = '__all__'

class ItensSerializer(ModelSerializer):
    class Meta:
        model = Itens
        fields = '__all__'

class LogAuditoriasSerializer(ModelSerializer):
    class Meta:
        model = LogAuditorias
        fields = '__all__'   

class ReparosSerializer(ModelSerializer):
    class Meta:
        model = Reparos
        fields = '__all__'


class UsuariosSerializer(ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
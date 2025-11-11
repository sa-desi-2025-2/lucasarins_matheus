from rest_framework.serializers import ModelSerializer
from maintence.models.logauditorias import LogAuditorias
from maintence.models import ItensReparo


class LogAuditoriasSerializer(ModelSerializer):
    class Meta:
        model = LogAuditorias
        fields = '__all__'   

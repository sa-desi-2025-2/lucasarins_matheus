from rest_framework.serializers import ModelSerializer
from maintence.models.alertas import Alertas

class AlertasSerializer(ModelSerializer):
    class Meta:
        model = Alertas
        fields = '__all__'

from rest_framework import serializers  
from rest_framework.serializers import ModelSerializer
from maintence.models.reparos import Reparos


class ReparosSerializer(ModelSerializer):
    roi_calculado = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    custo_total = serializers.SerializerMethodField()

    class Meta:
        model = Reparos
        fields = [
            'id_usuario',
            'roi_calculado',
            'custo_total',
            'id_reparo',
            'id_ativo',
            'data_reparo',
            'tipo',
            'descricao',
            'tempo_parada_hora',
            'extensao_vida_util',
            'unid_extensao_vida_util',
            'custo_total_peca',
            'anexos',
            'custo_mao_obra',
        ]

    def get_custo_total(self, obj):
        return obj.custo_total()
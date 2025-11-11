# maintence/views/ativos.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes  # ✅ IMPORT
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from maintence.models.ativos import Ativos
from maintence.serializers.ativos import AtivosSerializer

class AtivosViewSet(ModelViewSet):
    queryset = Ativos.objects.all()
    serializer_class = AtivosSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    total_reparos = Reparos.objects.count()
    custo_total = Reparos.objects.aggregate(total=Sum('custo_total_peca'))['total'] or 0
    roi_medio = Reparos.objects.aggregate(avg_roi=Avg('roi_calculado'))['avg_roi'] or 0
    ativos_mais_caro = Ativos.objects.annotate(total_gasto=Sum('reparos__custo_total_peca')).order_by('-total_gasto')[:5]
    ativos_list = [{'id': a.id_ativo, 'nome': a.nome, 'total_gasto': float(a.total_gasto or 0)} for a in ativos_mais_caro]

    return Response({
        'total_reparos': total_reparos,
        'custo_total': float(custo_total),
        'roi_medio': float(round(roi_medio,2)),
        'ativos_mais_gastos': ativos_list,
    })
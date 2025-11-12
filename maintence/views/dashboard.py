from django.shortcuts import render
from maintence.models import Ativos, Reparos, Alertas
from django.db.models import Sum, Avg
from django.db.models.functions import Coalesce

def dashboard_view(request):
    # Simulação de dados para o dashboard
    total_ativos = Ativos.objects.count()
    total_reparos = Reparos.objects.count()
    
    # Coalesce(None, 0) garante que se o resultado for None (sem reparos), ele retorna 0
    custo_total = Reparos.objects.aggregate(total=Coalesce(Sum('custo_total_peca'), 0))['total']
    roi_medio = Reparos.objects.aggregate(avg_roi=Coalesce(Avg('roi_calculado'), 0))['avg_roi']
    
    ultimos_reparos = Reparos.objects.order_by('-data_reparo')[:5]
    alertas_recentes = Alertas.objects.order_by('-data_criacao')[:5]
    
    # Dados para gráficos (exemplo)
    ativos_gastos_query = Ativos.objects.annotate(total_gasto=Coalesce(Sum('reparos__custo_total_peca'), 0)).order_by('-total_gasto')[:5]
    ativos_labels = [a.nome for a in ativos_gastos_query]
    ativos_gastos = [float(a.total_gasto) for a in ativos_gastos_query]
    
    # Simulação de dados para ROI por Ativo (para o gráfico)
    roi_labels = ['Ativo A', 'Ativo B', 'Ativo C', 'Ativo D', 'Ativo E']
    roi_valores = [15.5, -5.2, 20.0, 8.1, -1.0]

    context = {
        'total_ativos': total_ativos,
        'total_reparos': total_reparos,
        'custo_total': custo_total,
        'roi_medio': roi_medio,
        'ultimos_reparos': ultimos_reparos,
        'alertas_recentes': alertas_recentes,
        'ativos_labels': ativos_labels,
        'ativos_gastos': ativos_gastos,
        'roi_labels': roi_labels,
        'roi_valores': roi_valores,
    }
    return render(request, 'maintence/dashboard.html', context)

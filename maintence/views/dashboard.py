from django.shortcuts import render # <--- CORREÇÃO APLICADA
from maintence.models import Ativos, Reparos, Alertas
from django.db.models import Sum, Avg, DecimalField, Value # Importações necessárias
from django.db.models.functions import Coalesce

def dashboard_view(request):
    # Dados para o dashboard (agora reais do banco de dados)
    total_ativos = Ativos.objects.count()
    total_reparos = Reparos.objects.count()
    
    # 1. CORREÇÃO: Usando Value e DecimalField para evitar o erro de tipos mistos
    
    # Corrigindo o custo total
    custo_total = Reparos.objects.aggregate(
        total=Coalesce(
            Sum('custo_total_peca'), 
            Value(0.0, output_field=DecimalField())
        )
    )['total']
    
    # Corrigindo o ROI médio
    roi_medio = Reparos.objects.aggregate(
        avg_roi=Coalesce(
            Avg('roi_calculado'), 
            Value(0.0, output_field=DecimalField())
        )
    )['avg_roi']
    
    ultimos_reparos = Reparos.objects.order_by('-data_reparo')[:5]
    alertas_recentes = Alertas.objects.order_by('-data_criacao')[:5]
    
    # 2. CORREÇÃO: Aplicando a mesma correção para a agregação de gastos por ativo
    ativos_gastos_query = Ativos.objects.annotate(
        total_gasto=Coalesce(
            Sum('reparos__custo_total_peca'), 
            Value(0.0, output_field=DecimalField())
        )
    ).order_by('-total_gasto')[:5]
    
    ativos_labels = [a.nome for a in ativos_gastos_query]
    # Certifique-se de converter para float apenas se o template exigir
    ativos_gastos = [float(a.total_gasto) for a in ativos_gastos_query]
    
    # Dados para ROI por Ativo (para o gráfico) - AGORA REAL DO BANCO
    ativos_roi_query = Ativos.objects.annotate(
        roi_medio=Coalesce(
            Avg('reparos__roi_calculado'), 
            Value(0.0, output_field=DecimalField())
        )
    ).order_by('-roi_medio')[:5]
    
    roi_labels = [a.nome for a in ativos_roi_query]
    roi_valores = [float(a.roi_medio) for a in ativos_roi_query]

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

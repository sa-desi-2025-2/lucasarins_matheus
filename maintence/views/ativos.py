from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes  
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from maintence.models.ativos import Ativos
from maintence.models.reparos import Reparos 
from django.db.models import Sum, Avg 
from maintence.serializers.ativos import AtivosSerializer
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib import messages 

from django.shortcuts import render, redirect
from maintence.models import Ativos, Categoriaativos, Reparos 

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
def ativos_view(request):
    ativos = Ativos.objects.select_related('id_categoria').all()
    categorias = Categoriaativos.objects.all()
    context = {
        'ativos': ativos,
        'categorias': categorias
    }
    return render(request, 'maintence/ativos.html', context)

def ativos_criar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        id_categoria_id = request.POST.get('id_categoria')
        
        
        codigo_ativo = request.POST.get('codigo_ativo') or 'TEMP' 
        preco = request.POST.get('preco')
        data_aquisicao = request.POST.get('data_aquisicao')
        vida_util_esperada = request.POST.get('vida_util_esperada')
        unid_vida_util = request.POST.get('unid_vida_util')
        depreciacao_anual = request.POST.get('depreciacao_anual') or 0.0 
        localizacao = request.POST.get('localizacao')
        
        if nome and id_categoria_id and preco and data_aquisicao and vida_util_esperada and localizacao:
            Ativos.objects.create(
                nome=nome,
                descricao=descricao,
                id_categoria_id=id_categoria_id,
                codigo_ativo=codigo_ativo, 
                preco=preco,
                data_aquisicao=data_aquisicao,
                vida_util_esperada=vida_util_esperada,
                unid_vida_util=unid_vida_util or 'anos',
                localizacao=localizacao,
                depreciacao_anual=depreciacao_anual,
            )
            messmessages.success(request, 'Ativo excluído com sucesso!')
    return redirect('ativos')

def ativos_editar(request, id_ativo):
    ativo = get_object_or_404(Ativos, id_ativo=id_ativo)
    categorias = Categoriaativos.objects.all()
    
    context = {
        'ativo': ativo,
        'categorias': categorias,
    }
    return render(request, 'maintence/ativos_editar.html', context)

@require_POST
def ativos_atualizar(request, id_ativo):
    ativo = get_object_or_404(Ativos, id_ativo=id_ativo)
    
    if request.method == 'POST':
        ativo.nome = request.POST.get('nome')
        ativo.descricao = request.POST.get('descricao')
        ativo.id_categoria_id = request.POST.get('id_categoria')
        ativo.codigo_ativo = request.POST.get('codigo_ativo') or 'TEMP' 
        ativo.preco = request.POST.get('preco')
        ativo.data_aquisicao = request.POST.get('data_aquisicao')
        ativo.vida_util_esperada = request.POST.get('vida_util_esperada')
        ativo.unid_vida_util = request.POST.get('unid_vida_util') or 'anos'
        ativo.depreciacao_anual = request.POST.get('depreciacao_anual') or 0.0 
        ativo.localizacao = request.POST.get('localizacao')
        
        ativo.save()
        messages.success(request, 'Ativo atualizado com sucesso!')
        
    return redirect('ativos')

@require_POST
def ativos_excluir(request, id_ativo):
     #VERIFICAÇÃO DE PERMISSÃO DE ADMINISTRADOR
    if not request.user.is_staff:
        messages.error(request, 'Acesso negado. Apenas administradores podem excluir ativos.')
        return redirect('ativos')
        
    ativo = get_object_or_404(Ativos, id_ativo=id_ativo)
    ativo.delete()
    messages.success(request, 'Ativo excluído com sucesso!')
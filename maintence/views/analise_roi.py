from django.db.models import Sum, F
from django.shortcuts import render
from decimal import Decimal
from django.utils import timezone
from datetime import timedelta

from maintence.models import Ativos, Reparos, Categoriaativos


def analise_roi_view(request):

    periodo = request.GET.get("periodo")
    categoria = request.GET.get("categoria")
    ordenacao = request.GET.get("ordenacao", "roi_desc")

    reparos = Reparos.objects.select_related('id_ativo')

    if periodo:
        dias = int(periodo)
        data_limite = timezone.now() - timedelta(days=dias)
        reparos = reparos.filter(data_reparo__gte=data_limite)

    if categoria:
        reparos = reparos.filter(id_ativo__id_categoria=categoria)

    total_investido = reparos.aggregate(
        total=Sum(F('custo_total_peca') + F('custo_mao_obra'))
    )['total'] or Decimal('0.00')

    retorno_estimado = Decimal('0.00')

    for r in reparos:
        roi = r.calcular_roi()
        if roi is not None:
            retorno_estimado += (r.custo_total() * (roi / 100))

    if total_investido > 0:
        roi_geral = ((retorno_estimado) / total_investido) * 100
    else:
        roi_geral = Decimal('0')

    roi_geral = roi_geral.quantize(Decimal("0.01"))

    ativos = Ativos.objects.all()

    if categoria:
        ativos = ativos.filter(id_categoria=categoria)

    lista_ativos = []

    for ativo in ativos:

        reparos_ativo = reparos.filter(id_ativo=ativo.id_ativo)

        investimento_ativo = reparos_ativo.aggregate(
            total=Sum(F('custo_total_peca') + F('custo_mao_obra'))
        )['total'] or Decimal('0.00')

        valor_atual = Decimal(ativo.preco or 0)

        if investimento_ativo > 0:
            roi_ativo = ((valor_atual - investimento_ativo) / investimento_ativo) * 100
        else:
            roi_ativo = Decimal("0.00")

        lista_ativos.append({
            'id': ativo.id_ativo,
            'nome': ativo.nome,
            'valor_inicial': ativo.preco,
            'valor_atual': valor_atual,
            'custo_total_reparos': investimento_ativo,
            'roi_percentual': roi_ativo.quantize(Decimal("0.01")),
        })

    if ordenacao == "roi_desc":
        lista_ativos = sorted(lista_ativos, key=lambda x: x['roi_percentual'], reverse=True)

    elif ordenacao == "roi_asc":
        lista_ativos = sorted(lista_ativos, key=lambda x: x['roi_percentual'])

    elif ordenacao == "custo_desc":
        lista_ativos = sorted(lista_ativos, key=lambda x: x['custo_total_reparos'], reverse=True)

    elif ordenacao == "nome":
        lista_ativos = sorted(lista_ativos, key=lambda x: x['nome'].lower())

    categorias = Categoriaativos.objects.all()

    contexto = {
        'roi_geral': roi_geral,
        'total_investido': total_investido,
        'retorno_estimado': retorno_estimado.quantize(Decimal("0.01")),
        'categorias': categorias,
        'ativos': lista_ativos,
    }

    return render(request, "maintence/analise_roi.html", contexto)

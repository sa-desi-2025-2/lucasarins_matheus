from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect 
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models import Reparos, Ativos # Importa os models necessários
from maintence.serializers.reparos import ReparosSerializer
from django.db.models import Sum, Avg, Count
from rest_framework.response import Response
from maintence.models import Usuarios
from rest_framework import serializers
from rest_framework.views import APIView
from django.http import HttpResponse
import csv
from django.views.decorators.http import require_POST
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas






class ReparosViewSet(ModelViewSet):
    queryset = Reparos.objects.all()
    serializer_class = ReparosSerializer
    permission_classes = [IsAuthenticated]


    
class ReparosCSVExportView(APIView):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="reparos.csv"'
        writer = csv.writer(response)
        writer.writerow([
            'ID Reparo', 'ID Ativo', 'Data Reparo', 'Tipo', 'Descrição',
            'Tempo Parada (hora)', 'Extensão Vida Útil', 'Unid Extensão Vida Útil',
            'ID Usuário', 'ROI Calculado', 'Custo Total Peça', 'Custo Mão de Obra'
        ])
        reparos = Reparos.objects.all()
        for reparo in reparos:
            writer.writerow([
                reparo.id_reparo,
                reparo.id_ativo.id_ativo if reparo.id_ativo else '',
                reparo.data_reparo,
                reparo.tipo,
                reparo.descricao,
                reparo.tempo_parada_hora,
                reparo.extensao_vida_util,
                reparo.unid_extensao_vida_util,
                reparo.id_usuario.id_usuario if reparo.id_usuario else '',
                reparo.roi_calculado,
                reparo.custo_total_peca,
                reparo.custo_mao_obra
            ])
        return response

def exportar_reparos_pdf(request):
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reparos.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    y = 750


    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Relatório de Reparos")
    y -= 40


    reparos = Reparos.objects.all()

    p.setFont("Helvetica", 11)

    for reparo in reparos:
        texto = (
            f"ID: {reparo.id_reparo} | "
            f"Ativo: {reparo.id_ativo.id_ativo} | "
            f"Tipo: {reparo.tipo} | "
            f"Data: {reparo.data_reparo.strftime('%d/%m/%Y %H:%M')}"
        )
        p.drawString(50, y, texto)
        y -= 20

        if y < 60:   
            p.showPage()
            p.setFont("Helvetica", 11)
            y = 750

    p.showPage()
    p.save()

    return response

    def perform_create(self, serializer):
        user = getattr(self.request, 'user', None)
        if user and user.is_authenticated:
            serializer.save(id_usuario=user)
        else:
            serializer.save()
            
def manutencao_view(request):
    # Certifique-se de que os models Reparos e Ativos estão importados corretamente
    reparos = Reparos.objects.select_related('id_ativo').all()
    ativos = Ativos.objects.all()
    context = {
        'reparos': reparos,
        'ativos': ativos
    }
    return render(request, 'maintence/manutencao.html', context)

# Adicione a view de criação de reparos
def reparos_criar(request):
    if request.method == 'POST':
        id_ativo = request.POST.get("id_ativo")
        tipo = request.POST.get("tipo")
        descricao = request.POST.get("descricao")
        tempo_parada_hora = request.POST.get("tempo_parada_hora")
        extensao_vida_util = request.POST.get("extensao_vida_util")
        unid_extensao_vida_util = request.POST.get("unid_extensao_vida_util")
        custo_total_peca = request.POST.get("custo_total_peca")
        custo_mao_obra = request.POST.get("custo_mao_obra")

        Reparos.objects.create(
            id_ativo_id=id_ativo,
            tipo=tipo,
            descricao=descricao,
            tempo_parada_hora=tempo_parada_hora,
            extensao_vida_util=extensao_vida_util,
            unid_extensao_vida_util=unid_extensao_vida_util,
            custo_total_peca=custo_total_peca,
            custo_mao_obra=custo_mao_obra
        )

        messages.success(request, "Reparo cadastrado com sucesso!")

    return redirect('manutencao')
            


def reparos_editar(request, id_reparo):
    reparo = Reparos.objects.get(id_reparo=id_reparo)
    ativos = Ativos.objects.all()

    return render(request, 'maintence/reparos_editar.html', {
        'reparo': reparo,
        'ativos': ativos
    })
@require_POST
def reparos_excluir(request, id_reparo):
    """Exclui um reparo específico."""
    reparo = get_object_or_404(Reparos, id_reparo=id_reparo)
    reparo.delete()
    messages.success(request, "Reparo excluído com sucesso!")
    return redirect('manutencao')

def reparos_atualizar(request, id_reparo):
    if request.method == 'POST':
        reparo = Reparos.objects.get(id_reparo=id_reparo)

        reparo.id_ativo_id = request.POST.get("id_ativo")
        reparo.tipo = request.POST.get("tipo")
        reparo.descricao = request.POST.get("descricao")
        reparo.custo_total_peca = request.POST.get("custo_total_peca")
        reparo.custo_mao_obra = request.POST.get("custo_mao_obra")  
        reparo.tempo_parada_hora = request.POST.get("tempo_parada_hora")
        reparo.extensao_vida_util = request.POST.get("extensao_vida_util")
        reparo.unid_extensao_vida_util = request.POST.get("unid_extensao_vida_util")

        reparo.save()

        messages.success(request, "Reparo atualizado com sucesso!")

    return redirect('manutencao')

def reparos_listar(request):
    reparos = Reparos.objects.all()
    return render(request, 'maintence/reparos_listar.html', {
        'reparos': reparos
    })
    
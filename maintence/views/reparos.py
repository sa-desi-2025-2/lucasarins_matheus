from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models.reparos import Reparos
from maintence.serializers.reparos import ReparosSerializer
from django.db.models import Sum, Avg, Count
from rest_framework.response import Response
from maintence.models import Usuarios
from rest_framework import serializers
from rest_framework.views import APIView
from django.http import HttpResponse
import csv

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

        

                  
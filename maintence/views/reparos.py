from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models import Reparos, Ativos # Importa os models necessários
from maintence.serializers.reparos import ReparosSerializer
from django.db.models import Sum, Avg, Count
from rest_framework.response import Response


class ReparosViewSet(ModelViewSet):
    queryset = Reparos.objects.all()
    serializer_class = ReparosSerializer
    permission_classes = [IsAuthenticated]

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
        # Lógica para criar um novo reparo com os dados do POST
        # ...
        pass
    return redirect('manutencao')
            
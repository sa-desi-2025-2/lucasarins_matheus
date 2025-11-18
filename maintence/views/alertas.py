from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models import Alertas, Ativos
from maintence.serializers.alertas import AlertasSerializer
 
class AlertasViewSet(ModelViewSet):
    queryset = Alertas.objects.all()
    serializer_class = AlertasSerializer

def alertas_view(request):
    alertas = Alertas.objects.select_related('id_ativo').all()
    context = {
        'alertas': alertas,
        'ativos': Ativos.objects.all(),
        # Adicione aqui a lógica para contar alertas (se necessário para o template)
    }
    return render(request, 'maintence/alertas.html', context)

# Adicione a view de criação de alertas
def alertas_criar(request):
    if request.method == 'POST':
        # Implementar lógica de criação
        pass
    return redirect('alertas_view')

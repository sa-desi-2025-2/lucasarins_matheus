from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models import Alertas, Ativos
from maintence.serializers.alertas import AlertasSerializer
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404 
 
class AlertasViewSet(ModelViewSet):
    queryset = Alertas.objects.all()
    serializer_class = AlertasSerializer

def alertas_view(request):
    alertas = Alertas.objects.select_related('id_ativo').all()
    context = {
        'alertas': alertas,
        'ativos': Ativos.objects.all(),
        
    }
    return render(request, 'maintence/alertas.html', context)


def alertas_criar(request ):
    if request.method == 'POST':
        id_ativo_id = request.POST.get('id_ativo')
        tipo_alerta = request.POST.get('tipo_alerta')
        mensagem = request.POST.get('mensagem')
        
        if id_ativo_id and tipo_alerta:
            Alertas.objects.create(
                id_ativo_id=id_ativo_id,
                tipo_alerta=tipo_alerta,
                mensagem=mensagem,
                status_alerta='Ativo' # Assumindo que o status inicial é Ativo
            )
            messages.success(request, 'Alerta criado com sucesso!')
        else:
            messages.error(request, 'Erro ao criar alerta. Preencha todos os campos obrigatórios.')
            
        return redirect('alertas_view')
    return redirect('alertas_view')

@require_POST
def alertas_excluir(request, pk):
    alerta = get_object_or_404(Alertas, pk=pk)
    alerta.delete()
    messages.success(request, 'Alerta excluído com sucesso!')
    return redirect('alertas_view')
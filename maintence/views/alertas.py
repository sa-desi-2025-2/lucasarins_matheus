from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models import Alertas, Ativos
from maintence.serializers.alertas import AlertasSerializer
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404 
 
class AlertasViewSet(ModelViewSet ):
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
     
        limiar_porcentagem = request.POST.get('limiar_porcentagem') 
        limiar_roi = request.POST.get('limiar_roi')
 
        mensagem = request.POST.get('mensagem')

        if id_ativo_id and tipo_alerta and limiar_porcentagem and limiar_roi:
            Alertas.objects.create(
                id_ativo_id=id_ativo_id,
                tipo_alerta=tipo_alerta,
               
                limiar_porcentagem=limiar_porcentagem,
                limiar_roi=limiar_roi,
              
                mensagem=mensagem,
                status_alerta='Ativo' 
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
def alertas_editar(request, id_alerta):
    alerta = get_object_or_404(Alertas, id_alerta=id_alerta)
    ativos = Ativos.objects.all()
    
    context = {
        'alerta': alerta,
        'ativos': ativos,
    }
    return render(request, 'maintence/alertas_editar.html', context)

@require_POST
def alertas_atualizar(request, id_alerta):
    alerta = get_object_or_404(Alertas, id_alerta=id_alerta)
    
    if request.method == 'POST':
        alerta.id_ativo_id = request.POST.get('id_ativo')
        alerta.tipo_alerta = request.POST.get('tipo_alerta')
        alerta.limiar_porcentagem = request.POST.get('limiar_porcentagem')
        alerta.limiar_roi = request.POST.get('limiar_roi')
        alerta.status_alerta = request.POST.get('status_alerta')
        
        alerta.save()
        messages.success(request, 'Alerta atualizado com sucesso!')
        
    return redirect('alertas_view')
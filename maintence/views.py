from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated

from maintence.models import Alertas, Ativos, Categoriaativos, Fornecedores, Itens, ItensReparo, LogAuditorias, Reparos, Usuarios
from maintence.serializers import (
    AlertasSerializer,
    AtivosSerializer,
    CategoriaativosSerializer,
    FornecedoresSerializer,
    ItensSerializer,
    ItensReparoSerializer,
    LogAuditoriasSerializer,
    ReparosSerializer,
    UsuariosSerializer,
)


# ------------------ API VIEWSETS ------------------

class AlertasViewSet(ModelViewSet):
    queryset = Alertas.objects.all()
    serializer_class = AlertasSerializer


class AtivosViewSet(ModelViewSet):
    queryset = Ativos.objects.all()
    serializer_class = AtivosSerializer


class CategoriaativosViewSet(ModelViewSet):
    queryset = Categoriaativos.objects.all()
    serializer_class = CategoriaativosSerializer

class FornecedoresViewSet(ModelViewSet):
    queryset = Fornecedores.objects.all()
    serializer_class = FornecedoresSerializer

class ItensViewSet(ModelViewSet):
    queryset = Itens.objects.all()
    serializer_class = ItensSerializer

class ItensReparoViewSet(ModelViewSet):
    queryset = ItensReparo.objects.all()
    serializer_class = ItensReparoSerializer 

class LogAuditoriasViewSet(ModelViewSet):
    queryset = LogAuditorias.objects.all()
    serializer_class = LogAuditoriasSerializer

class ReparosViewSet(ModelViewSet):
    queryset = Reparos.objects.all()
    serializer_class = ReparosSerializer
    


class UsuariosViewSet(ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer


# ------------------ PÁGINA DE CADASTRO ------------------

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        user = request.POST.get('user')  
        email = request.POST.get('email')
        re = request.POST.get('re')
        senha = request.POST.get('senha')
        confirmar = request.POST.get('confirmar-senha')

        # Verifica se senhas coincidem
        if senha != confirmar:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('cadastro')

        # Verifica se email ou RE já existem
        if Usuarios.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado!')
            return redirect('cadastro')

        if Usuarios.objects.filter(re=re).exists():
            messages.error(request, 'RE já cadastrado!')
            return redirect('cadastro')

        # Criptografa senha
        senha_hash = make_password(senha)

        # Cria usuário no banco
        novo_usuario = Usuarios(
            nome=nome,
            email=email,
            senha_hash=senha_hash,
            perfil_acesso='Comum',  # valor padrão
            re=re
        )
        novo_usuario.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('cadastro')

    return render(request, 'maintence/cadastro.html')

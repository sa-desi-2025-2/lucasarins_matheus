from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models import Usuarios # Adicionei este import para garantir

def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        user = request.POST.get('user')  
        email = request.POST.get('email')
        re = request.POST.get('re')
        senha = request.POST.get('senha')
        confirmar = request.POST.get('confirmar-senha')

        # ... (lógica de validação e criação de usuário) ...

        novo_usuario = Usuarios(
            nome=nome,
            email=email,
            senha_hash=senha_hash,
            perfil_acesso='Comum',  # valor padrão
            re=re
        )
        novo_usuario.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login') # <--- CORRIGIDO: Redireciona para o login

    return render(request, 'maintence/cadastro.html')

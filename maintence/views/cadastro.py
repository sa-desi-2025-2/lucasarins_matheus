from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models import Usuarios


def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        user = request.POST.get('user')  
        email = request.POST.get('email')
        re = request.POST.get('re')
        senha = request.POST.get('senha')
        confirmar = request.POST.get('confirmar-senha')

        if senha != confirmar:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'maintence/cadastro.html')
        
        senha_hash = make_password(senha)


        novo_usuario = Usuarios(
            nome=nome,
            email=email,
            senha_hash=senha_hash, 
            perfil_acesso='Comum',
            re=re
        )
        novo_usuario.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')

    return render(request, 'maintence/cadastro.html')

# maintence/views/auth.py (Trecho Corrigido)

from django.shortcuts import render, redirect
from django.contrib import messages
from maintence.models import Usuarios
from django.contrib.auth.hashers import check_password # <--- NOVO IMPORT

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha_digitada = request.POST.get('senha')

        try:
            # 1. Tenta encontrar o usuário pelo email
            usuario = Usuarios.objects.get(email=email)
        except Usuarios.DoesNotExist:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'maintence/login.html')

        # 2. VERIFICAÇÃO DA SENHA COM HASH
        # Compara a senha digitada com o hash armazenado no campo 'senha_hash'
        if check_password(senha_digitada, usuario.senha_hash):
            # Login bem-sucedido:
            request.session['usuario_id'] = usuario.id_usuario # <--- CORREÇÃO APLICADA
            request.session['usuario_nome'] = usuario.nome
            
            messages.success(request, f'Bem-vindo, {usuario.nome}!')
            return redirect('dashboard')
        else:
            # Senha incorreta
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'maintence/login.html')

    return render(request, 'maintence/login.html')

def logout_view(request):
    # Se você estiver usando o sistema de autenticação do Django:
    # logout(request)
    
    # Se você estiver usando um sistema de sessão manual:
    if 'usuario_id' in request.session:
        del request.session['usuario_id']
        
    messages.info(request, 'Você foi desconectado com sucesso.')
    return redirect('login')
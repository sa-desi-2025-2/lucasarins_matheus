from django.shortcuts import render, redirect
from django.contrib import messages
from maintence.models import Usuarios
from django.contrib.auth.hashers import check_password 

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha_digitada = request.POST.get('senha')

        try:
            usuario = Usuarios.objects.get(email=email)
        except Usuarios.DoesNotExist:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'maintence/login.html')

        #VERIFICAÇÃO DA SENHA COM HASH
        if check_password(senha_digitada, usuario.senha_hash):
            request.session['usuario_id'] = usuario.id_usuario 
            request.session['usuario_nome'] = usuario.nome
            
            messages.success(request, f'Bem-vindo, {usuario.nome}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'maintence/login.html')

    return render(request, 'maintence/login.html')

def logout_view(request):
  

    if 'usuario_id' in request.session:
        del request.session['usuario_id']
        
    messages.info(request, 'Você foi desconectado com sucesso.')
    return redirect('login')
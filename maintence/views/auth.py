from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        

      
        from maintence.models import Usuarios
        try:
            user = Usuarios.objects.get(email=email)
            if user.senha_hash == senha: # Substituir por `check_password`
                # Lógica de login do Django (requer adaptação do seu model `Usuarios` para herdar de `AbstractUser`)
                # Por agora, vamos usar a sessão de forma simples:
                request.session['user_id'] = user.id_usuario
                return redirect('dashboard')
            else:
                messages.error(request, 'Credenciais inválidas.')
        except Usuarios.DoesNotExist:
            messages.error(request, 'Usuário não encontrado.')
            
    return render(request, 'maintence/login.html')

def logout_view(request):
    logout(request) # ou request.session.flush()
    return redirect('login')
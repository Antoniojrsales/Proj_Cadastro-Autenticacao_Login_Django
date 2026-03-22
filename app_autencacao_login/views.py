from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages # Para mensagens de feedback
from django.contrib.auth.decorators import user_passes_test

def login(request): # Mudei o nome para evitar conflito
    if request.method == 'GET':
        # Se o usuário já estiver logado, não precisa ver a tela de login
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'app_autenticacao_login/pages/login.html')
    
    username = request.POST.get('username')
    senha = request.POST.get('senha')

    usuario = authenticate(username=username, password=senha)

    if usuario is not None:
        auth_login(request, usuario)
        messages.success(request, f"Bem-vindo(a), {username}!")
        return redirect('home') # Manda para a página principal do salão
    else:
        messages.error(request, "Usuário ou senha inválidos.")
        return redirect('login')
    
@login_required(login_url='login')
def home(request):
    return render(request, 'app_autenticacao_login/pages/home.html')

def apenas_admin(user):
    return user.is_superuser

@user_passes_test(apenas_admin, login_url='login') # Bloqueia o acesso direto pela URL
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'app_autenticacao_login/pages/cadastro.html')
    
    # Pegando os dados
    username = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    # 1. Validação Básica
    if not username or not senha:
        messages.error(request, "Preencha todos os campos obrigatórios.")
        return redirect('cadastro')

    # 2. Verificação de existência
    if User.objects.filter(username=username).exists():
        messages.warning(request, "Este nome de usuário já está em uso.")
        return redirect('cadastro')

    # 3. Criação segura
    User.objects.create_user(username=username, email=email, password=senha)
    
    messages.success(request, f"Funcionário {username} cadastrado com sucesso!")
    return redirect('login') # Redireciona para o login após cadastrar

# 5. Função de Logout
def logout(request):
    auth_logout(request)
    messages.info(request, "Você saiu do sistema.")
    return redirect('login')

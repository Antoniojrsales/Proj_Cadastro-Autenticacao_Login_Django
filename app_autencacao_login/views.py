from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'app_autenticacao_login/pages/home.html')

def cadastro(request):
    return render(request, 'app_autenticacao_login/pages/cadastro.html')

def login(request):
    return render(request, 'app_autenticacao_login/pages/login.html')
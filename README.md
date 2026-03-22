# 🔐 Sistema de Autenticação e Gestão de Acessos

Este projeto é um módulo de segurança robusto desenvolvido em Django, focado na autenticação e gerenciamento de perfis de usuários. A ferramenta implementa um fluxo completo de CRUD para usuários, utilizando o sistema de autenticação nativo do Django para garantir a segurança dos dados e o controle de permissões em tempo real.

## ✅ Etapas de Inicialização

- Estruturação do projeto em pastas
- Criação do ambiente virtual
- Definição das bibliotecas principais (via `requirements.txt`)
- Configuração do `.gitignore`
- Primeiros arquivos adicionados ao controle de versão

## 📁 Estrutura Inicial de Pastas

```
Proj_cadastro-autenticacao_login_django/
├── ambiente_login_Django/
├── app_autenticacao_login/
│   └── migrations/  
│   └── static/
│       └── app_autenticacao_login/
│           └── css/
│               └── style.css/
│   └── templates/
│       └── app_autenticacao_login/
│           └── pages/
│               └── cadastro.html
│               └── home.html
│               └── login.html
│           └── partials/
│               └── head.html
│   └── __init__.py
│   └── admin.py
│   └── apps.py
│   └── models.py
│   └── tests.py
│   └── urls.py
│   └── views.py
│   └── base_templates/
│       └── global/
│           └── folha_rosto.html  
│   └── Proj_Auth_Login/ 
│   └── __init__.py
│   └── asgi.py
│   └── settings.py
│   └── urls.py
│   └── wsgi.py
├── utils/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 🛠 Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes ferramentas e bibliotecas:

* **Backend:** Python 3.11+ e Django 5.x.
* **Frontend:** Django Templates, HTML5, CSS3 e FontAwesome para ícones.
* **Segurança:** Django Contrib Auth (Hashing de senhas e Gerenciamento de Sessão).

## ⚙️ Como Instalar e Rodar o Projeto
Para executar a aplicação em sua máquina local, siga os passos abaixo:

1. Clonagem e Configuração do Ambiente
```
# Clone o repositório
git clone [https://github.com/Antoniojrsales/Proj_Cadastro-Autenticacao_Login_Django]
cd Proj_Cadastro-Autenticacao_Login_Django

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

## ✨ Funcionalidades Principais

| Recurso | Descrição |
| :--- | :--- |
| **Validação Dinâmica:** | Verificação de existência de usuário em tempo real. |
| **Níveis de Acesso (RBAC):** | Interface adaptativa que oculta funcionalidades administrativas (como cadastro) de usuários comuns. |
| **Feedback ao Usuário:** | Implementação do Django Messages Framework para alertas de sucesso e erro. |

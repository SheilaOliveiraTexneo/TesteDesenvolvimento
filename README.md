# Sistema de Controle de Solicitação de Estoque

Aplicativo web responsivo para gerenciamento de estoque e atendimento de solicitações internas, desenvolvido com Python (Flask), HTML, CSS e JavaScript.

## 🎯 Funcionalidades

- ✅ Cadastro de Produtos com upload de imagem
- ✅ Cadastro de Partidas vinculadas a produtos
- ✅ Cadastro de Solicitantes
- ✅ Solicitações de Estoque com numeração automática
- ✅ Dashboard com indicadores em tempo real
- ✅ Painel Kanban de atendimento
- ✅ Autenticação por usuário
- ✅ Perfis de acesso (Admin, Operador, Consulta)
- ✅ Histórico de alterações e auditoria
- ✅ Exportação para Excel
- ✅ Impressão de relatórios

## 🛠️ Stack Tecnológico

- **Backend**: Python + Flask
- **Frontend**: HTML5 + CSS3 + JavaScript + Bootstrap 5
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Autenticação**: Flask-Login
- **ORM**: SQLAlchemy

## 📁 Estrutura do Projeto

```
estoque-app/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── utils/
├── migrations/
├── tests/
├── config.py
├── requirements.txt
└── run.py
```

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.9+
- pip
- Virtualenv

### Passos

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente: `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows)
4. Instale dependências: `pip install -r requirements.txt`
5. Execute migrações: `flask db upgrade`
6. Inicie a aplicação: `python run.py`
7. Acesse em: `http://localhost:5000`

## 📊 Banco de Dados

As tabelas incluem:
- **produtos**: Código, descrição e foto
- **partidas**: ID da partida e relacionamento com produtos
- **solicitantes**: Código e nome
- **solicitacoes**: Solicitações com ID automático, status e prioridade
- **usuarios**: Autenticação e perfis
- **auditoria**: Histórico de todas as alterações

## 👤 Usuários Padrão

- **Admin**: admin@estoque.com / admin123 (Acesso total)
- **Operador**: operador@estoque.com / operador123 (Gerencia solicitações)
- **Consulta**: consulta@estoque.com / consulta123 (Apenas visualização)

## 📝 Licença

Este projeto é de uso interno.

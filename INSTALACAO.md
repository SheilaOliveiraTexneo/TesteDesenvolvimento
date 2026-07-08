# Guia de Instalação e Uso - Sistema de Controle de Estoque

## 🚀 Instalação Rápida

### 1. Clonar o Repositório

```bash
git clone https://github.com/SheilaOliveiraTexneo/TesteDesenvolvimento.git
cd TesteDesenvolvimento
git checkout feature/estoque-app
```

### 2. Criar Ambiente Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

```bash
cp .env.example .env
```

Edite o arquivo `.env` conforme necessário (ou deixe os valores padrão para desenvolvimento).

### 5. Inicializar Banco de Dados

```bash
python run.py init-db
```

Isso criará as tabelas e inserirá os usuários padrão.

### 6. Executar a Aplicação

```bash
python run.py
```

A aplicação estará disponível em: **http://localhost:5000**

---

## 👤 Usuários Padrão de Teste

Três usuários pré-configurados com diferentes níveis de acesso:

### Admin (Acesso Total)
- **Email:** admin@estoque.com
- **Senha:** admin123
- **Permissões:** Criar, editar, deletar em todos os módulos

### Operador (Gerencia Solicitações)
- **Email:** operador@estoque.com
- **Senha:** operador123
- **Permissões:** Criar e editar solicitações, visualizar todos os dados

### Consulta (Apenas Visualização)
- **Email:** consulta@estoque.com
- **Senha:** consulta123
- **Permissões:** Apenas visualizar dados

---

## 📁 Estrutura de Arquivos

```
TesteDesenvolvimento/
├── app/
│   ├── models/                 # Modelos de banco de dados
│   │   ├── __init__.py
│   │   ├── user.py            # Usuários e autenticação
│   │   ├── produto.py         # Produtos
│   │   ├── partida.py         # Partidas
│   │   ├── solicitante.py     # Solicitantes
│   │   ├── solicitacao.py     # Solicitações de estoque
│   │   └── auditoria.py       # Logs de auditoria
│   ├── routes/                 # Rotas e views
│   │   ├── auth.py            # Autenticação
│   │   ├── main.py            # Página principal
│   │   ├── dashboard.py       # Dashboard e Kanban
│   │   ├── produtos.py        # CRUD de produtos
│   │   ├── partidas.py        # CRUD de partidas
│   │   ├── solicitantes.py    # CRUD de solicitantes
│   │   └── solicitacoes.py    # CRUD de solicitações
│   ├── templates/              # Templates HTML
│   │   ├── base.html          # Template base
│   │   ├── auth/
│   │   ├── dashboard/
│   │   ├── produtos/
│   │   ├── partidas/
│   │   ├── solicitantes/
│   │   └── solicitacoes/
│   ├── static/                 # Arquivos estáticos
│   │   └── uploads/           # Uploads de imagens
│   ├── utils.py               # Funções auxiliares
│   └── __init__.py            # Inicialização da app
├── config.py                   # Configurações
├── run.py                      # Arquivo principal
├── requirements.txt            # Dependências
├── .env.example                # Exemplo de variáveis de ambiente
├── .gitignore
└── README.md
```

---

## 📊 Funcionalidades Principais

### 1. **Dashboard**
- Visão geral com indicadores em tempo real
- Total de solicitações, por status e por prioridade
- Histórico das últimas solicitações

### 2. **Kanban**
- Visualização tipo Kanban com 3 colunas: Solicitado, Em Atendimento, Finalizado
- Código de cores por prioridade
- Contadores automáticos

### 3. **Fila de Atendimento**
- Organização por status e prioridade
- Acesso rápido para atualizar solicitações
- Ordenação automática

### 4. **Módulo de Produtos**
- CRUD completo de produtos
- Upload de imagens
- Busca por código ou descrição
- Ordenação e paginação

### 5. **Módulo de Partidas**
- Associação com produtos
- Busca por partida ou produto
- Validação automática

### 6. **Módulo de Solicitantes**
- Cadastro de solicitantes
- Código único por solicitante
- Busca e filtros

### 7. **Módulo de Solicitações**
- Numeração automática (000001, 000002, ...)
- 5 níveis de prioridade com código de cores
- 3 status: Solicitado → Em Atendimento → Finalizado
- Auto-preenchimento de dados ao selecionar partida/solicitante
- Campo de observações
- Exportação para Excel
- Auditoria completa

### 8. **Segurança**
- Sistema de autenticação por usuário/senha
- Controle de permissões por perfil
- Logs de auditoria de todas as alterações
- Hash de senhas com Werkzeug

---

## 🎨 Cores de Prioridade

| Prioridade | Cor | Significado |
|-----------|-----|-------------|
| 1 | 🔴 Vermelho | Urgente |
| 2 | 🟠 Laranja | Muito Alta |
| 3 | 🟡 Amarelo | Alta |
| 4 | 🔵 Azul | Média |
| 5 | 🟢 Verde | Baixa |

---

## 📚 API Endpoints (Internos)

### Autenticação
- `POST /auth/login` - Login de usuário
- `GET /auth/logout` - Logout

### Dashboard
- `GET /dashboard/` - Dashboard principal
- `GET /dashboard/kanban` - Visualização Kanban
- `GET /dashboard/atendimento` - Fila de atendimento

### Produtos
- `GET /produtos/` - Listar produtos
- `GET /produtos/novo` - Formulário novo produto
- `POST /produtos/novo` - Criar produto
- `GET /produtos/<id>/editar` - Editar produto
- `POST /produtos/<id>/editar` - Salvar edição
- `POST /produtos/<id>/deletar` - Deletar produto
- `GET /produtos/api/buscar/<codigo>` - API: Buscar por código

### Partidas
- `GET /partidas/` - Listar partidas
- `GET /partidas/novo` - Novo
- `POST /partidas/novo` - Criar
- `GET /partidas/<id>/editar` - Editar
- `POST /partidas/<id>/editar` - Salvar
- `POST /partidas/<id>/deletar` - Deletar
- `GET /partidas/api/buscar/<id_partida>` - API: Buscar

### Solicitantes
- `GET /solicitantes/` - Listar
- `GET /solicitantes/novo` - Novo
- `POST /solicitantes/novo` - Criar
- `GET /solicitantes/<id>/editar` - Editar
- `POST /solicitantes/<id>/editar` - Salvar
- `POST /solicitantes/<id>/deletar` - Deletar
- `GET /solicitantes/api/buscar/<codigo>` - API: Buscar

### Solicitações
- `GET /solicitacoes/` - Listar
- `GET /solicitacoes/nova` - Novo
- `POST /solicitacoes/nova` - Criar
- `GET /solicitacoes/<id>/editar` - Editar
- `POST /solicitacoes/<id>/editar` - Salvar
- `POST /solicitacoes/<id>/deletar` - Deletar
- `GET /solicitacoes/exportar/excel` - Exportar para Excel

---

## 🔧 Configurações

### Desenvolvimento

Arquivo `.env`:
```
FLASK_ENV=development
FLASK_APP=run.py
SECRET_KEY=seu-secret-key-aqui
DATABASE_URL=sqlite:///estoque.db
```

### Produção

Para produção, altere:
```
FLASK_ENV=production
DATABASE_URL=postgresql://user:password@localhost/estoque_db
SECRET_KEY=gere-uma-chave-forte-aqui
```

---

## 📦 Banco de Dados

### Tabelas Criadas

1. **usuarios** - Usuários do sistema
2. **produtos** - Catálogo de produtos
3. **partidas** - Partidas de produtos
4. **solicitantes** - Solicitantes de estoque
5. **solicitacoes** - Solicitações de estoque
6. **auditoria_logs** - Histórico de alterações

---

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'flask'"
**Solução:** Instale as dependências com `pip install -r requirements.txt`

### Erro: "database is locked"
**Solução:** Feche outros processos que estão acessando o banco e limpe a pasta `__pycache__`

### Erro: "Address already in use"
**Solução:** A porta 5000 já está em uso. Altere em `run.py`: `app.run(port=5001)`

### Uploads não aparecem
**Solução:** Crie a pasta `app/static/uploads/` manualmente ou reinicie a app

---

## 🚀 Deploy

### Usando Gunicorn (Produção)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

### Usando Docker

Crie um `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "run:app"]
```

---

## 📝 Próximas Melhorias

- [ ] Notificações por email
- [ ] Integração com API externa
- [ ] Backup automático
- [ ] Relatórios avançados
- [ ] Mobile app
- [ ] Testes automatizados
- [ ] Autenticação OAuth2
- [ ] API RESTful completa

---

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no repositório GitHub.

---

**Desenvolvido com ❤️ usando Flask e Bootstrap**

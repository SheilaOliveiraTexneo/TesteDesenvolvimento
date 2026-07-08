# Sistema de Controle de Solicitação de Estoque

## 📋 Visão Geral

Aplicativo web responsivo para gerenciamento de estoque e atendimento de solicitações internas. O sistema permite o cadastro e manutenção de produtos, partidas, solicitantes e solicitações de estoque, com controle de prioridade, status e acompanhamento operacional.

**Stack:** Python Flask + SQLAlchemy + Bootstrap 5

---

## ✨ Funcionalidades Principais

### 📊 Dashboard
- ✅ Indicadores em tempo real (Total, Solicitado, Em Atendimento, Finalizado)
- ✅ Gráfico de solicitações por prioridade
- ✅ Histórico das últimas solicitações
- ✅ Interface intuitiva e responsiva

### 🎯 Kanban Board
- ✅ 3 colunas: Solicitado, Em Atendimento, Finalizado
- ✅ Código de cores por prioridade (1-5)
- ✅ Contadores automáticos
- ✅ Acesso rápido para edição

### 📦 Gerenciamento de Produtos
- ✅ CRUD completo (Create, Read, Update, Delete)
- ✅ Upload de imagens
- ✅ Busca por código ou descrição
- ✅ Ordenação e paginação
- ✅ Histórico de alterações

### 📮 Gerenciamento de Partidas
- ✅ Associação com produtos
- ✅ Busca por partida ou produto
- ✅ Validação automática de existência
- ✅ CRUD com integridade referencial

### 👥 Gerenciamento de Solicitantes
- ✅ Cadastro com código único
- ✅ Nome e identificação
- ✅ Busca rápida
- ✅ CRUD com proteção de integridade

### 📬 Solicitações de Estoque (Módulo Principal)
- ✅ **ID Automático**: Numeração sequencial (000001, 000002, ...)
- ✅ **5 Níveis de Prioridade** com código de cores:
  - 🔴 Prioridade 1 (Vermelho - Urgente)
  - 🟠 Prioridade 2 (Laranja - Muito Alta)
  - 🟡 Prioridade 3 (Amarelo - Alta)
  - 🔵 Prioridade 4 (Azul - Média)
  - 🟢 Prioridade 5 (Verde - Baixa)
- ✅ **3 Status**: Solicitado → Em Atendimento → Finalizado
- ✅ **Auto-preenchimento** de dados (Produto e Solicitante)
- ✅ **Campos Customizáveis**: Lote, Número de Rocas, Observações
- ✅ **Auditoria Completa** de todas as alterações
- ✅ **Exportação para Excel** com formatação
- ✅ **Busca Avançada** com múltiplos filtros
- ✅ **Paginação** de resultados

### 🔐 Segurança
- ✅ Autenticação por usuário/senha
- ✅ 3 Perfis de Acesso:
  - **Admin**: Acesso total a todos os módulos
  - **Operador**: Gerencia solicitações e visualiza dados
  - **Consulta**: Apenas visualização
- ✅ Criptografia de senhas com Werkzeug
- ✅ Logs de auditoria com rastreamento de usuário
- ✅ Controle de permissões granular

### 📈 Relatórios e Exportação
- ✅ Exportação de solicitações para Excel
- ✅ Formatação profissional com cores e cabeçalhos
- ✅ Impressão de relatórios
- ✅ Filtros avançados para análise

---

## 🚀 Início Rápido

### Pré-requisitos
- Python 3.9+
- pip
- Git

### Instalação (Linux/Mac)

```bash
# 1. Clonar repositório
git clone https://github.com/SheilaOliveiraTexneo/TesteDesenvolvimento.git
cd TesteDesenvolvimento
git checkout feature/estoque-app

# 2. Executar script de setup
chmod +x setup.sh
./setup.sh

# 3. Iniciar aplicação
source venv/bin/activate
python run.py
```

### Instalação (Windows)

```bash
# 1. Clonar repositório
git clone https://github.com/SheilaOliveiraTexneo/TesteDesenvolvimento.git
cd TesteDesenvolvimento
git checkout feature/estoque-app

# 2. Executar script de setup
setup.bat

# 3. Iniciar aplicação
venv\Scripts\activate.bat
python run.py
```

### Acesso

🌐 **URL**: http://localhost:5000

👤 **Usuários de Teste**:
- Admin: `admin@estoque.com` / `admin123`
- Operador: `operador@estoque.com` / `operador123`
- Consulta: `consulta@estoque.com` / `consulta123`

---

## 📁 Estrutura do Projeto

```
TesteDesenvolvimento/
├── app/
│   ├── models/              # Modelos de banco de dados
│   ├── routes/              # Rotas e controladores
│   ├── templates/           # Templates HTML (Jinja2)
│   ├── static/              # CSS, JS, imagens
│   ├── utils.py             # Funções auxiliares
│   └── __init__.py          # Factory da aplicação
├── config.py                # Configurações
├── run.py                   # Ponto de entrada
├── requirements.txt         # Dependências Python
├── setup.sh                 # Script setup (Linux/Mac)
├── setup.bat                # Script setup (Windows)
├── INSTALACAO.md            # Guia detalhado de instalação
└── README.md                # Este arquivo
```

---

## 🗄️ Banco de Dados

### Tabelas Principais

**usuarios**
- Autenticação e controle de acesso
- Campos: id, username, email, password_hash, role, ativo, data_criacao

**produtos**
- Catálogo de produtos
- Campos: id, codigo (único), descricao, foto, data_criacao, data_atualizacao

**partidas**
- Partidas de produtos
- Campos: id, id_partida (único), produto_id (FK), data_criacao

**solicitantes**
- Solicitantes de estoque
- Campos: id, codigo (único), nome, data_criacao

**solicitacoes**
- Solicitações de estoque (módulo principal)
- Campos: id, id_solicitacao (automático), partida_id, produto_id, solicitante_id, prioridade, lote, numero_rocas, data_solicitacao, status, observacoes, data_criacao, data_atualizacao

**auditoria_logs**
- Histórico de alterações
- Campos: id, usuario_id, tabela, operacao (INSERT/UPDATE/DELETE), registro_id, dados_antes, dados_depois, descricao, data_criacao

---

## 🎨 Interface

### Design
- ✅ **Responsivo**: Funciona em desktop, tablet e smartphone
- ✅ **Moderno**: Bootstrap 5 com cores vibrantes
- ✅ **Intuitivo**: Menu lateral com ícones
- ✅ **Acessível**: Compatível com leitores de tela
- ✅ **Rápido**: Otimizado para performance

### Componentes
- Dashboard com cards de indicadores
- Tabelas com busca e paginação
- Formulários com validação
- Modais de confirmação
- Notificações de feedback
- Kanban com drag-and-drop

---

## 🔧 Configuração

### Variáveis de Ambiente (.env)

```env
FLASK_ENV=development          # development ou production
FLASK_APP=run.py              # Arquivo principal
SECRET_KEY=sua-chave-secreta  # Chave para sessões
DATABASE_URL=sqlite:///estoque.db  # URL do banco
```

### Configurações por Ambiente

**Development** (`config.py`)
- Debug ativado
- SQLite local
- CSRF desativado em testes

**Production**
- Debug desativado
- PostgreSQL/MySQL
- HTTPS obrigatório
- Senhas seguras

---

## 📚 Documentação Adicional

- [Guia Detalhado de Instalação](INSTALACAO.md)
- [API REST Endpoints](docs/API.md) *(em desenvolvimento)*
- [Guia do Desenvolvedor](docs/DEVELOPER.md) *(em desenvolvimento)*

---

## 🚀 Deploy

### Heroku

```bash
heroku login
heroku create seu-app-name
git push heroku feature/estoque-app:main
heroku run python run.py init-db
```

### Railway / Render

Conecte o repositório GitHub e configure as variáveis de ambiente.

### VPS (Ubuntu/Debian)

```bash
sudo apt-get install python3-pip python3-venv nginx gunicorn
# ... configurar gunicorn e nginx
```

---

## 🐛 Troubleshooting

| Problema | Solução |
|----------|----------|
| Port 5000 em uso | Altere em `run.py`: `app.run(port=5001)` |
| Database locked | Feche outros processos ou reinicie |
| Uploads não aparecem | Crie pasta: `app/static/uploads/` |
| Permissão denied | Verifique permissões: `chmod -R 755 app/` |

---

## 📊 Estatísticas do Projeto

- **Linhas de Código**: ~2000+
- **Modelos**: 6
- **Rotas**: 30+
- **Templates**: 15+
- **Funcionalidades**: 50+
- **Usuários**: 3 perfis de acesso

---

## 🎓 Tecnologias Utilizadas

- **Backend**: Python 3.9+, Flask 2.3, SQLAlchemy 3.0
- **Frontend**: HTML5, Bootstrap 5, JavaScript (vanilla)
- **Banco de Dados**: SQLite (dev), PostgreSQL (prod)
- **Autenticação**: Flask-Login, Werkzeug
- **Exportação**: OpenPyXL (Excel)
- **Deploy**: Gunicorn, nginx

---

## 📝 Roadmap

- [ ] Notificações em tempo real (WebSocket)
- [ ] Integração com WhatsApp/Telegram
- [ ] API RESTful completa com Swagger
- [ ] Mobile app nativa (React Native)
- [ ] Dashboard avançado com gráficos (Chart.js)
- [ ] Backup automático na nuvem
- [ ] Suporte a múltiplos idiomas (i18n)
- [ ] Testes automatizados (pytest)
- [ ] Docker Compose para desenvolvimento
- [ ] CI/CD com GitHub Actions

---

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor:

1. Faça um Fork
2. Crie uma branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto é de uso interno da Texneo. Todos os direitos reservados.

---

## 📞 Contato e Suporte

**Desenvolvedor:** Sheila Oliveira  
**Email:** sheila.oliveira@texneo.com  
**GitHub:** [@SheilaOliveiraTexneo](https://github.com/SheilaOliveiraTexneo)  

Para reportar bugs ou solicitar features, abra uma issue no repositório.

---

## ❤️ Agradecimentos

- Inspirado em sistemas de controle de estoque profissionais
- Desenvolvido com ❤️ e ☕
- Obrigado a todos que contribuíram!

---

**Versão**: 1.0.0  
**Data**: Julho 2026  
**Status**: ✅ Production Ready

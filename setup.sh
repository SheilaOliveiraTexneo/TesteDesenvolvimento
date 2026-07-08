#!/bin/bash
# Script de inicialização do projeto

echo "========================================"
echo "Sistema de Controle de Estoque"
echo "Script de Inicialização"
echo "========================================"
echo ""

# Criar ambiente virtual
echo "📦 Criando ambiente virtual..."
python3 -m venv venv

# Ativar ambiente virtual
echo "🔌 Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências
echo "📚 Instalando dependências..."
pip install -r requirements.txt

# Criar arquivo .env
if [ ! -f .env ]; then
    echo "⚙️  Criando arquivo .env..."
    cp .env.example .env
fi

# Criar pasta de uploads
echo "📁 Criando pasta de uploads..."
mkdir -p app/static/uploads/produtos
mkdir -p app/static/uploads/partidas

# Inicializar banco de dados
echo "🗄️  Inicializando banco de dados..."
python run.py init-db

echo ""
echo "✅ Instalação concluída com sucesso!"
echo ""
echo "📌 Para iniciar o servidor, execute:"
echo "   source venv/bin/activate"
echo "   python run.py"
echo ""
echo "🌐 Acesse em: http://localhost:5000"
echo ""
echo "👤 Usuários padrão:"
echo "   Admin: admin@estoque.com / admin123"
echo "   Operador: operador@estoque.com / operador123"
echo "   Consulta: consulta@estoque.com / consulta123"
echo ""

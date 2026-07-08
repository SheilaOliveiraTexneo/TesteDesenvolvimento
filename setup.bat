@echo off
REM Script de inicialização do projeto (Windows)

echo ========================================
echo Sistema de Controle de Estoque
echo Script de Inicializacao
echo ========================================
echo.

REM Criar ambiente virtual
echo Package instalacao em progresso...
python -m venv venv

REM Ativar ambiente virtual
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Instalar dependências
echo Instalando dependências...
pip install -r requirements.txt

REM Criar arquivo .env
if not exist .env (
    echo Criando arquivo .env...
    copy .env.example .env
)

REM Criar pasta de uploads
echo Criando pasta de uploads...
if not exist "app\static\uploads\produtos" mkdir app\static\uploads\produtos
if not exist "app\static\uploads\partidas" mkdir app\static\uploads\partidas

REM Inicializar banco de dados
echo Inicializando banco de dados...
python run.py init-db

echo.
echo Instalacao concluida com sucesso!
echo.
echo Para iniciar o servidor, execute:
echo    venv\Scripts\activate.bat
echo    python run.py
echo.
echo Acesse em: http://localhost:5000
echo.
echo Usuarios padrao:
echo    Admin: admin@estoque.com / admin123
echo    Operador: operador@estoque.com / operador123
echo    Consulta: consulta@estoque.com / consulta123
echo.
pause

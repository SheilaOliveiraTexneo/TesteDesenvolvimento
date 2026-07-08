import os
from app import create_app, db
from app.models import User, Produto, Partida, Solicitante, Solicitacao, AuditoriaLog

config_name = os.environ.get('FLASK_ENV', 'development')
app = create_app(config_name)

@app.shell_context_processor
def make_shell_context():
    """Contexto do shell Flask"""
    return {
        'db': db,
        'User': User,
        'Produto': Produto,
        'Partida': Partida,
        'Solicitante': Solicitante,
        'Solicitacao': Solicitacao,
        'AuditoriaLog': AuditoriaLog
    }

@app.cli.command()
def init_db():
    """Inicializa o banco de dados com dados de exemplo"""
    db.create_all()
    
    # Criar usuários padrão
    if User.query.first() is None:
        admin = User(
            username='admin',
            email='admin@estoque.com',
            role='admin'
        )
        admin.set_password('admin123')
        
        operador = User(
            username='operador',
            email='operador@estoque.com',
            role='operador'
        )
        operador.set_password('operador123')
        
        consulta = User(
            username='consulta',
            email='consulta@estoque.com',
            role='consulta'
        )
        consulta.set_password('consulta123')
        
        db.session.add(admin)
        db.session.add(operador)
        db.session.add(consulta)
        db.session.commit()
        
        print('✅ Banco de dados inicializado com usuários padrão')
    else:
        print('ℹ️ Banco de dados já contém dados')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

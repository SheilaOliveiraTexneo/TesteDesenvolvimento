from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name='development'):
    """Factory para criar a aplicação Flask"""
    app = Flask(__name__)
    
    # Configuração
    app.config.from_object(config[config_name])
    
    # Criar pasta de uploads
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Inicializar extensões
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor, faça login para acessar esta página.'
    login_manager.login_message_category = 'info'
    
    # Registrar blueprints
    from app.routes import auth_bp, main_bp, produtos_bp, partidas_bp, solicitantes_bp, solicitacoes_bp, dashboard_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(produtos_bp)
    app.register_blueprint(partidas_bp)
    app.register_blueprint(solicitantes_bp)
    app.register_blueprint(solicitacoes_bp)
    app.register_blueprint(dashboard_bp)
    
    # Contexto de aplicação
    with app.app_context():
        db.create_all()
    
    return app

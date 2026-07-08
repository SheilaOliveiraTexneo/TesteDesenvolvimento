from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    """Modelo de Usuário"""
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='consulta')  # admin, operador, consulta
    ativo = db.Column(db.Boolean, default=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    ultimo_acesso = db.Column(db.DateTime)
    
    def set_password(self, password):
        """Define a senha criptografada"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verifica se a senha está correta"""
        return check_password_hash(self.password_hash, password)
    
    def tem_permissao(self, permissao):
        """Verifica se o usuário tem permissão"""
        if self.role == 'admin':
            return True
        
        permissoes = {
            'operador': ['visualizar', 'criar', 'editar', 'deletar_solicitacao'],
            'consulta': ['visualizar']
        }
        
        return permissao in permissoes.get(self.role, [])
    
    def __repr__(self):
        return f'<User {self.username}>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

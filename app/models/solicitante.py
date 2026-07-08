from app import db
from datetime import datetime

class Solicitante(db.Model):
    """Modelo de Solicitante"""
    __tablename__ = 'solicitantes'
    
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), unique=True, nullable=False, index=True)
    nome = db.Column(db.String(255), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamentos
    solicitacoes = db.relationship('Solicitacao', backref='solicitante', lazy=True)
    
    def __repr__(self):
        return f'<Solicitante {self.codigo}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'nome': self.nome,
            'data_criacao': self.data_criacao.isoformat(),
            'data_atualizacao': self.data_atualizacao.isoformat()
        }

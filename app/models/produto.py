from app import db
from datetime import datetime

class Produto(db.Model):
    """Modelo de Produto"""
    __tablename__ = 'produtos'
    
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), unique=True, nullable=False, index=True)
    descricao = db.Column(db.String(255), nullable=False)
    foto = db.Column(db.String(255))
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamentos
    partidas = db.relationship('Partida', backref='produto', lazy=True, cascade='all, delete-orphan')
    solicitacoes = db.relationship('Solicitacao', backref='produto', lazy=True)
    
    def __repr__(self):
        return f'<Produto {self.codigo}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'descricao': self.descricao,
            'foto': self.foto,
            'data_criacao': self.data_criacao.isoformat(),
            'data_atualizacao': self.data_atualizacao.isoformat()
        }

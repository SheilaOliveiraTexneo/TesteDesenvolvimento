from app import db
from datetime import datetime

class Partida(db.Model):
    """Modelo de Partida"""
    __tablename__ = 'partidas'
    
    id = db.Column(db.Integer, primary_key=True)
    id_partida = db.Column(db.String(50), unique=True, nullable=False, index=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamentos
    solicitacoes = db.relationship('Solicitacao', backref='partida', lazy=True)
    
    def __repr__(self):
        return f'<Partida {self.id_partida}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'id_partida': self.id_partida,
            'produto_id': self.produto_id,
            'produto_codigo': self.produto.codigo,
            'produto_descricao': self.produto.descricao,
            'data_criacao': self.data_criacao.isoformat(),
            'data_atualizacao': self.data_atualizacao.isoformat()
        }

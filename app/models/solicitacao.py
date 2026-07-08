from app import db
from datetime import datetime

class Solicitacao(db.Model):
    """Modelo de Solicitação de Estoque"""
    __tablename__ = 'solicitacoes'
    
    id = db.Column(db.Integer, primary_key=True)
    id_solicitacao = db.Column(db.String(10), unique=True, nullable=False, index=True)
    partida_id = db.Column(db.Integer, db.ForeignKey('partidas.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    solicitante_id = db.Column(db.Integer, db.ForeignKey('solicitantes.id'), nullable=False)
    prioridade = db.Column(db.Integer, default=3)  # 1-5, onde 1 é mais importante
    lote = db.Column(db.String(100))
    numero_rocas = db.Column(db.Integer)
    data_solicitacao = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='solicitado')  # solicitado, em_atendimento, finalizado
    observacoes = db.Column(db.Text)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Solicitacao {self.id_solicitacao}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'id_solicitacao': self.id_solicitacao,
            'partida_id': self.partida_id,
            'produto': self.produto.to_dict(),
            'solicitante': self.solicitante.to_dict(),
            'prioridade': self.prioridade,
            'lote': self.lote,
            'numero_rocas': self.numero_rocas,
            'data_solicitacao': self.data_solicitacao.isoformat(),
            'status': self.status,
            'observacoes': self.observacoes,
            'data_criacao': self.data_criacao.isoformat(),
            'data_atualizacao': self.data_atualizacao.isoformat()
        }
    
    @staticmethod
    def gerar_id_solicitacao():
        """Gera o próximo ID de solicitação"""
        ultima = Solicitacao.query.order_by(Solicitacao.id.desc()).first()
        if ultima:
            numero = int(ultima.id_solicitacao) + 1
        else:
            numero = 1
        return str(numero).zfill(6)

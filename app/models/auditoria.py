from app import db
from datetime import datetime
from flask_login import current_user

class AuditoriaLog(db.Model):
    """Modelo de Log de Auditoria"""
    __tablename__ = 'auditoria_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    tabela = db.Column(db.String(100), nullable=False)
    operacao = db.Column(db.String(20), nullable=False)  # INSERT, UPDATE, DELETE
    registro_id = db.Column(db.Integer)
    dados_antes = db.Column(db.Text)
    dados_depois = db.Column(db.Text)
    descricao = db.Column(db.Text)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<AuditoriaLog {self.tabela} {self.operacao}>'
    
    @staticmethod
    def registrar(tabela, operacao, registro_id, dados_antes=None, dados_depois=None, descricao=None):
        """Registra uma auditoria"""
        usuario_id = current_user.id if current_user.is_authenticated else None
        
        log = AuditoriaLog(
            usuario_id=usuario_id,
            tabela=tabela,
            operacao=operacao,
            registro_id=registro_id,
            dados_antes=dados_antes,
            dados_depois=dados_depois,
            descricao=descricao
        )
        
        db.session.add(log)
        db.session.commit()

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Solicitacao, Produto, Solicitante
from sqlalchemy import func

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
@login_required
def index():
    """Dashboard principal com indicadores"""
    total_solicitacoes = Solicitacao.query.count()
    solicitado = Solicitacao.query.filter_by(status='solicitado').count()
    em_atendimento = Solicitacao.query.filter_by(status='em_atendimento').count()
    finalizado = Solicitacao.query.filter_by(status='finalizado').count()
    
    # Contar por prioridade
    por_prioridade = {}
    for i in range(1, 6):
        por_prioridade[f'prioridade_{i}'] = Solicitacao.query.filter_by(prioridade=i).count()
    
    # Últimas 5 solicitações
    ultimas_solicitacoes = Solicitacao.query.order_by(Solicitacao.data_criacao.desc()).limit(5).all()
    
    contexto = {
        'total_solicitacoes': total_solicitacoes,
        'solicitado': solicitado,
        'em_atendimento': em_atendimento,
        'finalizado': finalizado,
        'por_prioridade': por_prioridade,
        'ultimas_solicitacoes': ultimas_solicitacoes
    }
    
    return render_template('dashboard/index.html', **contexto)

@dashboard_bp.route('/kanban')
@login_required
def kanban():
    """Painel Kanban de atendimento"""
    solicitacoes = Solicitacao.query.order_by(
        Solicitacao.status,
        Solicitacao.prioridade,
        Solicitacao.data_solicitacao
    ).all()
    
    # Agrupar por status
    por_status = {
        'solicitado': [],
        'em_atendimento': [],
        'finalizado': []
    }
    
    for sol in solicitacoes:
        por_status[sol.status].append(sol)
    
    return render_template('dashboard/kanban.html', por_status=por_status)

@dashboard_bp.route('/atendimento')
@login_required
def fila_atendimento():
    """Fila de atendimento"""
    if not current_user.tem_permissao('editar'):
        flash('Você não tem permissão para acessar esta página', 'danger')
        return redirect(url_for('dashboard.index'))
    
    # Buscar por status e prioridade
    solicitado = Solicitacao.query.filter_by(status='solicitado').order_by(
        Solicitacao.prioridade,
        Solicitacao.data_solicitacao
    ).all()
    
    em_atendimento = Solicitacao.query.filter_by(status='em_atendimento').order_by(
        Solicitacao.prioridade,
        Solicitacao.data_solicitacao
    ).all()
    
    return render_template(
        'dashboard/fila_atendimento.html',
        solicitado=solicitado,
        em_atendimento=em_atendimento
    )

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Solicitante, AuditoriaLog

solicitantes_bp = Blueprint('solicitantes', __name__, url_prefix='/solicitantes')

@solicitantes_bp.route('/')
@login_required
def listar():
    """Lista todos os solicitantes"""
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    search_type = request.args.get('search_type', 'codigo')
    sort_by = request.args.get('sort', 'codigo')
    order = request.args.get('order', 'asc')
    
    query = Solicitante.query
    
    if search:
        if search_type == 'codigo':
            query = query.filter(Solicitante.codigo.ilike(f'%{search}%'))
        else:  # nome
            query = query.filter(Solicitante.nome.ilike(f'%{search}%'))
    
    # Ordenamento
    order_column = getattr(Solicitante, sort_by, Solicitante.codigo)
    query = query.order_by(order_column.asc() if order == 'asc' else order_column.desc())
    
    paginated = query.paginate(page=page, per_page=10)
    
    return render_template(
        'solicitantes/listar.html',
        solicitantes=paginated.items,
        paginated=paginated,
        search=search,
        search_type=search_type,
        sort_by=sort_by,
        order=order
    )

@solicitantes_bp.route('/novo', methods=['GET', 'POST'])
@login_required
def novo():
    """Criar novo solicitante"""
    if not current_user.tem_permissao('criar'):
        flash('Você não tem permissão para criar solicitantes', 'danger')
        return redirect(url_for('solicitantes.listar'))
    
    if request.method == 'POST':
        codigo = request.form.get('codigo').strip()
        nome = request.form.get('nome').strip()
        
        # Validar
        if Solicitante.query.filter_by(codigo=codigo).first():
            flash(f'Solicitante com código {codigo} já existe', 'danger')
            return redirect(url_for('solicitantes.novo'))
        
        solicitante = Solicitante(codigo=codigo, nome=nome)
        db.session.add(solicitante)
        db.session.flush()
        
        # Registrar auditoria
        AuditoriaLog.registrar(
            'solicitantes',
            'INSERT',
            solicitante.id,
            dados_depois=str(solicitante.to_dict()),
            descricao=f'Novo solicitante criado: {codigo}'
        )
        
        db.session.commit()
        flash(f'Solicitante {codigo} criado com sucesso', 'success')
        return redirect(url_for('solicitantes.listar'))
    
    return render_template('solicitantes/form.html', solicitante=None)

@solicitantes_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar(id):
    """Editar solicitante"""
    if not current_user.tem_permissao('editar'):
        flash('Você não tem permissão para editar solicitantes', 'danger')
        return redirect(url_for('solicitantes.listar'))
    
    solicitante = Solicitante.query.get_or_404(id)
    
    if request.method == 'POST':
        novo_codigo = request.form.get('codigo').strip()
        nome = request.form.get('nome').strip()
        
        # Verificar se código já existe
        if novo_codigo != solicitante.codigo:
            if Solicitante.query.filter_by(codigo=novo_codigo).first():
                flash(f'Solicitante com código {novo_codigo} já existe', 'danger')
                return redirect(url_for('solicitantes.editar', id=id))
        
        dados_antes = str(solicitante.to_dict())
        
        solicitante.codigo = novo_codigo
        solicitante.nome = nome
        
        db.session.commit()
        
        # Registrar auditoria
        AuditoriaLog.registrar(
            'solicitantes',
            'UPDATE',
            solicitante.id,
            dados_antes=dados_antes,
            dados_depois=str(solicitante.to_dict()),
            descricao=f'Solicitante {novo_codigo} atualizado'
        )
        
        flash('Solicitante atualizado com sucesso', 'success')
        return redirect(url_for('solicitantes.listar'))
    
    return render_template('solicitantes/form.html', solicitante=solicitante)

@solicitantes_bp.route('/<int:id>/deletar', methods=['POST'])
@login_required
def deletar(id):
    """Deletar solicitante"""
    if not current_user.tem_permissao('deletar'):
        flash('Você não tem permissão para deletar solicitantes', 'danger')
        return redirect(url_for('solicitantes.listar'))
    
    solicitante = Solicitante.query.get_or_404(id)
    
    # Verificar se possui solicitações
    if solicitante.solicitacoes:
        flash('Não é possível deletar um solicitante com solicitações', 'danger')
        return redirect(url_for('solicitantes.listar'))
    
    dados_antes = str(solicitante.to_dict())
    
    db.session.delete(solicitante)
    db.session.commit()
    
    # Registrar auditoria
    AuditoriaLog.registrar(
        'solicitantes',
        'DELETE',
        id,
        dados_antes=dados_antes,
        descricao=f'Solicitante deletado: {solicitante.codigo}'
    )
    
    flash('Solicitante deletado com sucesso', 'success')
    return redirect(url_for('solicitantes.listar'))

@solicitantes_bp.route('/api/buscar/<codigo>')
@login_required
def api_buscar(codigo):
    """API para buscar solicitante"""
    solicitante = Solicitante.query.filter_by(codigo=codigo).first()
    
    if solicitante:
        return jsonify(solicitante.to_dict())
    
    return jsonify({'erro': 'Solicitante não encontrado'}), 404

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Partida, Produto, AuditoriaLog

partidas_bp = Blueprint('partidas', __name__, url_prefix='/partidas')

@partidas_bp.route('/')
@login_required
def listar():
    """Lista todas as partidas"""
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    search_type = request.args.get('search_type', 'partida')
    sort_by = request.args.get('sort', 'id_partida')
    order = request.args.get('order', 'asc')
    
    query = Partida.query.join(Produto)
    
    if search:
        if search_type == 'partida':
            query = query.filter(Partida.id_partida.ilike(f'%{search}%'))
        else:  # produto
            query = query.filter(
                db.or_(
                    Produto.codigo.ilike(f'%{search}%'),
                    Produto.descricao.ilike(f'%{search}%')
                )
            )
    
    # Ordenamento
    if sort_by == 'codigo_produto':
        order_column = Produto.codigo
    else:
        order_column = getattr(Partida, sort_by, Partida.id_partida)
    
    query = query.order_by(order_column.asc() if order == 'asc' else order_column.desc())
    
    paginated = query.paginate(page=page, per_page=10)
    
    return render_template(
        'partidas/listar.html',
        partidas=paginated.items,
        paginated=paginated,
        search=search,
        search_type=search_type,
        sort_by=sort_by,
        order=order
    )

@partidas_bp.route('/novo', methods=['GET', 'POST'])
@login_required
def novo():
    """Criar nova partida"""
    if not current_user.tem_permissao('criar'):
        flash('Você não tem permissão para criar partidas', 'danger')
        return redirect(url_for('partidas.listar'))
    
    if request.method == 'POST':
        id_partida = request.form.get('id_partida').strip()
        produto_codigo = request.form.get('produto_codigo').strip()
        
        # Validar partida
        if Partida.query.filter_by(id_partida=id_partida).first():
            flash(f'Partida {id_partida} já existe', 'danger')
            return redirect(url_for('partidas.novo'))
        
        # Buscar produto
        produto = Produto.query.filter_by(codigo=produto_codigo).first()
        if not produto:
            flash(f'Produto {produto_codigo} não encontrado', 'danger')
            return redirect(url_for('partidas.novo'))
        
        partida = Partida(id_partida=id_partida, produto_id=produto.id)
        db.session.add(partida)
        db.session.flush()
        
        # Registrar auditoria
        AuditoriaLog.registrar(
            'partidas',
            'INSERT',
            partida.id,
            dados_depois=str(partida.to_dict()),
            descricao=f'Nova partida criada: {id_partida}'
        )
        
        db.session.commit()
        flash(f'Partida {id_partida} criada com sucesso', 'success')
        return redirect(url_for('partidas.listar'))
    
    return render_template('partidas/form.html', partida=None, produtos=Produto.query.all())

@partidas_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar(id):
    """Editar partida"""
    if not current_user.tem_permissao('editar'):
        flash('Você não tem permissão para editar partidas', 'danger')
        return redirect(url_for('partidas.listar'))
    
    partida = Partida.query.get_or_404(id)
    
    if request.method == 'POST':
        id_partida = request.form.get('id_partida').strip()
        produto_codigo = request.form.get('produto_codigo').strip()
        
        # Verificar ID duplicado
        if id_partida != partida.id_partida:
            if Partida.query.filter_by(id_partida=id_partida).first():
                flash(f'Partida {id_partida} já existe', 'danger')
                return redirect(url_for('partidas.editar', id=id))
        
        # Buscar produto
        produto = Produto.query.filter_by(codigo=produto_codigo).first()
        if not produto:
            flash(f'Produto {produto_codigo} não encontrado', 'danger')
            return redirect(url_for('partidas.editar', id=id))
        
        dados_antes = str(partida.to_dict())
        
        partida.id_partida = id_partida
        partida.produto_id = produto.id
        
        db.session.commit()
        
        # Registrar auditoria
        AuditoriaLog.registrar(
            'partidas',
            'UPDATE',
            partida.id,
            dados_antes=dados_antes,
            dados_depois=str(partida.to_dict()),
            descricao=f'Partida {id_partida} atualizada'
        )
        
        flash('Partida atualizada com sucesso', 'success')
        return redirect(url_for('partidas.listar'))
    
    return render_template('partidas/form.html', partida=partida, produtos=Produto.query.all())

@partidas_bp.route('/<int:id>/deletar', methods=['POST'])
@login_required
def deletar(id):
    """Deletar partida"""
    if not current_user.tem_permissao('deletar'):
        flash('Você não tem permissão para deletar partidas', 'danger')
        return redirect(url_for('partidas.listar'))
    
    partida = Partida.query.get_or_404(id)
    
    # Verificar se possui solicitações
    if partida.solicitacoes:
        flash('Não é possível deletar uma partida com solicitações', 'danger')
        return redirect(url_for('partidas.listar'))
    
    dados_antes = str(partida.to_dict())
    
    db.session.delete(partida)
    db.session.commit()
    
    # Registrar auditoria
    AuditoriaLog.registrar(
        'partidas',
        'DELETE',
        id,
        dados_antes=dados_antes,
        descricao=f'Partida deletada: {partida.id_partida}'
    )
    
    flash('Partida deletada com sucesso', 'success')
    return redirect(url_for('partidas.listar'))

@partidas_bp.route('/api/buscar/<id_partida>')
@login_required
def api_buscar(id_partida):
    """API para buscar partida"""
    partida = Partida.query.filter_by(id_partida=id_partida).first()
    
    if partida:
        return jsonify(partida.to_dict())
    
    return jsonify({'erro': 'Partida não encontrada'}), 404

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Produto, AuditoriaLog
from app.utils import allowed_file, save_picture
import os

produtos_bp = Blueprint('produtos', __name__, url_prefix='/produtos')

@produtos_bp.route('/')
@login_required
def listar():
    """Lista todos os produtos"""
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    sort_by = request.args.get('sort', 'codigo')
    order = request.args.get('order', 'asc')
    
    query = Produto.query
    
    if search:
        query = query.filter(
            db.or_(
                Produto.codigo.ilike(f'%{search}%'),
                Produto.descricao.ilike(f'%{search}%')
            )
        )
    
    # Ordenamento
    order_column = getattr(Produto, sort_by, Produto.codigo)
    query = query.order_by(order_column.asc() if order == 'asc' else order_column.desc())
    
    paginated = query.paginate(page=page, per_page=10)
    
    return render_template(
        'produtos/listar.html',
        produtos=paginated.items,
        paginated=paginated,
        search=search,
        sort_by=sort_by,
        order=order
    )

@produtos_bp.route('/novo', methods=['GET', 'POST'])
@login_required
def novo():
    """Criar novo produto"""
    if not current_user.tem_permissao('criar'):
        flash('Você não tem permissão para criar produtos', 'danger')
        return redirect(url_for('produtos.listar'))
    
    if request.method == 'POST':
        codigo = request.form.get('codigo').strip()
        descricao = request.form.get('descricao').strip()
        
        # Validar
        if Produto.query.filter_by(codigo=codigo).first():
            flash(f'Produto com código {codigo} já existe', 'danger')
            return redirect(url_for('produtos.novo'))
        
        produto = Produto(codigo=codigo, descricao=descricao)
        
        # Salvar foto
        if 'foto' in request.files:
            file = request.files['foto']
            if file and allowed_file(file.filename):
                filename = save_picture(file, 'produtos')
                produto.foto = filename
        
        db.session.add(produto)
        db.session.flush()
        
        # Registrar auditoria
        AuditoriaLog.registrar(
            'produtos',
            'INSERT',
            produto.id,
            dados_depois=str(produto.to_dict()),
            descricao=f'Novo produto criado: {codigo}'
        )
        
        db.session.commit()
        flash(f'Produto {codigo} criado com sucesso', 'success')
        return redirect(url_for('produtos.listar'))
    
    return render_template('produtos/form.html', produto=None)

@produtos_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar(id):
    """Editar produto"""
    if not current_user.tem_permissao('editar'):
        flash('Você não tem permissão para editar produtos', 'danger')
        return redirect(url_for('produtos.listar'))
    
    produto = Produto.query.get_or_404(id)
    
    if request.method == 'POST':
        novo_codigo = request.form.get('codigo').strip()
        descricao = request.form.get('descricao').strip()
        
        # Verificar se código já existe em outro produto
        if novo_codigo != produto.codigo:
            if Produto.query.filter_by(codigo=novo_codigo).first():
                flash(f'Produto com código {novo_codigo} já existe', 'danger')
                return redirect(url_for('produtos.editar', id=id))
        
        dados_antes = str(produto.to_dict())
        
        produto.codigo = novo_codigo
        produto.descricao = descricao
        
        # Salvar foto
        if 'foto' in request.files:
            file = request.files['foto']
            if file and allowed_file(file.filename):
                filename = save_picture(file, 'produtos')
                produto.foto = filename
        
        db.session.commit()
        
        # Registrar auditoria
        AuditoriaLog.registrar(
            'produtos',
            'UPDATE',
            produto.id,
            dados_antes=dados_antes,
            dados_depois=str(produto.to_dict()),
            descricao=f'Produto {novo_codigo} atualizado'
        )
        
        flash('Produto atualizado com sucesso', 'success')
        return redirect(url_for('produtos.listar'))
    
    return render_template('produtos/form.html', produto=produto)

@produtos_bp.route('/<int:id>/deletar', methods=['POST'])
@login_required
def deletar(id):
    """Deletar produto"""
    if not current_user.tem_permissao('deletar'):
        flash('Você não tem permissão para deletar produtos', 'danger')
        return redirect(url_for('produtos.listar'))
    
    produto = Produto.query.get_or_404(id)
    
    # Verificar se possui partidas
    if produto.partidas:
        flash('Não é possível deletar um produto com partidas', 'danger')
        return redirect(url_for('produtos.listar'))
    
    dados_antes = str(produto.to_dict())
    
    db.session.delete(produto)
    db.session.commit()
    
    # Registrar auditoria
    AuditoriaLog.registrar(
        'produtos',
        'DELETE',
        id,
        dados_antes=dados_antes,
        descricao=f'Produto deletado: {produto.codigo}'
    )
    
    flash('Produto deletado com sucesso', 'success')
    return redirect(url_for('produtos.listar'))

@produtos_bp.route('/api/buscar/<codigo>')
@login_required
def api_buscar(codigo):
    """API para buscar produto"""
    produto = Produto.query.filter_by(codigo=codigo).first()
    
    if produto:
        return jsonify(produto.to_dict())
    
    return jsonify({'erro': 'Produto não encontrado'}), 404

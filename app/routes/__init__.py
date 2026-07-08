from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User
from datetime import datetime

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user is None or not user.check_password(password):
            flash('Email ou senha inválidos', 'danger')
            return redirect(url_for('auth.login'))
        
        if not user.ativo:
            flash('Usuário inativo', 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user)
        user.ultimo_acesso = datetime.utcnow()
        db.session.commit()
        
        flash(f'Bem-vindo, {user.username}!', 'success')
        return redirect(url_for('dashboard.index'))
    
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    """Realiza logout"""
    logout_user()
    flash('Você foi desconectado', 'info')
    return redirect(url_for('auth.login'))

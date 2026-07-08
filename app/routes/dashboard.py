from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Página principal - redireciona para dashboard"""
    from flask_login import current_user
    from flask import redirect, url_for
    
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    return redirect(url_for('auth.login'))

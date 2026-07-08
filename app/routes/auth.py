from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Produto, Partida, Solicitante, Solicitacao, AuditoriaLog
from app.utils import allowed_file, save_picture
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    """Página principal"""
    return redirect(url_for('dashboard.index'))

from werkzeug.utils import secure_filename
from app import db
import os
from datetime import datetime

def allowed_file(filename):
    """Verifica se o arquivo é permitido"""
    from config import Config
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def save_picture(file, folder):
    """Salva a imagem no servidor"""
    from config import Config
    
    filename = secure_filename(file.filename)
    # Adicionar timestamp para garantir unicidade
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
    filename = timestamp + filename
    
    folder_path = os.path.join(Config.UPLOAD_FOLDER, folder)
    os.makedirs(folder_path, exist_ok=True)
    
    file.save(os.path.join(folder_path, filename))
    
    return os.path.join(folder, filename)

def get_prioridade_cor(prioridade):
    """Retorna cor baseada na prioridade"""
    cores = {
        1: '#dc3545',  # Vermelho
        2: '#fd7e14',  # Laranja
        3: '#ffc107',  # Amarelo
        4: '#0d6efd',  # Azul
        5: '#198754'   # Verde
    }
    return cores.get(prioridade, '#6c757d')  # Cinza padrão

def get_status_badge(status):
    """Retorna classe Bootstrap para status"""
    badges = {
        'solicitado': 'badge-primary',
        'em_atendimento': 'badge-warning',
        'finalizado': 'badge-success'
    }
    return badges.get(status, 'badge-secondary')

from datetime import datetime
from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    rol = db.Column(db.String(20), nullable=False)
    aula_id = db.Column(db.Integer, db.ForeignKey('aula.id'))

class Aula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), unique=True, nullable=False)

class RegistroAsistencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(10), nullable=False)  # 'PRESENTE' o 'AUSENTE'

from app import create_app
from app.extensions import db
from app.models import User  # o cualquier modelo que hayas creado

app = create_app()

with app.app_context():
    # Crear las tablas en la base de datos
    db.create_all()

    # Crear un nuevo usuario de prueba
    test_user = User(name="Test", email="test@example.com", role="teacher")
    db.session.add(test_user)
    db.session.commit()

    # Consultar la base de datos
    users = User.query.all()
    for user in users:
        print(f"{user.id}: {user.name} - {user.email}")

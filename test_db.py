from app import create_app, db
from app.models import Role, User, Classroom, AttendanceRecord, TutorStudent, PasswordResetToken

def test_tables():
    print("Checking if tables exist in the database...")

    inspector = db.inspect(db.engine)
    tables = inspector.get_table_names()

    expected_tables = {
        'roles',
        'users',
        'classrooms',
        'attendance_records',
        'tutor_student',
        'password_reset_tokens'
    }

    missing = expected_tables - set(tables)

    if not missing:
        print("✅ All expected tables are present:")
        for table in sorted(tables):
            print(f"  - {table}")
    else:
        print("❌ Missing tables:")
        for table in missing:
            print(f"  - {table}")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        test_tables()

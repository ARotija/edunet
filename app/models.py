from datetime import datetime
from app import db

class Role(db.Model):
    __tablename__ = "roles"
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    # e.g. "STUDENT", "TEACHER", "TUTOR"

class Classroom(db.Model):
    __tablename__ = "classrooms"
    id     = db.Column(db.Integer, primary_key=True)
    name   = db.Column(db.String(64), unique=True, nullable=False)
    # e.g. "Room 101", "Aula A"

class User(db.Model):
    __tablename__ = "users"
    id             = db.Column(db.Integer, primary_key=True)
    email          = db.Column(db.String(120), unique=True, nullable=False)
    password_hash  = db.Column(db.String(128), nullable=False)
    role_id        = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    classroom_id   = db.Column(db.Integer, db.ForeignKey("classrooms.id"), nullable=True)
    # relationships:
    role           = db.relationship("Role", backref="users")
    classroom      = db.relationship("Classroom", backref="students")
    # Tutors and their students:
    tutor_students = db.relationship(
        "TutorStudent",
        back_populates="tutor",
        cascade="all, delete-orphan",
    )
    # As a student:
    tutor_links    = db.relationship(
        "TutorStudent",
        back_populates="student",
        cascade="all, delete-orphan",
    )

class TutorStudent(db.Model):
    __tablename__ = "tutor_student"
    id         = db.Column(db.Integer, primary_key=True)
    tutor_id   = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # relationships:
    tutor      = db.relationship("User", foreign_keys=[tutor_id], back_populates="tutor_students")
    student    = db.relationship("User", foreign_keys=[student_id], back_populates="tutor_links")

class AttendanceRecord(db.Model):
    __tablename__ = "attendance_records"
    id           = db.Column(db.Integer, primary_key=True)
    user_id      = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    classroom_id = db.Column(db.Integer, db.ForeignKey("classrooms.id"), nullable=False)
    timestamp    = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status       = db.Column(db.String(10), nullable=False)
    # status = "PRESENT" or "ABSENT"
    # relationships:
    user         = db.relationship("User", backref="attendance_records")
    classroom    = db.relationship("Classroom", backref="attendance_records")

class PasswordResetToken(db.Model):
    __tablename__ = "password_reset_tokens"
    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    token      = db.Column(db.String(128), unique=True, nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    used       = db.Column(db.Boolean, default=False, nullable=False)
    # relationship:
    user       = db.relationship("User", backref="reset_tokens")

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change_me_in_production")
    if not SECRET_KEY:
        raise RuntimeError("SECRET_KEY is not defined. Add it in .flaskenv.")
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + os.path.join(BASEDIR, "app.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

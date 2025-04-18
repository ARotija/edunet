import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise RuntimeError("SECRET_KEY is not defined. Add it in .flaskenv.")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

from flask import Flask 
from .config import config
from .db import db, migrate
from .models import *
from  .routes import student_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(student_bp, url_prefix="/student")

    return app
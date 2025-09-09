from flask import Flask 
from .config import config
from .db import db, migrate
from .models import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    return app
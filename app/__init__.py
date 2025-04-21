from flask import Flask
from .extensions import db, migrate
from .config import Config
from .routes import product_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(product_bp)

    return app

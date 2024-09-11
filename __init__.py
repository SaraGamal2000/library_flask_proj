from flask import Flask, current_app
from app.config import config_option
from app.models import db
from flask_migrate import Migrate
from app.books import books_blueprints
from flask_bootstrap import Bootstrap5


def my_app(config_name='prd'):
    app=Flask(__name__)
    current_config=config_option[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    db.init_app(app)
    app.config['SECRET_KEY'] = current_config.SECRET_KEY
    bootstrap = Bootstrap5(app)
    migrate=Migrate(app, db)
    app.register_blueprint(books_blueprints)
    return app
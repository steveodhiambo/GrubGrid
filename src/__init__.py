from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import DevelopmentConfig, ProductionConfig
from apifairy import APIFairy
import os

db = SQLAlchemy()
ma = Marshmallow()
api = APIFairy()

def create_app():
    app = Flask(__name__)
    if os.getenv("FLASK_ENV") == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    ma.init_app(app)
    app.config['APIFAIRY_TITLE'] = 'Restaurant API'
    app.config['APIFAIRY_VERSION'] = '1.0'
    api.init_app(app)

    from .routes import menu_routes, item_routes, food_routes
    app.register_blueprint(menu_routes.bp)
    app.register_blueprint(item_routes.bp)
    app.register_blueprint(food_routes.bp)


    return app

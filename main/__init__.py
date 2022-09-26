from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def initialize_db():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'AIzaSyDdkNpKFJt2n8M0gzbWp4q2LbJr1f73rso'
    app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///site.db'
    from main import models
    db.init_app(app)
    return app, db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'AIzaSyDdkNpKFJt2n8M0gzbWp4q2LbJr1f73rso'
    path = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_DATABASE_URI'] = path.replace("postgres", "postgresql")
    # app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///site.db'   

    from main import models
    db.init_app(app)

    from . import routes

    app.register_blueprint(routes.mainbp)

    return app
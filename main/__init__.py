from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'AIzaSyDdkNpKFJt2n8M0gzbWp4q2LbJr1f73rso'

    from . import routes

    app.register_blueprint(routes.mainbp)

    return app
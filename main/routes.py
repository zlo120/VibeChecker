from flask import render_template, redirect, url_for
from flask.blueprints import Blueprint

mainbp = Blueprint('main', __name__)

@mainbp.route("/")
def index():
    return render_template("index.html")
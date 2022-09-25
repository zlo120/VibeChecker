from flask import render_template, redirect, url_for, request, Response, jsonify
from flask.blueprints import Blueprint
import json

mainbp = Blueprint('main', __name__)

@mainbp.route("/")
def index():
    return render_template("index.html")

@mainbp.route("/create")
def create():
    return render_template("form.html")

@mainbp.route("/battle", methods = ['GET', 'POST'])
def battle():
    if request.method == 'POST':
        req = request.get_json()
        return jsonify({'hi':'hello'})

    return render_template("battle.html", curr_url = request.url_rule)
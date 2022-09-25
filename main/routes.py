from webbrowser import get
from flask import render_template, redirect, url_for, request, Response, jsonify
from flask.blueprints import Blueprint
from .utils import getGif
from random import choice
from string import ascii_letters

mainbp = Blueprint('main', __name__)

@mainbp.route("/")
def index():
    return render_template("index.html")

@mainbp.route("/create", methods = ['GET', 'POST'])
def create():
    if request.method == 'POST':
        req = request.get_json()
        # return jsonify({'ID':})

    x = ''.join(choice(ascii_letters) for i in range(6))
    URL = url_for('main.card', ID = '1' + x, _external = True )
    print(URL)
    return render_template("form.html")

@mainbp.route("/card/<string:ID>")
def card(ID): 
    return render_template("cardf.html", url = getGif("crazy"))

@mainbp.route("/battle", methods = ['GET', 'POST'])
def battle():
    if request.method == 'POST':
        req = request.get_json()
        return jsonify({'hi':'hello'})

    return render_template("battle.html", curr_url = request.url_rule)
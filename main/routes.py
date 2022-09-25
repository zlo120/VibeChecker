from inspect import Attribute
from webbrowser import get
from flask import render_template, redirect, url_for, request, Response, jsonify
from flask.blueprints import Blueprint
from .utils import getGif, generateDesc
from .type import *
from .models import Cards
import random

mainbp = Blueprint('main', __name__)

@mainbp.route("/")
def index():
    return render_template("index.html")

@mainbp.route("/form")
def form():
    return render_template("formf.html")

@mainbp.route("/create/<int:ID>/<string:name>")
def create(ID, name):
    if ID == 1:
        gif = getGif(name)
        ck = CryptoKing(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Type = 1,
            Name = name,
            Strength = ck.strength,
            Intelligence = ck.intelligence,
            Wealth = ck.wealth,
            Laziness = ck.laziness,
            Clumsiness = ck.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = ck.URL
        )

    if ID == 2:
        gif = getGif(name)
        ff = FreedomFighter(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Type = 2,
            Name = name,
            Strength = ff.strength,
            Intelligence = ff.intelligence,
            Wealth = ff.wealth,
            Laziness = ff.laziness,
            Clumsiness = ff.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = ff.URL
        )

    if ID == 3:
        gif = getGif(name)
        sjw = SJW(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Type = 3,
            Name = name,
            Strength = sjw.strength,
            Intelligence = sjw.intelligence,
            Wealth = sjw.wealth,
            Laziness = sjw.laziness,
            Clumsiness = sjw.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = sjw.URL
        )

    if ID == 4:
        gif = getGif(name)
        CC = CertifiedChad(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 4,
            Strength = CC.strength,
            Intelligence = CC.intelligence,
            Wealth = CC.wealth,
            Laziness = CC.laziness,
            Clumsiness = CC.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = CC.URL
        )

    if ID == 5:
        gif = getGif(name)
        GJ = GymJunkie(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 5,
            Strength = GJ.strength,
            Intelligence = GJ.intelligence,
            Wealth = GJ.wealth,
            Laziness = GJ.laziness,
            Clumsiness = GJ.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = GJ.URL
        )

    if ID == 6:
        gif = getGif(name)
        TT = TiktokTart(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 6,
            Strength = TT.strength,
            Intelligence = TT.intelligence,
            Wealth = TT.wealth,
            Laziness = TT.laziness,
            Clumsiness = TT.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = TT.URL
        )

    if ID == 7:
        gif = getGif(name)
        NN = NetflixNinja(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 7,
            Strength = NN.strength,
            Intelligence = NN.intelligence,
            Wealth = NN.wealth,
            Laziness = NN.laziness,
            Clumsiness = NN.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = NN.URL
        )
        
    if ID == 8:
        gif = getGif(name)
        SI = SociallyInadequate(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 8,
            Strength = SI.strength,
            Intelligence = SI.intelligence,
            Wealth = SI.wealth,
            Laziness = SI.laziness,
            Clumsiness = SI.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = SI.URL
        )

    if ID == 9:
        gif = getGif(name)
        K = Karen(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 9,
            Strength = K.strength,
            Intelligence = K.intelligence,
            Wealth = K.wealth,
            Laziness = K.laziness,
            Clumsiness = K.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = K.URL
        )

    if ID == 10:
        gif = getGif(name)
        DelD = DelusionalDonut(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 10,
            Strength = DelD.strength,
            Intelligence = DelD.intelligence,
            Wealth = DelD.wealth,
            Laziness = DelD.laziness,
            Clumsiness = DelD.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = DelD.URL
        )
    
    db.session.add(person)
    db.session.commit()
    # url_for('main.card', ID = '1' + ''.join(choice(ascii_letters) for i in range(6)), _external = True ) 
    return render_template("cardf.html", url = gif, person = person)

@mainbp.route("/card/<string:ID>")
def card(ID):
    person = Cards.query.filter_by(URLCode = ID).first()
    try:
        return render_template("cardf.html", url = person.ImageURL, person = person)
    except Exception:
        return "That code is invalid"

@mainbp.route("/processing")
def processing():
    return
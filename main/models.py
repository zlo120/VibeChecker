from . import db

class Cards(db.Model):
    __tablename__ = "cards"
    ID = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement=True)
    Type = db.Column(db.Integer, nullable = False) 
    Description = db.Column(db.String(512), nullable = False, unique = False)
    ImageURL = db.Column(db.String(512), nullable = False, unique = False)
    Name = db.Column(db.String(256), nullable = False, unique = False)
    Strength = db.Column(db.Integer, nullable = False)
    Intelligence = db.Column(db.Integer, nullable = False)
    Wealth = db.Column(db.Integer, nullable = False)
    Laziness = db.Column(db.Integer, nullable = False)
    Clumsiness = db.Column(db.Integer, nullable = False)
    isAVibe = db.Column(db.Integer, nullable = False)
    URLCode = db.Column(db.String(256), nullable = False)
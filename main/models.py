from . import db

class Cards(db.Model):
    __tablename__ = "cards"
    ID = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement=True)
    ImageURL = db.Column(db.String(256), nullable = False, unique = True)
    Name = db.Column(db.String(256), nullable = False, unique = True)
    Strength = db.Column(db.Integer, nullable = False)
    Intelligence = db.Column(db.Integer, nullable = False)
    Wealth = db.Column(db.Integer, nullable = False)
    Laziness = db.Column(db.Integer, nullable = False)
    Clumsiness = db.Column(db.Integer, nullable = False)
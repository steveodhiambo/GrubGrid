from .. import db

class Food(db.Model):
    food_id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(255))
    price = db.Column(db.Integer)
    category = db.Column(db.String(50))

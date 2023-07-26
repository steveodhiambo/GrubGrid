from .. import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(256))
    price = db.Column(db.Float)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))

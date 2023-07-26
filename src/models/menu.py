from .. import db
from ..models.item import Item

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    items = db.relationship('Item', backref='menu', lazy='dynamic')

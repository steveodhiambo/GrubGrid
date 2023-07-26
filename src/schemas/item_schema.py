from .. import ma
from ..models.item import Item

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        include_fk = True
        load_instance = True

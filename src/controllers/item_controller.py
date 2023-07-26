from .. import db
from ..models.item import Item
from ..schemas.item_schema import ItemSchema
from apifairy.decorators import body, response

item_schema = ItemSchema()

@body(ItemSchema)
@response(ItemSchema)
def get_item(item):
    item = Item.query.get(item.id)
    if item is None:
        return {'message': 'Item not found'}, 404
    return item_schema.dump(item)

@body(ItemSchema)
@response(ItemSchema, 201)
def create_item(item):
    db.session.add(item)
    db.session.commit()
    return item_schema.dump(item), 201

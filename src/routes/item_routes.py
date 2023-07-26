from flask import Blueprint
from ..controllers import item_controller
from apifairy import response
from ..schemas.item_schema import ItemSchema

bp = Blueprint('item', __name__,url_prefix='/items')

@bp.route('/<int:item_id>', methods=['GET'])
@response(ItemSchema)
def get_item(item_id):
    """
    Get all items
    ---
    get:
      description: Get item
      responses:
        200:
          description: successful operation
          content:
            application/json:
              schema: ItemSchema
    """
    return item_controller.get_item(item_id)

@bp.route('/', methods=['POST'])
def create_item():
    return item_controller.create_item()

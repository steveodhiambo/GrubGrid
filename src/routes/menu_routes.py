from flask import Blueprint
from ..controllers import menu_controller
from apifairy import response
from ..schemas.menu_schema import MenuSchema

bp = Blueprint('menu', __name__,url_prefix='/menus')

@bp.route('/<int:menu_id>', methods=['GET'])
@response(MenuSchema)
def get_menu(menu_id):
    """
    Get all menus
    ---
    get:
      description: Get menu
      responses:
        200:
          description: successful operation
          content:
            application/json:
              schema: MenuSchema
    """
    return menu_controller.get_menu(menu_id)

@bp.route('/', methods=['POST'])
def create_menu():
    return menu_controller.create_menu()

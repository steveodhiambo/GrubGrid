from .. import db
from ..models.menu import Menu
from ..schemas.menu_schema import MenuSchema
from apifairy.decorators import body, response

menu_schema = MenuSchema()

@body(MenuSchema)
@response(MenuSchema)
def get_menu(menu):
    menu = Menu.query.get(menu.id)
    if menu is None:
        return {'message': 'Menu not found'}, 404
    return menu_schema.dump(menu)

@body(MenuSchema)
@response(MenuSchema, 201)
def create_menu(menu):
    db.session.add(menu)
    db.session.commit()
    return menu_schema.dump(menu), 201

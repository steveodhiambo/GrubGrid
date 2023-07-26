from .. import ma
from ..models.menu import Menu

class MenuSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Menu
        include_relationships = True
        load_instance = True

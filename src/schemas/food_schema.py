from .. import ma
from ..models.food import Food

class FoodSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Food
        include_relationships = True
        load_instance = True
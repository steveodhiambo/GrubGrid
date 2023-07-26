from .. import db
from ..models.food import Food
from ..schemas.food_schema import FoodSchema

food_schema = FoodSchema()

def create_food(food_data):
    food = Food(**food_data)
    db.session.add(food)
    db.session.commit()
    return food_schema.dump(food), 201

def get_food(food_id):
    food = Food.query.get(food_id)
    if food is None:
        return {'message': 'Food not found'}, 404
    return food_schema.dump(food)

def update_food(food_id, food_data):
    food = Food.query.get(food_id)
    if food is None:
        return {'message': 'Food not found'}, 404
    food.update(food_data)
    db.session.commit()
    return food_schema.dump(food)

def delete_food(food_id):
    food = Food.query.get(food_id)
    if food is None:
        return {'message': 'Food not found'}, 404
    db.session.delete(food)
    db.session.commit()
    return '', 204

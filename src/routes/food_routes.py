from flask import Blueprint, request
from ..controllers import food_controller
from apifairy import response, body
from ..schemas.food_schema import FoodSchema

bp = Blueprint('food', __name__, url_prefix='/foods')

@bp.route('/', methods=['POST'])
@body(FoodSchema)
@response(FoodSchema, 201)
def create_food():
    print(request.json)
    return food_controller.create_food(request.json)

@bp.route('/<int:food_id>', methods=['GET'])
@response(FoodSchema)
def get_food(food_id):
    return food_controller.get_food(food_id)

@bp.route('/<int:food_id>', methods=['PUT'])
@body(FoodSchema)
@response(FoodSchema)
def update_food(food_id):
    return food_controller.update_food(food_id, request.json)

@bp.route('/<int:food_id>', methods=['DELETE'])
@response(None,status_code=204)
def delete_food(food_id):
    return food_controller.delete_food(food_id)

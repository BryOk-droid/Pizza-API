from flask import Blueprint

restaurant_pizza_bp = Blueprint("restaurant_pizza_bp", __name__)

@restaurant_pizza_bp.route("/", methods=["GET"])
def index():
    return {"message": "Restaurant Pizzas route working!"}

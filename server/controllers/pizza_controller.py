from flask import Blueprint

pizza_bp = Blueprint("pizza_bp", __name__)

@pizza_bp.route("/", methods=["GET"])
def index():
    return {"message": "Pizzas route working!"}

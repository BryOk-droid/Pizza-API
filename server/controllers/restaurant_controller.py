from flask import Blueprint

restaurant_bp = Blueprint("restaurant_bp", __name__)

@restaurant_bp.route("/", methods=["GET"])
def index():
    return {"message": "Restaurants route working!"}

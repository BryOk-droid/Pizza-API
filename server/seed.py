from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza


app = create_app()

with app.app_context():
    print("Clearing existing data...")
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    print("Seeding restaurants...")
    r1 = Restaurant(name="Mario's Pizza", address="123 Mushroom Lane")
    r2 = Restaurant(name="Luigi's Slice", address="456 Green Hill")
    r3 = Restaurant(name="Kiki's Pizza", address="789 Castle Street")

    print("Seeding pizzas...")
    p1 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    p2 = Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Cheese, Peppers, Onions, Mushrooms")
    p3 = Pizza(name="BBQ Chicken", ingredients="Dough, BBQ Sauce, Chicken, Cheese")

    print("Linking pizzas to restaurants...")
    rp1 = RestaurantPizza(price=10, pizza=p1, restaurant=r1)
    rp2 = RestaurantPizza(price=12, pizza=p2, restaurant=r1)
    rp3 = RestaurantPizza(price=8, pizza=p3, restaurant=r2)
    rp4 = RestaurantPizza(price=15, pizza=p1, restaurant=r3)

    db.session.add_all([r1, r2, r3, p1, p2, p3, rp1, rp2, rp3, rp4])
    db.session.commit()

    print("Done seeding 🌱")

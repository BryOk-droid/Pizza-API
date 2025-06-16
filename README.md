# Pizza API

A RESTful Flask API to manage restaurants, pizzas, and their many-to-many relationships using SQLAlchemy and Flask-Migrate.

---

## Project Checklist

- Flask app factory pattern
- SQLAlchemy models with relationships
- Alembic migrations for schema management
- Seed script for sample data
- API routes with validation
- Postman testable endpoints

---

## Setup Instructions

### Environment Setup

- Install pipenv
- Create and activate virtual environment

```bash
pipenv install
pipenv shell
```
### Set Flask app environment variable
```bash
export FLASK_APP=server/app.py
```
### Run the app
```bash
flask run
```
## Database Setup
### Migrations
 Initialize migration folder
 ```bash
 flask db init
```
Create migration scripts:
```bash
flask db migrate -m "Create tables for Restaurant, Pizza, RestaurantPizza"
```
Apply migrations:
```bash
flask db upgrade
```
### Seeding the Database
Run the seed file:
```bash
python -m server.seed
```
## API Routes Summary
| Method | Endpoint                | Description                             |
| ------ | ----------------------- | --------------------------------------- |
| GET    | `/pizzas`               | Get all pizzas                          |
| GET    | `/restaurants`          | Get all restaurants                     |
| GET    | `/restaurants/<int:id>` | Get one restaurant with its pizzas      |
| POST   | `/restaurant_pizzas`    | Link a pizza to a restaurant with price |
| DELETE | `/restaurants/<int:id>` | Delete a restaurant                     |

## Example Requests and Responses
Get /pizzas
```bash
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Cheese, Tomato, Basil"
  }
]
```
GET /restaurants/1
```bash
{
  "id": 1,
  "name": "Mama Mia Pizzeria",
  "address": "456 Dough Street",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Cheese, Tomato, Basil"
    }
  ]
}
```
POST /restaurant_pizzas

Request:
```bash
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 1
}
```
Response:
```bash
{
  "id": 1,
  "pizza_id": 1,
  "restaurant_id": 1,
  "price": 15
}
```
DELETE /restaurants/2
```bash
Status: 204 No Content
```

## Postman Usage Instructions
1. Start the Flask server:
```bash
flask run
```
2. Launch Postman and test using the following:

GET /pizzas

Method: GET

URL: http://127.0.0.1:5000/pizzas

POST /restaurant_pizzas

Method: POST

URL: http://127.0.0.1:5000/restaurant_pizzas

Headers: Content-Type: application/json

Body:
```bash
{
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 1
}
```
DELETE /restaurants/2

Method: DELETE

URL: http://127.0.0.1:5000/restaurants/2

## License


Copyright (c) 2025 Brian Okoth Omuga

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


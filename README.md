# Item Tracker API

A simple RESTful API built with FastAPI that connects to a MySQL database to manage items.

## Project Overview

This project demonstrates:

- RESTful API design
- Proper HTTP status codes
- Input validation using Pydantic
- Clean separation between API layer and business logic
- Database integration with MySQL
- Basic Git version control workflow

## Technologies Used

- Python 3
- FastAPI
- Uvicorn
- MySQL
- mysql-connector-python
- Docker & Docker Compose

## Project Structure


itemtracker_api/

main.py (API routes)

services.py (business logic)

database.py (database connection)

schemas.py (data validation models)

requirements.txt

Dockerfile

docker-compose.yml

.env


## Installation (Local Python)

Clone the repository:

git clone https://github.com/faniskioses/itemtracker_api.git
cd itemtracker_api

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt

Create a .env file in the project root with your database credentials:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=itemtracker

Run the API:

uvicorn main:app --reload

Open Swagger UI at http://127.0.0.1:8000/docs
 to test endpoints.

API Endpoints

GET / → Health check

GET /items → List all items

POST /items → Add a new item

DELETE /items/{item_id} → Delete an item by ID

## Running with Docker (Recommended)

Make sure Docker and Docker Compose are installed.

Create a .env file as above with your database credentials.

Run: 

docker-compose up --build

Your FastAPI service will be available at http://127.0.0.1:8000

Database is encapsulated in Docker, so no local setup is needed.

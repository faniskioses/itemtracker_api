Item Tracker API

A simple RESTful API built with FastAPI that connects to a MySQL database to manage items.

Project Overview

This project demonstrates:

RESTful API design

Proper HTTP status codes

Input validation using Pydantic

Clean separation between API layer and business logic

Database integration with MySQL

Basic Git version control workflow

Technologies Used

Python 3

FastAPI

Uvicorn

MySQL

mysql-connector-python

Project Structure

itemtracker_api/

main.py (API routes)

services.py (business logic)

database.py (database connection)

schemas.py (data validation models)

requirements.txt

Installation

Clone the repository:

git clone https://github.com/faniskioses/itemtracker_api.git

cd itemtracker_api

Create virtual environment:

python -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Database Setup

Create the database:

CREATE DATABASE itemtracker;

Create the table:

USE itemtracker;

CREATE TABLE items (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL,
quantity INT NOT NULL,
category VARCHAR(255) NOT NULL
);

Running the API

Start the server:

uvicorn main:app --reload

Open Swagger documentation:

http://127.0.0.1:8000/docs

Available Endpoints

GET /items
Returns all items (200 OK)

POST /items
Creates a new item (201 Created, 422 Validation Error)

DELETE /items/{item_id}
Deletes an item (200 OK, 404 Not Found, 422 Validation Error)

Purpose

This project was created as a backend exercise to demonstrate understanding of RESTful APIs, FastAPI best practices, database integration, and Git workflow.

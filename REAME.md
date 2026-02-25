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

## Project Structure

itemtracker_api/
- `main.py` (API routes)
- `services.py` (business logic)
- `database.py` (database connection)
- `schemas.py` (data validation models)
- `requirements.txt`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/faniskioses/itemtracker_api.git
cd itemtracker_api


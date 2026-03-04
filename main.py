from fastapi import FastAPI, HTTPException, status
from services import add_item, list_items, delete_item
from schemas import ItemCreate, ItemResponse
from typing import List

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Item Tracker API running"}

@app.get("/items", response_model=List[ItemResponse], status_code=status.HTTP_200_OK)
def get_items():
    return list_items() # just return data

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    return add_item(item.name, item.quantity, item.category) # return dict only
    

@app.delete("/items/{item_id}", status_code=status.HTTP_200_OK)
def remove_item(item_id: int):
    try:
        return delete_item(item_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
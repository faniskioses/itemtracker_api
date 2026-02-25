from fastapi import FastAPI, HTTPException, status
from services import add_item, list_items, delete_item
from schemas import ItemCreate 

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Item Tracker API running"}

@app.get("/items", status_code=status.HTTP_200_OK)
def get_items():
    return list_items() # just return data

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    return add_item(item.name, item.quantity, item.category) # return dict only
    

@app.delete("/items/{item_id}")
def remove_item(item_id: int):
    success = delete_item(item_id)
    if "error" in success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=success["error"])
    return success
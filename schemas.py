from pydantic import BaseModel 

class ItemCreate(BaseModel):
    name: str
    quantity: int
    category: str
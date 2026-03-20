from pydantic import BaseModel 

class ItemBase(BaseModel):
    name: str
    quantity: int
    category: str  

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int 

    class Config:
        from_attributes = True     
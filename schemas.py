from pydantic import BaseModel 

class ItemCreate(BaseModel):
    name: str
    quantity: int
    category: str  

class ItemResponse(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int 

    class Config:
        orm_mode = True     
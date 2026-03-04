from pydantic import BaseModel 

class ItemCreate(BaseModel):
    name: str
    quantity: int
    category: str  

class ItemResponse(BaseModel):
    id: int
    name: str
    quantity: int
    category: str

    class Config:
        orm_mode = True     
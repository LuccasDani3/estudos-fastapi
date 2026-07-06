from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str
    price: float = Field(gt=0)    
    id: int
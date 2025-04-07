from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class TradeBase(BaseModel):
    ticker: str
    price: float = Field(..., gt=0, description="Price must be greater than 0")
    quantity: int = Field(..., gt=0, description="Quantity must be greater than 0")
    side: str
    timestamp: Optional[datetime] = None

    @validator("side")
    def validate_side(cls, v):
        if v.lower() not in ["buy", "sell"]:
            raise ValueError("Side must be 'buy' or 'sell'")
        return v.lower()

class TradeCreate(TradeBase):
    pass

class TradeOut(TradeBase):
    id: int

    class Config:
        orm_mode = True

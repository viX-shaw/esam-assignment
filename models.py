from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, Field

class OrderItem(BaseModel):
    name: str = Field(..., max_length=30)
    quantity: int = Field(..., lt=10)
    price: int = Field(..., lt=1000000)


class OfferTypes(str, Enum):
    FLAT = "FLAT"
    DELIVERY = "DELIVERY"


class Offer(BaseModel):
    offer_type: OfferTypes
    offer_val: int = Field(..., ge=0)


class Order(BaseModel):
    order_items: List[OrderItem]
    distance: int = Field(..., ge=0, le=500000)
    offer: Optional[Offer] = Field(None)

class OrderTotal(BaseModel):
    order_total: int = Field(..., ge=0)
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Basic Request Body
@router.post("/items/")
async def create_item(item: Item):
    return item

# Use the model
@router.post("/items-with-model/")
async def create_item_with_model(item: Item):
    item_dict = item.model_dump()

    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({
            "price_with_tax": price_with_tax
        })

    return item_dict
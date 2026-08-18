from datetime import datetime

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


router = APIRouter()


fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


@router.put("/encoder-items/{id}")
def update_item(id: str, item: Item):

    json_compatible_item_data = jsonable_encoder(item)

    fake_db[id] = json_compatible_item_data

    return fake_db[id]
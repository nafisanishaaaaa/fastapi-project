from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from app.schemas.encoder import EncoderItem

router = APIRouter()


fake_db = {}


@router.put("/encoder-items/{id}")
def update_item(id: str, item: EncoderItem):

    json_compatible_item_data = jsonable_encoder(item)

    fake_db[id] = json_compatible_item_data

    return fake_db[id]
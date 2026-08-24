from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from app.schemas.item_update import ItemUpdate

router = APIRouter()


items = {
    "foo": {
        "name": "Foo",
        "price": 50.2
    },
    "bar": {
        "name": "Bar",
        "description": "The bartenders",
        "price": 62,
        "tax": 20.2
    }
}


# Get existing item
@router.get("/update-items/{item_id}")
async def read_item(item_id: str):
    return items[item_id]


# Update item using PUT
@router.put("/update-items/{item_id}")
async def update_item(item_id: str, item: ItemUpdate):

    update_item_encoded = jsonable_encoder(item)

    items[item_id] = update_item_encoded

    return update_item_encoded

# Partial update using PATCH
@router.patch("/body-update/{item_id}")
async def partial_update_item(item_id: str, item: ItemUpdate):

    stored_item_data = items[item_id]

    stored_item_model = ItemUpdate(**stored_item_data)

    update_data = item.model_dump(exclude_unset=True)

    updated_item = stored_item_model.model_copy(
        update=update_data
    )

    items[item_id] = jsonable_encoder(updated_item)

    return updated_item
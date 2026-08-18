from fastapi import APIRouter, HTTPException

router = APIRouter()


items = {
    "phone": "Samsung",
    "laptop": "Asus"
}


@router.get("/error-items/{item_id}")
async def read_item(item_id: str):

    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return {
        "item": items[item_id]
    }
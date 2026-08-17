from typing import Annotated,Literal
from fastapi import APIRouter,Query
from pydantic import BaseModel, Field

router = APIRouter()


fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


@router.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@router.get("/optional-items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {
            "item_id": item_id,
            "q": q
        }

    return {
        "item_id": item_id
    }

@router.get("/boolean-items/{item_id}")
async def read_boolean_item(
    item_id: str,
    q: str | None = None,
    short: bool = False
):
    item = {
        "item_id": item_id
    }

    if q:
        item.update({
            "q": q
        })

    if not short:
        item.update({
            "description": "This is an amazing item that has a long description"
        })

    return item

@router.get("/required-items/{item_id}")
async def read_required_item(
    item_id: str,
    needy: str
):
    item = {
        "item_id": item_id,
        "needy": needy
    }

    return item

class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@router.get("/filter-items/")
async def read_filter_items(
    filter_query: Annotated[FilterParams, Query()]
):
    return filter_query
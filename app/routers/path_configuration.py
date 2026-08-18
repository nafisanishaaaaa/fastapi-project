from fastapi import APIRouter, status
from pydantic import BaseModel


router = APIRouter()


class Product(BaseModel):
    name: str
    price: float


# Response Description
@router.post(
    "/products/",
    status_code=status.HTTP_201_CREATED,
    tags=["products"],
    summary="Create a product",
    response_description="The created product"
)
async def create_product(product: Product):
    """
    Create a product.

    - **name**: Product name
    - **price**: Product price
    """

    return product

# Deprecated Path Operation
@router.get(
    "/old-products/",
    tags=["products"],
    deprecated=True
)
async def old_products():
    return {
        "message": "This endpoint is deprecated"
    }

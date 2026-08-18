from fastapi import APIRouter, Depends


router = APIRouter()


# Dependency function
def common_parameters(
    q: str | None = None,
    skip: int = 0,
    limit: int = 100
):
    return {
        "q": q,
        "skip": skip,
        "limit": limit
    }


# Using dependency
@router.get("/dependency-items/")
async def read_items(
    commons: dict = Depends(common_parameters)
):
    return commons


@router.get("/dependency-users/")
async def read_users(
    commons: dict = Depends(common_parameters)
):
    return commons
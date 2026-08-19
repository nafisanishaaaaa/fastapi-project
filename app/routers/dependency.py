from fastapi import APIRouter, Depends


router = APIRouter()


# 1. Dependency function
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


# 2. Class Dependency
class CommonQueryParams:

    def __init__(
        self,
        q: str | None = None,
        skip: int = 0,
        limit: int = 100
    ):
        self.q = q
        self.skip = skip
        self.limit = limit


@router.get("/class-dependency/")
async def read_class_items(
    commons: CommonQueryParams = Depends(CommonQueryParams)
):
    return {
        "q": commons.q,
        "skip": commons.skip,
        "limit": commons.limit
    }

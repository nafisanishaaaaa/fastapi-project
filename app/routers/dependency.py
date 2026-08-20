from fastapi import APIRouter, Depends
from fastapi import Header, HTTPException


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


# Sub Dependency
# First dependency
def query_extractor(
    q: str | None = None
):
    return q

# Second dependency
def query_or_default(
    q: str | None = Depends(query_extractor)
):

    if q:
        return q

    return "No query provided"


# Using sub-dependency
@router.get("/sub-dependency/")
async def read_query(
    query: str = Depends(query_or_default)
):
    return {
        "q": query
    }


#path operation decorator
# Dependency 1: Token check
async def verify_token(
    x_token: str = Header()
):
    if x_token != "fake-super-secret-token":
        raise HTTPException(
            status_code=400,
            detail="X-Token header invalid"
        )


# Dependency 2: Key check
async def verify_key(
    x_key: str = Header()
):
    if x_key != "fake-super-secret-key":
        raise HTTPException(
            status_code=400,
            detail="X-Key header invalid"
        )

    return x_key


# Using dependencies in path operation decorator
@router.get(
    "/decorator-dependency/",
    dependencies=[
        Depends(verify_token),
        Depends(verify_key)
    ]
)
async def read_items():

    return [
        {
            "item": "Foo"
        },
        {
            "item": "Bar"
        }
    ]


#  Global Dependency Example
#
# from fastapi import FastAPI, Depends, Header, HTTPException
#
#
# # Dependency 1: Verify Token
# async def verify_token(
#     x_token: str = Header()
# ):
#
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(
#             status_code=400,
#             detail="X-Token header invalid"
#         )
#
#
# # Dependency 2: Verify Key
# async def verify_key(
#     x_key: str = Header()
# ):
#
#     if x_key != "fake-super-secret-key":
#         raise HTTPException(
#             status_code=400,
#             detail="X-Key header invalid"
#         )
#
#     return x_key
#
#
#
# # Global Dependency
#
# app = FastAPI(
#     dependencies=[
#         Depends(verify_token),
#         Depends(verify_key)
#     ]
# )
#
#
#
# @app.get("/items/")
# async def read_items():
#
#     return [
#         {
#             "item": "Foo"
#         },
#         {
#             "item": "Bar"
#         }
#     ]
#
#
#
# @app.get("/users/")
# async def read_users():
#
#     return [
#         {
#             "username": "Rick"
#         },
#         {
#             "username": "Morty"
#         }
#     ]


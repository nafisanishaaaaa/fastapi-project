from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm
)
from pydantic import BaseModel


router = APIRouter()


# Fake database

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False
    }
}



# OAuth2 Scheme

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token"
)



# Fake password hashing

def fake_hash_password(password: str):

    return "fakehashed" + password



# User Model

class User(BaseModel):

    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None



# User with password

class UserInDB(User):

    hashed_password: str



# Get user from fake database

def get_user(db, username: str):

    if username in db:

        user_dict = db[username]

        return UserInDB(**user_dict)



# Decode token

def fake_decode_token(token: str):

    user = get_user(
        fake_users_db,
        token
    )

    if user:

        return User(
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            disabled=user.disabled
        )



# Current user dependency

async def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    user = fake_decode_token(token)


    if not user:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )


    return user



# Login endpoint

@router.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    user = get_user(
        fake_users_db,
        form_data.username
    )


    if not user:

        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )



    hashed_password = fake_hash_password(
        form_data.password
    )


    if hashed_password != user.hashed_password:

        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )



    return {

        "access_token": user.username,
        "token_type": "bearer"

    }



# Protected route

@router.get("/users/me")
async def read_users_me(
    current_user: User = Depends(get_current_user)
):

    return current_user
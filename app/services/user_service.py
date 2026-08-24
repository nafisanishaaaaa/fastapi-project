from app.schemas.user import UserInDB

# Fake database
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        # generated hash for password: secret
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$ZMYxZZ7SmF8OfHu4T+DP/g$ZBWXYQGM7uNKpBg2BIzWqOrM+J/HBEl9Fw62EqytyTc",
        "disabled": False,
    }
}


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

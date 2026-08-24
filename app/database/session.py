from sqlmodel import SQLModel, create_engine, Session

# Import model so SQLModel.metadata knows about tables
from app.models.hero import Hero  # noqa: F401

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"


connect_args = {
    "check_same_thread": False
}

engine = create_engine(
    sqlite_url,
    connect_args=connect_args
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

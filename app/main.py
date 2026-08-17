from fastapi import FastAPI
from app.routers import path_parameter, query_parameter, request_body

app = FastAPI()
app.include_router(path_parameter.router)
app.include_router(query_parameter.router)
app.include_router(request_body.router)


@app.get("/")
def home():
    return {
        "message": "FastAPI started"
    }
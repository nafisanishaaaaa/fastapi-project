from fastapi import FastAPI
from app.routers import path_parameter, query_parameter, request_body, form_data, file_upload

app = FastAPI()
app.include_router(path_parameter.router)
app.include_router(query_parameter.router)
app.include_router(request_body.router)
app.include_router(form_data.router)
app.include_router(file_upload.router)


@app.get("/")
def home():
    return {
        "message": "FastAPI started"
    }
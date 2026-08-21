import time
from fastapi import FastAPI, Request
from app.routers import path_parameter,query_parameter,request_body,form_data,file_upload,error_handling,path_configuration,body_updates,dependency,security
from app.routers import json_encoder
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware
@app.middleware("http")
async def add_process_time_header(
    request: Request,
    call_next
):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Routers
app.include_router(path_parameter.router)
app.include_router(query_parameter.router)
app.include_router(request_body.router)
app.include_router(form_data.router)
app.include_router(file_upload.router)
app.include_router(error_handling.router)
app.include_router(path_configuration.router)
app.include_router(json_encoder.router)
app.include_router(body_updates.router)
app.include_router(dependency.router)
app.include_router(security.router)

@app.get("/")
def home():

    return {
        "message": "FastAPI started"
    }
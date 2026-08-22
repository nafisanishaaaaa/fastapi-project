import time
from fastapi import FastAPI, Request
from app.router import router
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_db_and_tables

app = FastAPI()
import uvicorn
create_db_and_tables()

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
app.include_router(router)

@app.get("/")
def home():

    return {
        "message": "FastAPI started"
    }

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )
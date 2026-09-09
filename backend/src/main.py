from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.tasks import router as tasks_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks_router)


@app.get("/")
def read_root():
    return {"message": "¡Hola! Mi API keep it cool man"}
from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from auth import get_token
from routes.tasks import router as tasks_router
from routes.positions import router as positions_router

app = FastAPI()

app.include_router(tasks_router)
app.include_router(positions_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "¡Hola! Mi API keep it cool man"}


@app.get("/me")
def get_me(token: str = Depends(get_token)):

    return {"message": "Token recibido correctamente", "token": token}

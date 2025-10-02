from fastapi import FastAPI
from api.routers import itens

app = FastAPI()

app.include_router(itens.router, prefix="/itens", tags=["Itens"])

@app.get("/")
def index():
    return {"message": "FastAPI running!!!"}

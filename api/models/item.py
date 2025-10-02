from pydantic import BaseModel

# modelo de item
class Item(BaseModel):
    nome: str
    preco: float


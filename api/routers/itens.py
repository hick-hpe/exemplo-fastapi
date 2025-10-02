from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from api.models.item import Item

router = APIRouter()
itens = []

@router.get("/")
def listar_itens():
    return {"itens": itens}

@router.post("/")
def cadastrar_item(item: Item):
    itens.append(item.dict())
    return JSONResponse(content={"msg": "Item cadastrado", "itens": itens}, status_code=201)

@router.get("/{item_id}/")
def obter_item(item_id: int):
    try:
        return {"item": itens[item_id]}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item não encontrado")

@router.put("/{item_id}/")
def atualizar_item(item_id: int, item: Item):
    try:
        itens[item_id] = item.dict()
        return {"msg": "Item atualizado", "item": itens[item_id]}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item não encontrado")

@router.delete("/{item_id}/")
def remover_item(item_id: int):
    try:
        item = itens.pop(item_id)
        return {"msg": "Item removido", "item": item}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item não encontrado")


# curl -X POST http://127.0.0.1:8000/itens/ -H "Content-Type: application/json" -d "{\"nome\": \"Notebook\", \"preco\": 3500.0}"

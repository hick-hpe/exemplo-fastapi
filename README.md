# exemplo-fastapi

Uma API simples desenvolvida com **FastAPI**, organizada com **routers** e **models**, pronta para CRUD básico de itens.

## Tecnologias utilizadas
- [FastAPI](https://fastapi.tiangolo.com/)
- [Poetry](https://python-poetry.org/) para gerenciamento de dependências e ambiente virtual

## Estrutura do projeto

```
exemplo-fastapi/
│
├─ api/
│ ├─ init.py
│ ├─ main.py # ponto de entrada da API
│ ├─ models/
│ │ ├─ init.py
│ │ └─ item.py # modelos Pydantic
│ └─ routers/
│ ├─ init.py
│ └─ itens.py # rotas relacionadas a itens
```


## Instalação e execução

1. Instale as dependências usando Poetry:
    ```bash
    poetry install
    ```

2. Execute a API:
    ```bash
    poetry run uvicorn api.main:app --reload
    ```

A API estará disponível em: http://127.0.0.1:8000/

## Endpoints disponíveis
| Método | Endpoint       | Descrição                  |
| ------ | -------------- | -------------------------- |
| GET    | `/`            | Retorna mensagem de status |
| GET    | `/itens/`      | Lista todos os itens       |
| POST   | `/itens/`      | Cadastra um novo item      |
| GET    | `/itens/{id}/` | Retorna um item pelo ID    |
| PUT    | `/itens/{id}/` | Atualiza um item pelo ID   |
| DELETE | `/itens/{id}/` | Remove um item pelo ID     |

Para os endpoints POST/PUT, o corpo deve ser enviado em JSON, por exemplo:

```json
{
    "nome": "Notebook",
    "preco": 3500.0
}
```

## Observações

- O projeto está configurado para desenvolvimento, usando `--reload` para recarregar automaticamente ao salvar alterações.
- Não há integração com banco de dados ainda; os itens são armazenados temporariamente em memória.

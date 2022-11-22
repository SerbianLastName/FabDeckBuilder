from typing import List
from aerich import aerich

from fastapi import FastAPI, HTTPException
from ..models.fabmodels import FabCard, Card_Pydantic
from pydantic import BaseModel

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from tortoise import Tortoise

Tortoise.init_models(["src.models.fabmodels"], "models") # Initialize Tortoise ORM before creating models.

app = FastAPI(title="Fab App")


class Status(BaseModel):
    message: str


@app.get("/cards", response_model=List[Card_Pydantic])
async def get_users():
    _return = await Card_Pydantic.from_queryset(FabCard.all())    
    return _return


@app.get(
    "/cards/{card_id}", response_model=Card_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def get_user(card_id: int):
    return await Card_Pydantic.from_queryset_single(FabCard.get(id=card_id))


register_tortoise(
    app,
    db_url="postgres://fabdatabase_user:fabdatabase_pass@db:5432/fabDB",
    modules={"models": ["src.models.fabmodels", "aerich.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
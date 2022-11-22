from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Cards


CardInSchema = pydantic_model_creator(
    Cards, name="CardIn", exclude=["id"], exclude_readonly=True)
CardOutSchema = pydantic_model_creator(
    Cards, name="Card"
)


class UpdateCard(BaseModel):
    title: Optional[str]
    content: Optional[str]
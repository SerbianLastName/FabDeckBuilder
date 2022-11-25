from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Decks


DeckInSchema = pydantic_model_creator(
    Decks, name="DeckIn", exclude=["id"], exclude_readonly=True
)
DeckOutSchema = pydantic_model_creator(Decks, name="Deck")


class UpdateDeck(BaseModel):
    deckName: Optional[str]
    deckPublic: Optional[bool]
    deckBlitz: Optional[bool]
    deckList: Optional[str]

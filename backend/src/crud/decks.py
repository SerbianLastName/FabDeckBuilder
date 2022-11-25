from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Decks
from src.schemas.decks import DeckOutSchema
from src.schemas.token import Status


async def get_decks():
    return await DeckOutSchema.from_queryset(Decks.all())


async def get_deck(deck_id) -> DeckOutSchema:
    return await DeckOutSchema.from_queryset_single(Decks.get(id=deck_id))


async def create_deck(deck, current_user) -> DeckOutSchema:
    if current_user.is_admin == True:
        deck_dict = deck.dict(exclude_unset=True)
        deck_obj = await Decks.create(**deck_dict)
        return await DeckOutSchema.from_tortoise_orm(deck_obj)
    raise HTTPException(status_code=403, detail=f"Not authorized to create")


async def update_deck(deck_id, deck, current_user) -> DeckOutSchema:
    try:
        db_deck = await DeckOutSchema.from_queryset_single(Decks.get(id=deck_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Deck {deck_id} not found")

    if current_user.is_admin != True:
        await Decks.filter(id=deck_id).update(**deck.dict(exclude_unset=True))
        return await DeckOutSchema.from_queryset_single(Decks.get(id=deck_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_deck(deck_id, current_user) -> Status:  # UPDATED
    try:
        db_deck = await DeckOutSchema.from_queryset_single(Decks.get(id=deck_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Deck {deck_id} not found")

    if current_user.is_admin != True:
        deleted_count = await Decks.filter(id=deck_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Deck {deck_id} not found")
        return Status(message=f"Deleted deck {deck_id}")  # UPDATED

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")

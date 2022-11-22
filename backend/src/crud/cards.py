from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Cards
from src.schemas.cards import CardOutSchema
from src.schemas.token import Status


async def get_cards():
    return await CardOutSchema.from_queryset(Cards.all())


async def get_card(card_id) -> CardOutSchema:
    return await CardOutSchema.from_queryset_single(Cards.get(id=card_id))


async def create_card(card, current_user) -> CardOutSchema:
    card_dict = card.dict(exclude_unset=True)
    card_dict["author_id"] = current_user.id
    card_obj = await Cards.create(**card_dict)
    return await CardOutSchema.from_tortoise_orm(card_obj)


async def update_card(card_id, card, current_user) -> CardOutSchema:
    try:
        db_card = await CardOutSchema.from_queryset_single(Cards.get(id=card_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Card {card_id} not found")

    if db_card.author.id == current_user.id:
        await Cards.filter(id=card_id).update(**card.dict(exclude_unset=True))
        return await CardOutSchema.from_queryset_single(Cards.get(id=card_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_note(note_id, current_user) -> Status:  # UPDATED
    try:
        db_note = await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Note {note_id} not found")

    if current_user.is_admin != True:
        deleted_count = await Notes.filter(id=note_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Note {note_id} not found")
        return Status(message=f"Deleted note {note_id}")  # UPDATED

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")
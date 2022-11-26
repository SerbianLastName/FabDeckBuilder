from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Cards
from src.schemas.cards import CardOutSchema
from src.schemas.token import Status


async def get_cards():
    return await CardOutSchema.from_queryset(Cards.all())


async def get_card(card_id) -> CardOutSchema:
    return await CardOutSchema.from_queryset_single(Cards.get(id=card_id))


async def create_card(card) -> CardOutSchema:
    # if current_user.is_admin == True:
    print("printing card")
    print(card)
    card_dict = card.dict(exclude_unset=True)
    card_obj = await Cards.create(**card_dict)
    return await CardOutSchema.from_tortoise_orm(card_obj)
    raise HTTPException(status_code=403, detail=f"Not authorized to create")


async def update_card(card_id, card, current_user) -> CardOutSchema:
    try:
        db_card = await CardOutSchema.from_queryset_single(Cards.get(id=card_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Card {card_id} not found")

    if current_user.is_admin != True:
        await Cards.filter(id=card_id).update(**card.dict(exclude_unset=True))
        return await CardOutSchema.from_queryset_single(Cards.get(id=card_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_card(card_id, current_user) -> Status:  # UPDATED
    try:
        db_card = await CardOutSchema.from_queryset_single(Cards.get(id=card_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Card {card_id} not found")

    if current_user.is_admin != True:
        deleted_count = await Cards.filter(id=card_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Card {card_id} not found")
        return Status(message=f"Deleted card {card_id}")  # UPDATED

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")

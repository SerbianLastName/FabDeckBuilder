from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.decks as crud
from src.auth.jwthandler import get_current_user
from src.schemas.decks import DeckOutSchema, DeckInSchema, UpdateDeck
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/decks",
    response_model=List[DeckOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_decks():
    return await crud.get_decks()


@router.get(
    "/deck/{deck_id}",
    response_model=DeckOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_deck(deck_id: int) -> DeckOutSchema:
    try:
        return await crud.get_deck(deck_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Deck does not exist",
        )


@router.post(
    "/decks", response_model=DeckOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_deck(
    deck: DeckInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> DeckOutSchema:
    return await crud.create_deck(deck, current_user)


@router.patch(
    "/deck/{deck_id}",
    dependencies=[Depends(get_current_user)],
    response_model=DeckOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_deck(
    deck_id: int,
    deck: UpdateDeck,
    current_user: UserOutSchema = Depends(get_current_user),
) -> DeckOutSchema:
    return await crud.update_deck(deck_id, deck, current_user)


@router.delete(
    "/deck/{deck_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_deck(
    deck_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_deck(deck_id, current_user)

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.cards as crud
from src.auth.jwthandler import get_current_user
from src.schemas.cards import CardOutSchema, CardInSchema, UpdateCard
from src.schemas.token import Status
from src.schemas.users import UserOutSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()


@router.get(
    "/cards",
    response_model=List[CardOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_cards():
    return await crud.get_cards()


@router.get(
    "/card/{card_id}",
    response_model=CardOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_card(card_id: int) -> CardOutSchema:
    try:
        return await crud.get_card(card_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Card does not exist",
        )


@router.post(
    "/cards", response_model=CardOutSchema, dependencies=[Depends(oauth2_scheme)]
)
# card: CardInSchema,
async def create_card(card: CardInSchema) -> CardOutSchema:
    print(card)
    return await crud.create_card(card)


@router.patch(
    "/card/{card_id}",
    dependencies=[Depends(get_current_user)],
    response_model=CardOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_card(
    card_id: int,
    card: UpdateCard,
    current_user: UserOutSchema = Depends(get_current_user),
) -> CardOutSchema:
    return await crud.update_card(card_id, card, current_user)


@router.delete(
    "/card/{card_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_card(
    card_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_card(card_id, current_user)

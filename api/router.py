from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from fastapi import APIRouter, Depends, status, HTTPException

from core.models import User
from core.schemas.user import UserRead, UserCreate
from core.utils.db_helper import db_helper
from core.utils.logger import logger
import core.crud.user as user_crud

router = APIRouter(prefix="/user", tags=["User"])


@router.get("", response_model=list[UserRead])
async def get_all_users(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ]
):
    users = await user_crud.get_all_users(session=session)
    return users


@router.post("", response_model=UserRead)
async def create_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_create: UserCreate,
):
    user = await user_crud.get_user_by_telegramm_account_name(
        session=session,
        telegramm_account=user_create.telegramm_account,
    )
    if user:
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            detail=f"Юзер с таким телеграмм аккаунтом {user_create.telegramm_account} уже наличествует в наличии",
        )
    else:
        user = await user_crud.add_user(
            session=session,
            insert_user=user_create,
        )
        return user


@router.delete("")
async def delete_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_id: int,
):
    try:
        await user_crud.delete_user_by_id(session=session, user_id=user_id)
        return {"message": f"User with id {user_id} deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"User with selected id {user_id} not found",
        )

from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, status
from core.schemas.user import UserRead, UserCreate
from core.utils.db_helper import db_helper
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


@router.post("", response_model=UserCreate)
async def create_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_create: UserCreate,
):
    user = await user_crud.add_user(
        session=session,
        insert_user=user_create,
    )
    return user


@router.delete("/")
async def delete_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_id: int,
):
    await user_crud.delete_user_by_id(session=session, user_id=user_id)
    return {"message": f"User with id {user_id} deleted"}

from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, status, HTTPException

from core.schemas.theme import ThemeCreate, ThemeRead
from core.utils.db_helper import db_helper
import core.crud.theme as theme_crud

router = APIRouter(prefix="/theme", tags=["Theme"])


@router.get("", response_model=list[ThemeRead])
async def get_all_themes(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ]
):
    themes = await theme_crud.get_all_themes(session=session)
    return themes


@router.post("", response_model=ThemeRead)
async def create_theme(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    theme_create: ThemeCreate,
):
    theme = await theme_crud.add_theme(session, theme_create)
    await session.commit()
    return theme


@router.get("/{user_id}", response_model=list[ThemeRead])
async def read_themes_by_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_id: int,
):
    try:
        themes = await theme_crud.get_theme_by_user(session, user_id)
        return themes
    except Exception as e:
        return {"error": e}


@router.delete("/{theme_id}")
async def delete_theme(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    theme_id: int,
):
    try:
        await theme_crud.delete_theme_by_id(session=session, theme_id=theme_id)
        return {"message": f"Theme with id {theme_id} deleted successfully"}
    except Exception:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"Theme with selected id {theme_id} not found",
        )

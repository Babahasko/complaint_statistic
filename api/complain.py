from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, status, HTTPException

from core.schemas.complain import ComplainCreate, ComplainRead, ComplainReadPretty
from core.utils.db_helper import db_helper
import core.crud.complain as complain_crud

router = APIRouter(prefix="/complain", tags=["Complain"])


@router.get("/show_all_complains/", response_model=list[ComplainRead])
async def get_all_complains(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ]
):
    complain = await complain_crud.get_all_complains(session=session)
    return complain


@router.post("", response_model=ComplainRead)
async def create_complain(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    complain_create: ComplainCreate,
):
    complain = await complain_crud.add_complain(session, complain_create)
    await session.commit()
    return complain


@router.get("/show_user_complains/", response_model=list[ComplainRead])
async def read_complain_by_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_id: int,
):
    try:
        complains = await complain_crud.get_complain_by_user(session, user_id)
        return complains
    except Exception as e:
        return {"error": e}

@router.get("/show_user_complains_pretty/", response_model=list[ComplainReadPretty])
async def read_complain_by_user_pretty(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_id: int,
):
    try:
        complains = await complain_crud.get_complain_by_user_pretty(session, user_id)
        return complains
    except Exception as e:
        return {"error": e}


@router.delete("/")
async def delete_complain(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    complain_id: int,
):
    try:
        await complain_crud.delete_complain_by_id(
            session=session, complain_id=complain_id
        )
        return {"message": f"Complain with id {complain_id} deleted successfully"}
    except Exception:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"Complain with selected id {complain_id} not found",
        )

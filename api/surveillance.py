from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, status, HTTPException

from core.schemas.surveillance import SurveillanceCreate, SurveillanceRead
from core.utils.db_helper import db_helper
import core.crud.surveillance as surveillance_crud

router = APIRouter(prefix="/surveillance", tags=["Surveillance"])


@router.get("/show_all_surveillances/", response_model=list[SurveillanceRead])
async def get_all_surveillance(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ]
):
    surveillances = await surveillance_crud.get_all_surveillances(session=session)
    return surveillances


@router.post("", response_model=SurveillanceRead)
async def create_surveillance(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    surveillance_create: SurveillanceCreate,
):
    user_surveillances = await surveillance_crud.get_surveillance_by_user(session, surveillance_create.user_id)
    for surveillance in user_surveillances:
        if surveillance.name == surveillance_create.name:
            raise HTTPException(
                status.HTTP_409_CONFLICT,
                detail=f"У вас уже есть объект с таким именем {surveillance_create.name}"
            )
    surveillance = await surveillance_crud.add_surveillance(
        session, surveillance_create
    )
    await session.commit()
    return surveillance


@router.get("/show_user_surveillances/", response_model=list[SurveillanceRead])
async def read_surveillance_by_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_id: int,
):
    try:
        surveillances = await surveillance_crud.get_surveillance_by_user(
            session, user_id
        )
        return surveillances
    except Exception as e:
        return {"error": e}


@router.delete("/")
async def delete_surveillance(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    surveillance_id: int,
):
    try:
        await surveillance_crud.delete_surveillance_by_id(
            session=session, surveillance_id=surveillance_id
        )
        return {
            "message": f"Surveillance with id {surveillance_id} deleted successfully"
        }
    except Exception:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"Surveillance with selected id {surveillance_id} not found",
        )

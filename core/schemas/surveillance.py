from pydantic import BaseModel


class SurveillanceRead(BaseModel):
    id: int
    name: str
    user_id: int


class SurveillanceCreate(BaseModel):
    name: str
    user_id: int


class SurveillanceUpdate(BaseModel):
    name: str

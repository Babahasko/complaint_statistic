from pydantic import BaseModel


class SurveillanceCreate(BaseModel):
    name: str
    user_id: int

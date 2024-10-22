from pydantic import BaseModel


class ThemeCreate(BaseModel):
    name: str
    user_id: int

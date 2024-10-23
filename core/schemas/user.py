from pydantic import BaseModel


class UserCreate(BaseModel):
    telegramm_account: str
    username: str


class UserUpdate(BaseModel):
    username: str

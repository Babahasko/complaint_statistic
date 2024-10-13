from pydantic import BaseModel

class UserCreate(BaseModel):
    telegramm_account: str
    name: str
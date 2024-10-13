from pydantic import BaseModel

class Surveillance(BaseModel):
    name: str
    user_id: int
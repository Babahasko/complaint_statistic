from pydantic import BaseModel

class ThemeCreate(BaseModel):
    name: str
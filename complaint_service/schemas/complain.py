from pydantic import BaseModel, ConfigDict

from datetime import datetime

class ComplainBase(BaseModel):
    who: str
    about: str
    whom: str
    data: datetime

class ComplainCreate(ComplainBase):
    pass

class ComplainRead(ComplainBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: int
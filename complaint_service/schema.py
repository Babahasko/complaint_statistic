from pydantic import BaseModel, ConfigDict

from datetime import datetime

class ComplainCreate(BaseModel):
    who: str
    about: str
    sender: str
    data: datetime

# class ComplainRead(Complain):
#     model_config = ConfigDict(
#         from_attributes=True
#     )
#     id: int
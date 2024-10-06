from pydantic import BaseModel, ConfigDict

from datetime import datetime

class Complain(BaseModel):
    who: str
    about: str
    whom: str
    data: datetime

# class ComplainRead(Complain):
#     model_config = ConfigDict(
#         from_attributes=True
#     )
#     id: int
from pydantic import BaseModel

from datetime import datetime

class ComplainCreate(BaseModel):
    user_id: int
    theme_id: int
    surveillance_id: int
    data: datetime
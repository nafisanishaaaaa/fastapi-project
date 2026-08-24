from datetime import datetime
from pydantic import BaseModel


class EncoderItem(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None

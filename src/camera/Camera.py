from pydantic import BaseModel, Field
from typing import Any
from uuid import uuid4
from datetime import datetime

class Photo(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)
    time: datetime | None = None
    img: Any
    
class Camera:
    def __init__(self) -> None:
        """Check if the camera is online, return error if not"""

    @staticmethod
    def get_photo() -> Photo:
        """Take the photo and return data from it"""
from pydantic import BaseModel
from typing import Optional


class MemeBase(BaseModel):
    text: str
    image_url: str


class MemeCreate(MemeBase):
    pass


class MemeUpdate(BaseModel):
    text: Optional[str] = None
    image_url: Optional[str] = None


class Meme(MemeBase):
    id: int

    class Config:
        from_attributes = True

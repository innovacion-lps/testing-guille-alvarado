from pydantic import BaseModel
from typing import Optional


class PositionCreate(BaseModel):
    title: str
    description: Optional[str] = None
    country: Optional[str] = None
    currency: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    requirements: list = []

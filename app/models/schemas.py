from datetime import datetime
from typing import Literal, Optional

from sqlmodel import Field, SQLModel

from app.core.units import Unit


class CreatedAtMixin(SQLModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(), nullable=False)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(), nullable=False)


class Incredient(CreatedAtMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    amount: str
    unit: Unit
    format: Literal["metric", "imperial"] = Field(default="metric")

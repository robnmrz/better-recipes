from typing import Literal

from pydantic import BaseModel, Field, field_validator
from pydantic_core import PydanticCustomError

from app.core.constants import Unit

ALLOWED_UNITS = Unit.list()


class Ingredient(BaseModel):
    """
    Base class for ingredients
    """

    name: str
    amount: str
    unit: str
    format: Literal["metric", "imperial"] = Field(default="metric")

    @field_validator("unit")
    def validate_unit(cls, unit):
        if unit not in ALLOWED_UNITS:
            raise PydanticCustomError(
                "incorrect_unit",
                "Incorrect unit. Allowed units: {}".format(ALLOWED_UNITS),
            )

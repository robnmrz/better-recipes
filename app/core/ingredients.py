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
    amount: float
    unit: str
    format: Literal["metric", "imperial"] = Field(default="metric")

    @field_validator("unit")
    def validate_unit(cls, unit):
        if unit not in ALLOWED_UNITS:
            raise PydanticCustomError(
                "incorrect_unit",
                "Incorrect unit. Allowed units: {}".format(ALLOWED_UNITS),
            )
        return unit

    def __add__(self, other: "Ingredient") -> "Ingredient":
        """
        Dunder method for adding two ingredients.
        Raises an error if the ingredients are not the same.
        Returns:
            Ingredient: with the sum of the amount of the two ingredients
        """
        if self.name.lower() != other.name.lower():
            raise PydanticCustomError(
                "unequal_ingredients",
                "Only the same ingredients can be added",
            )

        return Ingredient(
            name=other.name,
            amount=str(float(self.amount) + float(other.amount)),
            unit=self.unit,
            format=self.format,
        )

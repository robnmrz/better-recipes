from enum import Enum


class BaseEnum(Enum):
    """
    Base class for enums to inerhit from.
    Contains helper methods for enums.
    """

    @classmethod
    def list(cls):
        return [e.value for e in cls]


class Unit(BaseEnum):
    """
    Enum class for ingredient units
    """

    GRAMM = "g"
    KILOGRAMM = "kg"
    LITER = "l"
    MILLILITER = "ml"
    TSP = "tsp"
    TBSP = "tbsp"
    PCS = "pcs"

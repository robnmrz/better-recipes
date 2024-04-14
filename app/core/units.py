from pydantic import BaseModel

SI_UNIT_CATALOG = {"kg": 1, "g": 0.001, "l": 1, "ml": 0.001}


class Unit(BaseModel):
    """
    Abstract base class for units
    """

    @staticmethod
    def convert_si(amount: float, unit_name: str) -> float:
        """
        Convert the unit amount to the SI unit amount

        Params:
            amount: float, the amount to convert
            unit_name: str, the unit to convert to
        Returns:
            float: The amount in the SI unit
        """
        return amount * SI_UNIT_CATALOG[unit_name]

from typing import Any

from pydantic import BaseModel


class User(BaseModel):
    firstname: str = "Robin"
    name: str = "Merz"

    def model_post_init(self, __context: Any) -> None:
        self.full_name = f"{self.firstname} {self.name}"

    # @model_validator(mode="after")
    # def set_user_name(self) -> Self:
    #     """Set full name"""
    #     self._full_name = f"{self.firstname} {self.name}"
    #     return self

    def print_user_name(self) -> None:
        print(self.full_name)

    class Config:
        extra = "allow"

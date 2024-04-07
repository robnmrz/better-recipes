from abc import ABC, abstractmethod

from pydantic import BaseModel


class Embeddings(ABC, BaseModel):
    @abstractmethod
    def embed_query(self, text: str) -> list[float]:
        """
        Embed a query / text

        Args:
            text (str): The query to embed
        Returns:
            list[float]: The embedding
        """

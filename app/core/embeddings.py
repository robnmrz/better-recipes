from abc import ABC, abstractmethod

from pydantic import BaseModel, Field
from sentence_transformers import SentenceTransformer


class Embeddings(ABC, BaseModel):
    """
    Abstract base class for embedding models
    """

    @abstractmethod
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """
        Embed a list of documents
        Params:
            texts: list[str]): The documents to embed
        Returns:
            list[list[float]]: The embeddings
        """

    @abstractmethod
    def embed_query(self, text: str) -> list[float]:
        """
        Embed a query / text
        Params:
            text (str): The query to embed
        Returns:
            list[float]: The embedding
        """

    class Config:
        extra = "allow"


DEFAUTL_EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"


class SentenceTransformerEmbedding(Embeddings):
    st_model_id: str = DEFAUTL_EMBEDDING_MODEL
    st_model_kwargs: dict = Field(default_factory=dict)

    def __init__(self, **kwargs):
        """
        Init model client used for encoding
        """
        super().__init__(**kwargs)
        self.client: SentenceTransformer = SentenceTransformer(
            self.st_model_id, **self.st_model_kwargs
        )

    def embed_documents(self, texts: list[str], **kwargs) -> list[list[float]]:
        return self.client.encode(texts, **kwargs)

    def embed_query(self, text: str) -> list[float]:
        return self.client.encode([text])[0]

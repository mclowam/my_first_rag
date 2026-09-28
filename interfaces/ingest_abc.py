from abc import ABC, abstractmethod

from langchain_core.documents import Document


class DocumentSource(ABC):
    @abstractmethod
    def load(self) -> list[Document]: ...


class Chunker(ABC):
    @abstractmethod
    def split(self, docs: list[Document]) -> list[Document]: ...


class DocumentIndex(ABC):
    @abstractmethod
    def add(self, docs: list[Document]) -> int: ...
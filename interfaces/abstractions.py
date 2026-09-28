from abc import ABC, abstractmethod


class Retriever(ABC):
    @abstractmethod
    def retrieve(self, question: str) -> list[str]:
        pass


class Generator(ABC):
    @abstractmethod
    def generate(self, question: str, context: str) -> str:
        pass


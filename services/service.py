from interfaces.abstractions import Generator, Retriever


class RagService:
    def __init__(self, retriever: Retriever, generator: Generator):
        self._retriever = retriever
        self._generator = generator

    def ask(self, question: str) -> str:
        chunks = self._retriever.retrieve(question)
        if not chunks:
            return "I don't know."
        return self._generator.generate(question, "\n\n".join(chunks))
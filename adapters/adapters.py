from langchain_chroma import Chroma
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from interfaces.abstractions import Retriever, Generator


class ChromaRetriever(Retriever):
    def __init__(self, store: Chroma, k: int):
        self._store = store
        self._k = k

    def retrieve(self, question: str) -> list[str]:
        docs = self._store.similarity_search(question, k=self._k)
        return [d.page_content for d in docs]


class LLMGenerator(Generator):
    def __init__(self, llm: BaseChatModel, prompt: ChatPromptTemplate):
        self._chain = prompt | llm | StrOutputParser()

    def generate(self, question: str, context: str) -> str:
        return self._chain.invoke({"question": question, "context": context})
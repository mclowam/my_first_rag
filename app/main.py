from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from adapters import ChromaRetriever, LLMGenerator
from settings import Settings
from service import RagService
from store import build_store

PROMPT = ChatPromptTemplate.from_template(
    "Answer using only the context. "
    "If the answer isn't there, say \"I don't know.\"\n"
    "Question: {question}\n"
    "Context: {context}\n"
    "Answer:"
)


def build_service(s: Settings) -> RagService:
    llm = ChatOpenAI(model=s.chat_model, api_key=s.openai_api_key)
    return RagService(
        retriever=ChromaRetriever(build_store(s), s.top_k),
        generator=LLMGenerator(llm, PROMPT),
    )


if __name__ == "__main__":
    service = build_service(Settings())
    print(service.ask("What is prompt engineering? take the answer on russian"))
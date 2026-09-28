from langchain_chroma import Chroma
from langchain_community.embeddings import OpenAIEmbeddings

from settings import Settings


def build_store(s: Settings)-> Chroma:
    return Chroma(
        collection_name=s.collection,
        embedding_function=OpenAIEmbeddings(
            model=s.embedding_model, api_key=s.openai_api_key
        ),
        persist_directory=s.chroma_dir,
    )
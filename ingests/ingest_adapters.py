import hashlib

import bs4
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from interfaces.ingest_abc import Chunker, DocumentIndex, DocumentSource


class WebSource(DocumentSource):
    def __init__(self, url: str, css_classes: tuple[str, ...]):
        self._url = url
        self._classes = css_classes

    def load(self) -> list[Document]:
        strainer = bs4.SoupStrainer(class_=self._classes)
        loader = WebBaseLoader(
            web_paths=(self._url,), bs_kwargs={"parse_only": strainer}
        )
        return loader.load()


class RecursiveChunker(Chunker):
    def __init__(self, size: int, overlap: int):
        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size=size, chunk_overlap=overlap, add_start_index=True
        )

    def split(self, docs: list[Document]) -> list[Document]:
        return self._splitter.split_documents(docs)


class ChromaIndex(DocumentIndex):
    def __init__(self, store: Chroma):
        self._store = store

    def add(self, docs: list[Document]) -> int:
        ids = [self._make_id(d) for d in docs]
        return len(self._store.add_documents(docs, ids=ids))

    @staticmethod
    def _make_id(doc: Document) -> str:
        key = f"{doc.metadata.get('source')}:{doc.metadata.get('start_index')}"
        return hashlib.sha1(key.encode()).hexdigest()
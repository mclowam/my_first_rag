from interfaces.ingest_abc import Chunker, DocumentIndex, DocumentSource


class IngestionService:
    def __init__(
        self, source: DocumentSource, chunker: Chunker, index: DocumentIndex
    ):
        self._source = source
        self._chunker = chunker
        self._index = index

    def run(self) -> int:
        docs = self._source.load()
        chunks = self._chunker.split(docs)
        return self._index.add(chunks)
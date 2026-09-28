from settings import Settings
from ingest_adapters import ChromaIndex, RecursiveChunker, WebSource
from ingest_service import IngestionService
from store import build_store

if __name__ == "__main__":
    s = Settings()
    service = IngestionService(
        source=WebSource(s.source_url, ("post-title", "post-header", "post-content")),
        chunker=RecursiveChunker(s.chunk_size, s.chunk_overlap),
        index=ChromaIndex(build_store(s)),
    )
    print(f"Indexed {service.run()} chunks")
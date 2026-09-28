from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    openai_api_key: str
    chat_model: str
    embedding_model: str = "text-embedding-3-small"
    chroma_dir: str = "./chroma_db"
    collection: str = "prompt_engineering"
    top_k: int = 3

    source_url: str = "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/"
    chunk_size: int = 1000
    chunk_overlap: int = 200
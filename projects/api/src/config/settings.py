from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    mongodb_uri: str = Field(default="mongodb://localhost:27017", min_length=1)
    mongodb_database: str = Field(default="comments", min_length=1)
    mongodb_server_selection_timeout_ms: int = Field(default=5000, gt=0)


settings = Settings()

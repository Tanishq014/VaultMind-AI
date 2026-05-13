from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "VaultMind AI Engine"
    app_version: str = "0.1.0"
    environment: str = "local"
    log_level: str = "INFO"
    api_prefix: str = "/api"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

#object is once created and reused
@lru_cache
def get_settings() -> Settings:
    return Settings()
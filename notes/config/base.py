import os
from datetime import datetime
from typing import Any, Dict, Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = os.environ["APP_NAME"]
    APP_DESCRIPTION: Optional[str] = os.environ.get("APP_DESCRIPTION")
    APP_VERSION: str = os.environ["APP_VERSION"]
    APP_ENCODING_ALG: str = os.environ.get("APP_ENCODING_ALG", "HS256")
    APP_ISSUER: str = os.environ["APP_ISSUER"]
    APP_JWT_ENABLED: bool = os.environ["APP_JWT_ENABLED"] == "True"
    APP_LOG_NAME: str = os.environ["APP_LOG_NAME"]
    DEBUG: bool = os.environ["DEBUG"] == "True"

    DATABASE_URL: str = os.environ.get("DATABASE_URL")
    database_port_str: str = os.environ.get("DATABASE_PORT")
    DATABASE_PORT: int = int(database_port_str) if database_port_str else 5432
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    SQLALCHEMY_DATABASE_URI: str = (
        f"postgresql+psycopg2://{POSTGRES_USER}:"
        f"{POSTGRES_PASSWORD}@{DATABASE_URL}:"
        f"{DATABASE_PORT}/{POSTGRES_DB}"
    )
    SQLALCHEMY_ASYNC_DATABASE_URI: str = (
        f"postgresql+asyncpg://{POSTGRES_USER}:"
        f"{POSTGRES_PASSWORD}@{DATABASE_URL}:"
        f"{DATABASE_PORT}/{POSTGRES_DB}"
    )
    SQLALCHEMY_ECHO: bool = bool(os.environ["SQLALCHEMY_ECHO"] == "True")
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = bool(
        os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", "False") == "True"
    )
    # type: ignore
    POOL_RECYCLE: int = int(os.environ.get("SQLALCHEMY_POOL_RECYCLE", 299))
    # type: ignore
    POOL_TIMEOUT: int = int(os.environ.get("SQLALCHEMY_POOL_TIMEOUT", 20))

    SQLALCHEMY_ENGINE_OPTIONS: Dict[str, Any] = {
        "pool_recycle": POOL_RECYCLE,
        "pool_timeout": POOL_TIMEOUT,
    }
    ITEMS_PER_PAGE: int = 20
    DEPLOYED_AT: str = str(datetime.now())

    REDIS_HOST: str = os.environ.get("REDIS_HOST")
    redis_port_str: str = os.environ.get("REDIS_PORT")
    REDIS_PORT: int = int(redis_port_str)
    SESSION_TIMEOUT: int = int(os.environ["SESSION_TIMEOUT"])
    SESSION_COOKIE_NAME: str = os.environ["SESSION_COOKIE_NAME"]

    API_KEY_NAME: str = "X-Api-Key"
    SECRET_KEY: str = "61a9fd867e810f7e846946bd3ba4e0c6ebae2d39b9bfe7c276a40250a8942d83"
    API_KEY_VALUE: str = os.environ.get(
        "API_KEY_VALUE", "52b23c0a-cf59-48ef-be2f-921c45377ac8"
    )

    JOIN_DEPTH: int = 1


settings = Settings()

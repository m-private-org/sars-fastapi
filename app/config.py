from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    POSTGRES_USER: Optional[str] = None
    DB_USER: Optional[str] = None
    DB_PASS: Optional[str] = None
    DB_NAME: Optional[str] = None
    DB_HOST: Optional[str] = None
    DB_PORT: Optional[str] = None
    GCP_SERVICE_ACCOUNT: Optional[str] = None


settings = Settings()
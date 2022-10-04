from typing import List
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://admin:admin@localhost:5432/fastapi'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = '4-QE9i3FIem8-6in-IWsbzOSKJ9c03DV6lXpeyFmFeU'
    """_summary_
    import secrets
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'    
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 

    class Config:
        case_sensitive = True

settings: Settings = Settings()

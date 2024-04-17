# config.py

from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent.parent.parent

DB_PATH = ""


class TokenType(BaseModel):
    ACCESS: str = "access"
    REFRESH: str = "refresh"


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    JWT_PUBLIC_KEY: str = "guess-me"
    JWT_PRIVATE_KEY: str = "guess-me"
    REFRESH_TOKEN_EXPIRES_MINUTES: int = 60 * 24 * 7
    ACCESS_TOKEN_EXPIRES_MINUTES: int = 5
    JWT_ALGORITHM: str = "RS256"

    TOKEN_EXPIRES_MINUTES: int = 2
    TOKEN_URLSAFE_LEN: int = 32
    token_type: TokenType = TokenType()

    class Config:
        env_file = f"{BASE_DIR}/.env"


class DbSettings(BaseModel):
    db_url: str = f"postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres"
    db_echo: bool = False
    # db_echo: bool = True
    db_engine: str = "postgres"


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db: DbSettings = DbSettings()

    auth_jwt: AuthJWT = AuthJWT()

    CLIENT_ORIGIN: str = "http://localhost:8000"


settings = Settings()

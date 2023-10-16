from pydantic_settings import BaseSettings


class PostgresSettings(BaseSettings):
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str

    class Config:
        env_file = ".env"

    def get_db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


class Settings(PostgresSettings):
    pass

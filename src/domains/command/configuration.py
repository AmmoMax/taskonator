from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings


class DBConfig(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: str = Field(default="5432")
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_NAME: str
    POSTGRES_SCHEMA_NAME: str = Field(default="main")

    @property
    def postgres_url(self) -> str:
        return "postgresql+psycopg://{}:{}@{}:{}/{}".format(
            self.POSTGRES_USER,
            self.POSTGRES_PASSWORD.get_secret_value(),
            self.POSTGRES_HOST,
            self.POSTGRES_PORT,
            self.POSTGRES_NAME,
        )


class Config(BaseSettings):
    LOGGING_LEVEL: str = Field(default="DEBUG")

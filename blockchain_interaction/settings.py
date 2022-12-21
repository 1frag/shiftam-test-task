from pydantic import BaseSettings


class Settings(BaseSettings):
    avalanche_rpc: str

    class Config:
        env_file = ".env"


settings = Settings()

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    admin_id: int
    # for_test_id: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

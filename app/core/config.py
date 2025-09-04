from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "APIAluno"
    APP_VERSION: str = "1.0.0"

    model_config = SettingsConfigDict(
        env_file = ".env", env_file_encoding="utf-> uvicorn app.main:app.main --reload8"
    )

settings = Settings()
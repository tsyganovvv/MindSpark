from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    DOMEN: str
    
    OAUTH_GOOGLE_CLIENT_SECRET: str
    OAUTH_GOOGLE_CLIENT_ID: str
    GOOGLE_TOKEN_URL: str


    DEBUG:str
    MODEL_NAME: str
    DEVICE: str
    MODEL_PATH: str

    MAX_LENGTH: int
    TEMPERATURE: float
    DO_SAMPLE: bool
    REPETITION_PENALTY: float

    JWT_SECRET_KEY: str

    model_config = SettingsConfigDict(env_file='app/.env')


settings = Settings()
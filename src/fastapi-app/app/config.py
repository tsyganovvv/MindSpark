import os 
from dotenv import load_dotenv


load_dotenv()


class Settings:
    DOMEN=os.getenv("DOMEN", "mind-spark.ru")

    OAUTH_GOOGLE_CLIENT_SECRET=os.getenv("OAUTH_GOOGLE_CLIENT_SECRET", "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")
    OAUTH_GOOGLE_CLIENT_ID=os.getenv("OAUTH_GOOGLE_CLIENT_ID", "841010799248-tjvrjnptvs6868gshcdsthnau1k6bf51.apps.googleusercontent.com")
    GOOGLE_TOKEN_URL=os.getenv("GOOGLE_TOKEN_URL", "https://oauth2.googleapis.com/token")


    DEBUG = os.getenv("DEBUG", "Fasle") == True
    MODEL_NAME = os.getenv("MODEL_NAME", "rugpt3small_based_on_gpt2")
    DEVICE = os.getenv("DEVICE", "cpu")
    MODEL_PATH = os.getenv("MODEL_PATH", "ai-forever/rugpt3small_based_on_gpt2")

    MAX_LENGTH = 150
    TEMPERATURE = 0.7
    DO_SAMPLE = True
    REPETITION_PENALTY=1.3


settings = Settings()


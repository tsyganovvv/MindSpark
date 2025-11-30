import os 
from dotenv import load_dotenv


load_dotenv()


class Settings:
    DEBUG = os.getenv("DEBUG", "Fasle") == True
    MODEL_NAME = os.getenv("MODEL_NAME", "rugpt3large_based_on_gpt2")
    DEVICE = os.getenv("DEVICE", "cpu")

    MODEL_PATH = f"sberbank-ai/{MODEL_NAME}"
    MAX_LENGTH = 150
    TEMPERATURE = 0.7
    DO_SAMPLE = True


settings = Settings()


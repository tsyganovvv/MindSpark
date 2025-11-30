import os 
from dotenv import load_dotenv


load_dotenv()


class Settings:
    DEBUG = os.getenv("DEBUG", "Fasle") == True
    MODEL_NAME = os.getenv("MODEL_NAME", "rugpt3small_based_on_gpt2")
    DEVICE = os.getenv("DEVICE", "cpu")
    MODEL_PATH = os.getenv("MODEL_PATH", "ai-forever/rugpt3small_based_on_gpt2")

    MAX_LENGTH = 150
    TEMPERATURE = 0.7
    DO_SAMPLE = True
    REPETITION_PENALTY=1.3


settings = Settings()


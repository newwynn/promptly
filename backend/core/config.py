import os

class Settings:
    MODEL_NAME: str = os.getenv("MODEL_NAME", "sshleifer/tiny-gpt2")

settings = Settings()


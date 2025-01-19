import os
from dotenv import load_dotenv

load_dotenv()

class BotConfig:
    def __init__(self):
        self.token = os.getenv('BOT_TOKEN')
        self.postgres_user = os.getenv('POSTGRES_USER')
        self.postgres_password = os.getenv('POSTGRES_PASSWORD')
        self.postgres_db = os.getenv('POSTGRES_DB')
        self.postgres_host = os.getenv('POSTGRES_HOST')
        self.database_url = (f"postgresql://{self.postgres_user}:{self.postgres_password}"
                             f"@{self.postgres_host}/{self.postgres_db}")
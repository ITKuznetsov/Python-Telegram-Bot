from os import getenv
from dotenv import load_dotenv


load_dotenv()

class BotConfig:
    def __init__(self):
        self.token = getenv('BOT_TOKEN')
        self.postgres_user = getenv('POSTGRES_USER')
        self.postgres_password = getenv('POSTGRES_PASSWORD')
        self.postgres_db = getenv('POSTGRES_DB')
        self.postgres_host = getenv('POSTGRES_HOST')
        self.database_url = (f"postgresql://{self.postgres_user}:{self.postgres_password}"
                             f"@{self.postgres_host}/{self.postgres_db}")
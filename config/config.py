import os
from dotenv import load_dotenv

load_dotenv()

class BotConfig:
    def __init__(self):
        self.token = os.getenv('BOT_TOKEN')
        self.database_url = os.getenv('DATABASE_URL')
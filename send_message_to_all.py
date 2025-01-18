from sqlmodel import Session, select
from bot.utils.bot_initializer import BotInitializer
from config.config import BotConfig
from bot.models import User
from bot.database.engine import engine

def send_message_to_all():
    config = BotConfig()
    bot_initializer = BotInitializer(config.token, {})

    with Session(engine) as session:
        statement = select(User)
        users = session.exec(statement).all()
        for user in users:
            bot_initializer.bot.send_message(user.chat_id, "Это заготовленное сообщение для всех пользователей!")

if __name__ == "__main__":
    send_message_to_all()
from sqlmodel import Session, select
from bot.database.engine import engine
from bot.models import User
from bot.handlers.file_handler import FileHandler


class CommandHandler:
    def __init__(self, bot, commands):
        self.bot = bot
        self.commands = commands

    def handle_command(self, message):
        try:
            if message.text in self.commands:
                data = self.commands[message.text]
                if data.get('message'):
                    self.bot.send_message(message.from_user.id, data['message'])
                if data.get('files'):
                    FileHandler.send_files(self.bot, message.from_user.id, data['files'])
                if data.get('photos'):
                    FileHandler.send_photos(self.bot, message.from_user.id, data['photos'])
                if data.get('menu'):
                    self.bot.send_message(message.from_user.id, "Держись, меняю меню!", reply_markup=data['menu'])
            else:
                self.bot.send_message(message.from_user.id, 'Неизвестная команда.')

            with Session(engine) as session:
                statement = select(User).where(User.chat_id == message.from_user.id)
                user = session.exec(statement).first()
                if not user:
                    new_user = User(chat_id=message.from_user.id)
                    session.add(new_user)
                    session.commit()
        except Exception as e:
            print(f"Ошибка: {e}")
            self.bot.send_message(message.from_user.id, 'Произошла ошибка. Пожалуйста, попробуйте снова.')
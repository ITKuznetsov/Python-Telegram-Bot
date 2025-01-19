from telebot import TeleBot
from bot.handlers.command_handler import CommandHandler
from bot.handlers.menu_handler import MenuHandler


class BotInitializer:
    def __init__(self, token, commands):
        self.bot = TeleBot(token)
        self.commands = commands
        self.command_handler = CommandHandler(self.bot, self.commands)
        self.register_handlers()

    def register_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def start(message):
            markup = MenuHandler.create_first_menu()
            self.bot.send_message(message.from_user.id, "Привет!", reply_markup=markup)

        @self.bot.message_handler(content_types=['text'])
        def handle_text(message):
            self.command_handler.handle_command(message)

    def run(self):
        self.bot.polling(none_stop=True, interval=0)
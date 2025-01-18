from bot.utils.bot_initializer import BotInitializer
from config.config import BotConfig
from bot.handlers.menu_handler import MenuHandler

def main():
    try:
        config = BotConfig()
        commands = {
            'Второе меню': {
                'menu': MenuHandler.create_second_menu()
            },
            'Третье меню': {
                'menu': MenuHandler.create_third_menu()
            },
            'Главная': {
                'menu': MenuHandler.create_first_menu()
            },
            'Первая мок-кнопка': {
                'message': 'О, ты нажал на первую мок-кнопку?'
            },
            'Вторая мок-кнопка': {
                'message': 'Я вторая мок-кнопка!'
            },
            'Третья мок-кнопка': {
                'message': 'Третья мок-кнопка...'
            },
            'Четвертая мок-кнопка': {
                'message': 'Я последняя из мок-кнопок.'
            }
        }

        bot_initializer = BotInitializer(config.token, commands)
        print("Бот запущен успешно.")
        bot_initializer.run()
    except KeyboardInterrupt:
        print("\nБот остановлен пользователем.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Завершение работы бота.")

if __name__ == "__main__":
    main()
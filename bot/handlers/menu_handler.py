from telebot import types


class MenuHandler:
    @staticmethod
    def create_menu(buttons, row_width=2):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
        for i in range(0, len(buttons), row_width):
            row_buttons = buttons[i:i + row_width]
            markup.row(*[types.KeyboardButton(button) for button in row_buttons])
        return markup

    @staticmethod
    def create_first_menu():
        buttons = ['Первая мок-кнопка', 'Второе меню', 'Третье меню']
        return MenuHandler.create_menu(buttons)

    @staticmethod
    def create_second_menu():
        buttons = ['Вторая мок-кнопка', 'Главная']
        return MenuHandler.create_menu(buttons)

    @staticmethod
    def create_third_menu():
        buttons = ['Третья мок-кнопка', 'Четвертая мок-кнопка', 'Главная']
        return MenuHandler.create_menu(buttons)
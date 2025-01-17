class FileHandler:
    @staticmethod
    def send_photos(bot, chat_id, photos):
        for photo_path in photos:
            try:
                with open(photo_path, 'rb') as photo:
                    bot.send_photo(chat_id, photo)
            except Exception as e:
                print(f"Ошибка при отправке фото {photo_path}: {e}")
                bot.send_message(chat_id, f"Не удалось отправить фото: {photo_path}")

    @staticmethod
    def send_files(bot, chat_id, files):
        for file_path in files:
            try:
                with open(file_path, 'rb') as file:
                    bot.send_document(chat_id, file)
            except Exception as e:
                print(f"Ошибка при отправке файла {file_path}: {e}")
                bot.send_message(chat_id, f"Не удалось отправить файл: {file_path}")
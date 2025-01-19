# Python Telegram Bot
Telegram-бот с интеграцией PostgreSQL, созданный с использованием PyTelegramBotAPI, SQLModel и Alembic. Бот поддерживает обработку команд, динамическое меню, работу с файлами и фото, а также хранение данных пользователей в базе данных.
## Технологии
* Python
* PyTelegramBotAPI
* SQLModel (ORM для работы с PostgreSQL)
* Alembic (управление миграциями базы данных)
* PostgreSQL
* Docker

## Локальный запуск (с использованием Docker)
1. Создайте файл .env в корне проекта и заполните его необходимыми переменными окружения:
   ```bash
   touch .env
   ```
   Пример содержимого .env:
   ```bash
   BOT_TOKEN=your_telegram_bot_token
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=bot
   POSTGRES_HOST=db
   ```

2. Запустите проект с помощью Docker Compose:
   ```bash
   docker-compose up --build
   ```
## Локальный запуск (без Docker)
1. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Установите зависимости:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. Создайте файл .env и заполните его переменными окружения (см. пример выше, переменную POSTGRES_HOST установить в значение localhost).
4. Запустите PostgreSQL на вашем компьютере и создайте базу данных с именем, указанным в переменной окружения POSTGRES_DB.
5. Создайте и выполните миграции Alembic:
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   alembic upgrade head
   ```
6. Запустите бота:
   ```bash
   python main.py
   ```

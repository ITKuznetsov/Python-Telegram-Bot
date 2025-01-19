#!/bin/bash

echo "Creating database migrations..."
alembic revision --autogenerate -m "auto migration"

echo "Applying database migrations..."
alembic upgrade head

echo "Starting bot..."
python main.py
# Используем официальный образ Python
FROM python:3.14

# Установим рабочую директорию
WORKDIR /app

# Установим переменные окружения
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Установим зависимости системы
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Копируем requirements.txt
COPY ../requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .


# Открываем порт
EXPOSE 8000

# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
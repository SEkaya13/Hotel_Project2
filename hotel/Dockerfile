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
RUN pip install -r requirements.txt uvicorn
COPY .env .

# Копируем весь проект
COPY . .


# Открываем порт
EXPOSE 8000

# Запускаем сервер
CMD ["uvicorn", "hotel:application", "--host", "0.0.0.0", "--port", "8000"]
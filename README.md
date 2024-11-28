# Complaint_statistic

# Предназначение
Complaint_statistic API это сервис обеспечивающий работу [complaint_bot](https://github.com/Babahasko/Complaint_bot)

## Описание проекта
Проект на FastAPI предназначен для обеспечения регистрации пользователей и обеспечения основоного функционала приложения, а именно
1. Аутентификация, авторизация и регистрация пользователей
2. Запись и получение данных приложения в бд

## Запуск проекта
Копируем проект
```shell
git clone https://github.com/Babahasko/complaint_statistic.git
```

Создаём виртуальное окружение и активируем его
```shell
python -m venv .venv
.venv/Scripts/activate
```

Загружаем зависимости
```shell
poetry install
```
или
```shell
pip install requirements.txt
```

Прописываем переменные окружения в файле .env.template и переименовываем его в .env
Пример готового .env
```
MARIADB_URL=mysql+aiomysql://admin:admin1234@host.docker.internal:3306/app_db?charset=utf8mb4

MARIADB_ROOT_PASSWORD=1111
MARIADB_USER=admin
MARIADB_PASSWORD=admin1234
MARIADB_DATABASE=app_db
```
Запускаем docker-compose
```shell
docker-compose up -d --build
```

## Документация по API
Открываем страницу в браузере http://127.0.0.1:8000/docs. В ней же можно и протестировать работу API.
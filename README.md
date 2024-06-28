# Meme Collection Web App

Это веб-приложение на Python, использующее FastAPI, которое предоставляет API для работы с коллекцией мемов. Приложение состоит из двух сервисов: публичный API с бизнес-логикой и сервис для работы с медиа-файлами, использующий S3-совместимое хранилище (MinIO).

## Функциональность

- GET /memes: Получить список всех мемов (с пагинацией)
- GET /memes/{id}: Получить конкретный мем по его ID
- POST /memes: Добавить новый мем (с картинкой и текстом)
- PUT /memes/{id}: Обновить существующий мем
- DELETE /memes/{id}: Удалить мем

## Технологии

- FastAPI
- PostgreSQL
- MinIO (S3-совместимое хранилище)
- Docker и Docker Compose

## Требования

- Docker
- Docker Compose

## Установка и запуск

1. Клонируйте репозиторий:

git clone git@github.com:DmitryZhdanov-ScienceSoft/memes.git
cd memes

2. Создайте файл `.env` в корневой директории проекта и заполните его следующим содержимым:

POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=memes
MINIO_ROOT_USER=minio
MINIO_ROOT_PASSWORD=minio123


3. Запустите приложение с помощью Docker Compose:

docker-compose up -d


4. Приложение будет доступно по следующим адресам:
- FastAPI приложение: http://localhost:8000
- Swagger UI (документация API): http://localhost:8000/docs
- MinIO консоль: http://localhost:9001

## Использование

### Получение списка мемов


GET http://localhost:8000/memes?skip=0&limit=10


### Получение конкретного мема

GET http://localhost:8000/memes/{meme_id}

### Создание нового мема


POST http://localhost:8000/memes
Content-Type: application/json


{
"text": "Текст мема",
"image_url": "http://example.com/image.jpg"
}


### Обновление мема


PUT http://localhost:8000/memes/{meme_id}
Content-Type: application/json


{
"text": "Новый текст мема",
"image_url": "http://example.com/new_image.jpg"
}


### Удаление мема

DELETE http://localhost:8000/memes/{meme_id}

## Разработка

Для внесения изменений в код:

1. Остановите работающие контейнеры:

docker-compose down

2. Внесите необходимые изменения в код.

3. Пересоберите и запустите контейнеры:

docker-compose up --build -d

## Тестирование

Для запуска тестов используйте следующую команду:

docker-compose run public_api pytest


## Структура проекта


meme-app/
├── public_api/
│   ├── Dockerfile
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── requirements.txt
├── media_service/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── tests/
│   └── test_public_api.py
├── docker-compose.yml
└── README.md
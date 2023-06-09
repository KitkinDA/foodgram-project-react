# Проект Foodgram

![.github/workflows/foodgram_workflow.yml](https://github.com/KitkinDA/foodgram-project-react/actions/workflows/foodgram_workflows.yaml/badge.svg)

 ### Описание
Foodgram- это веб-приложение, где вы можете делиться своими рецептами и просматривать рецепты других пользователей, а так же добавлять их в избранное и корзину покупок.

[Ссылка на развернутый проект](http://158.160.107.9/signin)

Суперюзер:

- login: Admin@mail.ru
- password: Admin

Пользователь:

- login: dmitry@mail.ru
- password: test123456

 ### Технологии

- Python
- Django
- DRF
- Docker
- Docker-compose
- PostgreSQL
- nginx
- gunicorn
- JWT + Djoser
- Docker Hub
- GitHub Actions
- Yandex.Cloud

### Запуск проекта 
 1 Склонируйте репозиторий.
 ```bash
 git clone https://github.com/KitkinDA/foodgram-project-react.git
 ```
 2 Установите и активируйте виртуальное окружение:
 ```bash
 python -m venv venv
 source venv/Scripts/activate 
 python -m pip install --upgrade pip
 ```
 3 Установите зависимости из файла requirements.txt
 ```bash
 pip install -r requirements.txt
 ```


4 [Установите (если ещё у Вас его нету) docker и docker-compose. ](https://docs.docker.com/)

 
5 Создайте .env файл в директории /infra со следующим содержанием:
 ```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
 ```
6 Из директории /infra выполните командy:
 ```bash
docker-compose up
  ```
7 Выполните миграции (с миграциями загрузится база с ингредиентами и тегами), загрузите статику, создайте суперпользователя:
 ```bash
docker-compose exec -T backend python manage.py makemigrations recipes
docker-compose exec -T backend python manage.py migrate
docker-compose exec -T backend python manage.py collectstatic --no-input
docker-compose exec -T backend python manage.py createsuperuser
 ```
8 Сервис будет доступен по http://localhost/.

9 Документация доступна после запуска проекта по адресу:
http://localhost/api/docs/


## Разработка backend : [Киткин Дмитрий](https://github.com/KitkinDA)
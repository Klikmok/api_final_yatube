# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com:Klikmok/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Перейти в директорию с файлом manage.py:

```
cd yatube_api
```
Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
# Примеры запросов

### GET Получение всех публикаций
http://127.0.0.1:8000/api/v1/posts/

Пример ответа с пагинацией:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
### POST Создание публикации
http://127.0.0.1:8000/api/v1/posts/

Пример запроса:
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Пример ответа:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
## Для отдельной публикации

http://127.0.0.1:8000/api/v1/posts/{id}/

### GET Получение отдельной публикации
Пример ответа:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
### PUT Обновление публикации
Пример запроса:
```
{
"text": "string",
"image": "string",
"group": 0
}
```
Пример ответа:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
### PATCH Частичное обновление публикации
Пример запроса:
{
"text": "string",
}
Пример ответа:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
## DELETE Удаление публикации
}
Пример ответа:
```
{
  "detail": "Страница не найдена."
}
```
### GET Получение всех комментариев
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

Пример ответа:
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

### POST Добавление комментария

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

Пример запроса:
```
{
"text": "Комментарий."
}
```
Пример ответа:
## Запросы к одтельному комментарию
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/


### GET Получение отдельного комментария
Пример ответа:
```
{
  "id": 0,
  "author": "Автор",
  "text": "Комментарий",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
### PUT Обновление комментария
Пример запроса:
```
{
  "text": "string"
}
```
Пример ответа:
```
{
  "id": 0,
  "author": "Автор",
  "text": "Комментарий",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
### PATCH Частичное обновление комментария
Пример запроса:
```
{
  "text": "string"
}
```
Пример ответа:
```
{
  "id": 0,
  "author": "Автор",
  "text": "Комментарий",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
### DELETE Удаление комментария
Пример ответа:
```
{
  "detail": "Страница не найдена."
}
```
## GET Получение списка сообществ
http://127.0.0.1:8000/api/v1/groups/

Пример ответа:
```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```
## GET Получение отдельного сообщества
http://127.0.0.1:8000/api/v1/groups/{id}/

Пример ответа:
```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```
## GET Получение собственных подписок
http://127.0.0.1:8000/api/v1/follow/

Пример ответа:
```
[
  {
    "user": "Ваш юзернэйм",
    "following": "Юзернэйм того, на кого вы подписались"
  }
]
```
## POST Подписка на кого-либо
http://127.0.0.1:8000/api/v1/follow/

Пример запроса:
```
{
  "following": "string"
}
```
Пример ответа:
```
[
  {
    "user": "Ваш юзернэйм",
    "following": "Юзернэйм того, на кого вы подписались"
  }
]
```
## POST Получить JWT-токен
http://127.0.0.1:8000/api/v1/jwt/create/

Пример запроса:
```
{
  "username": "string",
  "password": "string"
}
```
Пример ответа:
```
[
{
  "refresh": "string",
  "access": "string"
}
]
```
## POST Обновить JWT-токен
http://127.0.0.1:8000/api/v1/jwt/refresh/

Пример запроса:
```
{
  "refresh": "string"
}
```
Пример ответа:
```
[
{
  "access": "string"
}
]
```
## POST Проверить JWT-токен
http://127.0.0.1:8000/api/v1/jwt/verify/

Пример запроса:
```
{
  "token": "string"
}
```
Пример ответа:
```
{
  "token": [
    "Обязательное поле."
  ]
}
```
## Описание проекта
### Финальная версия API проекта Yatube. Yatube - это настоящая социальная сеть. В ней вы можете постить свои публикации, комментировать чужие, подписываться на понравившихся авторов и многое другое.

### Мы ждем вас!!!

## Использованные технологии
Django Rest Api, Django Framework, Python 3.9, Djoster, Django-JWT.
## Автор
Рыбаков Алексей, город Магнитогорск, с помощью "Яндекс Практикума".
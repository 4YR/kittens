## Описание проекта

Этот проект представляет собой REST API для котят. API предоставляет возможность пользователям управлять информацией о котятах и породах. Он включает следующие методы:

-  Позволяет получить все доступные породы котят.
-  Позволяет получить информацию обо всех котятах.
-  Позволяет получить детальную информацию о конкретном котенке.
-  Пользователи могут добавлять новых котят в систему.
-  Пользователи могут изменять данные о котятах, которых они добавили.
-  Позволяет пользователям удалять котят, добавленных ими.
-  Система использует JWT для аутентификации пользователей.

## Установка приложения

1. Скачайте приложение по ссылке: https://github.com/4YR/kittens.git
2. В терминале выполните команду:

   ```bash
   docker compose up

3. Перейдите по ссылке: http://localhost:8000/api/token/.
4. Введите следующие данные для авторизации:
- **Username**: admin
- **Password**: pass
- Для остальных users Password: 12345678QqQ
5. Скопируйте полученный токен из поля "access". 
Если действие токена закончится (он действует всего 5 мин.) скопировать из поля "refresh" токен,
перейти по ссылке http://127.0.0.1:8000/api/token/refresh/ и вставить токен, скопировать новый токен из "access" и заново авторизоваться.
6. Перейдите на вкладку: http://localhost:8000/swagger/
7. Нажмите на кнопку "Authorize" и введите токен в формате Bearer <токен> в появившемся поле "Value".

## Возможности Swagger UI

На данной вкладке вы можете:

- Получать список всех пород.
- Получать список всех котят.
- Получать подробную информацию о котенке.
- Добавлять информацию о котенке.
- Изменять информацию о котенке.
- Добавлять рейтинг котят.

Для добавления рейтинга введите следующее:
```{
    "score": 5  // Или любое другое значение, которое вы хотите установить
}```

## Запуск тестов

Чтобы запустить тесты с помощью pytest, выполните следующие шаги:

1. Откройте терминал и выполните команду:
```bash
docker ps
2. Скопируйте CONTAINER ID для контейнера web.
3. Введите команду:
```bash
docker exec -it <скопированный ID> sh
4. Внутри контейнера выполните:
```bash
pytest
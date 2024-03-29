# Проект: Приложение атомных привычек

**Russian** | [English](docs_eng/README.md)

## Описание проекта
Проект "Приложение атомных привычек" представляет собой backend часть SPA веб-приложения, созданного на языке программирования Python с использованием Django REST framework.
Идея приложения основана на концепции отслеживания полезных привычек, вдохновленной книгой Джеймса Клира «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.
Проект включает в себя backend-часть, ответственную за обработку данных и бизнес-логику.

Покрытие проекта тестами составляет более 90%, что подчеркивает уровень надежности и стабильности системы.

## Составляющие части проекта

Проект состоит из следующих компонентов:

1. **Приложение users:**
    - Содержит модель для пользователя `User`
    - Содержит команду `csu` для создания суперпользователя через терминал
    - Содержит механизм CRUD `UserViewSet` на основе viewSet и сериализатор `UserSerializer`
    - Содержит тесты в файле `tests.py` для модели `User`

2. **Приложение habits:**
   - Содержит модель привычек `Habit` и модель вознаграждения `Award`
   - Содержит механизм CRUD для привычек и наград на основе `generics` и сериализаторы для данных представлений
   - Содержит пагинацию привычек `HabitPaginator` и реализацию проверки прав доступа в файле `permissions.py`
   - Содержит класс для взаимодействия с телеграм ботом `TelegramNotificationBot` в файле `services.py`
   - В файле `tasks.py` находится реализация периодической задачи отправки уведомлений `task_send_notification`
   - В файле `validators.py` содержатся валидаторы для привычек
   - В файле `tests.py` содержатся тесты для моделей `Habit` и `Award`

## Технологии
   - Проект разработан на языке программирования `Python` с использованием `Django REST framework`
   - Для работы с базой данных используется сторонняя библиотека `psycopg2-binary`
   - Для выполнения отложенных задач(автоматической рассылки уведомлений) используется `Celery`
   - Для проекта настроен `CORS`, чтобы frontend мог подключаться к проекту на развернутом сервере
   - В проекте подключена API документация при помощи библиотеки `drf-yasg`
   - Для взаимодействия с API телеграм используется библиотека `requests`
   - Для определения процента покрытия проекта тестами используется библиотека `coverage`
   - Для управления виртуальным окружением используется инструмент `poetry`
   - Для взаимодействия с переменными окружения применяется библиотека `python-dotenv`

## Как установить и запустить проект
   - Необходимо выполнить `git clone` репозитория https://github.com/pavel-akulich/app_of_habits
   - Установите все зависимости из файла `pyproject.toml`
   - Создайте базу данных и выполните миграции к базе данных `python manage.py migrate`
   - Настройте необходимые переменные окружения указанные в файле `.env.sample`
   - Запустите сервер `python3 manage.py runserver`
   - Для запуска и обработки отложенных задач запустите `Celery` при помощи команд в терминале:
     * `celery -A config worker -l INFO`
     * `celery -A config beat -l info -S django`
   - Для рассылки уведомлений создайте и настройте телеграм бот 
   - Для получения `telegram_id` используйте сторонний бот, например `Get My ID` - https://t.me/getmyid_bot

## Запуск при помощи Docker
Для более простого запуска проекта при помощи `Docker`, после клонирования репозитория вы можете выполнить следующие шаги:
   - При помощи команды `docker compose up --build` соберите и запустите все сервисы
   - После успешного выполнения предыдущего шага, ваше приложение будет доступно по адресу http://localhost:8000/ или http://127.0.0.1:8000/

## Примечания
   - Проект может быть доработан и расширен для более широкого использования
   - API документация после запуска проекта на локальном сервере доступна по адресу http://127.0.0.1:8000/ и http://127.0.0.1:8000/docs/
   - Переменные окружения, необходимые для работы проекта можно посмотреть в файле `.env.sample`
   - Все необходимые зависимости находятся в файле `pyproject.toml`

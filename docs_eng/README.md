# Project: Atomic Habits App

[Russian](../README.md) | **English**

## Project Description

The project "Atomic Habits App" constitutes the backend part of a Single Page Application (SPA) web application, developed using the Python programming language with the Django REST framework.
The concept of the application is based on the idea of tracking beneficial habits, inspired by James Clear's book "Atomic Habits." The book focuses on acquiring new beneficial habits and eliminating old detrimental ones.
The project encompasses the backend component, responsible for data processing and business logic.

The test coverage of the project exceeds 90%, emphasizing the system's high level of reliability and stability.

## Project Components
The project consists of the next components:

1. **Users Application:**
    - Includes the user model `User`
    - Contains the `csu` command for creating a superuser via the terminal
    - Encompasses the CRUD mechanism with `UserViewSet` based on the ViewSet and `UserSerializer`
    - Includes tests in the `tests.py` file for the `User` model

2. **Habits Application:**
   - Includes the habit model `Habit` and the award model `Award`
   - Encompasses the CRUD mechanism for habits and awards based on `generics`, along with serializers for data representations
   - Implements pagination for habits using `HabitPaginator` and access permission checks in the `permissions.py` file
   - Includes a class for interacting with the Telegram bot `TelegramNotificationBot` in the `services.py` file
   - The `tasks.py` file contains the implementation of a periodic task for sending notifications `task_send_notification`
   - Validators for habits are defined in the `validators.py` file
   - The `tests.py` file contains tests for the `Habit` and `Award` models

## Technologies
   - The project is developed using the `Python` programming language with the `Django REST framework`
   - Utilizes the third-party library `psycopg2-binary` for database interactions
   - Implements deferred task execution (automatic notification dispatch) using `Celery`
   - Configures `CORS` for the project to enable frontend connections to the deployed server
   - Integrates API documentation into the project using the `drf-yasg` library
   - Utilizes the `requests` library for interacting with the Telegram API
   - Determines the test coverage percentage using the `coverage` library
   - Manages the virtual environment using the `poetry` tool
   - Handles environmental variables with the `python-dotenv` library

## How to Install and Run the Project
   - `git clone` the repository at https://github.com/pavel-akulich/app_of_habits 
   - Install all dependencies from the `pyproject.toml` file
   - Create a database and apply migrations to the database using the command `python manage.py migrate`
   - Configure the necessary environment variables as specified in the `.env.sample` file 
   - Start the server using the command `python3 manage.py runserver`
   - To run and process deferred tasks, start `Celery` with the following commands in the terminal:
     * `celery -A config worker -l INFO`
     * `celery -A config beat -l info -S django`
   - Create and configure a Telegram bot for notifications
   - Use a third-party bot such as Get My ID https://t.me/getmyid_bot to obtain the `telegram_id` for notifications

## Run using Docker
To run the project more easily using `Docker`, after cloning the repository, you can follow these steps:
   - Using the `docker compose up --build` command, assemble and launch all services
- After successfully completing the previous step, your application will be available at http://localhost:8000/ or http://127.0.0.1:8000/

## Notes
   - The project can be further developed and extended for broader use
   - After running the project on a local server, the API documentation is available at http://127.0.0.1:8000/ and http://127.0.0.1:8000/docs/
   - View the required environment variables for the project in the `.env.sample` file
   - All necessary dependencies are listed in the `pyproject.toml` file

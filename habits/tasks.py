import datetime

from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.serializers.habit import HabitSerializer
from habits.services import TelegramNotificationBot


@shared_task
def task_send_notification():
    """
    Celery task to send habit notifications to users.

    Retrieves all habits from the database and checks if it's time to send notifications
    to users based on the difference between the habit execution time and the current time.
    If the time difference is within a certain range (1 to 2 hours), a notification is sent.

    Returns:
        None
    """

    habits = Habit.objects.all()

    now_time = datetime.datetime.utcnow().replace(tzinfo=timezone.utc).time()

    for habit in habits:
        serializer = HabitSerializer(habit)
        habit_data = serializer.data
        chat_id = habit_data.get('telegram_id')

        habit_execution_time = habit.execution_time

        # Creating datetime objects with the same date, for subsequent subtraction
        now_datetime = datetime.datetime.combine(datetime.date.today(), now_time)
        habit_execution_datetime = datetime.datetime.combine(datetime.date.today(), habit_execution_time)

        time_difference = habit_execution_datetime - now_datetime

        if 3600 < time_difference.total_seconds() <= 2 * 3600:
            text_to_send = (f'Вам напоминание:\n Вы хотели {habit.action} в {habit_execution_time}\n Где? Это'
                            f' прекрасное место - {habit.place}\n Не ленитесь, это займет всего '
                            f'{habit.time_to_complete} секунд')
            if habit.award:
                text_to_send += f'\nВ награду вы можете {habit.award.reward}'

            tg_bot = TelegramNotificationBot()
            tg_bot.send_habit_notification(text_to_send, chat_id)

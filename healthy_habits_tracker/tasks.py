from datetime import datetime

from celery import shared_task

from healthy_habits_tracker.models import Habit
from healthy_habits_tracker.services import telegram_message


@shared_task
def habit_push():
    """Задание на отправку сообщения в Телеграм с напоминанием о привычке"""

    habits = Habit.objects.all().order_by("time")
    current_time = datetime.now().time()
    for habit in habits:
        if habit.user.tg_chat_id and habit.time > current_time:
            tg_chat_id = habit.user.tg_chat_id
            message = habit
            telegram_message(tg_chat_id, message)

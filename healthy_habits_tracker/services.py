import requests

from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL


def telegram_message(tg_chat_id, message):
    """Функция отправки сообщения в Телеграм"""

    parameters = {"chat_id": tg_chat_id,
                  "text": message}
    r = requests.get(f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage", params=parameters)
    if r.status_code == 200:
        print("Сообщение отправлено")
    else:
        print("Ошибка отправки")

import requests

from config import settings


class TelegramNotificationBot:
    """
    Utilizes Telegram API for sending notifications to users.

    Attributes:
        URL (str): The base URL for the Telegram API.
        TOKEN (str): The Telegram bot token obtained from the settings.

    Methods:
        send_habit_notification(text: str, chat_id: int) -> None:
            Sends a habit notification to the specified chat ID.
    """

    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN

    def send_habit_notification(self, text, chat_id) -> None:
        """
        Sends a habit notification to the specified chat ID.

        Args:
            text (str): The text of the notification.
            chat_id (int): The chat ID of the recipient.

        Returns:
            None
        """

        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )

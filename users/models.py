from django.contrib.auth.models import AbstractUser
from django.db import models

from habits.models import NULLABLE


class User(AbstractUser):
    """
    Custom user model extending AbstractUser.

    Attributes:
        email (EmailField): Email address of the user, unique.
        avatar (ImageField): Avatar image of the user.
        phone (CharField): Phone number of the user.
        country (CharField): Country of the user.
        telegram_id (PositiveIntegerField): Telegram ID for notifications.
        USERNAME_FIELD (str): Field used for authentication, set to 'email'.
        REQUIRED_FIELDS (list): List of required fields for user creation.
    """

    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='users_avatar/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=40, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    telegram_id = models.PositiveIntegerField(default=None, verbose_name='telegram id для уведомлений', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

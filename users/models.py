from django.contrib.auth.models import AbstractUser
from django.db import models

NULFLAG = {"blank": True, "null": True}


class User(AbstractUser):

    email = models.EmailField(max_length=100, verbose_name="email", unique=True, help_text="emaıl")

    username = models.CharField(max_length=30, verbose_name="Имя пользователя",
                                help_text="Имя пользователя", **NULFLAG)

    phone_number = models.CharField(max_length=12, verbose_name="Номер телефона",
                                    help_text="Номер телефона", **NULFLAG)

    avatar = models.ImageField(upload_to="users/avatar", verbose_name="Аватар", help_text="Аватар", **NULFLAG)

    country = models.CharField(max_length=100, verbose_name="Страна", help_text="Cтрана", **NULFLAG)

    tg_chat_id = models.CharField(max_length=100, verbose_name="tg_chat_id", help_text="Enter chat ID", **NULFLAG)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользоаптель"
        verbose_name_plural = "Пользователи"
        permissions = [
            ("set_is_active", "Может блокировать пользователя"),
        ]

    def __str__(self):
        return self.email

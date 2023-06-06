from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name="Адрес электронной почты",
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Логин",
    )
    first_name = models.CharField(
        max_length=150,
        unique=False,
        verbose_name="Имя",
    )
    last_name = models.CharField(
        max_length=150,
        unique=False,
        verbose_name="Фамилия",
    )
    password = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Пароль",
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "password"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

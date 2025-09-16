from django.db import models

from users.models import User

NULFLAG = {"blank": True, "null": True}


class Habit(models.Model):

    owner = models.ForeignKey(User, verbose_name="Пользователь", related_name="Привычки",
                              on_delete=models.CASCADE, **NULFLAG)

    place = models.CharField(max_length=256, verbose_name="Место выполнения привычки",
                             help_text="Место выполнения привычки", **NULFLAG)

    time = models.TimeField(verbose_name="Время", help_text="Введите время выполнения привычки")

    action = models.CharField(max_length=256, verbose_name="Действие, которое нужно выполнить",
                              help_text="Действие, которое нужно выполнить")

    is_pleasant_habit = models.BooleanField(default=False, verbose_name="Признак приятной привычки")

    associated_habit = models.ForeignKey("self", verbose_name="Связанная приятная привычка",
                                         on_delete=models.SET_NULL,
                                         help_text="Данные признак указывается только для Полезной привычки",
                                         **NULFLAG)

    periodicity = models.PositiveSmallIntegerField(default=1, verbose_name="Периодичность выполнения в днях",
                                                   help_text="Периодичность выполнения в днях")

    execution_time = models.PositiveSmallIntegerField(default=120, verbose_name="Длительность выполнения в секундах",
                                                      help_text="Длительность выполнения в секундах")

    award = models.CharField(max_length=200, verbose_name="Вознаграждение", **NULFLAG)

    is_public = models.BooleanField(default=True, verbose_name="Признак публичности")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.owner} будет делать {self.action} в {self.time} в {self.place}"

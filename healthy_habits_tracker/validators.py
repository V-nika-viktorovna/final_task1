from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError


class SimultaneousSelectionValidator:
    """Исключение одновременного выбора связанной привычки и указания вознаграждения"""

    def __init__(self, award, associated_habit):
        self.award = award
        self.associated_habit = associated_habit

    def __call__(self, value):
        award = dict(value).get(self.award)
        associated_habit = dict(value).get(self.associated_habit)
        if award and associated_habit:
            raise exceptions.ValidationError(
                "Нельзя выбирать связанную привычку и вознаграждения одновременно."
            )


class AssociatedHabitValidator:
    """Могут попадать только привычки с признаком приятной привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        associated_habit = dict(value).get(self.field)
        if associated_habit and not associated_habit.is_pleasant_habit:
            raise serializers.ValidationError(
                "В связанные привычки могут попадать только привычки "
                "с признаком приятной привычки."
            )


class PleasantHabitAwardsValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки"""

    def __init__(self, pleasant_habit, award):
        self.pleasant_habit = pleasant_habit
        self.award = award

    def __call__(self, value):
        associated_habit = dict(value).get("associated_habit")
        pleasant_habit = dict(value).get(self.pleasant_habit)
        award = dict(value).get(self.award)

        if award is not None and pleasant_habit is True:
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения."
            )

        if pleasant_habit and associated_habit:
            raise serializers.ValidationError(
                "У приятной привычки не может быть связанной привычки."
            )


def time_validator(value):
    """Проверка длительности выполнения задания"""

    if value > 120:
        raise ValidationError("Время выполнения задания не должно превышать 120 секунд.")


def periodicity_validator(value):
    """Проверяет чтобы нельзя было выполнять привычку реже, чем 1 раз в 7 дней."""

    if value > 7:
        raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")

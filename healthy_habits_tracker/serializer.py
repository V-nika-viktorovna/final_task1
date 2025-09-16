from rest_framework import serializers

from healthy_habits_tracker.models import Habit
from healthy_habits_tracker.validators import (AssociatedHabitValidator,
                                               PleasantHabitAwardsValidator,
                                               SimultaneousSelectionValidator,
                                               periodicity_validator,
                                               time_validator)


class HabitSerializer(serializers.ModelSerializer):

    periodicity = serializers.IntegerField(validators=[periodicity_validator])
    execution_time = serializers.IntegerField(validators=[time_validator])

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            SimultaneousSelectionValidator("associated_habit", "award"),
            AssociatedHabitValidator("associated_habit"),
            PleasantHabitAwardsValidator("pleasant_habits", "award"),
        ]

from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from healthy_habits_tracker.models import Habit
from healthy_habits_tracker.pagination import HealthyHabitsTrackerPagination
from healthy_habits_tracker.serializer import HabitSerializer
from users.permissions import Owner


class HabitCreateAPIView(CreateAPIView):

    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitUpdateAPIView(UpdateAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (Owner,)


class HabitDestroyAPIView(DestroyAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (Owner,)


class HabitListAPIView(ListAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (
        IsAuthenticated,
        Owner,
    )
    pagination_class = HealthyHabitsTrackerPagination

    def get_queryset(self):

        return Habit.objects.filter(owner=self.request.user).order_by("id")


class HabitRetrieveAPIView(RetrieveAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (Owner,)


class PublicHabitListAPIView(ListAPIView):

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = HealthyHabitsTrackerPagination

    def get_queryset(self):
        """Отображения только публичных привычек."""

        return Habit.objects.filter(is_public=True).order_by("id")

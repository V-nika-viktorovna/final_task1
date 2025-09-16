from django.urls import path

from healthy_habits_tracker.apps import HealthyHabitsTrackerConfig
from healthy_habits_tracker.views import (HabitCreateAPIView,
                                          HabitDestroyAPIView,
                                          HabitListAPIView,
                                          HabitRetrieveAPIView,
                                          HabitUpdateAPIView,
                                          PublicHabitListAPIView)

app_name = HealthyHabitsTrackerConfig.name

urlpatterns = [
    path("create/", HabitCreateAPIView.as_view(), name="habits_create"),

    path("<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habits_update"),

    path("<int:pk>/destroy/", HabitDestroyAPIView.as_view(), name="habits_destroy"),

    path("habits/", HabitListAPIView.as_view(), name="habits_list"),

    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habits_retrieve"),

    path("public/", PublicHabitListAPIView.as_view(), name="public"),
]

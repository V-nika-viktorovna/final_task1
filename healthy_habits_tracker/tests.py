from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from healthy_habits_tracker.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.test")
        self.habit = Habit.objects.create(owner=self.user, place="test", time="01:00:00", action="Test")
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):

        data = {
            "owner": self.user.pk,
            "place": "набережная",
            "time": "19:00:00",
            "action": "прогулка",
            "periodicity": 7,
            "execution_time": 110,
        }

        url = reverse("healthy_habits_tracker:habits_create")
        response = self.client.post(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("owner"), self.user.pk)
        self.assertEqual(data.get("place"), "набережная")
        self.assertEqual(data.get("time"), "19:00:00")
        self.assertEqual(data.get("action"), "прогулка")
        self.assertEqual(data.get("execution_time"), 110)

    def test_list_habit(self):

        response = self.client.get(reverse("healthy_habits_tracker:habits_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):

        url = reverse("healthy_habits_tracker:habits_destroy", args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_habit(self):

        url = reverse("healthy_habits_tracker:habits_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("owner"), self.habit.owner.id)
        self.assertEqual(data.get("place"), self.habit.place)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_update_habit(self):

        url = reverse("healthy_habits_tracker:habits_update", args=(self.habit.pk,))
        data = {
            "user": self.user.pk,
            "place": "набережная",
            "time": "19:00:00",
            "action": "пробежка",
            "periodicity": 7,
            "execution_time": 110,
        }
        response = self.client.put(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("owner"), self.habit.owner.id)
        self.assertEqual(data.get("place"), "набережная")
        self.assertEqual(data.get("action"), "пробежка")

    def test_list_public_habit(self):

        response = self.client.get(reverse("healthy_habits_tracker:public"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

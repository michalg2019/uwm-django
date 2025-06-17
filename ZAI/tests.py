from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

# === MODELE ===
from event.models import Pogoda  # Zmień na własny model

class ExampleModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='testuser',
            email='test@test.pl',
        )
        self.user.set_password('testpassword')
        self.obj = Pogoda.objects.create(name="Test name",
        description="test description",
        start_date="2025-06-15",
        end_date="2025-06-15",
        location="test",
        organizer=self.user
    )

    def test_model_creation(self):
        self.assertEqual(self.obj.name, "Test name")
        self.assertIsInstance(self.obj, Pogoda)

    def test_model_str(self):
        self.assertEqual(str(self.obj), "Test name")

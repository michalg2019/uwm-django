import datetime
import zoneinfo

from django.test import TestCase

from event.models import Event
from user.models import User


class EventTest(TestCase):
    def test_event_creation(self):
        testuser = User.objects.create_user(username="testuser")
        warsaw_tz = zoneinfo.ZoneInfo("Europe/Warsaw")
        start_date = datetime.datetime(2021, 1, 1).astimezone(warsaw_tz)
        end_date = datetime.datetime(2021, 1, 2).astimezone(warsaw_tz)

        event = Event.objects.create(
            name="Test Event",
            description="Test Event Description",
            start_date=start_date,
            end_date=end_date,
            location="Test Location",
            organizer=testuser,
        )
        self.assertEqual(event.name, "Test Event")
        self.assertEqual(event.description, "Test Event Description")
        self.assertEqual(event.start_date, start_date)
        self.assertEqual(event.end_date, end_date)
        self.assertEqual(event.location, "Test Location")
        self.assertEqual(event.organizer, testuser)

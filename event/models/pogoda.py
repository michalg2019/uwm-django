from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel, BaseManager
from user.models import User

class PogodaManager(BaseManager):
    def upcoming(self):
        return self.filter(date__gte=timezone.now())

class Pogoda(BaseModel):
    class Type(models.TextChoices):
        ONLINE = 'online', _('Zdalnie')
        OFFLINE = 'offline', _('Stacjonarnie')
        HYBRID = 'hybrid', _('Hybrydowe')

    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    type = models.CharField(choices=Type.choices, default=Type.OFFLINE, max_length=100)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_pogodas')

    objects = PogodaManager()

    class Meta:
        db_table = 'pogoda'
        ordering = ['start_date']

    def __str__(self):
        return self.name
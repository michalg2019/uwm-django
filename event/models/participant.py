from django.db import models

from core.models import BaseModel, BaseManager
from event.models.pogoda import Pogoda
from user.models import User


class Participant(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participations')
    pogoda = models.ForeignKey(Pogoda, on_delete=models.CASCADE, related_name='participants')

    class Meta:
        db_table = 'participant'
        unique_together = ('user', 'pogoda')

    objects = BaseManager()

    def __str__(self):
        return f"{self.user.username} -> {self.pogoda.title}"
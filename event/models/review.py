from django.db import models

from core.models import BaseModel, BaseManager
from event.models.pogoda import Pogoda
from user.models import User


class Review(BaseModel):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    event = models.ForeignKey(Pogoda, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)

    objects = BaseManager()

    class Meta:
        db_table = 'review'
        unique_together = ('user', 'event')

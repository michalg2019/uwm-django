from django.db import models

# Create your models here.

class Film(models.Model):
    nazwa = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(blank=False)
    opis = models.TextField(default="")
    premiera = models.DateField(null=True, blank=True)
    metacritic_score = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.nazwa, self.rok)

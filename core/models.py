from django.db import models
from django.http import Http404


class BaseManager(models.Manager):
    def get_object(self, pk):
        try:
            return self.get(pk=pk)
        except Exception:
            raise Http404


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

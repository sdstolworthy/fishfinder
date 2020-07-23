from django.db import models
from django.db.models import Manager, ObjectDoesNotExist
from uuid import uuid4


class BaseManager(Manager):
    def get_or_none(self, **kwargs):
        """Returns the object if it exists or None if it doesn't"""
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    objects = BaseManager()

    class Meta:
        abstract = True


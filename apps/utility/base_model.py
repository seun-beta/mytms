import uuid

from django.db import models


class TimeStampedUUIDModel(models.Model):
    # pkid = models.BigAutoField(primary_key=True, editable=False)
    # id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now=True, help_text="created time")
    updated_at = models.DateTimeField(auto_now_add=True, help_text="updated time")

    class Meta:
        abstract = True

        ordering = ["-created_at", "-updated_at"]

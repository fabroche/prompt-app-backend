from django.db import models
from django.contrib.auth.models import User
import uuid


class User(User):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True)

    def __str__(self):
        return self.username

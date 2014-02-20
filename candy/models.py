from django.db import models

from uuidfield import UUIDField

class Lollipop(models.Model):
    uuid = UUIDField(auto=True)
    name = models.CharField(max_length=32)

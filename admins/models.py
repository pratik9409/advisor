from django.db import models
import uuid
# Create your models here.


class advisor(models.Model):
    advisor_id = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length = 100)
    url = models.CharField(max_length = 150)

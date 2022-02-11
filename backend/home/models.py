from django.conf import settings
from django.db import models


class FlashCard(models.Model):
    "Generated Model"
    front = models.TextField()
    back = models.TextField()

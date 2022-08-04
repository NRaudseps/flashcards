# DJANGO
from django.db import models


class FlashCard(models.Model):
    class Meta:
        app_label = "flashcards"

    question = models.CharField(max_length=1028)
    answer = models.CharField(max_length=1028)
    box = models.IntegerField(default=1)
    pub_date = models.DateTimeField(auto_now_add=True)

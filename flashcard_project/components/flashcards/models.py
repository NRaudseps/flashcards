# DJANGO
from django.core.validators import MaxValueValidator
from django.db import models


class FlashCard(models.Model):
    MAX_BOX_COUNT = 5

    class Meta:
        app_label = "flashcards"

    question = models.CharField(max_length=1028)
    answer = models.CharField(max_length=1028)
    box = models.IntegerField(default=1, validators=[MaxValueValidator(MAX_BOX_COUNT)])
    pub_date = models.DateTimeField(auto_now_add=True)

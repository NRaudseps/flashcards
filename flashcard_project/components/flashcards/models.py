# DJANGO
from django.db import models


class Box(models.Model):
    class Meta:
        app_label = "flashcards"

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class FlashCard(models.Model):
    class Meta:
        app_label = "flashcards"

    question = models.CharField(max_length=1028)
    answer = models.CharField(max_length=1028)
    box = models.ForeignKey("Box", on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

# DJANGO
from django.db import models


class Box(models.Model):
    name = models.CharField(max_length=256)


class FlashCard(models.Model):
    question = models.CharField(max_length=1028)
    answer = models.CharField(max_length=1028)
    box = models.ForeignKey("Box", on_delete=models.CASCADE)

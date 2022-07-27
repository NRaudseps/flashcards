# DJANGO
from django import forms

from . import models


class FlashCardForm(forms.ModelForm):
    class Meta:
        model = models.FlashCard
        fields = ["question", "answer", "box"]
